---
title: PL/SQL Record types, Bulk Collect, and Collections.
tags: db
date: 2022-12-20
---

> 转载：[PL/SQL Tutorial: Chapter 6 - Database Star](https://www.databasestar.com/pl-sql-tutorial-chapter-6/)

In this chapter, we'll learn about:

- Using data types based on tables and columns
- Understanding what collections are
- Using the BULK COLLECT keyword to fetch data in bulk

These are all great features of the PL/SQL language and will take your code to the next level.

## Field Types

In earlier code, we declared variables to hold values we loaded from the database.

```sql
DECLARE
  l_fname VARCHAR2(50);
BEGIN
  SELECT fname
  INTO l_fname
  FROM person;
  DBMS_OUTPUT.PUT_LINE('The name is ' || l_fname);
END;
```

The l_fname variable is a VARCHAR2(50). This just happens to be the same as the table we created:

```sql
CREATE TABLE person (
  fname VARCHAR2(50)
);
```

But what if the table declaration changes? We shouldn't be forcing our code to be the same as the table in this way, because we would have to change our code.

There is a better way to do it, and that's using the %TYPE attribute.

The TYPE attribute will let you declare a variable based on the type of a column in a table. This means it is automatically linked to, or set the same as a column that exist. There's no need to look up the data type manually or change the code if your table changes.

The code to do that looks like this:

```sql
DECLARE
  variable_name table_name.column_name %TYPE;
BEGIN
…
```

After specifying the variable name, you specify the column and table name separated by a period. You then specify %TYPE, which indicates that your variable has the same type as this column.

## Example – Using the %TYPE Attribute

We can update our code to use this:

```sql
DECLARE
  l_fname person.fname%TYPE;
BEGIN
  SELECT fname
  INTO l_fname
  FROM person;
  DBMS_OUTPUT.PUT_LINE('The name is ' || l_fname);
END;
```

The output of this code is:

```
Statement processed.
The name is John
```

This makes your code easier to maintain.

## Example – Two Variables Using %TYPE

You can declare multiple variables that use the %TYPE attribute if you need to.

Let's say our table looked like this:

```sql
CREATE TABLE person (
  fname VARCHAR2(50),
  lname VARCHAR2(50),
  salary NUMBER(8)
);

INSERT INTO person (fname, lname, salary)
VALUES ('John', 'Smith', 50000);
```

We have one record:

| **FNAME** | **LNAME** | **SALARY** |
| --------- | --------- | ---------- |
| John      | Smith     | 50000      |

Our PL/SQL code can output this record by using variables and the %TYPE attribute.

```sql
DECLARE
  l_fname person.fname%TYPE;
  l_lname person.lname%TYPE;
  l_salary person.salary%TYPE;
BEGIN
  SELECT fname, lname, salary
  INTO l_fname, l_lname, l_salary
  FROM person;
  DBMS_OUTPUT.PUT_LINE('The name is ' ||
    l_fname || ' ' || l_lname ||
    ' with a salary of ' || l_salary);
END;
```

We have used three variables (one for each column), each related to the column in the table.

The output of this code is:

```
Statement processed.
The name is John Smith with a salary of 50000
```

## Row Types

Another useful feature of PL/SQL is the ability to create a variable that has the same data type of an entire table row.

In the example above, we had three separate variables for each of the different columns:

```sql
DECLARE
  l_fname person.fname%TYPE;
  l_lname person.lname%TYPE;
  l_salary person.salary%TYPE;
BEGIN
…
```

This may seem OK, but what if we want to use 5 or 10 columns? We would need to declare a lot of variables.

In PL/SQL, you can declare a single variable and set the type of it equal to the entire row. It kind of works like an array, where each element or attribute is equal to one column.

We can do this using the %ROWTYPE attribute:

```sql
DECLARE
  variable_name table_name%ROWTYPE;
BEGIN
…
```

We don't need to specify any column names here: just the variable name, the table to base it on, and %ROWTYPE.

How do we access the values? We use variable_name.column_name.

Let's see an example:

```sql
DECLARE
  l_row_person person%ROWTYPE;
BEGIN
  SELECT fname, lname, salary
  INTO l_row_person.fname, l_row_person.lname, l_row_person.salary
  FROM person;
  DBMS_OUTPUT.PUT_LINE('The name is ' ||
    l_row_person.fname || ' ' || l_row_person.lname ||
    ' with a salary of ' || l_row_person.salary);
END;
```

This code includes a few changes:

- There is a single variable called l_row_person, which has a type equal to the person table (using %ROWTYPE).
- The SELECT INTO is selecting the column values into separate attributes of the l_row_person variable, one for each column.
- The PUT_LINE function uses the attributes of the l_row_person variable. For example, l_row_person.fname is the fname column from the person table.

This results in less code and seems easier to read. It can make a big difference in larger programs.

The output of this code is:

```
Statement processed.
The name is John Smith with a salary of 50000
```

## Cursor-Based Records

In the earlier example, we used %ROWTYPE to create a variable based on the data type of a table's columns.

In an earlier chapter, we also looked at using [cursors](https://www.databasestar.com/sql-cursor/) to select records. Here's an example:

```sql
DECLARE
  l_fname VARCHAR2(50);
  CURSOR c_person IS
  SELECT fname FROM person;
BEGIN
  OPEN c_person;
  FETCH c_person INTO l_fname;
  DBMS_OUTPUT.PUT_LINE('Name is: ' || l_fname);
  CLOSE c_person;
END;
```

This code will select the fname into a variable. Another way to do this is to declare a variable that is equal to the type of the cursor, rather than the table or the column. This is helpful if you have a complicated query that gets data from multiple tables.

The code would look like this:

```sql
DECLARE
  CURSOR c_person IS
  SELECT fname, lname, salary FROM person;
  c_person_rec c_person%ROWTYPE;
BEGIN
  OPEN c_person;
  FETCH c_person INTO c_person_rec;
  DBMS_OUTPUT.PUT_LINE('The name is ' ||
    c_person_rec.fname || ' ' || c_person_rec.lname ||
    ' with a salary of ' || c_person_rec.salary);
  CLOSE c_person;
END;
```

This works similar to using a table. The output of this query is:

```
Statement processed.
The name is John Smith with a salary of 50000
```

## PL/SQL Collections

PL/SQL includes a feature called collections. A collection in PL/SQL is a set of values that have the same data type. It's similar to an array that we've learned about earlier in this guide, but there are several differences.

| **Object Type** | **Number of Elements** | **Index Type** | **Dense or Sparse** | **Can be an Object** |
| --------------- | ---------------------- | -------------- | ------------------- | -------------------- |
| Varray          | Fixed                  | Number         | Dense               | Yes                  |
| Index By Table  | Variable               | String         | Either              | No                   |
| Nested Table    | Variable               | Number         | Either              | Yes                  |

We'll learn about the two types of collections in this section: an Index By Table and a Nested Table.

## Index By Table

An Index By Table (also known as an associative array) is a type of variable that stores key-value pairs. Like arrays in other programming languages, the keys can be numbers or strings.

Creating a variable using an Index By Table is done in the following way:

```sql
TYPE type_name IS TABLE OF element_data_type [NOT NULL] INDEX BY index_data_type;
variable_name type_name;
```

In this code, we declare a type, and then a variable of that type. The type has a name that we can provide, and we specify the data type of the elements and the data type of the index.

An example of this feature is:

```sql
DECLARE
  TYPE first_name IS TABLE OF VARCHAR2(50) INDEX BY PLS_INTEGER;
  name_list first_name;
BEGIN
..
END;
```

How can we populate and use this list? We add items, or elements, to the list by specifying the key in brackets and using the := symbol:

```sql
name_list(1) := 'John';
```

We can add several elements to this variable:

```sql
DECLARE
  TYPE first_name IS TABLE OF VARCHAR2(50) INDEX BY PLS_INTEGER;
  name_list first_name;
BEGIN
  name_list(1) := 'John';
  name_list(2) := 'Susan';
  name_list(3) := 'Mark';
  name_list(4) := 'Debra';
END;
```

How do we access the values in the list to output them? We can use the FIRST and NEXT functions of the variable, as well as a loop. These functions are built into the Index By Table data type.

Our code looks like this:

```sql
DECLARE
  TYPE first_name IS TABLE OF VARCHAR2(50) INDEX BY PLS_INTEGER;
  name_list first_name;
  current_name_id PLS_INTEGER;
BEGIN
  name_list(1) := 'John';
  name_list(2) := 'Susan';
  name_list(3) := 'Mark';
  name_list(4) := 'Debra';
  current_name_id := name_list.FIRST;
  WHILE current_name_id IS NOT NULL LOOP
    DBMS_OUTPUT.PUT_LINE('The name is ' || name_list(current_name_id));
    current_name_id := name_list.NEXT(current_name_id);
  END LOOP;
END;
```

There is a lot to take in here:

- We have declared a new variable called current_name_id which stores the index of the collection, and is used for the loop.
- The name_list.FIRST will return the index of the first element, which has been stored in the current_name_id variable;
- A WHILE loop will loop through the name_list and output the value of the name_list element.
- The current_name_id variable is incremented using the name_list.NEXT function.

The output of this code is:

```
Statement processed.
The name is John
The name is Susan
The name is Mark
The name is Debra
```

## Example – Index By Table with Select Query

You can also use an Index By Table with a SELECT query on the database.

Using our person table from earlier, this code will select the data from that table into the collection:

```sql
DECLARE
  CURSOR c_person IS
  SELECT fname, lname, salary FROM person;
  TYPE col_person IS TABLE OF person.fname%TYPE INDEX BY PLS_INTEGER;
  person_list col_person;
  rowcounter PLS_INTEGER := 0;
BEGIN
  FOR i IN c_person LOOP
    rowcounter := rowcounter + 1;
    person_list(rowcounter) := i.fname;
    DBMS_OUTPUT.PUT_LINE('The name is ' || person_list(rowcounter));
  END LOOP;
END;
```

The output will show:

```
Statement processed.
The name is John
The name is Susan
The name is Mark
The name is Debra
```

So that's how you can use an index by table, or associative array, in PL/SQL.

## Nested Table

A nested table in PL/SQL is another type of collection. It's very similar to an Index By Table, except it always has an integer for an index. It does not have an INDEX BY clause;

The syntax for creating one is:

```sql
TYPE type_name IS TABLE OF element_data_type [NOT NULL];
variable_name type_name;
```

We declare the name of the type and the element type, then we declare a variable of that type.

An example of this in action can be done by modifying the example from earlier:

```sql
DECLARE
  TYPE first_name IS TABLE OF VARCHAR2(50);
  name_list first_name;
BEGIN
  name_list := first_name('John', 'Susan', 'Mark', 'Debra');
  FOR i IN 1 .. name_list.count LOOP
    DBMS_OUTPUT.PUT_LINE('The name is ' || name_list(i));
  END LOOP;
END;
```

This is less code than earlier examples, but it shows the concept of a Nested Table.

The output of this code is:

```
Statement processed.
The name is John
The name is Susan
The name is Mark
The name is Debra
```

## When To Use Index By Tables, Nested Tables, or VArrays in PL/SQL

We've learned about Index By Tables, Nested Tables, and Varrays. How do we know when to use each of them?

Oracle has some [recommendations](https://docs.oracle.com/cd/B28359_01/appdev.111/b28370/collections.htm).

When to use an Index By Table/Associative Array:

- When you have a small lookup table, as it's created each time in memory whenever you run your code

When to use a Nested Table:

- When the index values are not consecutive
- When there is not a set number of index values
- You need to delete some of the elements

When to use a Varray:

- The number of elements is known in advance
- The elements are usually accessed in order

## Bulk Collect

Our PL/SQL code often contains PL/SQL code (declaring variables, loops, IF statements) and SQL code (SELECT, INSERT, UPDATE). This makes our programs quite powerful.

However, it can also make our programs quite slow if they are not written correctly.

Each time an SQL statement is run from PL/SQL, a “context switch” is performed. The server switches from running the PL/SQL code to running the SQL code. This involves a small amount of work by the server. This may not be noticeable with one statement, but if you're running hundreds or thousands of statements, across many users, then it can really add up.

Let's say we had this PL/SQL code that updated the salary in our person table.

Here's our setup data.

```sql
DELETE FROM person;
INSERT INTO person (fname, lname, salary)
VALUES ('John', 'Smith', 20000);
INSERT INTO person (fname, lname, salary)
VALUES ('Susan', 'Jones', 30000);
INSERT INTO person (fname, lname, salary)
VALUES ('Mark', 'Blake', 25000);
INSERT INTO person (fname, lname, salary)
VALUES ('Debra', 'Carlson', 40000);
```

Here's our PL/SQL code.

```sql
BEGIN
  FOR current_rec IN (SELECT fname
  FROM person) LOOP

    DBMS_OUTPUT.PUT_LINE('Name: ' || current_rec.fname);

    UPDATE person p
    SET p.salary = p.salary + 1000
    WHERE p.fname = current_rec.fname;

  END LOOP;
END;
```

The output is:

```
1 row(s) updated.
Name: John
Name: Susan
Name: Mark
Name: Debra
```

In this code, we have a query that selects names. We loop through this collection and update the person table for each entry in the collection, which means it runs the UPDATE statement four times.

We can run a SELECT statement to check the new values.

```sql
SELECT * FROM person;
```

| **FNAME** | **LNAME** | **SALARY** |
| --------- | --------- | ---------- |
| John      | Smith     | 21000      |
| Susan     | Jones     | 31000      |
| Mark      | Blake     | 26000      |
| Debra     | Carlson   | 41000      |

We can see that each of the salary values has been increased by 1. However, the UPDATE statement has run 4 separate times. This is something we want to avoid.

We also want to avoid using a cursor for loop as we have here. A cursor for loop is where we have a FOR loop that includes a SELECT query in its criteria. It allows you to loop through each record and process it, as we have done in our code.

However, a cursor for loop is slow as it processes each row individually. It also performs a context switch between the SQL engine (running the SELECT query) and the PL/SQL engine (the FOR loop) There are better ways to do this: using a [feature called BULK COLLECT](https://www.databasestar.com/oracle-bulk-insert/).

BULK COLLECT allows you to fetch all rows from a SELECT query into a collection in a single statement. The SQL code is run once, and the remainder of the logic is performed in PL/SQL. This greatly reduces the context switching between SQL and PL/SQL, improving the performance of your code.

## Example – BULK COLLECT

So how do we do this? We can introduce a variable to hold our data, and replace the cursor for loop with a SELECT and BULK COLLECT:

```sql
DECLARE
  TYPE name_type IS TABLE OF person.fname%TYPE;
  name_list name_type;
BEGIN
  SELECT fname
  BULK COLLECT INTO name_list
  FROM person;
  FOR i IN 1 .. name_list.count LOOP

    UPDATE person p
    SET p.salary = p.salary + 1000
    WHERE p.fname = name_list(i);

  END LOOP;
END;
```

The changes we have made here are:

- We've declared a new TYPE called name_type, which is a table of values of the same type as the person.fname column.
- We've declared a new variable based on that type, called name_list.
- We've run a SELECT statement which selects the fname column into the name_list variable, using BULK COLLECT. This means all values from the query are added into this collection.

The loop is then run based on the data already loaded into the name_list variable.

The output is:

```
1 row(s) updated.
Name: John
Name: Susan
Name: Mark
Name: Debra
```

This improves the performance of the SELECT statement. But what about the UPDATE statement?

## FORALL in PL/SQL

The UPDATE statement in the earlier code is run each time during the loop. This means that there is a context switch between PL/SQL and SQL each time the statement is run. In this example, it happens 4 times, but in a real database, it can happen hundreds or thousands of times.

If you can put your SQL code outside the loop, then that is better. The code will only run once on all the rows that need to be updated.

However, if you have logic that means you can't do this, you can use a feature called FORALL.

In PL/SQL, the FORALL statement will tell the database to generate and run all of the DML statements that would have been generated separately and run them at once. This reduces the time taken and the context switches.

To do this, change the code to ensure the UPDATE statement is inside a FORALL:

```sql
DECLARE
  TYPE name_type IS TABLE OF person.fname%TYPE;
  name_list name_type;
BEGIN
  SELECT fname
  BULK COLLECT INTO name_list
  FROM person;
  FORALL i IN 1 .. name_list.count
    UPDATE person p
    SET p.salary = p.salary + 1000
    WHERE p.fname = name_list(i);
END;
```

This will run the UPDATE statements once on the database.

You can check the before and after using this code:

```sql
SELECT * FROM person;

DECLARE
  TYPE name_type IS TABLE OF person.fname%TYPE;
  name_list name_type;
BEGIN
  SELECT fname
  BULK COLLECT INTO name_list
  FROM person;
  FORALL i IN 1 .. name_list.count
    UPDATE person p
    SET p.salary = p.salary + 1000
    WHERE p.fname = name_list(i);
END;
/

SELECT * FROM person;
```

This shows the SELECT query results before the code:

| **FNAME** | **LNAME** | **SALARY** |
| --------- | --------- | ---------- |
| John      | Smith     | 20000      |
| Susan     | Jones     | 30000      |
| Mark      | Blake     | 25000      |
| Debra     | Carlson   | 40000      |

And the SELECT query results after the code:

| **FNAME** | **LNAME** | **SALARY** |
| --------- | --------- | ---------- |
| John      | Smith     | 21000      |
| Susan     | Jones     | 31000      |
| Mark      | Blake     | 26000      |
| Debra     | Carlson   | 41000      |

So that's how you can use both BULK COLLECT and FORALL to improve the performance of your PL/SQL code. If you want to learn more about these features, read this article: [Bulk Processing with BULK COLLECT and FORALL](https://blogs.oracle.com/oraclemagazine/bulk-processing-with-bulk-collect-and-forall).

## Conclusion

Field and record types are handy features of PL/SQL and allow you to declare variables based on the type of a column or an entire row in a database table. They improve the maintainability of your code.

PL/SQL also allows you to use collections. These are similar to arrays but have some other advantages. The two types of collections are Index By Table and Nested Table.

Running SELECT statements or other DML statements individually can impact the performance of your code. It's better to switch between PL/SQL and SQL as little as possible. The BULK COLLECT and FORALL features allow you to do that in a better way.
