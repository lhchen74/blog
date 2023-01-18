---
title: Recursive Subquery Factoring Hierarchical Queries Using Recursive WITH Clauses
tags: db
date: 2022-06-22
---

> 转载：[ORACLE-BASE - Recursive Subquery Factoring : Hierarchical Queries Using Recursive WITH Clauses](https://oracle-base.com/articles/11g/recursive-subquery-factoring-11gr2)

This articles gives an overview of how to query hierarchical data in Oracle databases using recursive subquery factoring. This functionality was introduced in Oracle 11g Release 2, giving an alternative to the method of performing hierarchical queries from [previous versions](https://oracle-base.com/articles/misc/hierarchical-queries).

## Setup

The following table contains hierarchical data.

```sql
DROP TABLE tab1 PURGE;

CREATE TABLE tab1 (
  id        NUMBER,
  parent_id NUMBER,
  CONSTRAINT tab1_pk PRIMARY KEY (id),
  CONSTRAINT tab1_tab1_fk FOREIGN KEY (parent_id) REFERENCES tab1(id)
);

CREATE INDEX tab1_parent_id_idx ON tab1(parent_id);

INSERT INTO tab1 VALUES (1, NULL);
INSERT INTO tab1 VALUES (2, 1);
INSERT INTO tab1 VALUES (3, 2);
INSERT INTO tab1 VALUES (4, 2);
INSERT INTO tab1 VALUES (5, 4);
INSERT INTO tab1 VALUES (6, 4);
INSERT INTO tab1 VALUES (7, 1);
INSERT INTO tab1 VALUES (8, 7);
INSERT INTO tab1 VALUES (9, 1);
INSERT INTO tab1 VALUES (10, 9);
INSERT INTO tab1 VALUES (11, 10);
INSERT INTO tab1 VALUES (12, 9);
COMMIT;
```

## Basic Hierarchical Query

A recursive subquery factoring clause must contain two query blocks combined by a `UNION ALL` set operator. The first block is known as the anchor member, which can not reference the query name. It can be made up of one or more query blocks combined by the `UNION ALL`, `UNION`, `INTERSECT` or `MINUS` set operators. The second query block is known as the recursive member, which must reference the query name once.

The following query uses a recursive `WITH` clause to perform a tree walk. The anchor member queries the root nodes by testing for records with no parents. The recursive member successively adds the children to the root nodes.

```sql
SET PAGESIZE 20 LINESIZE 110

WITH t1(id, parent_id) AS (
  -- Anchor member.
  SELECT id,
         parent_id
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SELECT id,
       parent_id
FROM   t1;

        ID  PARENT_ID
---------- ----------
         1
         2          1
         7          1
         9          1
         3          2
         4          2
         8          7
        10          9
        12          9
         5          4
         6          4
        11         10
```

The ordering of the rows is specified using the `SEARCH` clause, which can use two methods.

- `BREADTH FIRST BY` : Sibling rows are returned before child rows are processed.
- `DEPTH FIRST BY` : Child rows are returned before siblings are processed.

The following queries show the result of these differing ordering methods.

```sql
WITH t1(id, parent_id) AS (
  -- Anchor member.
  SELECT id,
         parent_id
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH BREADTH FIRST BY id SET order1
SELECT id,
       parent_id
FROM   t1
ORDER BY order1;

        ID  PARENT_ID
---------- ----------
         1
         2          1
         7          1
         9          1
         3          2
         4          2
         8          7
        10          9
        12          9
         5          4
         6          4
        11         10


WITH t1(id, parent_id) AS (
  -- Anchor member.
  SELECT id,
         parent_id
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
SELECT id,
       parent_id
FROM   t1
ORDER BY order1;

        ID  PARENT_ID
---------- ----------
         1
         2          1
         3          2
         4          2
         5          4
         6          4
         7          1
         8          7
         9          1
        10          9
        11         10
        12          9
```

## Implement Equivalent of LEVEL

The following example shows how we can determine the `LEVEL` of the hierarchy the current row resides in.

```sql
COLUMN tree FORMAT A20

WITH t1(id, parent_id, lvl) AS (
  -- Anchor member.
  SELECT id,
         parent_id,
         1 AS lvl
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id,
         lvl+1
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
SELECT id,
       parent_id,
       RPAD('.', (lvl-1)*2, '.') || id AS tree,
       lvl
FROM t1
ORDER BY order1;

        ID  PARENT_ID TREE                        LVL
---------- ---------- -------------------- ----------
         1            1                             1
         2          1 ..2                           2
         3          2 ....3                         3
         4          2 ....4                         3
         5          4 ......5                       4
         6          4 ......6                       4
         7          1 ..7                           2
         8          7 ....8                         3
         9          1 ..9                           2
        10          9 ....10                        3
        11         10 ......11                      4
        12          9 ....12                        3
```

## Implement Equivalent of CONNECT_BY_ROOT

The next example shows how to mimic `CONNECT_BY_ROOT` functionality.

```sql
WITH t1(id, parent_id, lvl, root_id) AS (
  -- Anchor member.
  SELECT id,
         parent_id,
         1 AS lvl,
         id AS root_id
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id,
         lvl+1,
         t1.root_id
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
SELECT id,
       parent_id,
       RPAD('.', (lvl-1)*2, '.') || id AS tree,
       lvl,
       root_id
FROM t1
ORDER BY order1;

        ID  PARENT_ID TREE                        LVL    ROOT_ID
---------- ---------- -------------------- ---------- ----------
         1            1                             1          1
         2          1 ..2                           2          1
         3          2 ....3                         3          1
         4          2 ....4                         3          1
         5          4 ......5                       4          1
         6          4 ......6                       4          1
         7          1 ..7                           2          1
         8          7 ....8                         3          1
         9          1 ..9                           2          1
        10          9 ....10                        3          1
        11         10 ......11                      4          1
        12          9 ....12                        3          1
```

## Implement Equivalent of SYS_CONNECT_BY_PATH

The following example shows how to mimic the `SYS_CONNECT_BY_PATH` functionality.

```sql
COLUMN path FORMAT A20

WITH t1(id, parent_id, lvl, root_id, path) AS (
  -- Anchor member.
  SELECT id,
         parent_id,
         1 AS lvl,
         id AS root_id,
         TO_CHAR(id) AS path
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id,
         lvl+1,
         t1.root_id,
         t1.path || '-' || t2.id AS path
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
SELECT id,
       parent_id,
       RPAD('.', (lvl-1)*2, '.') || id AS tree,
       lvl,
       root_id,
       path
FROM t1
ORDER BY order1;

        ID  PARENT_ID TREE                        LVL    ROOT_ID PATH
---------- ---------- -------------------- ---------- ---------- --------------------
         1            1                             1          1 1
         2          1 ..2                           2          1 1-2
         3          2 ....3                         3          1 1-2-3
         4          2 ....4                         3          1 1-2-4
         5          4 ......5                       4          1 1-2-4-5
         6          4 ......6                       4          1 1-2-4-6
         7          1 ..7                           2          1 1-7
         8          7 ....8                         3          1 1-7-8
         9          1 ..9                           2          1 1-9
        10          9 ....10                        3          1 1-9-10
        11         10 ......11                      4          1 1-9-10-11
        12          9 ....12                        3          1 1-9-12
```

## Implement Equivalent of CONNECT_BY_ISLEAF

The following example shows how to mimic the `CONNECT_BY_ISLEAF` functionality.

There is no natural way to find the leaf nodes until the result set is produced, so we use the `LEAD` analytic function in the main select list to check the next row in the result set. If it has a level that is less than or equal to the current row, we know the current row must be a leaf node.

```sql
WITH t1(id, parent_id, lvl, root_id, path) AS (
  -- Anchor member.
  SELECT id,
         parent_id,
         1 AS lvl,
         id AS root_id,
         TO_CHAR(id) AS path
  FROM   tab1
  WHERE  parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id,
         lvl+1,
         t1.root_id,
         t1.path || '-' || t2.id AS path
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
SELECT id,
       parent_id,
       RPAD('.', (lvl-1)*2, '.') || id AS tree,
       lvl,
       root_id,
       path,
       CASE 
         WHEN LEAD(lvl, 1, 1) OVER (ORDER BY order1) <= lvl THEN 1
         ELSE 0
       END leaf
FROM t1
ORDER BY order1;


        ID  PARENT_ID TREE                        LVL    ROOT_ID PATH                       LEAF
---------- ---------- -------------------- ---------- ---------- -------------------- ----------
         1            1                             1          1 1                             0
         2          1 ..2                           2          1 1-2                           0
         3          2 ....3                         3          1 1-2-3                         1
         4          2 ....4                         3          1 1-2-4                         0
         5          4 ......5                       4          1 1-2-4-5                       1
         6          4 ......6                       4          1 1-2-4-6                       1
         7          1 ..7                           2          1 1-7                           0
         8          7 ....8                         3          1 1-7-8                         1
         9          1 ..9                           2          1 1-9                           0
        10          9 ....10                        3          1 1-9-10                        0
        11         10 ......11                      4          1 1-9-10-11                     1
        12          9 ....12                        3          1 1-9-12                        1

SQL>
```

## Cyclic Hierarchical Query (NOCYCLE and CONNECT_BY_ISCYCLE)

It is possible for a hierarchy to be cyclical, which can represent a problem when querying the data.

```sql
-- Create a cyclic reference
UPDATE tab1 SET parent_id = 9 WHERE id = 1;
COMMIT;


WITH t1(id, parent_id, lvl, root_id, path) AS (
  -- Anchor member.
  SELECT id,
         parent_id,
         1 AS lvl,
         id AS root_id,
         TO_CHAR(id) AS path
  FROM   tab1
  WHERE  id = 1 --Because UPDATE tab1 SET parent_id = 9 WHERE id = 1; Here cannot use parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id,
         lvl+1,
         t1.root_id,
         t1.path || '-' || t2.id AS path
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
SELECT id,
       parent_id,
       RPAD('.', (lvl-1)*2, '.') || id AS tree,
       lvl,
       root_id,
       path
FROM t1
ORDER BY order1;
     *
ERROR at line 27:
ORA-32044: cycle detected while executing recursive WITH query
```

The `NOCYCLE` and `CONNECT_BY_ISCYCLE` functionality is replicated using the `CYCLE` clause. By specifying this clause, the cycle is detected and the recursion stops, with the cycle column set to the specified value, to indicate the row where the cycle is detected. Unlike the `CONNECT BY NOCYCLE` method, which stops at the row before the cycle, this method stops at the row after the cycle.

```sql
WITH t1(id, parent_id, lvl, root_id, path) AS (
  -- Anchor member.
  SELECT id,
         parent_id,
         1 AS lvl,
         id AS root_id,
         TO_CHAR(id) AS path
  FROM   tab1
  WHERE  id = 1 --Because UPDATE tab1 SET parent_id = 9 WHERE id = 1; Here cannot use parent_id IS NULL
  UNION ALL
  -- Recursive member.
  SELECT t2.id,
         t2.parent_id,
         lvl+1,
         t1.root_id,
         t1.path || '-' || t2.id AS path
  FROM   tab1 t2, t1
  WHERE  t2.parent_id = t1.id
)
SEARCH DEPTH FIRST BY id SET order1
CYCLE id SET cycle TO 1 DEFAULT 0
SELECT id,
       parent_id,
       RPAD('.', (lvl-1)*2, '.') || id AS tree,
       lvl,
       root_id,
       path,
       cycle
FROM t1
ORDER BY order1;

        ID  PARENT_ID TREE                        LVL    ROOT_ID PATH                 C
---------- ---------- -------------------- ---------- ---------- -------------------- -
         1          9 1                             1          1 1                    0
         2          1 ..2                           2          1 1-2                  0
         3          2 ....3                         3          1 1-2-3                0
         4          2 ....4                         3          1 1-2-4                0
         5          4 ......5                       4          1 1-2-4-5              0
         6          4 ......6                       4          1 1-2-4-6              0
         7          1 ..7                           2          1 1-7                  0
         8          7 ....8                         3          1 1-7-8                0
         9          1 ..9                           2          1 1-9                  0
         1          9 ....1                         3          1 1-9-1                1
        10          9 ....10                        3          1 1-9-10               0
        11         10 ......11                      4          1 1-9-10-11            0
        12          9 ....12                        3          1 1-9-12               0
```

For more information see:

- [Recursive Subquery Factoring](http://docs.oracle.com/database/121/SQLRF/statements_10002.htm#i2077142)
- [Hierarchical Queries in Oracle (Recursive WITH Clause) ](https://www.youtube.com/watch?v=RIs9HaceYIc)
- [Hierarchical Queries in Oracle](https://oracle-base.com/articles/misc/hierarchical-queries)
- [Hierarchical Queries in Oracle (CONNECT BY) ](https://www.youtube.com/watch?v=HXFUXYFdB-Y)
- [WITH Clause : Subquery Factoring](https://oracle-base.com/articles/misc/with-clause)
- [WITH Clause Enhancements in Oracle Database 12c Release 1 (12.1)](https://oracle-base.com/articles/12c/with-clause-enhancements-12cr1)