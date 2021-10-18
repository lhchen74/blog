---
title: SQLServer
tags: db
date: 2019-12-19
---

### 创建 temp table

```sql
create table #edi_temp (
	head_id varchar(25),
	transfer_time varchar(100)
);

select * from #edi_temp;
```

### 批量插入数据

```sql
insert into #edi_temp values
('H00039827', '2019/3/27 14:15:13'),
('H00039871', '2019/5/13 13:10:49'),
('H00039872', '2019/5/13 13:10:49'),
('H00039873', '2019/5/13 13:10:49')
```

### 多表联合更新

```sql
update edi_head
   set transfer_time = cast(b.transfer_time as datetime) from edi_head a, #edi_temp b
 where a.head_id = b.head_id;
```

### 常用函数

#### ISNULL

```sql
--isnull 类似于 Oracle nvl
select isnull(null, 'S'); --S
select isnull('R', 'S');  --R
```

#### GETDATE

```sql
--getdate() 类似于 Oracle sysdate
--如下类似于 Oracle: select sysdate from dual;
select getdate();
```
