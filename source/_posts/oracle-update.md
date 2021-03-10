---
title: Update a table with data from another table
tags: db
date: 2020-04-30
---

### 问题

table1

| id  | name | description |
| --- | ---- | ----------- |
| 1   | a    | aaa         |
| 2   | b    | bbb         |
| 3   | c    | ccc         |

table2

| id  | name | description |
| --- | ---- | ----------- |
| 1   | x    | xxx         |
| 2   | y    | yyy         |

通过 id 更新 table2 的 name 和 description 到 table1

result

| id  | name | description |
| --- | ---- | ----------- |
| 1   | x    | xxx         |
| 2   | y    | yyy         |
| 3   | c    | ccc         |

test data

```sql
create table table1(
   id   number,
   name varchar2(10),
   description varchar2(100)
);

insert into table1
select 1, 'a', 'aaa' from dual
union
select 2, 'b', 'bbb' from dual
union
select 3, 'c', 'ccc' from dual;


create table2 as select * from table1 where 1 <> 1;

insert into table2
select 1, 'x', 'xxx' from dual
union
select 2, 'y', 'yyy' from dual
```

### 方式 1

这种情况下需要添加 `WHERE EXISTS (SELECT 1 FROM table2 t2 WHERE t1.id = t2.id)` 只更新 table2 中存在的数据，如果不添加会将 table1 id = 3 的 name, description 更新为 null

```sql
UPDATE table1 t1
   SET (name, description) =
       (SELECT t2.name, t2.description FROM table2 t2 WHERE t2.id = t1.id)
 WHERE EXISTS (SELECT 1 FROM table2 t2 WHERE t1.id = t2.id)
```

### 方式 2

这种方式执行速度比较快

```sql
MERGE INTO table1 t1
USING (
   -- For more complicated queries you can use WITH clause here
   SELECT * FROM table2
) t2
ON (t1.id = t2.id)
WHEN MATCHED THEN
  UPDATE SET t1.name = t2.name, t1.description = t2.description;
```

### 方式 3

```SQL
BEGIN
  FOR i in (select id, name, description from table2) LOOP
    UPDATE table1
       SET name = i.name, description = i.description
     WHERE id = i.id;
  END LOOP;
END;
```
