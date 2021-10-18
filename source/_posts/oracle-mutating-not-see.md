---
title: Oracle PL/SQL mutating not see
tag: db
date: 2021-04-30
---

Question In get_item_project_code use `ssc_t_edi_head` then update it meanwhile will occurs the error: "ORA-04091: table YSC.SSC_T_EDI_HEAD is mutating, trigger/function may not see it".

```sql
function get_item_project_code(p_head_id in varchar2, p_org_id in number) return varchar2
is
    l_return varchar2(10);
begin
    begin
        select mci.attribute6
        into l_return
        from mtl_customer_items       mci,
                mtl_customer_item_xrefs  mcix,
                mtl_system_items_b       msib,
                wsh_new_deliveries       wnd,
                wsh_delivery_assignments wda,
                wsh_delivery_details     wdd,
                hz_cust_site_uses_all    hcsua,
                hz_cust_acct_sites_all   hcasa,
                hz_cust_accounts         hca,
                ssc_t_edi_head           seh
        where 1 = 1
            and mci.customer_item_id = mcix.customer_item_id
            and mci.inactive_flag = 'N'
            and mcix.inventory_item_id = msib.inventory_item_id
            and mcix.inactive_flag = 'N'
            and msib.segment1 = seh.part_no
            and wnd.delivery_id = wda.delivery_id
            and wda.delivery_detail_id = wdd.delivery_detail_id
            and wnd.name = seh.delivery_no
            and wdd.ship_to_site_use_id = hcsua.site_use_id
            and hcsua.cust_acct_site_id = hcasa.cust_acct_site_id
            and hcasa.cust_account_id = hca.cust_account_id
            and hca.cust_account_id = mci.customer_id
            and seh.head_id = p_head_id
            and seh.org_id = p_org_id
        group by mci.attribute6;
    exception
        when others then
        debug('get_item_project_code error: ' || sqlerrm, 'Y');
        l_return := null;
    end;

    return l_return;
end get_item_project_code;


update ssc_t_edi_head sh
   set sh.item_project_code = get_item_project_code(sh.head_id,
                                                    sh.customer,
                                                    sh.org_id)
 where sh.customer = 'CUSTOMER';
```

### Test SubQuery

```sql
--same error
update ssc_t_edi_head sh
   set sh.item_project_code =
       (select get_item_project_code(sh.head_id,
                                     sh.customer,
                                     sh.org_id)
          from dual)
 where sh.customer = 'CUSTOMER';


update ssc_t_edi_head so
   set so.item_project_code =
       (select get_item_project_code(sh.head_id,
                                     sh.customer,
                                     sh.org_id)
          from ssc_t_edi_head sh
         where sh.customer = 'CUSTOMER'
           and so.head_id = sh.head_id
           and so.org_id = sh.org_id)
 where so.customer = 'CUSTOMER';
```

### Test With

```sql
--ORA-00928: missing SELECT keyword
with t as
 (select sh.head_id,
         sh.org_id,
         get_item_project_code(sh.head_id,
                               sh.customer,
                               sh.org_id) code
    from ssc_t_edi_head sh
   where sh.customer = 'CUSTOMER')

update ssc_t_edi_head sh
   set sh.item_project_code = (select t.code
                                 from t
                                where sh.head_id = t.head_id
                                  and sh.org_id = t.org_id)
 where sh.customer = 'CUSTOMER';


--same error
update ssc_t_edi_head h
   set h.item_project_code =
       (with t as (select sh.head_id,
                          sh.org_id,
                          get_item_project_code(sh.head_id,
                                                sh.customer,
                                                sh.org_id) code
                     from ssc_t_edi_head sh
                    where sh.customer = 'CUSTOMER')
         select t.code
           from t
          where t.head_id = h.head_id
            and t.org_id = h.org_id)
 where h.customer = 'CUSTOMER';
```

### Test Merge

```sql
--same error
MERGE INTO ssc_t_edi_head dest
USING (select sh.head_id,
              sh.customer,
              sh.org_id,
              get_item_project_code(sh.head_id,
                                    sh.customer,
                                    sh.org_id) item_project_code
         from ssc_t_edi_head sh
        where sh.customer = 'CUSTOMER') src
ON (src.head_id = dest.head_id and src.customer = dest.customer and src.org_id = dest.org_id)
WHEN MATCHED THEN
  UPDATE
     SET dest.item_project_code = src.item_project_code
   WHERE dest.customer = 'CUSTOMER';
```

### Test Cursor

```sql
--ok
declare
  cursor cur_data is
    select sh.head_id,
           sh.customer,
           sh.org_id,
           get_item_project_code(sh.head_id,
                                 sh.customer,
                                 sh.org_id) item_project_code
      from ssc_t_edi_head sh
     where sh.customer = 'CUSTOMER';
begin
  for c in cur_data loop
    update ssc_t_edi_head sh
       set sh.item_project_code = c.item_project_code
     where sh.head_id = c.head_id
       and sh.customer = c.customer
       and sh.org_id = c.org_id;
  end loop;
end;
```

### Test Hint

```sql
--ok
update ssc_t_edi_head h
   set h.item_project_code =
       (with t as (select /*+ materialize */ sh.head_id,
                          sh.org_id,
                          get_item_project_code(sh.head_id,
                                                sh.customer,
                                                sh.org_id) code
                     from ssc_t_edi_head sh
                    where sh.customer = 'CUSTOMER')
         select t.code
           from t
          where t.head_id = h.head_id
            and t.org_id = h.org_id)
 where h.customer = 'CUSTOMER';
```

### PRAGMA AUTONOMOUS_TRANSACTION

```sql
--ok
function get_item_project_code(p_head_id in varchar2, p_org_id in number) return varchar2
is
    l_return varchar2(10);
    PRAGMA AUTONOMOUS_TRANSACTION;
begin
    begin
        select mci.attribute6
        into l_return
        from mtl_customer_items       mci,
                mtl_customer_item_xrefs  mcix,
                mtl_system_items_b       msib,
                wsh_new_deliveries       wnd,
                wsh_delivery_assignments wda,
                wsh_delivery_details     wdd,
                hz_cust_site_uses_all    hcsua,
                hz_cust_acct_sites_all   hcasa,
                hz_cust_accounts         hca,
                ssc_t_edi_head           seh
        where 1 = 1
            and mci.customer_item_id = mcix.customer_item_id
            and mci.inactive_flag = 'N'
            and mcix.inventory_item_id = msib.inventory_item_id
            and mcix.inactive_flag = 'N'
            and msib.segment1 = seh.part_no
            and wnd.delivery_id = wda.delivery_id
            and wda.delivery_detail_id = wdd.delivery_detail_id
            and wnd.name = seh.delivery_no
            and wdd.ship_to_site_use_id = hcsua.site_use_id
            and hcsua.cust_acct_site_id = hcasa.cust_acct_site_id
            and hcasa.cust_account_id = hca.cust_account_id
            and hca.cust_account_id = mci.customer_id
            and seh.head_id = p_head_id
            and seh.org_id = p_org_id
        group by mci.attribute6;
    exception
        when others then
        debug('get_item_project_code error: ' || sqlerrm, 'Y');
        l_return := null;
    end;

    return l_return;
end get_item_project_code;
```
