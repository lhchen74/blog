---
title: Oracle Parse XML
tags: db
date: 2020-3-17
---

> 转载: [ORACLE-BASE - XMLTABLE : Convert XML Data into Rows and Columns using SQL](https://oracle-base.com/articles/misc/xmltable-convert-xml-data-into-rows-and-columns-using-sql)

## Tag-Based XML

This example uses tag-based XML, where each data element for an employee is surrounded by its own start and end tag.

First we create a table to hold our XML document and populate it with a document containing multiple rows of data. Using `XMLFOREST` gives us a separate tag for each column in the query.

```sql
CREATE TABLE xml_tab (
  id        NUMBER,
  xml_data  XMLTYPE
);

DECLARE
  l_xmltype XMLTYPE;
BEGIN
  SELECT XMLELEMENT("employees",
           XMLAGG(
             XMLELEMENT("employee",
               XMLFOREST(
                 e.empno AS "empno",
                 e.ename AS "ename",
                 e.job AS "job",
                 TO_CHAR(e.hiredate, 'DD-MON-YYYY') AS "hiredate"
               )
             )
           )
         )
  INTO   l_xmltype
  FROM   emp e;

  INSERT INTO xml_tab VALUES (1, l_xmltype);
  COMMIT;
END;
/
```

We can see the resulting row containing the tag-based XML using the following query.

```sql
SET LONG 5000
SELECT x.xml_data.getClobVal()
FROM   xml_tab x;

X.XML_DATA.GETCLOBVAL()
--------------------------------------------------------------------------------
<employees>
  <employee>
    <empno>7369</empno>
    <ename>SMITH</ename>
    <job>CLERK</job>
    <hiredate>17-DEC-1980</hiredate>
  </employee>
  <employee>
    <empno>7499</empno>
    <ename>ALLEN</ename>
    <job>SALESMAN</job>
    <hiredate>20-FEB-1981</hiredate>
  </employee>
  <employee>
    <empno>7521</empno>
    <ename>WARD</ename>
    <job>SALESMAN</job>
    <hiredate>22-FEB-1981</hiredate>
  </employee>
  <employee>
    <empno>7566</empno>
    <ename>JONES</ename>
    <job>MANAGER</job>
    <hiredate>02-APR-1981</hiredate>
  </employee>
  <employee>
    <empno>7654</empno>
    <ename>MARTIN</ename>
    <job>SALESMAN</job>
    <hiredate>28-SEP-1981</hiredate>
  </employee>
  <employee>
    <empno>7698</empno>
    <ename>BLAKE</ename>
    <job>MANAGER</job>
    <hiredate>01-MAY-1981</hiredate>
  </employee>
  <employee>
    <empno>7782</empno>
    <ename>CLARK</ename>
    <job>MANAGER</job>
    <hiredate>09-JUN-1981</hiredate>
  </employee>
  <employee>
    <empno>7788</empno>
    <ename>SCOTT</ename>
    <job>ANALYST</job>
    <hiredate>19-APR-1987</hiredate>
  </employee>
  <employee>
    <empno>7839</empno>
    <ename>KING</ename>
    <job>PRESIDENT</job>
    <hiredate>17-NOV-1981</hiredate>
  </employee>
  <employee>
    <empno>7844</empno>
    <ename>TURNER</ename>
    <job>SALESMAN</job>
    <hiredate>08-SEP-1981</hiredate>
  </employee>
  <employee>
    <empno>7876</empno>
    <ename>ADAMS</ename>
    <job>CLERK</job>
    <hiredate>23-MAY-1987</hiredate>
  </employee>
  <employee>
    <empno>7900</empno>
    <ename>JAMES</ename>
    <job>CLERK</job>
    <hiredate>03-DEC-1981</hiredate>
  </employee>
  <employee>
    <empno>7902</empno>
    <ename>FORD</ename>
    <job>ANALYST</job>
    <hiredate>03-DEC-1981</hiredate>
  </employee>
  <employee>
    <empno>7934</empno>
    <ename>MILLER</ename>
    <job>CLERK</job>
    <hiredate>23-JAN-1982</hiredate>
  </employee>
</employees>

1 row selected.

SQL>
```

The `XMLTABLE` operator allows us to split the XML data into rows and project columns on to it. We effectively make a cartesian product between the data table and the `XMLTABLE` call, which allows `XMLTABLE` to split a XML document in a single row into multiple rows in the final result set. The table column is identified as the source of the data using the `PASSING` clause. The rows are identified using a XQuery expression, in this case '/employees/employee'. Columns are projected onto the resulting XML fragments using the `COLUMNS` clause, which identifies the relevant tags using the `PATH` expression and assigns the desired column names and data types. Be careful with the names of the columns in the `COLUMNS` clause. If you use anything other than upper case, they will need to be quoted to make direct reference to them. Notice we are querying using the alias of the `XMLTABLE` call, rather than the regular table alias.

```sql
SELECT xt.*
FROM   xml_tab x,
       XMLTABLE('/employees/employee'
         PASSING x.xml_data
         COLUMNS
           empno     VARCHAR2(4)  PATH 'empno',
           ename     VARCHAR2(10) PATH 'ename',
           job       VARCHAR2(9)  PATH 'job',
           hiredate  VARCHAR2(11) PATH 'hiredate'
         ) xt;

EMPN ENAME      JOB       HIREDATE
---- ---------- --------- -----------
7369 SMITH      CLERK     17-DEC-1980
7499 ALLEN      SALESMAN  20-FEB-1981
7521 WARD       SALESMAN  22-FEB-1981
7566 JONES      MANAGER   02-APR-1981
7654 MARTIN     SALESMAN  28-SEP-1981
7698 BLAKE      MANAGER   01-MAY-1981
7782 CLARK      MANAGER   09-JUN-1981
7788 SCOTT      ANALYST   19-APR-1987
7839 KING       PRESIDENT 17-NOV-1981
7844 TURNER     SALESMAN  08-SEP-1981
7876 ADAMS      CLERK     23-MAY-1987
7900 JAMES      CLERK     03-DEC-1981
7902 FORD       ANALYST   03-DEC-1981
7934 MILLER     CLERK     23-JAN-1982

14 rows selected.

SQL>
```

## Attribute-Based XML

This example uses attribute-based XML, where each data element for an employee is defined as an attribute of the employee tag, not a separate tag.

Truncate the table we defined for the previous example and populate it with a document containing multiple rows of data. Using `XMLATTRIBUTES` creates an attribute for each column in the query.

```sql
TRUNCATE TABLE xml_tab;

DECLARE
  l_xmltype XMLTYPE;
BEGIN
  SELECT XMLELEMENT("employees",
           XMLAGG(
             XMLELEMENT("employee",
               XMLATTRIBUTES(
                 e.empno AS "empno",
                 e.ename AS "ename",
                 e.job AS "job",
                 TO_CHAR(e.hiredate, 'DD-MON-YYYY') AS "hiredate"
               )
             )
           )
         )
  INTO   l_xmltype
  FROM   emp e;

  INSERT INTO xml_tab VALUES (1, l_xmltype);
  COMMIT;
END;
/
```

We can see the resulting row containing the attribute-based XML using the following query.

```sql
SET LONG 5000
SELECT x.xml_data.getClobVal()
FROM   xml_tab x;

X.XML_DATA.GETCLOBVAL()
--------------------------------------------------------------------------------
<employees>
  <employee empno="7369" ename="SMITH" job="CLERK" hiredate="17-DEC-1980"/>
  <employee empno="7499" ename="ALLEN" job="SALESMAN" hiredate="20-FEB-1981"/>
  <employee empno="7521" ename="WARD" job="SALESMAN" hiredate="22-FEB-1981"/>
  <employee empno="7566" ename="JONES" job="MANAGER" hiredate="02-APR-1981"/>
  <employee empno="7654" ename="MARTIN" job="SALESMAN" hiredate="28-SEP-1981"/>
  <employee empno="7698" ename="BLAKE" job="MANAGER" hiredate="01-MAY-1981"/>
  <employee empno="7782" ename="CLARK" job="MANAGER" hiredate="09-JUN-1981"/>
  <employee empno="7788" ename="SCOTT" job="ANALYST" hiredate="19-APR-1987"/>
  <employee empno="7839" ename="KING" job="PRESIDENT" hiredate="17-NOV-1981"/>
  <employee empno="7844" ename="TURNER" job="SALESMAN" hiredate="08-SEP-1981"/>
  <employee empno="7876" ename="ADAMS" job="CLERK" hiredate="23-MAY-1987"/>
  <employee empno="7900" ename="JAMES" job="CLERK" hiredate="03-DEC-1981"/>
  <employee empno="7902" ename="FORD" job="ANALYST" hiredate="03-DEC-1981"/>
  <employee empno="7934" ename="MILLER" job="CLERK" hiredate="23-JAN-1982"/>
</employees>

1 row selected.

SQL>
```

The `XMLTABLE` operator allows us to split the XML data into rows and project columns on to it. Notice this time the `PATH` expression uses a "@" to indicate this is an attribute, rather than a tag.

```sql
SELECT xt.*
FROM   xml_tab x,
       XMLTABLE('/employees/employee'
         PASSING x.xml_data
         COLUMNS
           empno     VARCHAR2(4)  PATH '@empno',
           ename     VARCHAR2(10) PATH '@ename',
           job       VARCHAR2(9)  PATH '@job',
           hiredate  VARCHAR2(11) PATH '@hiredate'
         ) xt;

EMPN ENAME      JOB       HIREDATE
---- ---------- --------- -----------
7369 SMITH      CLERK     17-DEC-1980
7499 ALLEN      SALESMAN  20-FEB-1981
7521 WARD       SALESMAN  22-FEB-1981
7566 JONES      MANAGER   02-APR-1981
7654 MARTIN     SALESMAN  28-SEP-1981
7698 BLAKE      MANAGER   01-MAY-1981
7782 CLARK      MANAGER   09-JUN-1981
7788 SCOTT      ANALYST   19-APR-1987
7839 KING       PRESIDENT 17-NOV-1981
7844 TURNER     SALESMAN  08-SEP-1981
7876 ADAMS      CLERK     23-MAY-1987
7900 JAMES      CLERK     03-DEC-1981
7902 FORD       ANALYST   03-DEC-1981
7934 MILLER     CLERK     23-JAN-1982

14 rows selected.

SQL>
```

## Nested XML

So far we have dealt with simple XML, but we sometimes have to deal with XML containing multiple levels of nesting. The simplest way to handle this to deal with the first layer, presenting the next layer down as an XML fragment in an `XMLTYPE`, which can then be processed using `XMLTABLE` in the next step.

Truncate the test table and insert a row of nested XML. The example below produces a list of departments, with every department containing a nested list of employees for that department.

```sql
TRUNCATE TABLE xml_tab;

DECLARE
  l_xmltype XMLTYPE;
BEGIN
  SELECT XMLELEMENT("departments",
           XMLAGG(
             XMLELEMENT("department",
               XMLFOREST(
                 d.deptno AS "department_number",
                 d.dname AS "department_name",
                 (SELECT XMLAGG(
                           XMLELEMENT("employee",
                             XMLFOREST(
                               e.empno AS "employee_number",
                               e.ename AS "employee_name"
                             )
                           )
                         )
                  FROM   emp e
                  WHERE  e.deptno = d.deptno
                 ) "employees"
               )
             )
           )
         )
  INTO   l_xmltype
  FROM   dept d;

  INSERT INTO xml_tab VALUES (1, l_xmltype);
  COMMIT;
END;
/
```

We can see the resulting row containing the nested XML using the following query.

```sql
SET LONG 5000
SELECT x.xml_data.getClobVal()
FROM   xml_tab x;

X.XML_DATA.GETCLOBVAL()
--------------------------------------------------------------------------------
<departments>
  <department>
    <department_number>10</department_number>
    <department_name>ACCOUNTING</department_name>
    <employees>
      <employee>
        <employee_number>7782</employee_number>
        <employee_name>CLARK</employee_name>
      </employee>
      <employee>
        <employee_number>7839</employee_number>
        <employee_name>KING</employee_name>
      </employee>
      <employee>
        <employee_number>7934</employee_number>
        <employee_name>MILLER</employee_name>
      </employee>
    </employees>
  </department>
  <department>
    <department_number>20</department_number>
    <department_name>RESEARCH</department_name>
    <employees>
      <employee>
        <employee_number>7369</employee_number>
        <employee_name>SMITH</employee_name>
      </employee>
      <employee>
        <employee_number>7566</employee_number>
        <employee_name>JONES</employee_name>
      </employee>
      <employee>
        <employee_number>7788</employee_number>
        <employee_name>SCOTT</employee_name>
      </employee>
      <employee>
        <employee_number>7876</employee_number>
        <employee_name>ADAMS</employee_name>
      </employee>
      <employee>
        <employee_number>7902</employee_number>
        <employee_name>FORD</employee_name>
      </employee>
    </employees>
  </department>
  <department>
    <department_number>30</department_number>
    <department_name>SALES</department_name>
    <employees>
      <employee>
        <employee_number>7499</employee_number>
        <employee_name>ALLEN</employee_name>
      </employee>
      <employee>
        <employee_number>7521</employee_number>
        <employee_name>WARD</employee_name>
      </employee>
      <employee>
        <employee_number>7654</employee_number>
        <employee_name>MARTIN</employee_name>
      </employee>
      <employee>
        <employee_number>7698</employee_number>
        <employee_name>BLAKE</employee_name>
      </employee>
      <employee>
        <employee_number>7844</employee_number>
        <employee_name>TURNER</employee_name>
      </employee>
      <employee>
        <employee_number>7900</employee_number>
        <employee_name>JAMES</employee_name>
      </employee>
    </employees>
  </department>
  <department>
    <department_number>40</department_number>
    <department_name>OPERATIONS</department_name>
  </department>
</departments>


1 row selected.

SQL>
```

To make things simpler we've split out the layers using the `WITH` clause, but this could also be done with inline-views. The "departments_data" entry in the `WITH` clause extracts the basic department data, along with an XML fragment containing the employees for that department. The "employees_data" entry selects the department data from the "departments_data" entry, then extracts the employee information from the "employees" `XMLTYPE` using `XMLTABLE` in the normal way. Finally we select the flattened data from the "employees_data" entry.

```sql
WITH
  departments_data AS (
    SELECT xt.*
    FROM   xml_tab x,
           XMLTABLE('/departments/department'
             PASSING x.xml_data
             COLUMNS
               deptno     VARCHAR2(4)  PATH 'department_number',
               dname      VARCHAR2(10) PATH 'department_name',
               employees  XMLTYPE      PATH 'employees'
             ) xt
  ),
  employees_data AS (
    SELECT deptno,
           dname,
           xt2.*
    FROM   departments_data dd,
           XMLTABLE('/employees/employee'
             PASSING dd.employees
             COLUMNS
               empno      VARCHAR2(4)  PATH 'employee_number',
               ename      VARCHAR2(10) PATH 'employee_name'
             ) xt2
  )
SELECT * FROM employees_data;

DEPT DNAME      EMPN ENAME
---- ---------- ---- ----------
10   ACCOUNTING 7782 CLARK
10   ACCOUNTING 7839 KING
10   ACCOUNTING 7934 MILLER
20   RESEARCH   7369 SMITH
20   RESEARCH   7566 JONES
20   RESEARCH   7788 SCOTT
20   RESEARCH   7876 ADAMS
20   RESEARCH   7902 FORD
30   SALES      7499 ALLEN
30   SALES      7521 WARD
30   SALES      7654 MARTIN
30   SALES      7698 BLAKE
30   SALES      7844 TURNER
30   SALES      7900 JAMES

14 rows selected.

SQL>
```

That looks like it has worked, but we've lost department "40", which has no employees. If we want to show that row we need to do a `LEFT OUTER JOIN` between the "departments_data" entry and the `XMLTABLE`, as shown below. Notice the join condition of "1=1" in the second `WITH` clause entry.

```sql
WITH
  departments_data AS (
    SELECT xt.*
    FROM   xml_tab x,
           XMLTABLE('/departments/department'
             PASSING x.xml_data
             COLUMNS
               deptno     VARCHAR2(4)  PATH 'department_number',
               dname      VARCHAR2(10) PATH 'department_name',
               employees  XMLTYPE      PATH 'employees'
             ) xt
  ),
  employees_data AS (
    SELECT deptno,
           dname,
           xt2.*
    FROM   departments_data dd
           LEFT OUTER JOIN
             XMLTABLE('/employees/employee'
               PASSING dd.employees
               COLUMNS
                 empno      VARCHAR2(4)  PATH 'employee_number',
                 ename      VARCHAR2(10) PATH 'employee_name'
               ) xt2 ON 1=1
  )
SELECT * FROM employees_data;

DEPT DNAME      EMPN ENAME
---- ---------- ---- ----------
10   ACCOUNTING 7782 CLARK
10   ACCOUNTING 7839 KING
10   ACCOUNTING 7934 MILLER
20   RESEARCH   7369 SMITH
20   RESEARCH   7566 JONES
20   RESEARCH   7788 SCOTT
20   RESEARCH   7876 ADAMS
20   RESEARCH   7902 FORD
30   SALES      7499 ALLEN
30   SALES      7521 WARD
30   SALES      7654 MARTIN
30   SALES      7698 BLAKE
30   SALES      7844 TURNER
30   SALES      7900 JAMES
40   OPERATIONS

15 rows selected.

SQL>
```

## XML Data in Variables

Not all XML data you want to process is already stored in a table. In some cases, the XML is stored in a PL/SQL variable. The `XMLTABLE` operator can work with this also.

```sql
SET SERVEROUTPUT ON
DECLARE
  l_xml VARCHAR2(32767);
BEGIN
  l_xml := '<employees>
  <employee>
    <empno>7369</empno>
    <ename>SMITH</ename>
    <job>CLERK</job>
    <hiredate>17-DEC-1980</hiredate>
  </employee>
  <employee>
    <empno>7499</empno>
    <ename>ALLEN</ename>
    <job>SALESMAN</job>
    <hiredate>20-FEB-1981</hiredate>
  </employee>
</employees>';

  FOR cur_rec IN (
    SELECT xt.*
    FROM   XMLTABLE('/employees/employee'
             PASSING XMLTYPE(l_xml)
             COLUMNS
               empno     VARCHAR2(4)  PATH 'empno',
               ename     VARCHAR2(10) PATH 'ename',
               job       VARCHAR2(9)  PATH 'job',
               hiredate  VARCHAR2(11) PATH 'hiredate'
             ) xt)
  LOOP
    DBMS_OUTPUT.put_line('empno=' || cur_rec.empno ||
                         '  ename=' || cur_rec.ename ||
                         '  job=' || cur_rec.job||
                         '  hiredate=' || cur_rec.hiredate);
  END LOOP;
END;
/
empno=7369  ename=SMITH  job=CLERK  hiredate=17-DEC-1980
empno=7499  ename=ALLEN  job=SALESMAN  hiredate=20-FEB-1981

PL/SQL procedure successfully completed.

SQL>
```

In the previous example, the XML was being held in regular string variable, so we we had to convert it to an `XMLTYPE` using a constructor in the `PASSING` clause. If the data had already been in an `XMLTYPE` variable, this constructor would not have been necessary. Let's repeat the previous example, but put the XML into an `XMLTYPE` before using `XMLTABLE` on it. Notice the `PASSING` clause no longer needs the `XMLTYPE` constructor.

```sql
SET SERVEROUTPUT ON
DECLARE
  l_xml XMLTYPE;
BEGIN
  l_xml := XMLTYPE('<employees>
  <employee>
    <empno>7369</empno>
    <ename>SMITH</ename>
    <job>CLERK</job>
    <hiredate>17-DEC-1980</hiredate>
  </employee>
  <employee>
    <empno>7499</empno>
    <ename>ALLEN</ename>
    <job>SALESMAN</job>
    <hiredate>20-FEB-1981</hiredate>
  </employee>
</employees>');

  FOR cur_rec IN (
    SELECT xt.*
    FROM   XMLTABLE('/employees/employee'
             PASSING l_xml
             COLUMNS
               empno     VARCHAR2(4)  PATH 'empno',
               ename     VARCHAR2(10) PATH 'ename',
               job       VARCHAR2(9)  PATH 'job',
               hiredate  VARCHAR2(11) PATH 'hiredate'
             ) xt)
  LOOP
    DBMS_OUTPUT.put_line('empno=' || cur_rec.empno ||
                         '  ename=' || cur_rec.ename ||
                         '  job=' || cur_rec.job||
                         '  hiredate=' || cur_rec.hiredate);
  END LOOP;
END;
/
empno=7369  ename=SMITH  job=CLERK  hiredate=17-DEC-1980
empno=7499  ename=ALLEN  job=SALESMAN  hiredate=20-FEB-1981

PL/SQL procedure successfully completed.

SQL>
```

Here's a more complicated example of using `XMLTABLE` against some XML returned from an OBIEE web service.

```sql
SET SERVEROUTPUT ON
DECLARE
  l_xml     VARCHAR2(32767);
BEGIN
  l_xml := '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:sawsoap="urn://oracle.bi.webservices/v6">
   <soap:Body>
      <sawsoap:executeSQLQueryResult>
         <sawsoap:return xsi:type="sawsoap:QueryResults">
            <sawsoap:rowset>
<![CDATA[<rowset xmlns="urn:schemas-microsoft-com:xml-analysis:rowset">
<Row><Column0>1000</Column0><Column1>East Region</Column1></Row>
<Row><Column0>2000</Column0><Column1>West Region</Column1></Row>
<Row><Column0>1500</Column0><Column1>Central Region</Column1></Row>
</rowset>]]>
</sawsoap:rowset>
            <sawsoap:queryID/>
            <sawsoap:finished>true</sawsoap:finished>
         </sawsoap:return>
      </sawsoap:executeSQLQueryResult>
   </soap:Body>
</soap:Envelope>';

  FOR cur_rec IN (
    SELECT a.mydata, xt.*
    FROM   (
            -- Pull out just the CDATA value.
            SELECT EXTRACTVALUE(XMLTYPE(l_xml), '//sawsoap:rowset/text()','xmlns:sawsoap="urn://oracle.bi.webservices/v6"') AS mydata
            FROM dual
           ) a,
           -- Specify the path that marks a new row, remembering to use the correct namespace.
           XMLTABLE(XMLNAMESPACES(default 'urn:schemas-microsoft-com:xml-analysis:rowset'), '/rowset/Row'
             PASSING XMLTYPE(a.mydata)
             COLUMNS
               column0  NUMBER(4)    PATH 'Column0',
               column1  VARCHAR2(20) PATH 'Column1'
             ) xt)
  LOOP
    DBMS_OUTPUT.put_line('column0=' || cur_rec.column0 || '  column1=' || cur_rec.column1);
  END LOOP;
END;
/
column0=1000  column1=East Region
column0=2000  column1=West Region
column0=1500  column1=Central Region

PL/SQL procedure successfully completed.

SQL>
```

## Filtering Rows with XPath

We can limit the rows returned by altering the XPath expression. In the following example we only return rows with the job type of "CLERK".

```sql
SELECT xt.*
FROM   xml_tab x,
       XMLTABLE('/employees/employee[job="CLERK"]'
         PASSING x.xml_data
         COLUMNS
           empno     VARCHAR2(4)  PATH 'empno',
           ename     VARCHAR2(10) PATH 'ename',
           job       VARCHAR2(9)  PATH 'job',
           hiredate  VARCHAR2(11) PATH 'hiredate'
         ) xt;

EMPN ENAME      JOB       HIREDATE
---- ---------- --------- -----------
7369 SMITH      CLERK     17-DEC-1980
7876 ADAMS      CLERK     23-MAY-1987
7900 JAMES      CLERK     03-DEC-1981
7934 MILLER     CLERK     23-JAN-1982

4 rows selected.

SQL>
```

We could parameterise the job type using variable in the XPath, which is prefixed with a "\$". The value for this variable is then passed in the `PASSING` clause. The variable must be aliases using `AS` and double quoted to make sure the name and case matches that of the variable in the XPath expression.

```sql
VARIABLE v_job VARCHAR2(10);
EXEC :v_job := 'CLERK';

SELECT xt.*
FROM   xml_tab x,
       XMLTABLE('/employees/employee[job=$job]'
         PASSING x.xml_data, :v_job AS "job"
         COLUMNS
           empno     VARCHAR2(4)  PATH 'empno',
           ename     VARCHAR2(10) PATH 'ename',
           job       VARCHAR2(9)  PATH 'job',
           hiredate  VARCHAR2(11) PATH 'hiredate'
         ) xt;

EMPN ENAME      JOB       HIREDATE
---- ---------- --------- -----------
7369 SMITH      CLERK     17-DEC-1980
7876 ADAMS      CLERK     23-MAY-1987
7900 JAMES      CLERK     03-DEC-1981
7934 MILLER     CLERK     23-JAN-1982

4 rows selected.

SQL>
```

## Performance

The `XMLTABLE` operator works really well with small XML documents, or tables with many rows, each of which contain a small XML document. As the XML documents get bigger the performance gets worse compared to the [manual parse](https://oracle-base.com/articles/9i/parse-xml-documents-9i) method. When dealing with large XML documents you may have to forgo the convenience for the `XMLTABLE` operator in favour of a manual solution.
