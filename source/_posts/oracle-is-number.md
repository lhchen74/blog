---
title: Oracle Check IS NUMBER
date: 2021-11-05
tags: db
---

> 转载：[IS NUMBER - Oracle FAQ](https://www.orafaq.com/wiki/IS_NUMBER)

Oracle doesn't have a built-in **IS_NUMERIC** function to check is a value is numeric, but over the years people developed innovative alternatives. This page will discuss some of them:

## SQL solution

Pure SQL solutions usually use [TRANSLATE](https://www.orafaq.com/wiki/TRANSLATE) or [REGEXP_LIKE](https://www.orafaq.com/wiki/index.php?title=REGEXP_LIKE&action=edit&redlink=1) to identify numeric data. Some examples:

```sql
SELECT CASE WHEN TRIM(TRANSLATE(col1, '0123456789-,.', ' ')) IS NULL
            THEN 'numeric'
            ELSE 'alpha'
       END
FROM tab1;

SELECT CASE WHEN REGEXP_LIKE(col1, '^\d+(\.\d+)?$')
            THEN 'numeric'
            ELSE 'alpha'
      END
FROM  tab1;
```

## PL/SQL solution

A more elegant method would be to create a PL/SQL function that can be used for checking:

```sql
CREATE OR REPLACE FUNCTION is_number (p_string IN VARCHAR2)
  RETURN INT
IS
  v_num NUMBER;
BEGIN
  v_num := TO_NUMBER(p_string);
  RETURN 1;
EXCEPTION
WHEN VALUE_ERROR THEN
  RETURN 0;
END is_number;
/
```

## Comments

Find not null and not numerical value.

```sql
SELECT col1
  FROM tab1
 WHERE col1 IS NOT NULL
   AND CASE WHEN REGEXP_LIKE(col1, '^\d+(\.\d+)?$')
            THEN 'numeric'
            ELSE 'alpha'
       END = 'alpha';
```
