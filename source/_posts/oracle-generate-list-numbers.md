---
title: SQL Server vs. Oracle Generate Series or List of Numbers
date: 2022-09-14
tags: db
---

> 转载：[SQL Server vs. Oracle: Generate Series or List of Numbers](https://sqlbisam.blogspot.com/2014/01/generate-series-or-list-of-numbers.html)

To generate a list of numbers or series in Oracle or SQL Server, we need to use recursive CTE, if we call the CTE within the CTE then it is called recursive CTE.

## SQL Server

```sql
WITH REC_CTE(ROW_NUM) AS (
    --create first record, if we want to start the series from 10 then change it from 1 to 10
    SELECT 1 AS ROW_NUM
    UNION ALL
    --calling REC_CTE within REC_CTE and add value 1 to get next number
    SELECT ROW_NUM+1 FROM REC_CTE
    --limit the number of rows
    WHERE ROW_NUM<100
)
--now select the CTE to get the list of values
SELECT * FROM REC_CTE;
```

## Oracle

### Oracle 11g version 2 and higher

```sql
WITH REC_CTE(ROW_NUM) AS (
    --create first record, if we want to start the series from 10 then change it from 1 to 10
    SELECT 1 AS ROW_NUM FROM DUAL
    UNION ALL
    --calling REC_CTE within REC_CTE and add value 1 to get next number
    SELECT ROW_NUM+1 FROM REC_CTE
    --limit the number of rows to 100
    WHERE ROW_NUM<100
)
--now select the CTE to get the list of values
SELECT * FROM REC_CTE;
```

### Oracle Other

Oracle provides a set of hierarchy functions such as START WITH, LEVEL, PRIOR, CONNECT BY, CONNECT_BY_ROOT.

Example1:

```sql
--below script will retrieve first hundred numbers

SELECT ROWNUM FROM DUAL
--limit the number of rows to 100
CONNECT BY ROWNUM <= 100;
```

Example2:

```sql
--we can use level if we want to create a series from number other than 1

SELECT LEVEL AS LVL FROM DUAL
-- if we want to start the series from 10 then change it from 3 to 10
WHERE LEVEL >=3
--limit the number of rows to 100
CONNECT BY LEVEL<100
```

If you need to check the version of oracle, use below script.

```sql
SELECT * FROM V$VERSION
WHERE BANNER LIKE 'ORACLE%';
```

Above we have added 1 when we called the CTE with in CTE, if we add 2 then we will get even number series and so on.

## Comments

In SQL Server column alias list is not necessary, we can prune `REC_CTE(ROW_NUM)` to `REC_CTE`. But in Oracle will occurs _ORA-32039: recursive WITH clause must have column alias list_ error.

```sql
WITH REC_CTE AS (
    SELECT 1 AS ROW_NUM
    UNION ALL
    SELECT ROW_NUM + 1 FROM REC_CTE
    WHERE ROW_NUM < 100
)

SELECT * FROM REC_CTE;
```
