---
title: oracle error
tags: db
date: 2019-03-22
---

### ORA-01422

exact fetch returns more than requested number of rows

```sql
--查询到 per_box_qty 是多条记录
select per_box_qty into l_box_num
  from som_packing_item_setup
 where organization_id = p_org_id
   and assembly_item_id = p_item_id;
```

### ORA-06502 numeric or value error: character string buffer too small

```sql
--数据库中字段 location varchar2(40)
--当 location 存储的字段大于 30 时 插入 l_ship_to_location 会出现此错误
l_ship_to_location varchar2(30);
select hcsua.location into l_ship_to_location
  from hz_cust_site_uses_all hcsua;
```

### ORA-01858 a non-numeric character was found where a numeric was expected

```sql
--sysdate 是日期类型，'R' 是字符类型，类型不匹配
select nvl(sysdate,'R') from dual;
```

### ORA-00979 not a GROUP BY expression

```sql
--如果分组，查找的字段必须都要 group by
select seh.cust_po_number from som_edi_temp_h seh group by seh.edi_id;
```

### ORA-00957 duplicate column name

```sql
--对同一个字段插入多次
insert into babb_test_som_edi_tem_h(edi_date, edi_date) values (sysdate, sysdate);
```

### ORA-00936 missing expression

```sql
--缺少edi_type的值
--在字符串拼接插入时需要注意为 null 的情况，因为 'a' || ',' || null || ',' || 'b' 返回 a,,b
insert into babb_test_som_edi_tem_h(edi_date, edi_type) values (sysdate,);
```

### ORA-00917 missing comma

```sql
--PALLET ID 中间有空格，如果栏位有空格需要使用双引号 "PALLET_ID"
insert into babb_temp (PALLET ID, MAC) values ('PL001', 'M001');
```

### PLS-00428: an INTO clause is expected in this SELECT statement

PL/SQL block must has an INTO clause in SELECT statement

```sql
begin
  execute immediate 'select 1 from dual'; --After sql should has ;, if add will occurs error: ORA-00911: invalid character
end;

--PLS-00428: an INTO clause is expected in this SELECT statement
begin
  execute immediate 'begin select 1 from dual; end;';
end;
```
