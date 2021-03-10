---
title: oracle trigger
tags: db
date: 2019-06-06
---

> 十步杀一人，千里不留行；事了拂身去，深藏功与名。 - 李白

## 触发器类型及划分

| 按划分类型     | 触发器的类型                    | 触发条件                                              |
| -------------- | ------------------------------- | ----------------------------------------------------- |
| 按照触发的时间 | BEFORE 触发器，指事前触发器     | 在触发语句执行前触发器被触发                          |
|                | AFTER 触发器，指事后触发器      | 在触发语句执行以后触发器被触发                        |
|                | INSTEAD OF 触发器，指替代触发器 | 触发语句被触发器操作替代                              |
| 按照触发的事件 | DML 触发器                      | 对表或视图执行 DML 操作时触发的触发器                 |
|                | DDL 触发器                      | 在数据库中执行 DDL 操作时触发的触发器                 |
|                | 用户事件触发器                  | 与用户执行的 DCL 操作或 LOGON/LOGOFF 操作相关的触发器 |
|                | 系统事件触发器                  | 是指由数据库系统事件触发的触发器                      |

其中，DML 触发器，按照触发时 DML 操作影响的记录多少，又可分为：

-   行级触发器：DML 语句每操作一行，行级触发器就会被调用一次
-   语句级触发器：DML 语句不论影响多少行数据，语句级触发器只被调用一次

DDL 触发器又可以分为：

-   数据库级 DDL 触发器：数据库中任何用户执行了相应的 DDL 操作该类触发器都被触发。
-   用户级 DDL 触发器：只有在创建触发器时指定方案的用户执行相应的 DDL 操作时触发器才被触发，其他用户执行该 DDL 操作时触发器不会被触发。

## 触发器相关使用

### 安全性检查

利用触发器对在 scott.emp 表上执行的 DML 操作进行安全性检查，只有 scott 用户登录数据库后才能向该表中执行 DML 操作，这是一个语句级触发器，DML 语句不论影响多少行数据，触发器只被调用一次。

```sql
create or replace trigger tri_dm1
 before insert or update or delete on scott.emp
 begin
   if user <>'SCOTT' then
     raise_application_error(-20001,'You don''t have access to modify this table.');
   end if;
 end;
 /
```

### 数据复制

在 scott 用户下创建能实现 scott.emp 和 employee 两表之间同步复制的 DML 触发器。

```sql
create or replace trigger duplicate_emp
 after update or insert or delete on scott.emp
 for each row
 begin
   if inserting then
     insert into  employee values (:new.empno,:new.ename,:new.job,:new.mgr,
                                   :new.hiredate,:new.sal,:new.comm,:new.deptno);
   elsif deleting then
     delete from employee where empno=:old.empno;
   else
     update employee set empno=:new.empno,ename=:new.ename,job=:new.job,
                         mgr=:new.mgr,hiredate=:new.hiredate,sal=:new.sal,comm=:new.comm,
                          deptno=:new.deptno
     where empno=:old.empno;
   end if;
  end;
 /
```

### 日志记录

在 emp 表上建立语句级触发器，将对 emp 表执行的操作记录到 emp_log 表中。

```sql
 create or replace trigger dm1_log
 after insert or update or delete on scott.emp
 declare
   oper emp_log.oper%type;
  begin
    if inserting then
       oper:='insert';
    elsif deleting then
       oper:='delete';
    else
       oper:='update';
    end if;
    insert into emp_log  values(user,sysdate,oper);
 end;
 /
```

### 表字段预处理

在插入之前用 mtl_system_items_b 表字段更新 som_edi_temp_d 表的字段

```sql
create or replace trigger update_som_edi_temp
before insert on som_edi_temp_d
for each row
declare

begin

  select msib.default_shipping_org into :new.ship_from_org_id
  from   mtl_customer_items mci
        ,mtl_customer_item_xrefs mcix
        ,mtl_system_items_b msib
  where 1= 1
  and   mci.customer_item_id = mcix.customer_item_id
  and   mci.inactive_flag = 'N'
  and   mcix.inventory_item_id = msib.inventory_item_id
  and   mcix.inactive_flag = 'N'
  and   mci.customer_item_number = :new.customer_item_number
  group by msib.default_shipping_org;
exception
   when others then
        null;

end;
```
