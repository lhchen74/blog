---
title: Oracle Common SQL
tags: db
date: 2018-08-08
---

### Get quarter date

```sql
/**
    Q1 =>  11/1 ~ 1/31
    Q2 =>  2/1  ~ 4/30
    Q3 =>  5/1  ~ 7/31
    Q4 =>  8/1  ~ 10/31 
*/
function get_quarter_date(p_flag in varchar2) return date
is
   l_return  date;
   l_month   number;
   l_year    number;
   l_day     number;
   l_loc     varchar2(10) := p_flag;
begin
  
   select extract(year from sysdate)  into l_year  from dual;
   select extract(month from sysdate) into l_month from dual;
   select extract(day from sysdate)   into l_day   from dual;
     
   l_year   := case when l_loc = 'START' then 
                   case when l_month in (1) then l_year-1 
                   else l_year end
               else 
                   case when l_month in (11,12) then l_year+1 
                   else l_year end
               end;

   l_month  := case when l_loc = 'START' then 
                   case when l_month in (2,3,4)   then 2
                        when l_month in (5,6,7)   then 5
                        when l_month in (8,9,10)  then 8
                        when l_month in (11,12,1) then 11
                    end 
               else 
                   case when l_month in (2,3,4)   then 4
                        when l_month in (5,6,7)   then 7
                        when l_month in (8,9,10)  then 10
                        when l_month in (11,12,1) then 1
                    end
               end;
               
   l_day    := case when l_loc = 'START' then 
                   1 
               else 
                   case when l_month in (2,3,4) then 30 
                   else 31 end 
               end;
   
   
   l_return :=  to_date(to_char(l_year) || '/' || to_char(l_month) || '/' || to_char(l_day),'yyyy/mm/dd');
   
   return l_return;

end get_quarter_date;
```

```sql
--sysdate 2022/06/22

select get_quarter_date('START') quater_start,
       get_quarter_date('END') quater_end
  from dual;

--quater_start   quarter_end
--2022-05-01	 2022-07-31
```

### Fetch max of group

```sql
--method1
select *
  from som_edi_temp_d setd
 where seq_id = (select max(setd2.seq_id)
                   from som_edi_temp_d setd2
                  where setd.po_line = setd2.po_line
                    and setd2.cust_po_number = '4512229779')

--method2
select a.*
  from som_edi_temp_d a,
       (select sd.po_line, max(sd.seq_id) seq_id
          from som_edi_temp_d sd
         where sd.cust_po_number = '4512229779'
         group by sd.po_line) b
 where a.po_line = b.po_line
   and a.seq_id = b.seq_id

--method3
--num 也会查询出来
select *
  from (select sd.*,
               row_number() over(partition by po_line order by seq_id desc) as num
          from som_edi_temp_d sd
         where sd.cust_po_number = '4512229779') t
 where t.num = 1
```

### Batch check columns

```sql
function check_columns_required(p_head_id in varchar2, p_org_id in number) return varchar2
    is
      l_carton_empty_count  number;
      l_pallet_empty_count  number;
      l_mac_empty_count     number;
      l_csn_empty_count     number;
      
      l_error_msg           varchar2(500);
    begin
      begin 
         
         select sum(decode(seb.customer_pallet_no, 'N/A', 1, null, 1, 0)),
                sum(decode(seb.customer_carton_no, 'N/A', 1, null, 1, 0)),
                sum(decode(seb.mac_id, 'N/A', 1, null, 1, 0)),
                sum(decode(seb.customer_sn, 'N/A', 1, null, 1, 0))
           into l_pallet_empty_count,
                l_carton_empty_count,
                l_mac_empty_count,
                l_csn_empty_count
           from ssc_t_edi_head seh, ssc_t_edi_body seb
          where seh.head_id = seb.head_id
            and seh.org_id = seb.org_id
            and seh.head_id = p_head_id
            and seh.org_id = p_org_id;
         
         if l_pallet_empty_count > 0 then
            l_error_msg := l_error_msg || 'CUSTOMER_PALLET_NO EMPTY; ';
         end if;
         
         if l_carton_empty_count > 0 then
            l_error_msg := l_error_msg || 'CUSTOMER_CARTON_NO EMPTY; ';
         end if;
         
         if l_mac_empty_count > 0 then
            l_error_msg := l_error_msg || 'MAC_ID EMPTY; ';
         end if;
         
         if l_csn_empty_count > 0 then
            l_error_msg := l_error_msg || 'CUSTOMER_SN EMPTY; ';
         end if;
         
      exception
        when others then
           debug('check_columns_required error: ' || sqlerrm, 'Y');
           l_error_msg := 'check_columns_required error; ';
      end;
      
      return l_error_msg;
end check_columns_required;
```
