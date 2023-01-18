---
title: Oracle DML RETURNING INTO Clause
tags: db
date: 2022-03-31
---

## Setup

The following test table is used to demonstrate `RETURNING INTO` clause.

```sql
DROP TABLE t1;
DROP SEQUENCE t1_seq;

CREATE TABLE t1 (
  id NUMBER(10),
  description VARCHAR2(50),
  CONSTRAINT t1_pk PRIMARY KEY (id)
);

CREATE SEQUENCE t1_seq;

INSERT INTO t1 VALUES (t1_seq.nextval, 'ONE');
INSERT INTO t1 VALUES (t1_seq.nextval, 'TWO');
INSERT INTO t1 VALUES (t1_seq.nextval, 'THREE');
COMMIT;
```

## Basic INSERT, UPDATE and DELETE

The `RETURNING INTO` clause allows us to return column values for rows affected by DML statements. The returned data could be a single column, multiple columns or expressions.

When we insert data using a sequence to generate our primary key value, we can return the primary key value as follows.

```sql
SET SERVEROUTPUT ON
DECLARE
  l_id t1.id%TYPE;
BEGIN
  INSERT INTO t1 VALUES (t1_seq.nextval, 'FOUR')
  RETURNING id INTO l_id;
  COMMIT;

  DBMS_OUTPUT.put_line('ID=' || l_id);
END;
/
ID=4

PL/SQL procedure successfully completed.

SQL>
```

The syntax is also available for update and delete statements.

```sql
SET SERVEROUTPUT ON
DECLARE
  l_id t1.id%TYPE;
BEGIN
  UPDATE t1
  SET    description = description
  WHERE  description = 'FOUR'
  RETURNING id INTO l_id;

  DBMS_OUTPUT.put_line('UPDATE ID=' || l_id);

  DELETE FROM t1
  WHERE  description = 'FOUR'
  RETURNING id INTO l_id;

  DBMS_OUTPUT.put_line('DELETE ID=' || l_id);

  COMMIT;
END;
/
UPDATE ID=4
DELETE ID=4

PL/SQL procedure successfully completed.

SQL>
```

## DML Affecting Multiple Rows - Returning Into Collections

When DML affects multiple rows we can still use the `RETURNING INTO` clause, but if we want values returned for all rows touched we must return the values into a collection using the `BULK COLLECT` clause.

```sql
SET SERVEROUTPUT ON
DECLARE
  TYPE t_tab IS TABLE OF t1.id%TYPE;
  l_tab t_tab;
BEGIN
  UPDATE t1
  SET    description = description
  RETURNING id BULK COLLECT INTO l_tab;

  FOR i IN l_tab.first .. l_tab.last LOOP
    DBMS_OUTPUT.put_line('UPDATE ID=' || l_tab(i));
  END LOOP;

  COMMIT;
END;
/
UPDATE ID=1
UPDATE ID=2
UPDATE ID=3

PL/SQL procedure successfully completed.

SQL>
```

We can also use the `RETURNING INTO` clause in combination with bulk binds.

```sql
SET SERVEROUTPUT ON
DECLARE
  TYPE t_desc_tab IS TABLE OF t1.description%TYPE;
  TYPE t_tab IS TABLE OF t1%ROWTYPE;
  l_desc_tab t_desc_tab := t_desc_tab('FIVE', 'SIX', 'SEVEN');
  l_tab   t_tab;
BEGIN

  FORALL i IN l_desc_tab.first .. l_desc_tab.last
    INSERT INTO t1 VALUES (t1_seq.nextval, l_desc_tab(i))
    RETURNING id, description BULK COLLECT INTO l_tab;

  FOR i IN l_tab.first .. l_tab.last LOOP
    DBMS_OUTPUT.put_line('INSERT ID=' || l_tab(i).id ||
                         ' DESC=' || l_tab(i).description);
  END LOOP;

  COMMIT;
END;
/
INSERT ID=5 DESC=FIVE
INSERT ID=6 DESC=SIX
INSERT ID=7 DESC=SEVEN

PL/SQL procedure successfully completed.

SQL>
```

This functionality is also available from dynamic SQL.

```sql
SET SERVEROUTPUT ON
DECLARE
  TYPE t_tab IS TABLE OF t1.id%TYPE;
  l_tab t_tab;
BEGIN
  EXECUTE IMMEDIATE 'UPDATE t1
                     SET    description = description
                     RETURNING id INTO :l_tab'
  RETURNING BULK COLLECT INTO l_tab;

  FOR i IN l_tab.first .. l_tab.last LOOP
    DBMS_OUTPUT.put_line('UPDATE ID=' || l_tab(i));
  END LOOP;

  COMMIT;
END;
/
UPDATE ID=1
UPDATE ID=2
UPDATE ID=3

PL/SQL procedure successfully completed.

SQL>
```

## DML Affecting Multiple Rows - Returning With Aggregations

We are not forced to use collections when using the `RETURNING INTO` clause with DML that affects multiple rows. If the output is aggregated, it can be placed into a regular variable. Thanks to [Oren Nakdimon](http://db-oriented.com/2017/05/12/returning-into/) for making me aware of this.

```sql
SET SERVEROUTPUT ON
DECLARE
  l_max_id NUMBER;
BEGIN
  UPDATE t1
  SET    description = description
  RETURNING MAX(id) INTO l_max_id;

  DBMS_OUTPUT.put_line('l_max_id=' || l_max_id);

  COMMIT;
END;
/
l_max_id=3

PL/SQL procedure successfully completed.

SQL>
```

For more information see:

-   [RETURNING INTO Clause](http://docs.oracle.com/cd/B28359_01/appdev.111/b28370/returninginto_clause.htm)

## Comments

`RETURNING INTO` can not use for `INSERT INTO ... SELECT ...`

```sql
CREATE OR REPLACE TRIGGER YSC.som_hub_dn_upload_header_bi1 BEFORE
INSERT ON som_hub_dn_upload_header FOR EACH ROW WHEN (NEW.header_id is null)
BEGIN
  SELECT som_hub_dn_upload_header_s.NEXTVAL INTO :NEW.header_id FROM DUAL;
END;
```

```sql
DECLARE
  l_header_id number;
BEGIN
  INSERT INTO som_hub_dn_upload_header
    (DELIVERY_ID,
     DELIVERY_NAME,
     ETA_DATE,
     DELIVERY_QUANTITY,
     WAREHOUSE,
     LOCATION,
     SHIPPING_DATE,
     CUSTOMER_PO)
    SELECT DISTINCT seh.delivery_id,
                    seh.delivery_id,
                    sysdate,
                    seh.delivery_quantity,
                    'MS',
                    'K' || sev.account_number,
                    seh.ship_date,
                    seh.customer_po
      FROM som_edi_856_header seh,
           som_edi_customer_sites_v sev
     WHERE seh.customer_id = sev.cust_account_id
       AND seh.delivery_id = '82418'
    RETURNING INTO l_header_id;
END;

-- ORA-06550: line 24, column 5:
-- PL/SQL: ORA-00933: SQL command not properly ended
-- ORA-06550: line 4, column 3:
-- PL/SQL: SQL Statement ignored
```
