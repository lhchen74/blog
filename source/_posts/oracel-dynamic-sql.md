---
title: Oracle Dynamic SQL
tags: db
date: 2020-08-13
---

> reproduced:[Performing SQL Operations with Native Dynamic SQL](https://docs.oracle.com/cd/B12037_01/appdev.101/b10807/11_dynam.htm#i14500)

# Performing SQL Operations with Native Dynamic SQL

_A happy and gracious flexibility ... —_ Matthew Arnold

This chapter shows you how to use native dynamic SQL (dynamic SQL for short), a PL/SQL interface that makes your programs more flexible, by building and processing SQL statements at run time.

With dynamic SQL, you can directly execute any kind of SQL statement (even data definition and data control statements). You can build statements where you do not know table names, `WHERE` clauses, and other information in advance.

## Why Use Dynamic SQL?

You need dynamic SQL in the following situations:

-   You want to execute a SQL data definition statement (such as `CREATE`), a data control statement (such as `GRANT`), or a session control statement (such as `ALTER` `SESSION`). Unlike `INSERT`, `UPDATE`, and `DELETE` statements, these statements cannot be included directly in a PL/SQL program.
-   You want more flexibility. For example, you might want to pass the name of a schema object as a parameter to a procedure. You might want to build different search conditions for the `WHERE` clause of a `SELECT` statement.
-   You want to issue a query where you do not know the number, names, or datatypes of the columns in advance. In this case, you use the `DBMS_SQL` package rather than the `OPEN-FOR` statement.

If you have older code that uses the `DBMS_SQL` package, the techniques described in this chapter using `EXECUTE IMMEDIATE` and `OPEN-FOR` generally provide better performance, more readable code, and extra features such as support for objects and collections. (For a comparison with DBMS*SQL, see [\_Oracle Database Application Developer's Guide - Fundamentals*](https://docs.oracle.com/cd/B12037_01/appdev.101/b10795/toc.htm).)

## Building a Dynamic Query with Dynamic SQL

You use three statements to process a dynamic multi-row query: `OPEN-FOR`, `FETCH`, and `CLOSE`. First, you `OPEN` a cursor variable `FOR` a multi-row query. Then, you `FETCH` rows from the result set one at a time. When all the rows are processed, you `CLOSE` the cursor variable. (For more information about cursor variables, see ["Using Cursor Variables (REF CURSORs)"](https://docs.oracle.com/cd/B12037_01/appdev.101/b10807/06_ora.htm#i7106).)

## Examples of Dynamic SQL for Records, Objects, and Collections

**Example 7-3 Dynamic SQL Fetching into a Record**

As the following example shows, you can fetch rows from the result set of a dynamic multi-row query into a record:

```sql
DECLARE
   TYPE EmpCurTyp IS REF CURSOR;
   emp_cv   EmpCurTyp;
   emp_rec  emp%ROWTYPE;
   sql_stmt VARCHAR2(200);
   my_job   VARCHAR2(15) := 'CLERK';
BEGIN
   sql_stmt := 'SELECT * FROM emp WHERE job = :j';
   OPEN emp_cv FOR sql_stmt USING my_job;
   LOOP
      FETCH emp_cv INTO emp_rec;
      EXIT WHEN emp_cv%NOTFOUND;
      -- process record
   END LOOP;
   CLOSE emp_cv;
END;
/
```

**Example 7-4 Dynamic SQL for Object Types and Collections**

The next example illustrates the use of objects and collections. Suppose you define object type `Person` and `VARRAY` type `Hobbies`, as follows:

```sql
CREATE TYPE Person AS OBJECT (name VARCHAR2(25), age NUMBER);
CREATE TYPE Hobbies IS VARRAY(10) OF VARCHAR2(25);
```

Using dynamic SQL, you can write a package that uses these types:

```sql
CREATE OR REPLACE PACKAGE teams AS
   PROCEDURE create_table (tab_name VARCHAR2);
   PROCEDURE insert_row (tab_name VARCHAR2, p Person, h Hobbies);
   PROCEDURE print_table (tab_name VARCHAR2);
END;
/

CREATE OR REPLACE PACKAGE BODY teams AS
   PROCEDURE create_table (tab_name VARCHAR2) IS
   BEGIN
      EXECUTE IMMEDIATE 'CREATE TABLE ' || tab_name ||
         ' (pers Person, hobbs Hobbies)';
   END;

   PROCEDURE insert_row (
      tab_name VARCHAR2,
      p Person,
      h Hobbies) IS
   BEGIN
      EXECUTE IMMEDIATE 'INSERT INTO ' || tab_name ||
         ' VALUES (:1, :2)' USING p, h;
   END;

   PROCEDURE print_table (tab_name VARCHAR2) IS
      TYPE RefCurTyp IS REF CURSOR;
      cv RefCurTyp;
      p  Person;
      h  Hobbies;
   BEGIN
      OPEN cv FOR 'SELECT pers, hobbs FROM ' || tab_name;
      LOOP
         FETCH cv INTO p, h;
         EXIT WHEN cv%NOTFOUND;
         -- print attributes of 'p' and elements of 'h'
      END LOOP;
      CLOSE cv;
   END;
END;
/
```

From an anonymous block, you might call the procedures in package `TEAMS`:

```sql
DECLARE
   team_name VARCHAR2(15);
BEGIN
   team_name := 'Notables';
   teams.create_table(team_name);
   teams.insert_row(team_name, Person('John', 31),
      Hobbies('skiing', 'coin collecting', 'tennis'));
   teams.insert_row(team_name, Person('Mary', 28),
      Hobbies('golf', 'quilting', 'rock climbing'));
   teams.print_table(team_name);
END;
/
```

## Guidelines for Dynamic SQL

This section shows you how to take full advantage of dynamic SQL and how to avoid some common pitfalls.

### When to Use or Omit the Semicolon with Dynamic SQL

When building up a single SQL statement in a string, do not include any semicolon at the end.

When building up a PL/SQL anonymous block, include the semicolon at the end of each PL/SQL statement and at the end of the anonymous block.

For example:

```sql
BEGIN
   EXECUTE IMMEDIATE 'dbms_output.put_line(''No semicolon'')';
   EXECUTE IMMEDIATE 'BEGIN dbms_output.put_line(''semicolons''); END;';
END;
```

### Improving Performance of Dynamic SQL with Bind Variables

When you code `INSERT`, `UPDATE`, `DELETE`, and `SELECT` statements directly in PL/SQL, PL/SQL turns the variables into bind variables automatically, to make the statements work efficiently with SQL. When you build up such statements in dynamic SQL, you need to specify the bind variables yourself to get the same performance.

In the example below, Oracle opens a different cursor for each distinct value of `emp_id`. This can lead to resource contention and poor performance as each statement is parsed and cached.

```sql
CREATE PROCEDURE fire_employee (emp_id NUMBER) AS
BEGIN
   EXECUTE IMMEDIATE
      'DELETE FROM emp WHERE empno = ' || TO_CHAR(emp_id);
END;
/
```

You can improve performance by using a bind variable, which allows Oracle to reuse the same cursor for different values of `emp_id`:

```sql
CREATE PROCEDURE fire_employee (emp_id NUMBER) AS
BEGIN
   EXECUTE IMMEDIATE
      'DELETE FROM emp WHERE empno = :num' USING emp_id;
END;
/
```

### Passing Schema Object Names As Parameters

Suppose you need a procedure that accepts the name of any database table, then drops that table from your schema. You must build a string with a statement that includes the object names, then use `EXECUTE IMMEDIATE` to execute the statement:

```sql
CREATE PROCEDURE drop_table (table_name IN VARCHAR2) AS
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE ' || table_name;
END;
/
```

Use concatenation to build the string, rather than trying to pass the table name as a bind variable through the `USING` clause.

### Using Duplicate Placeholders with Dynamic SQL

Placeholders in a dynamic SQL statement are associated with bind arguments in the `USING` clause by position, not by name. If you specify a sequence of placeholders like `:a, :a, :b, :b`, you must include four items in the `USING` clause. For example, given the dynamic string

```sql
sql_stmt := 'INSERT INTO payroll VALUES (:x, :x, :y, :x)';
```

the fact that the name X is repeated is not significant. You can code the corresponding `USING` clause with four different bind variables:

```sql
EXECUTE IMMEDIATE sql_stmt USING a, a, b, a;
```

If the dynamic statement represents a PL/SQL block, the rules for duplicate placeholders are different. Each unique placeholder maps to a single item in the `USING` clause. If the same placeholder appears two or more times, all references to that name correspond to one bind argument in the `USING` clause. In the following example, all references to the placeholder `X` are associated with the first bind argument `A`, and the second unique placeholder `Y` is associated with the second bind argument B.

```sql
DECLARE
   a NUMBER := 4;
   b NUMBER := 7;
BEGIN
   plsql_block := 'BEGIN calc_stats(:x, :x, :y, :x); END;'
   EXECUTE IMMEDIATE plsql_block USING a, b;
END;
/
```

### Using Cursor Attributes with Dynamic SQL

The SQL cursor attributes `%FOUND`, `%ISOPEN`, `%NOTFOUND`, and `%ROWCOUNT` work when you issue an `INSERT`, `UPDATE`, `DELETE`, or single-row `SELECT` statement in dynamic SQL:

```sql
EXECUTE IMMEDIATE 'DELETE FROM employees WHERE employee_id > 1000';
rows_deleted := SQL%ROWCOUNT;
```

Likewise, when appended to a cursor variable name, the cursor attributes return information about the execution of a multi-row query:

```sql
OPEN c1 FOR 'SELECT * FROM employees';
FETCH c1 BULK COLLECT INTO rec_tab;
rows_fetched := c1%ROWCOUNT;
```

For more information about cursor attributes, see ["Using Cursor Expressions"](https://docs.oracle.com/cd/B12037_01/appdev.101/b10807/06_ora.htm#i44913).

### Passing Nulls to Dynamic SQL

The literal `NULL` is not allowed in the `USING` clause. To work around this restriction, replace the keyword `NULL` with an uninitialized variable:

```sql
DECLARE
   a_null CHAR(1); -- set to NULL automatically at run time
BEGIN
   EXECUTE IMMEDIATE 'UPDATE emp SET comm = :x' USING a_null;
END;
/
```

### Using Database Links with Dynamic SQL

PL/SQL subprograms can execute dynamic SQL statements that use database links to refer to objects on remote databases:

```sql
PROCEDURE delete_dept (db_link VARCHAR2, dept_id INTEGER) IS
BEGIN
   EXECUTE IMMEDIATE 'DELETE FROM departments@' || db_link ||
      ' WHERE deptno = :num' USING dept_id;
END;
/
```

The targets of remote procedure calls (RPCs) can contain dynamic SQL statements. For example, suppose the following standalone function, which returns the number of rows in a table, resides on the Chicago database:

```sql
CREATE FUNCTION row_count (tab_name VARCHAR2) RETURN INTEGER AS
   rows INTEGER;
BEGIN
   EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || tab_name INTO rows;
   RETURN rows;
END;
/
```

From an anonymous block, you might call the function remotely, as follows:

```sql
DECLARE
   emp_count INTEGER;
BEGIN
   emp_count := row_count@chicago('employees');
END;
/
```

### Using Invoker Rights with Dynamic SQL

Dynamic SQL lets you write schema-management procedures that can be centralized in one schema, and can be called from other schemas and operate on the objects in those schemas.

For example, this procedure can drop any kind of database object:

```sql
CREATE OR REPLACE PROCEDURE drop_it (kind IN VARCHAR2, name IN
VARCHAR2)
AUTHID CURRENT_USER
AS
BEGIN
   EXECUTE IMMEDIATE 'DROP ' || kind || ' ' || name;
END;
/
```

Let's say that this procedure is part of the `HR` schema. Without the `AUTHID` clause, the procedure would always drop objects in the `HR` schema, regardless of who calls it. Even if you pass a fully qualified object name, this procedure would not have the privileges to make changes in other schemas.

The `AUTHID` clause lifts both of these restrictions. It lets the procedure run with the privileges of the user that invokes it, and makes unqualified references refer to objects in that user's schema.

For details, see ["Using Invoker's Rights Versus Definer's Rights (AUTHID Clause)"](https://docs.oracle.com/cd/B12037_01/appdev.101/b10807/08_subs.htm#i18574).

### Using Pragma RESTRICT_REFERENCES with Dynamic SQL

A function called from SQL statements must obey certain rules meant to control side effects. (See ["Controlling Side Effects of PL/SQL Subprograms"](https://docs.oracle.com/cd/B12037_01/appdev.101/b10807/08_subs.htm#i22204).) To check for violations of the rules, you can use the pragma `RESTRICT_REFERENCES`. The pragma asserts that a function does not read or write database tables or package variables. (For more information, See [_Oracle Database Application Developer's Guide - Fundamentals_](https://docs.oracle.com/cd/B12037_01/appdev.101/b10795/toc.htm).)

If the function body contains a dynamic `INSERT`, `UPDATE`, or `DELETE` statement, the function always violates the rules "write no database state" (`WNDS`) and "read no database state" (`RNDS`). PL/SQL cannot detect those side-effects automatically, because dynamic SQL statements are checked at run time, not at compile time. In an `EXECUTE` `IMMEDIATE` statement, only the `INTO` clause can be checked at compile time for violations of `RNDS`.

### Avoiding Deadlocks with Dynamic SQL

In a few situations, executing a SQL data definition statement results in a deadlock. For example, the procedure below causes a deadlock because it attempts to drop itself. To avoid deadlocks, never try to `ALTER` or `DROP` a subprogram or package while you are still using it.

```sql
CREATE OR REPLACE PROCEDURE calc_bonus (emp_id NUMBER) AS
BEGIN
   EXECUTE IMMEDIATE 'DROP PROCEDURE calc_bonus'; -- deadlock!
END;
/
```

### Backward Compatibility of the USING Clause

When a dynamic `INSERT`, `UPDATE`, or `DELETE` statement has a `RETURNING` clause, output bind arguments can go in the `RETURNING` `INTO` clause or the `USING` clause. In new applications, use the `RETURNING` `INTO` clause. In old applications, you can continue to use the `USING` clause.
