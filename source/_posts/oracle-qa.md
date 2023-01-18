---
title: Oracle Q&A
tags: db
date: 2022-07-20
---

```sql
function get_qty_per_pallet(p_invoice_line_id in number) return number
  is 
    l_return number;
  begin
    begin
      select distinct
             spm.pallet_stack_qty *
             spm.qty_carton_per_stack * 
             spm.fg_item_per_carton
        into l_return
        from som_commercial_invoice_lines scl, 
             oe_order_lines_all           ool,
             wsh_carrier_services         wcs,
             som_packing_material_setup   spm
        where scl.so_line_id = ool.line_id
         and upper(ool.shipping_method_code) = upper(wcs.ship_method_code)
         and instr(upper(spm.shipping_method_code), upper(wcs.attribute2)) <> 0
         and spm.organization_id = 85
         and spm.inventory_item_id = scl.inventory_item_id
         and scl.invoice_line_id = p_invoice_line_id;
    exception
      when others then
        debug('get_qty_per_pallet error: ' || sqlerrm);
        l_return := null;
    end;
    
    return l_return;
  end get_qty_per_pallet;
```

当 get_qty_per_pallet 以如下方式调用时，会进入到 get_qty_per_pallet 的 exception 中, 打印 *get_qty_per_pallet error: ORA-01403: no data found* 但是最终结果是正确的，看起来外部的 `som_commercial_invoice_lines sel ` 和函数内部的 `som_commercial_invoice_lines scl` 先进行连接，之后再通过 `seh.invoice_no = 'EX001'` 这个条件筛选。

```sql
select count(1)
  into l_qty_per_pallet_error_count
  from som_commercial_invoice_headers seh, 
       som_commercial_invoice_lines sel 
 where seh.invoice_header_id = sel.invoice_header_id
   and seh.invoice_no = 'EX001'
   and get_qty_per_pallet(sel.invoice_line_id) is null;
```

使用 exists 不会有这种情况。

```sql
select sel.invoice_line_id
--into l_qty_per_pallet_error_count
  from som_commercial_invoice_headers seh, som_commercial_invoice_lines sel
 where seh.invoice_header_id = sel.invoice_header_id
   and seh.invoice_no = 'EX001'
   and exists (select 1
                 from dual
                where som_edi_dachser_pkg.get_qty_per_pallet(sel.invoice_line_id) is null)
```

