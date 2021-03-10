---
title: oracle join
date: 2018-08-08
tags: db
---

# Oracle 左右全连接

> 越觉得厚重的情绪越荒诞得遥远，越难于去细致地描述，便惊觉语言是多么的苍白无力。我想，这恐怕便是人类音乐与绘画等艺术诞生的起源。

## 测试数据

```sql
create table a(id number);
create table b(id number);
insert into a values(1);
insert into a values(2);
insert into a values(3);
insert into b values(1);
insert into b values(2);
insert into b values(4);
commit;
```

## 左外连接

```sql
--左外连接会显示左边表的所有数据
--主流数据库通用的方法
select * from a left join b on a.id=b.id;

--oracle特有的方法
select * from a, b where a.id=b.id(+);

        ID         ID
---------- ----------
         1          1
         2          2
         3
```

## 右外连接

```sql
--右外连接会显示右边表所有数据
--主流数据库通用的方法
select * from a right join b on a.id=b.id;

--oracle特有的方法
select * from a, b where a.id(+)=b.id;

        ID         ID
---------- ----------
         1          1
         2          2
                    4
```

## 内连接

```sql
--主流数据库通用的方法
select * from a join b on a.id=b.id;

--where关联
select * from a, b where a.id=b.id;

        ID         ID
---------- ----------
         1          1
         2          2
```

## 全外连接

```sql
--主流数据库通用的方法
select * from a full join b on a.id=b.id;

--oracle特有的方法
select * from a, b where a.id = b.id(+)
union
select * from a, b where a.id(+) = b.id;

        ID         ID
---------- ----------
         1          1
         2          2
         3
                    4
```

## 完全连接(交叉连接或者笛卡尔积)

```sql
--主流数据库通用的方法
select * from a, b;

--或者
select * from a cross join b;

        ID         ID
---------- ----------
         1          1
         1          2
         1          4
         2          1
         2          2
         2          4
         3          1
         3          2
         3          4
```

## 注意

左向外连接，`+` 在右边，返回左边表所有符合条件数据
右向外连接，`+` 在左边，返回右边表所有符合条件数据

```sql
--注意这里没有第二个加号，会直接过滤掉数据，只显示符合条件的记录
select * from a, b where a.id = b.id(+) and b.id = 2;

        ID         ID
---------- ----------
         2          2

--注意where上第二个加号，它的作用是修改右边表记录的显示，例如如果b.id(+) = 2，显示为2，否则显示null
select * from a, b where a.id = b.id(+) and b.id(+) = 2;

        ID         ID
---------- ----------
         2          2
         3
         1
```
