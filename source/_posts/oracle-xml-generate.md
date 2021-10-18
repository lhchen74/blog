---
title: Oracle Generate Xml
tags: db
date: 2020-3-17
---

> 转载: [ORACLE-BASE - SQL/XML (SQLX) : Generating XML using SQL](https://oracle-base.com/articles/misc/sqlxml-sqlx-generating-xml-content-using-sql)

The example code in this article assumes you have access to the SCOTT schema.

## The Past

In Oracle 9i Release 1 it was necessary to use several database object types to create complex XML documents using SQL.

```sql
CREATE TYPE emp_row AS OBJECT (
  EMPNO     NUMBER(4),
  ENAME     VARCHAR2(10),
  JOB       VARCHAR2(9),
  MGR       NUMBER(4),
  HIREDATE  DATE,
  SAL       NUMBER(7,2),
  COMM      NUMBER(7,2)
);
/

CREATE TYPE emp_tab AS TABLE OF emp_row;
/

CREATE TYPE dept_row AS OBJECT (
  DEPTNO    NUMBER(2),
  DNAME     VARCHAR2(14),
  LOC       VARCHAR2(13),
  EMP_LIST  emp_tab
);
/

SELECT SYS_XMLAGG (
         SYS_XMLGEN(
           dept_row(
             d.deptno, d.dname, d.loc,
             CAST(MULTISET(SELECT e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm
                           FROM   emp e
                           WHERE  e.deptno = d.deptno) AS emp_tab)
           ),
           SYS.XMLGENFORMATtYPE.createFormat('DEPT')
         )
       ) AS "XML_QUERY"
FROM   dept d
WHERE  d.deptno = 10;

XML_QUERY
----------------------------------------------------------------------------------------------------
<?xml version="1.0"?>
<ROWSET>
  <DEPT>
    <DEPTNO>10</DEPTNO>
    <DNAME>ACCOUNTING</DNAME>
    <LOC>NEW YORK</LOC>
    <EMP_LIST>
      <EMP_ROW>
        <EMPNO>7782</EMPNO>
        <ENAME>CLARK</ENAME>
        <JOB>MANAGER</JOB>
        <MGR>7839</MGR>
        <HIREDATE>09-JUN-1981 00:00:00</HIREDATE>
        <SAL>2450</SAL>
      </EMP_ROW>
      <EMP_ROW>
        <EMPNO>7839</EMPNO>
        <ENAME>KING</ENAME>
        <JOB>PRESIDENT</JOB>
        <HIREDATE>17-NOV-1981 00:00:00</HIREDATE>
        <SAL>5000</SAL>
      </EMP_ROW>
      <EMP_ROW>
        <EMPNO>7934</EMPNO>
        <ENAME>MILLER</ENAME>
        <JOB>CLERK</JOB>
        <MGR>7782</MGR>
        <HIREDATE>23-JAN-1982 00:00:00</HIREDATE>
        <SAL>1300</SAL>
      </EMP_ROW>
    </EMP_LIST>
  </DEPT>
</ROWSET>

1 row selected.

SQL>
```

This may cause administration problems as the number of database object types will increase drastically as the number of XML extracts increase.

## SQL/XML Functions

The SQL/XML functions present in Oracle9i Release 2 allow nested structures to be queried in a standard way with no additional database object definitions. In this article I will only present those I use most frequently.

### XMLELEMENT

The `XMLELEMENT` function is the basic unit for turning column data into XML fragments. In the following example, the first parameter specifies the tag name to be used and the second specifies the column that will supply the data contained within the tag.

```sql
SELECT XMLELEMENT("name", e.ename) AS employee
FROM   emp e
WHERE  e.empno = 7782;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<name>CLARK</name>

1 row selected.

SQL>
```

The `XMLELEMENT` function can also be used to group together and place a tag around existing XML fragments.

```sql
SELECT XMLELEMENT("employee",
         XMLELEMENT("works_number", e.empno),
         XMLELEMENT("name", e.ename)
       ) AS employee
FROM   emp e
WHERE  e.empno = 7782;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employee><works_number>7782</works_number><name>CLARK</name></employee>

1 row selected.

SQL>
```

### XMLATTRIBUTES

The `XMLATRIBUTES` function converts column data into attributes of the parent element. The function call should contain one or more columns in a comma separated list. The attribute names will match the column names using the default uppercase unless an alias is used.

```sql
SELECT XMLELEMENT("employee",
         XMLATTRIBUTES(
           e.empno AS "works_number",
           e.ename AS "name")
       ) AS employee
FROM   emp e
WHERE  e.empno = 7782;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employee works_number="7782" name="CLARK"></employee>

1 row selected.

SQL>
```

The parent `XMLELEMENT` can contain both attributes and child tags.

```sql
SELECT XMLELEMENT("employee",
         XMLATTRIBUTES(e.empno AS "works_number"),
         XMLELEMENT("name",e.ename),
         XMLELEMENT("job",e.job)
       ) AS employee
FROM   emp e
WHERE  e.empno = 7782;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employee works_number="7782"><name>CLARK</name><job>MANAGER</job></employee>

1 row selected.

SQL>
```

### XMLFOREST

Using `XMLELEMENT` to deal with lots of columns is rather clumsy. Like `XMLATTRIBUTES`, the `XMLFOREST` function allows you to process multiple columns at once.

```sql
SELECT XMLELEMENT("employee",
         XMLFOREST(
           e.empno AS "works_number",
           e.ename AS "name",
           e.job AS "job")
       ) AS employee
FROM   emp e
WHERE  e.empno = 7782;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employee><works_number>7782</works_number><name>CLARK</name><job>MANAGER</job></employee>

1 row selected.

SQL>
```

### XMLAGG

So far we have just looked at creating individual XML fragments. What happens if we start dealing with multiple rows of data?

```sql
SELECT XMLELEMENT("employee",
         XMLFOREST(
           e.empno AS "works_number",
           e.ename AS "name")
       ) AS employees
FROM   emp e
WHERE  e.deptno = 10;

EMPLOYEES
----------------------------------------------------------------------------------------------------
<employee><works_number>7782</works_number><name>CLARK</name></employee>
<employee><works_number>7839</works_number><name>KING</name></employee>
<employee><works_number>7934</works_number><name>MILLER</name></employee>

3 rows selected.

SQL>
```

We got the XML we wanted, but it is returned as three fragments in three separate rows. The `XMLAGG` function allows is to aggregate these separate fragments into a single fragment. In the following example we can see the three fragments are now presented in a single row.

```sql
SELECT XMLAGG(
         XMLELEMENT("employee",
           XMLFOREST(
             e.empno AS "works_number",
             e.ename AS "name")
         )
       ) AS employees
FROM   emp e
WHERE  e.deptno = 10;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employee><works_number>7782</works_number><name>CLARK</name></employee><employee><works_number>7839
</works_number><name>KING</name></employee><employee><works_number>7934</works_number><name>MILLER</
name></employee>

1 row selected.

SQL>
```

Without a root (base) tag, this is not a well formed document, so we must surround it in an `XMLELEMENT`

```sql
SELECT XMLELEMENT("employees",
         XMLAGG(
           XMLELEMENT("employee",
             XMLFOREST(
               e.empno AS "works_number",
               e.ename AS "name")
           )
         )
       ) AS employees
FROM   emp e
WHERE  e.deptno = 10;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employees><employee><works_number>7782</works_number><name>CLARK</name></employee><employee><works_
number>7839</works_number><name>KING</name></employee><employee><works_number>7934</works_number><na
me>MILLER</name></employee></employees>

1 row selected.

SQL>
```

### XMLROOT

The `XMLROOT` function allows us to place an XML declaration tag at the start of our XML document. In newer database versions, this function is either deprecated, or removed entirely. If you need and XML declaration, you should add it manually to the document.

```sql
SELECT XMLROOT(
         XMLELEMENT("employees",
           XMLAGG(
             XMLELEMENT("employee",
               XMLFOREST(
                 e.empno AS "works_number",
                 e.ename AS "name")
             )
           )
         )
       ) AS employees
FROM   emp e
WHERE  e.deptno = 10;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<?xml version="1.0" encoding="US-ASCII"?>
<employees>
  <employee>
    <works_number>7782</works_number>
    <name>CLARK</name>
  </employee>
  <employee>
    <works_number>7839</works_number>
    <name>KING</name>
  </employee>
  <employee>
    <works_number>7934</works_number>
    <name>MILLER</name>
  </employee>
</employees>

1 row selected.

SQL>
```

### XMLCDATA

The `XMLCDATA` function surrounds column data with a CDATA tag.

```sql
SELECT XMLELEMENT("employees",
         XMLAGG(
           XMLELEMENT("employee",
             XMLFOREST(
               e.empno AS "works_number",
               XMLCDATA(e.ename) AS "name")
           )
         )
       ) AS employees
FROM   emp e
WHERE  e.deptno = 10;

EMPLOYEE
----------------------------------------------------------------------------------------------------
<employees>
  <employee>
    <works_number>7782</works_number>
    <name><![CDATA[CLARK]]></name>
  </employee>
  <employee>
    <works_number>7839</works_number>
    <name><![CDATA[KING]]></name>
  </employee>
  <employee>
    <works_number>7934</works_number>
    <name><![CDATA[MILLER]]></name>
  </employee>
</employees>


1 row selected.

SQL>
```

## Putting It Together

The following example shows something a little more complex, including a nested query.

```sql
SELECT XMLELEMENT("dept_list",
         XMLAGG (
           XMLELEMENT("dept",
             XMLATTRIBUTES(d.deptno AS "deptno"),
             XMLFOREST(
               d.deptno AS "deptno",
               d.dname AS "dname",
               d.loc AS "loc",
               (SELECT XMLAGG(
                         XMLELEMENT("emp",
                           XMLFOREST(
                             e.empno AS "empno",
                             e.ename AS "ename",
                             e.job AS "job",
                             e.mgr AS "mgr",
                             e.hiredate AS "hiredate",
                             e.sal AS "sal",
                             e.comm AS "comm"
                           )
                         )
                       )
                FROM   emp e
                WHERE  e.deptno = d.deptno
               ) "emp_list"
             )
           )
         )
       ) AS "depts"
FROM   dept d
WHERE  d.deptno = 10;

depts
----------------------------------------------------------------------------------------------------
<dept_list>
  <dept deptno="10">
    <deptno>10</deptno>
    <dname>ACCOUNTING</dname>
    <loc>NEW YORK</loc>
    <emp_list>
      <emp>
        <empno>7782</empno>
        <ename>CLARK</ename>
        <job>MANAGER</job>
        <mgr>7839</mgr>
        <hiredate>1981-06-09</hiredate>
        <sal>2450</sal>
      </emp>
      <emp>
        <empno>7839</empno>
        <ename>KING</ename>
        <job>PRESIDENT</job>
        <hiredate>1981-11-17</hiredate>
        <sal>5000</sal>
      </emp>
      <emp>
        <empno>7934</empno>
        <ename>MILLER</ename>
        <job>CLERK</job>
        <mgr>7782</mgr>
        <hiredate>1982-01-23</hiredate>
        <sal>1300</sal>
      </emp>
    </emp_list>
  </dept>
</dept_list>

1 row selected.

SQL>
```
