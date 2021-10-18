---
title: Oracle With
tags: db
date: 2020-01-21
---

> 转载: [ORACLE-BASE - WITH Clause : Subquery Factoring in Oracle](https://oracle-base.com/articles/misc/with-clause)

## Setup

The examples below use the following tables.

```sql
-- DROP TABLE EMP PURGE;
-- DROP TABLE DEPT PURGE;

CREATE TABLE DEPT (
  DEPTNO NUMBER(2) CONSTRAINT PK_DEPT PRIMARY KEY,
  DNAME VARCHAR2(14),
  LOC VARCHAR2(13)
) ;

CREATE TABLE EMP (
  EMPNO NUMBER(4) CONSTRAINT PK_EMP PRIMARY KEY,
  ENAME VARCHAR2(10),
  JOB VARCHAR2(9),
  MGR NUMBER(4),
  HIREDATE DATE,
  SAL NUMBER(7,2),
  COMM NUMBER(7,2),
  DEPTNO NUMBER(2) CONSTRAINT FK_DEPTNO REFERENCES DEPT
);

INSERT INTO DEPT VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES (30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES (40,'OPERATIONS','BOSTON');

INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,to_date('17-12-1980','dd-mm-yyyy'),800,NULL,20);
INSERT INTO EMP VALUES (7499,'ALLEN','SALESMAN',7698,to_date('20-2-1981','dd-mm-yyyy'),1600,300,30);
INSERT INTO EMP VALUES (7521,'WARD','SALESMAN',7698,to_date('22-2-1981','dd-mm-yyyy'),1250,500,30);
INSERT INTO EMP VALUES (7566,'JONES','MANAGER',7839,to_date('2-4-1981','dd-mm-yyyy'),2975,NULL,20);
INSERT INTO EMP VALUES (7654,'MARTIN','SALESMAN',7698,to_date('28-9-1981','dd-mm-yyyy'),1250,1400,30);
INSERT INTO EMP VALUES (7698,'BLAKE','MANAGER',7839,to_date('1-5-1981','dd-mm-yyyy'),2850,NULL,30);
INSERT INTO EMP VALUES (7782,'CLARK','MANAGER',7839,to_date('9-6-1981','dd-mm-yyyy'),2450,NULL,10);
INSERT INTO EMP VALUES (7788,'SCOTT','ANALYST',7566,to_date('13-JUL-87','dd-mm-rr')-85,3000,NULL,20);
INSERT INTO EMP VALUES (7839,'KING','PRESIDENT',NULL,to_date('17-11-1981','dd-mm-yyyy'),5000,NULL,10);
INSERT INTO EMP VALUES (7844,'TURNER','SALESMAN',7698,to_date('8-9-1981','dd-mm-yyyy'),1500,0,30);
INSERT INTO EMP VALUES (7876,'ADAMS','CLERK',7788,to_date('13-JUL-87', 'dd-mm-rr')-51,1100,NULL,20);
INSERT INTO EMP VALUES (7900,'JAMES','CLERK',7698,to_date('3-12-1981','dd-mm-yyyy'),950,NULL,30);
INSERT INTO EMP VALUES (7902,'FORD','ANALYST',7566,to_date('3-12-1981','dd-mm-yyyy'),3000,NULL,20);
INSERT INTO EMP VALUES (7934,'MILLER','CLERK',7782,to_date('23-1-1982','dd-mm-yyyy'),1300,NULL,10);
COMMIT;
```



## Subquery Factoring

The `WITH` clause, or subquery factoring clause, is part of the SQL-99 standard and was added into the Oracle SQL syntax in Oracle 9.2. The WITH clause may be processed as an inline view or resolved as a temporary table. The advantage of the latter is that repeated references to the subquery may be more efficient as the data is easily retrieved from the temporary table, rather than being requeried by each reference. You should assess the performance implications of the `WITH` clause on a case-by-case basis.

This article shows how the `WITH` clause can be used to reduce repetition and simplify complex SQL statements. I'm not suggesting the following queries are the best way to retrieve the required information. They merely demonstrate the use of the WITH clause.

Using the SCOTT schema, for each employee we want to know how many other people are in their department. Using an inline view we might do the following.

```
-- Non-ANSI Syntax
SELECT e.ename AS employee_name,
       dc.dept_count AS emp_dept_count
FROM   emp e,
       (SELECT deptno, COUNT(*) AS dept_count
        FROM   emp
        GROUP BY deptno) dc
WHERE  e.deptno = dc.deptno;

-- ANSI Syntax
SELECT e.ename AS employee_name,
       dc.dept_count AS emp_dept_count
FROM   emp e
       JOIN (SELECT deptno, COUNT(*) AS dept_count
             FROM   emp
             GROUP BY deptno) dc
         ON e.deptno = dc.deptno;
```

Using a `WITH` clause this would look like the following.

```sql
-- Non-ANSI Syntax
WITH dept_count AS (
  SELECT deptno, COUNT(*) AS dept_count
  FROM   emp
  GROUP BY deptno)
SELECT e.ename AS employee_name,
       dc.dept_count AS emp_dept_count
FROM   emp e,
       dept_count dc
WHERE  e.deptno = dc.deptno;

-- ANSI Syntax
WITH dept_count AS (
  SELECT deptno, COUNT(*) AS dept_count
  FROM   emp
  GROUP BY deptno)
SELECT e.ename AS employee_name,
       dc.dept_count AS emp_dept_count
FROM   emp e
       JOIN dept_count dc ON e.deptno = dc.deptno;
```

The difference seems rather insignificant here.

What if we also want to pull back each employees manager name and the number of people in the managers department? Using the inline view it now looks like this.

```sql
-- Non-ANSI Syntax
SELECT e.ename AS employee_name,
       dc1.dept_count AS emp_dept_count,
       m.ename AS manager_name,
       dc2.dept_count AS mgr_dept_count
FROM   emp e,
       (SELECT deptno, COUNT(*) AS dept_count
             FROM   emp
             GROUP BY deptno) dc1,
       emp m,
       (SELECT deptno, COUNT(*) AS dept_count
        FROM   emp
        GROUP BY deptno) dc2
WHERE  e.deptno = dc1.deptno
AND    e.mgr = m.empno
AND    m.deptno = dc2.deptno;

-- ANSI Syntax
SELECT e.ename AS employee_name,
       dc1.dept_count AS emp_dept_count,
       m.ename AS manager_name,
       dc2.dept_count AS mgr_dept_count
FROM   emp e
       JOIN (SELECT deptno, COUNT(*) AS dept_count
             FROM   emp
             GROUP BY deptno) dc1
         ON e.deptno = dc1.deptno
       JOIN emp m ON e.mgr = m.empno
       JOIN (SELECT deptno, COUNT(*) AS dept_count
             FROM   emp
             GROUP BY deptno) dc2
         ON m.deptno = dc2.deptno;
```

Using the `WITH` clause this would look like the following.

```sql
-- Non-ANSI Syntax
WITH dept_count AS (
  SELECT deptno, COUNT(*) AS dept_count
  FROM   emp
  GROUP BY deptno)
SELECT e.ename AS employee_name,
       dc1.dept_count AS emp_dept_count,
       m.ename AS manager_name,
       dc2.dept_count AS mgr_dept_count
FROM   emp e,
       dept_count dc1,
       emp m,
       dept_count dc2
WHERE  e.deptno = dc1.deptno
AND    e.mgr = m.empno
AND    m.deptno = dc2.deptno;

-- ANSI Syntax
WITH dept_count AS (
  SELECT deptno, COUNT(*) AS dept_count
  FROM   emp
  GROUP BY deptno)
SELECT e.ename AS employee_name,
       dc1.dept_count AS emp_dept_count,
       m.ename AS manager_name,
       dc2.dept_count AS mgr_dept_count
FROM   emp e
       JOIN dept_count dc1 ON e.deptno = dc1.deptno
       JOIN emp m ON e.mgr = m.empno
       JOIN dept_count dc2 ON m.deptno = dc2.deptno;
```

So we don't need to redefine the same subquery multiple times. Instead we just use the query name defined in the `WITH` clause, making the query much easier to read.

If the contents of the `WITH` clause is sufficiently complex, Oracle may decide to resolve the result of the subquery into a global temporary table. This can make multiple references to the subquery more efficient. The `MATERIALIZE` and `INLINE` optimizer hints can be used to influence the decision. The undocumented `MATERIALIZE` hint tells the optimizer to resolve the subquery as a global temporary table, while the `INLINE` hint tells it to process the query inline.

```sql
WITH dept_count AS (
  SELECT /*+ MATERIALIZE */ deptno, COUNT(*) AS dept_count
  FROM   emp
  GROUP BY deptno)
SELECT ...

WITH dept_count AS (
  SELECT /*+ INLINE */ deptno, COUNT(*) AS dept_count
  FROM   emp
  GROUP BY deptno)
SELECT ...
```

Even when there is no repetition of SQL, the `WITH` clause can simplify complex queries, like the following example that lists those departments with above average wages.

```sql
WITH 
  dept_costs AS (
    SELECT dname, SUM(sal) dept_total
    FROM   emp e, dept d
    WHERE  e.deptno = d.deptno
    GROUP BY dname),
  avg_cost AS (
    SELECT SUM(dept_total)/COUNT(*) avg
    FROM   dept_costs)
SELECT *
FROM   dept_costs
WHERE  dept_total > (SELECT avg FROM avg_cost)
ORDER BY dname;
```

In the previous example, the main body of the query is very simple, with the complexity hidden in the `WITH` clause.

## MATERIALIZE Hint

The undocumented `MATERIALIZE` hint was mentioned above, but there seems to be a little confusion over how it is implemented. We can see what is happening under the covers using SQL trace.

Create a test table.

```
CONN test/test

CREATE TABLE t1 AS
SELECT level AS id
FROM   dual
CONNECT BY level <= 100;
```

Check the trace file location.

```
SELECT value
FROM   v$diag_info
WHERE  name = 'Default Trace File';

VALUE
--------------------------------------------------------------------------------
/u01/app/oracle/diag/rdbms/cdb1/cdb1/trace/cdb1_ora_4278.trc

SQL>
```

Trace a statement using the `MATERIALIZE` hint.

```sql
EXEC DBMS_MONITOR.session_trace_enable;

WITH query1 AS (
  SELECT /*+ MATERIALIZE */ * FROM t1
)
SELECT * FROM query1;

EXEC DBMS_MONITOR.session_trace_disable;
```

The following abbreviated output shows some points of interest in the resulting trace file. Notice the "CREATE GLOBAL TEMPORARY T" and "TABLE ACCESS FULL SYS_TEMP_0FD9D662B_2E34FB" lines. It certainly seems to be using a global temporary table.

```sql
=====================
PARSING IN CURSOR #140100560521424 len=174 dep=1 uid=0 oct=1 lid=0 tim=733844612 hv=1878591410 ad='80b179f0' sqlid='40a2untrzk1xk'
CREATE GLOBAL TEMPORARY T
END OF STMT
...
=====================
...
=====================
PARSING IN CURSOR #140100560423976 len=77 dep=0 uid=109 oct=3 lid=109 tim=733865863 hv=3518560624 ad='a35bc6c0' sqlid='9fzhbw78vjybh'
WITH query1 AS (
  SELECT /*+ MATERIALIZE */ * FROM t1
)
SELECT * FROM query1
END OF STMT
...
STAT #140100560423976 id=1 cnt=100 pid=0 pos=1 obj=0 op='TEMP TABLE TRANSFORMATION  (cr=15 pr=1 pw=1 time=19589 us)'
STAT #140100560423976 id=2 cnt=0 pid=1 pos=1 obj=0 op='LOAD AS SELECT  (cr=3 pr=0 pw=1 time=16243 us)'
STAT #140100560423976 id=3 cnt=100 pid=2 pos=1 obj=91676 op='TABLE ACCESS FULL T1 (cr=3 pr=0 pw=0 time=1514 us cost=3 size=300 card=100)'
STAT #140100560423976 id=4 cnt=100 pid=1 pos=2 obj=0 op='VIEW  (cr=12 pr=1 pw=0 time=1257 us cost=2 size=1300 card=100)'
STAT #140100560423976 id=5 cnt=100 pid=4 pos=1 obj=4254950955 op='TABLE ACCESS FULL SYS_TEMP_0FD9D662B_2E34FB (cr=12 pr=1 pw=0 time=1203 us cost=2 size=300 card=100)'
...
=====================
```