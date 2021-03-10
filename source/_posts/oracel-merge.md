---
title: oracle merge
tags: db
date: 2020-07-24
---

> reproduced:[ORACLE-BASE - MERGE Statement Enhancements in Oracle Database 10g](https://oracle-base.com/articles/10g/merge-enhancements-10g)

### Test Table

The following examples use the table defined below.

```sql
CREATE TABLE test1 AS
SELECT *
FROM   all_objects
WHERE  1=2;
```

### Optional Clauses

The `MATCHED` and `NOT MATCHED` clauses are now optional making all of the following examples valid.

```sql
-- Both clauses present.
MERGE INTO test1 a
  USING all_objects b
    ON (a.object_id = b.object_id)
  WHEN MATCHED THEN
    UPDATE SET a.status = b.status
  WHEN NOT MATCHED THEN
    INSERT (object_id, status)
    VALUES (b.object_id, b.status);

-- No matched clause, insert only.
MERGE INTO test1 a
  USING all_objects b
    ON (a.object_id = b.object_id)
  WHEN NOT MATCHED THEN
    INSERT (object_id, status)
    VALUES (b.object_id, b.status);

-- No not-matched clause, update only.
MERGE INTO test1 a
  USING all_objects b
    ON (a.object_id = b.object_id)
  WHEN MATCHED THEN
    UPDATE SET a.status = b.status;
```

### Conditional Operations

Conditional inserts and updates are now possible by using a `WHERE` clause on these statements.

```sql
-- Both clauses present.
MERGE INTO test1 a
  USING all_objects b
    ON (a.object_id = b.object_id)
  WHEN MATCHED THEN
    UPDATE SET a.status = b.status
    WHERE  b.status != 'VALID'
  WHEN NOT MATCHED THEN
    INSERT (object_id, status)
    VALUES (b.object_id, b.status)
    WHERE  b.status != 'VALID';

-- No matched clause, insert only.
MERGE INTO test1 a
  USING all_objects b
    ON (a.object_id = b.object_id)
  WHEN NOT MATCHED THEN
    INSERT (object_id, status)
    VALUES (b.object_id, b.status)
    WHERE  b.status != 'VALID';

-- No not-matched clause, update only.
MERGE INTO test1 a
  USING all_objects b
    ON (a.object_id = b.object_id)
  WHEN MATCHED THEN
    UPDATE SET a.status = b.status
    WHERE  b.status != 'VALID';
```

### DELETE Clause

An optional `DELETE WHERE` clause can be added to the `MATCHED` clause to clean up after a merge operation. Only those rows in the destination table that match both the `ON` clause and the `DELETE WHERE` are deleted. If you add a `WHERE` clause to the update in the matched clause, we can think of this as additional match criteria for the delete, as only rows that are touched by the update are available for the `DELETE` clause to remove. Depending on which table the `DELETE WHERE` references, it can target the rows prior or post update. The following examples clarify this.

Create a source table with 5 rows as follows.

```sql
CREATE TABLE source AS
SELECT level AS id,
       CASE
         WHEN MOD(level, 2) = 0 THEN 10
         ELSE 20
       END AS status,
       'Description of level ' || level AS description
FROM   dual
CONNECT BY level <= 5;

SELECT * FROM source;

        ID     STATUS DESCRIPTION
---------- ---------- -----------------------
         1         20 Description of level 1
         2         10 Description of level 2
         3         20 Description of level 3
         4         10 Description of level 4
         5         20 Description of level 5

5 rows selected.

SQL>
```

Create the destination table using a similar query, but this time with 10 rows.

```sql
CREATE TABLE destination AS
SELECT level AS id,
       CASE
         WHEN MOD(level, 2) = 0 THEN 10
         ELSE 20
       END AS status,
       'Description of level ' || level AS description
FROM   dual
CONNECT BY level <= 10;

SELECT * FROM destination;

         1         20 Description of level 1
         2         10 Description of level 2
         3         20 Description of level 3
         4         10 Description of level 4
         5         20 Description of level 5
         6         10 Description of level 6
         7         20 Description of level 7
         8         10 Description of level 8
         9         20 Description of level 9
        10         10 Description of level 10

10 rows selected.

SQL>
```

The following `MERGE` statement will update all the rows in the destination table that have a matching row in the source table. The additional `DELETE WHERE` clause will delete only those rows that were matched, already in the destination table, and meet the criteria of the `DELETE WHERE` clause.

```sql
MERGE INTO destination d
  USING source s
    ON (s.id = d.id)
  WHEN MATCHED THEN
    UPDATE SET d.description = 'Updated'
    DELETE WHERE d.status = 10;

5 rows merged.

SQL>

SELECT * FROM destination;

        ID     STATUS DESCRIPTION
---------- ---------- -----------------------
         1         20 Updated
         3         20 Updated
         5         20 Updated
         6         10 Description of level 6
         7         20 Description of level 7
         8         10 Description of level 8
         9         20 Description of level 9
        10         10 Description of level 10

8 rows selected.

SQL>
```

Notice there are rows with a status of "10" that were not deleted. This is because there was no match between the source and destination for these rows, so the delete was not applicable.

The following example shows the `DELETE WHERE` can be made to match against values of the rows before the update operation, not after. In this case, all matching rows have their status changed to "10", but the `DELETE WHERE` references the source data, so the status is checked against the source, not the updated values.

```sql
ROLLBACK;

MERGE INTO destination d
  USING source s
    ON (s.id = d.id)
  WHEN MATCHED THEN
    UPDATE SET  d.description = 'Updated',
                d.status = 10
    DELETE WHERE s.status = 10;

5 rows merged.

SQL>

SELECT * FROM destination;

        ID     STATUS DESCRIPTION
---------- ---------- -----------------------
         1         10 Updated
         3         10 Updated
         5         10 Updated
         6         10 Description of level 6
         7         20 Description of level 7
         8         10 Description of level 8
         9         20 Description of level 9
        10         10 Description of level 10

8 rows selected.

SQL>
```

Notice, no extra rows were deleted compared to the previous example.

By switching the DELETE WHERE to reference the destination table, the extra updated rows can be deleted also.

```sql
ROLLBACK;

MERGE INTO destination d
  USING source s
    ON (s.id = d.id)
  WHEN MATCHED THEN
    UPDATE SET  d.description = 'Updated',
                d.status = 10
    DELETE WHERE d.status = 10;

5 rows merged.

SQL>

SELECT * FROM destination;

        ID     STATUS DESCRIPTION
---------- ---------- -----------------------
         6         10 Description of level 6
         7         20 Description of level 7
         8         10 Description of level 8
         9         20 Description of level 9
        10         10 Description of level 10

5 rows selected.
```
