---
title: SQL Window Functions: The Ultimate Guide
date: 2022-12-11
tags: db
---

> 转载：[SQL Window Functions: The Ultimate Guide - Database Star](https://www.databasestar.com/sql-window-functions/)

What is an SQL window function? Why should you know about it? And what can it help you with?

You may have heard of SQL window functions before, or they may be completely new to you.

Learn all about them in this guide.

## What is a Window Function?

**A window function is a type of SQL function that lets you perform calculations based on data in different rows.**

It's the same as an SQL analytic function.

What does this mean? And how is it useful?

Let's see an example. A common example is calculating a [running total in SQL](https://www.databasestar.com/sql-running-total/).

Let's say we have a table called orders, and that contains an order data and a total amount of the order. And let's say we want to calculate the running total of order amounts, or the "total so far" of orders placed. This total would be added to the previous total and keep increasing.

So, if we have an orders table that looked like this:

| **order_id** | **order_date** | **order_total** |
| ------------ | -------------- | --------------- |
| 1            | 2020-04-03     | 100             |
| 2            | 2020-04-03     | 250             |
| 3            | 2020-04-04     | 80              |
| 4            | 2020-04-05     | 10              |

We could calculate a running total that would make our results look like this:

| **order_id** | **order_date** | **order_total** | **running_total** |
| ------------ | -------------- | --------------- | ----------------- |
| 1            | 2020-04-03     | 100             | 100               |
| 2            | 2020-04-03     | 250             | 350               |
| 3            | 2020-04-04     | 80              | 430               |
| 4            | 2020-04-05     | 10              | 440               |

Notice how an extra column is added, called running_total. And this running total is the order_total value of that row plus the previous row's running total.

So the first value is 100, then 250 is added in the second row to have a running total of 350. In the third row, 80 is added to 350 to get 430. Finally, the fourth row adds 10 to get a running total of 440.

This is what window functions let you do. You can use window functions to access values from other rows, to do things such as:

- Calculate running totals
- Calculate sums of groups without using Group By
- Rank values within groups
- And more

Window functions are separate from [GROUP BY clauses](https://www.databasestar.com/sql-group-by/). You can see in the example above that each row is listed. There is no grouping of orders in any form.

## Which Databases Include Window Functions?

The following databases include the windowing function feature:

- [Oracle](https://www.databasestar.com/oracle-database/)
- [SQL Server](https://www.databasestar.com/sql-server/)
- [MySQL](https://www.databasestar.com/mysql/) as of version 8.0
- [PostgreSQL](https://www.databasestar.com/postgresql/)

There may be others, as this is not a complete list.

## The Basic Syntax of a Window Function

So how do we use this kind of function? What does an SQL window function look like?

The syntax of a window function in SQL looks like this:

```sql
window_function (expression)
OVER (
  [ PARTITION BY partition_clause ]
  [ ORDER BY order_clause ]
)
```

The square brackets [] indicate that this part of the function is optional.

The window_function can be one of many functions, such as [SUM](https://www.databasestar.com/sql-sum/). We'll see a whole range of examples in this guide.

The expression after the window function can be a column or other expression you want to apply to the function.

The OVER keyword indicates that this is to be treated as a window function.

The PARTITION BY partition clause will let you define the window of data the function looks at. What does this mean? We'll see some examples shortly to explain this.

Finally, the ORDER BY clause can be added inside the window function and is used to define the order that the function runs on the data. This is separate to the [order the overall results are displayed](https://www.databasestar.com/sql-order-by/).

## SQL Window Function Example: Calculate a Running Total with SUM

Now we've seen the syntax of a window function, let's see an example.

We saw an earlier example output of calculating a running total. The example showed orders:

| **order_id** | **order_date** | **order_total** | **running_total** |
| ------------ | -------------- | --------------- | ----------------- |
| 1            | 2020-04-03     | 100             | 100               |
| 2            | 2020-04-03     | 250             | 350               |
| 3            | 2020-04-04     | 80              | 430               |
| 4            | 2020-04-05     | 10              | 440               |

How do we write an SQL query to do this?

### Set Up Sample Data

First, let's create the table and populate it. You'll probably need to adjust the data types for this depending on the database you're using.

```sql
CREATE TABLE orders (
  order_id INT,
  order_date DATE,
  order_total INT
);
INSERT INTO orders (order_id, order_date, order_total) VALUES
(1, '2020-04-03', 100),
(2, '2020-04-03', 250),
(3, '2020-04-04', 80),
(4, '2020-04-05', 10);
```

Now we can select from the table to see what it looks like:

```sql
SELECT order_id, order_date, order_total
FROM orders;
```

| **order_id** | **order_date** | **order_total** |
| ------------ | -------------- | --------------- |
| 1            | 2020-04-03     | 100             |
| 2            | 2020-04-03     | 250             |
| 3            | 2020-04-04     | 80              |
| 4            | 2020-04-05     | 10              |

How do we calculate the running total using an SQL window function?

### Add an SQL Window Function

We can add a function to define the running total. A running total, or any total, will use the SUM function, as it adds numbers together. And in this example, we are adding the order_total value together:

```sql
SELECT
order_id,
order_date,
order_total,
SUM(order_total)
FROM orders;
```

To use this as a window function, and to calculate a running total, we add the OVER keyword:

```sql
SELECT
order_id,
order_date,
order_total,
SUM(order_total) OVER ()
FROM orders;
```

Now, inside the OVER keyword, we can add two things:

- The partition clause, which defines the window or range or sub-group of data we are looking at
- The order by clause, which defines how the data is ordered for the calculation.

For the running total, we want to calculate this based on all records, not a specific window or range or sub-group. So, we can leave this optional clause out, as by default it will include all records.

We want to include the ORDER BY clause though. This will let us define how the running total is calculated. A running total is a total of all of the previous rows.

But how do we know what a previous row is?

The previous row is the one with the previous order id. It could also be the order date, but in this example, there are multiple records with the same date. So let's use the order id.

We can update our query to use the order by clause within the OVER clause:

```sql
SELECT
order_id,
order_date,
order_total,
SUM(order_total) OVER (ORDER BY order_id ASC)
FROM orders;
```

We'll also give it a column alias of running_total so we know what it is in the result set. Also, because the order of the result set is not guaranteed when we run [a SELECT query](https://www.databasestar.com/sql-select-statement/), we should add an ORDER BY clause to the overall query.

```sql
SELECT
order_id,
order_date,
order_total,
SUM(order_total) OVER (ORDER BY order_id ASC) AS running_total
FROM orders
ORDER BY order_id ASC;
```

This function should now calculate the SUM of the order_total column, across all records so far, when ordered by the order ID.

Let's see the results:

| **order_id** | **order_date** | **order_total** | **running_total** |
| ------------ | -------------- | --------------- | ----------------- |
| 1            | 2020-04-03     | 100             | 100               |
| 2            | 2020-04-03     | 250             | 350               |
| 3            | 2020-04-04     | 80              | 430               |
| 4            | 2020-04-05     | 10              | 440               |

Woohoo! We've successfully calculated a running total using an SQL window function.

## Using the SQL Partition by Clause to Create Windows

In the earlier example, the running total calculation was done for all records. Window functions let you specify a window, and we didn't specify a window for the earlier example so the entire result set was used.

A window is a set of rows that the function looks at when performing its calculation. You can think of it like a subgroup for the function. It's also known as a partition.

To demonstrate the windowing feature of a windowing function, we'll need a bit more data in our sample table:

```sql
INSERT INTO orders (order_id, order_date, order_total) VALUES
(5, '2020-04-03', 120),
(6, '2020-04-04', 90),
(7, '2020-04-04', 50),
(8, '2020-04-04', 15);
```

Now we can select from the table to see what it looks like:

```sql
SELECT order_id, order_date, order_total
FROM orders;
```

| **order_id** | **order_date** | **order_total** |
| ------------ | -------------- | --------------- |
| 1            | 2020-04-03     | 100             |
| 2            | 2020-04-03     | 250             |
| 3            | 2020-04-04     | 80              |
| 4            | 2020-04-05     | 10              |
| 5            | 2020-04-03     | 120             |
| 6            | 2020-04-04     | 90              |
| 7            | 2020-04-04     | 50              |
| 8            | 2020-04-04     | 15              |

Now, how do we use the windowing feature? We use the PARTITION BY clause as part of the function.

The PARTITION BY clause lets us specify a column to use as a window, partition, or subgroup.

In this example, we want to see a running total for each day. Instead of seeing an overall running total, we want to see the total for each day, and for it to reset each day.

We can do this:

```sql
SELECT
order_id,
order_date,
order_total,
SUM(order_total) OVER (
  PARTITION BY order_date
  ORDER BY order_id ASC) AS running_total
FROM orders
ORDER BY order_id ASC;
```

Notice the only change made was adding PARTITION BY order_date. This means that the SUM function is used to calculate a running total, but it's calculated for each set of different order_dates.

If we run the query, we'll get this result:

| **order_id** | **order_date** | **order_total** | **running_total** |
| ------------ | -------------- | --------------- | ----------------- |
| 1            | 2020-04-03     | 100             | 100               |
| 2            | 2020-04-03     | 250             | 350               |
| 3            | 2020-04-04     | 80              | 80                |
| 4            | 2020-04-05     | 10              | 10                |
| 5            | 2020-04-03     | 120             | 470               |
| 6            | 2020-04-04     | 90              | 170               |
| 7            | 2020-04-04     | 50              | 220               |
| 8            | 2020-04-04     | 15              | 235               |

We can see the running_total is different. The number changes with each row and isn't really in order.

The problem here is that we are ordering by the order_id field. It makes it harder to read when the data is ordered in a different order to the partition.

Let's order by the order_date instead.

```sql
SELECT
order_id,
order_date,
order_total,
SUM(order_total) OVER (
  PARTITION BY order_date
  ORDER BY order_id ASC) AS running_total
FROM orders
ORDER BY order_date ASC;
```

| **order_id** | **order_date** | **order_total** | **running_total** |
| ------------ | -------------- | --------------- | ----------------- |
| 1            | 2020-04-03     | 100             | 100               |
| 2            | 2020-04-03     | 250             | 350               |
| 5            | 2020-04-03     | 120             | 470               |
| 3            | 2020-04-04     | 80              | 80                |
| 6            | 2020-04-04     | 90              | 170               |
| 7            | 2020-04-04     | 50              | 220               |
| 8            | 2020-04-04     | 15              | 235               |
| 4            | 2020-04-05     | 10              | 10                |

These results look better. We can see in rows 1-3 (order ID 1, 2, 5), the running total increases, as these values have the same order_date.

When we get to row 4 (order ID 3), the order_date is different, so the running_total is reset to 80 which is the order total value of that row.

Rows 5 to 7 (order ID 6, 7, 8) increase the running total because they have the same order_date, and the running_total is reset on row 8 (order ID 4) because the order_date changes.

So, that's how you can use the PARTITION BY in a query. You can use it to calculate the result of a function on a group of records.

Notice how all of the rows from the table are shown. You don't need to use the GROUP BY clause to get this kind of function working. This can be helpful in many situations.

## COUNT Example

In our examples so far, we've used the SUM function. There are many more functions we can use as window functions and using the SQL partition by keyword. One of [those functions is COUNT](https://www.databasestar.com/sql-count/).

### COUNT as a Window Function

Let's say we are working on the orders database and we had a question from one of the users:

"How can I see the running count of the number of orders? I want to see the order details, but I also want to see how many orders have been placed for each day."

We can do this in the same way as using SUM, except we use the COUNT function. The COUNT function will count the number of records, and it can be used as a window function.

```sql
SELECT
order_id,
order_date,
order_total,
COUNT(*) OVER (ORDER BY order_date ASC) AS running_count
FROM orders
ORDER BY order_date ASC;
```

In this example, we have selected some columns from the orders table, and also used the COUNT(\*) function to count rows. We have ordered by the order_date column as well.

Here are the results:

| **order_id** | **order_date** | **order_total** | **running_count** |
| ------------ | -------------- | --------------- | ----------------- |
| 1            | 2020-04-03     | 100             | 3                 |
| 2            | 2020-04-03     | 250             | 3                 |
| 5            | 2020-04-03     | 120             | 3                 |
| 3            | 2020-04-04     | 80              | 7                 |
| 6            | 2020-04-04     | 90              | 7                 |
| 7            | 2020-04-04     | 50              | 7                 |
| 8            | 2020-04-04     | 15              | 7                 |
| 4            | 2020-04-05     | 10              | 8                 |

The results show the order details and the running count of orders for each day. The count increases with each day: showing 3 on the first day, then 7 on the second day (original 3 plus 4 from the day), then 8 on the third day (the 7 from previously plus the 1 from the day).

### COUNT with PARTITION BY

What if the user saw this and said, "actually, I would prefer to see the number of orders just for that day, not the count overall".

We could change our query by adding a PARTITION BY clause, so that the COUNT only looks at the rows for that order date and not all records.

```sql
SELECT
order_id,
order_date,
order_total,
COUNT(*) OVER (
  PARTITION BY order_date
  ORDER BY order_date ASC) AS day_count
FROM orders
ORDER BY order_date ASC;
```

I've also renamed the column alias to day_count as I think this describes the data better.

Here's the result:

| **order_id** | **order_date** | **order_total** | **day_count** |
| ------------ | -------------- | --------------- | ------------- |
| 1            | 2020-04-03     | 100             | 3             |
| 2            | 2020-04-03     | 250             | 3             |
| 5            | 2020-04-03     | 120             | 3             |
| 3            | 2020-04-04     | 80              | 4             |
| 6            | 2020-04-04     | 90              | 4             |
| 7            | 2020-04-04     | 50              | 4             |
| 8            | 2020-04-04     | 15              | 4             |
| 4            | 2020-04-05     | 10              | 1             |

We can see that using the SQL PARTITION BY clause has caused the COUNT value to only be calculated on records for that date.

This example is similar to the SUM example in that it uses an aggregate function for each row.

### COUNT with PARTITION BY Different to ORDER BY

In the example earlier we had the same column for PARTITION BY and ORDER BY. What if we used different columns? We can partition by the order date, to calculate the COUNT based on the order date, but order by the order_id?

```sql
SELECT
order_id,
order_date,
order_total,
COUNT(*) OVER (
  PARTITION BY order_date
  ORDER BY order_id ASC) AS day_count
FROM orders
ORDER BY order_date ASC;
```

Here are the results:

| **order_id** | **order_date** | **order_total** | **day_count** |
| ------------ | -------------- | --------------- | ------------- |
| 1            | 2020-04-03     | 100             | 1             |
| 2            | 2020-04-03     | 250             | 2             |
| 5            | 2020-04-03     | 120             | 3             |
| 3            | 2020-04-04     | 80              | 1             |
| 6            | 2020-04-04     | 90              | 2             |
| 7            | 2020-04-04     | 50              | 3             |
| 8            | 2020-04-04     | 15              | 4             |
| 4            | 2020-04-05     | 10              | 1             |

We can see the COUNT value is different for each row and is actually incremented. So, when the order_id changes, the COUNT changes, but the COUNT is only operating on the records that have the same order_date.

So this is how you can change some of the parameters of the window functions to get different results.

## AVG Example

We've seen examples of using SUM and COUNT. Can we do the same with other aggregate functions [such as AVG](https://www.databasestar.com/sql-avg/)?

Yes, we can write a window function with AVG.

This can answer the question of, "how can I see the average order total so far with the order details?"

### AVG Window Function Example

To do that, we can write the following query:

```sql
SELECT
order_id,
order_date,
order_total,
AVG(order_total) OVER (ORDER BY order_date ASC) AS running_avg
FROM orders
ORDER BY order_date ASC;
```

This calculates the average of the order total for each order_date and displays it in a separate column.

Here are the results:

| **order_id** | **order_date** | **order_total** | **running_avg** |
| ------------ | -------------- | --------------- | --------------- |
| 1            | 2020-04-03     | 100             | 156             |
| 2            | 2020-04-03     | 250             | 156             |
| 5            | 2020-04-03     | 120             | 156             |
| 3            | 2020-04-04     | 80              | 100             |
| 6            | 2020-04-04     | 90              | 100             |
| 7            | 2020-04-04     | 50              | 100             |
| 8            | 2020-04-04     | 15              | 100             |
| 4            | 2020-04-05     | 10              | 89              |

What do these results mean? It shows the average of the order total for each day and all of the days before it.

- On 2020-04-03, the average is 156, as it includes the values of 100, 250, and 120)
- On 2020-04-04, the average changes to 100. The order totals for this day are all under 100 (80, 90, 50), but the average includes all values before it, which are the values from 2020-04-03.
- On 2020-04-05, the average is 89, as it includes all values before it as well.

### AVG Window Function with PARTITION BY

What if we want to see the average for the day only, not the running average?

We can do that using the PARTITION BY clause. We can add the order_date as a partition, which should show us the average for each date rather than a running average.

```sql
SELECT
order_id,
order_date,
order_total,
AVG(order_total) OVER (
  PARTITION BY order_date
  ORDER BY order_date ASC) AS day_avg
FROM orders
ORDER BY order_date ASC;
```

Here are the results:

| **order_id** | **order_date** | **order_total** | **day_avg** |
| ------------ | -------------- | --------------- | ----------- |
| 1            | 2020-04-03     | 100             | 156         |
| 2            | 2020-04-03     | 250             | 156         |
| 5            | 2020-04-03     | 120             | 156         |
| 3            | 2020-04-04     | 80              | 58          |
| 6            | 2020-04-04     | 90              | 58          |
| 7            | 2020-04-04     | 50              | 58          |
| 8            | 2020-04-04     | 15              | 58          |
| 4            | 2020-04-05     | 10              | 10          |

We can see the numbers are different. The average is calculated as an average just for that day, not the entire result set so far, because we used the PARTITION BY clause.

## ROW_NUMBER Example

Another use of window functions is to find the row number.

SQL has a function called ROW_NUMBER which returns the row's number in the result set. It exists in Oracle, SQL Server, PostgreSQL, and MySQL as of version 8.0.

### Basic ROW_NUMBER

To see the ROW_NUMBER function, we can try to use this function when querying a table.

```sql
SELECT
order_id,
order_date,
order_total,
ROW_NUMBER()
FROM orders
ORDER BY order_date ASC;
```

When we run this error, we'll get an error. The exact error depends on the database, and in SQL Server it displays this error:

```
The function 'ROW_NUMBER' must have an OVER clause.
```

This means we can't just call the function, we need to have an OVER clause.

### ROW_NUMBER as a Window Function

Let's try adding an OVER clause to the [ROW_NUMBER function](https://www.databasestar.com/row_number-sql-server/):

```sql
SELECT
order_id,
order_date,
order_total,
ROW_NUMBER() OVER(ORDER BY order_date ASC) AS row_num
FROM orders
ORDER BY order_date ASC;
```

This looks similar to other window functions. We've added an ORDER BY clause inside the OVER clause of the ROW_NUMBER function, so the function knows how to calculate the row number.

Here are the results:

| **order_id** | **order_date** | **order_total** | **row_num** |
| ------------ | -------------- | --------------- | ----------- |
| 1            | 2020-04-03     | 100             | 1           |
| 2            | 2020-04-03     | 250             | 2           |
| 5            | 2020-04-03     | 120             | 3           |
| 3            | 2020-04-04     | 80              | 4           |
| 6            | 2020-04-04     | 90              | 5           |
| 7            | 2020-04-04     | 50              | 6           |
| 8            | 2020-04-04     | 15              | 7           |
| 4            | 2020-04-05     | 10              | 8           |

We can see the ROW_NUMBER function (in the column called rownum, different to the [Oracle rownum function](https://www.databasestar.com/oracle-rownum/)) is incremented by 1 for each row, effectively showing the number of the row. This is useful if you ever need to return this in an SQL query rather than calculate it programmatically.

For example, if you want to display a ladder or standings of a sporting competition, you could use the ROW_NUMBER function to calculate their ranking or ladder position.

### ROW_NUMBER with PARTITION BY

What if you want to calculate the row number within a certain partition or window of data? You can do that with the SQL PARTITION BY clause.

This query will show the row number of each row that has the same order_date.

```sql
SELECT
order_id,
order_date,
order_total,
ROW_NUMBER() OVER(PARTITION BY order_date ORDER BY order_id ASC) AS rownum
FROM orders
ORDER BY order_date ASC;
```

Here are the results:

| **order_id** | **order_date** | **order_total** | **rownum** |
| ------------ | -------------- | --------------- | ---------- |
| 1            | 2020-04-03     | 100             | 1          |
| 2            | 2020-04-03     | 250             | 2          |
| 5            | 2020-04-03     | 120             | 3          |
| 3            | 2020-04-04     | 80              | 1          |
| 6            | 2020-04-04     | 90              | 2          |
| 7            | 2020-04-04     | 50              | 3          |
| 8            | 2020-04-04     | 15              | 4          |
| 4            | 2020-04-05     | 10              | 1          |

Notice how the rownum column (which is from the ROW_NUMBER function) is reset to 1 each time the order_date changes. This means the row number is calculated separately for each order_date.

As with all of these functions, you can change the parameters to give you the ordering and calculations you want.

## Ranking results with RANK and DENSE_RANK

There are two more functions that allow you to see the number of a row: [RANK and DENSE_RANK](https://www.databasestar.com/sql-rank/).

RANK allows you to find the rank or position of a row in a group of rows. DENSE_RANK is a similar function and allows you to find the rank of a row.

Sounds similar to ROW_NUMBER, right?

Well, the differences between ROW_NUMBER, RANK, and DENSE_RANK are:

- ROW_NUMBER will give every row a unique sequential number
- RANK will give matching rows the same number and skip numbers
- DENSE_RANK will give matching rows the same number but doesn't skip numbers

Let's see an example of these functions.

### Example of RANK

Let's say we wanted to find the rank of our orders based on the order_amount.

First, let's insert a couple of rows that have the same order_amount to see how they impact our output.

```sql
INSERT INTO orders (order_id, order_date, order_total)
VALUES (9, '2020-04-04', 100),
VALUES (10, '2020-04-05', 100);
```

Next, our SELECT query would look like this. We've ordered by the order_amount to make it easier to follow.

```sql
SELECT
order_id,
order_date,
order_total,
RANK() OVER(ORDER BY order_total DESC) AS row_rank
FROM orders
ORDER BY order_total DESC;
```

The results are:

| **order_id** | **order_date** | **order_total** | **row_rank** |
| ------------ | -------------- | --------------- | ------------ |
| 2            | 2020-04-03     | 250             | 1            |
| 5            | 2020-04-03     | 120             | 2            |
| 9            | 2020-04-04     | 100             | 3            |
| 10           | 2020-04-05     | 100             | 3            |
| 1            | 2020-04-03     | 100             | 3            |
| 6            | 2020-04-04     | 90              | 6            |
| 3            | 2020-04-04     | 80              | 7            |
| 7            | 2020-04-04     | 50              | 8            |
| 8            | 2020-04-04     | 15              | 9            |
| 4            | 2020-04-05     | 10              | 10           |

We can see the rows have been ordered by the order_total column in descending order. The row_rank shows the ranking of the rows.

Notice that there are three records with the same order_total, which all have the rank 3. The next row that follows has the rank of 6, because the ranks of 4 and 5 are skipped. This is part of how the RANK function works.

### Example of RANK With a Partition

We can use the PARTITION BY clause with the RANK function. This will allow us to see the rank of a row within a partition or group of other rows.

For example, partitioning on the order_date column will give us this query:

```sql
SELECT
order_id,
order_date,
order_total,
RANK() OVER(
  PARTITION BY order_date
  ORDER BY order_total DESC) AS row_rank
FROM orders
ORDER BY order_total DESC;
```

The results are:

| **order_id** | **order_date** | **order_total** | **row_rank** |
| ------------ | -------------- | --------------- | ------------ |
| 2            | 2020-04-03     | 250             | 1            |
| 5            | 2020-04-03     | 120             | 2            |
| 1            | 2020-04-03     | 100             | 3            |
| 9            | 2020-04-04     | 100             | 1            |
| 10           | 2020-04-05     | 100             | 1            |
| 6            | 2020-04-04     | 90              | 2            |
| 3            | 2020-04-04     | 80              | 3            |
| 7            | 2020-04-04     | 50              | 4            |
| 8            | 2020-04-04     | 15              | 5            |
| 4            | 2020-04-05     | 10              | 2            |

The row_rank is incremented for each order_date. The results are shown in a different order: we can see order ID 9 has a rank of 1, and order id 6 has a rank of 2. They are both on the same date but order ID 10 is showing in between them. This is because the ordering of the result set is different to the partitioning.

So, this shows that you can order by one column for your result set and another inside your window function.

### Example of DENSE_RANK

Now let's see the same example but using DENSE_RANK.

```sql
SELECT
order_id,
order_date,
order_total,
DENSE_RANK() OVER(ORDER BY order_total DESC) AS row_rank
FROM orders
ORDER BY order_total DESC;
```

The results are:

| **order_id** | **order_date** | **order_total** | **row_rank** |
| ------------ | -------------- | --------------- | ------------ |
| 2            | 2020-04-03     | 250             | 1            |
| 5            | 2020-04-03     | 120             | 2            |
| 9            | 2020-04-04     | 100             | 3            |
| 10           | 2020-04-05     | 100             | 3            |
| 1            | 2020-04-03     | 100             | 3            |
| 6            | 2020-04-04     | 90              | 4            |
| 3            | 2020-04-04     | 80              | 5            |
| 7            | 2020-04-04     | 50              | 6            |
| 8            | 2020-04-04     | 15              | 7            |
| 4            | 2020-04-05     | 10              | 8            |

This is a similar output to the RANK function. However, possible RANK values are not skipped. After order ID 9, 10, and 1, the next order ID of 6 has a rank of 4.

### RANK, DENSE_RANK, and ROW_NUMBER

We mentioned the differences between RANK, DENSE_RANK, and ROW_NUMBER earlier. Let's see an example of these functions:

```sql
SELECT
order_id,
order_date,
order_total,
ROW_NUMBER() OVER(ORDER BY order_total DESC) AS row_num,
RANK() OVER(ORDER BY order_total DESC) AS row_rank,
DENSE_RANK() OVER(ORDER BY order_total DESC) AS row_denserank
FROM orders
ORDER BY order_total DESC;
```

We can see the query uses multiple window functions in the same query. This is possible in SQL. We could have even used different parameters in our functions.

The results are:

| **order_id** | **order_date** | **order_total** | **row_num** | **row_rank** | **row_denserank** |
| ------------ | -------------- | --------------- | ----------- | ------------ | ----------------- |
| 2            | 2020-04-03     | 250             | 1           | 1            | 1                 |
| 5            | 2020-04-03     | 120             | 2           | 2            | 2                 |
| 9            | 2020-04-04     | 100             | 3           | 3            | 3                 |
| 10           | 2020-04-05     | 100             | 4           | 3            | 3                 |
| 1            | 2020-04-03     | 100             | 5           | 3            | 3                 |
| 6            | 2020-04-04     | 90              | 6           | 6            | 4                 |
| 3            | 2020-04-04     | 80              | 7           | 7            | 5                 |
| 7            | 2020-04-04     | 50              | 8           | 8            | 6                 |
| 8            | 2020-04-04     | 15              | 9           | 9            | 7                 |
| 4            | 2020-04-05     | 10              | 10          | 10           | 8                 |

There are a few things to notice here:

- ROW_NUMBER gives each row a unique number from 1-10.
- RANK gives the same number to rows with the same order_total, skipping over numbers they would have gotten (e.g. 4, 5)
- DENSE_RANK gives the same number to rows with the same order_total, but does not skip any numbers.

## Other Window Functions

There are many other functions that can be used as window functions that we have not covered here:

- MAX
- MIN
- LAG
- LEAD
- FIRST_VALUE
- LAST_VALUE
- CUME_DIST
- NTILE
- PERCENT_RANK

## Frequently Asked Questions

Here are some frequently asked questions, or things you should know, about SQL window functions.

### Why Can't I Just Use Subqueries?

You might have noticed that you can get the same results using subqueries and [joins](https://www.databasestar.com/sql-joins/).

This is true. But, there are some advantages of using SQL window/analytic functions instead of subqueries and joins to get this result.

- **Easier to write**. Once you understand how window functions work, they are easier to write than subqueries and joins to get the same result.
- **Easier to maintain**. If you have a complex query, it can be harder to maintain it if you are using subqueries to get the same result that a window function would.
- **May be faster**. Most of the time, using the database's built-in functionality is faster than writing your own. Using these window functions will likely make your code run faster than using subqueries.

### When Are Window Functions Performed?

When the database processes a query, the window functions are the last set of operations performed, except for the ORDER BY clause. This means that the joins, the WHERE clause, GROUP BY clause, and HAVING clause are all performed first, and then the window functions are performed.

This also means that the window functions can only appear in the SELECT list or the ORDER BY clause.

### Can You Nest Window Functions?

Yes and no.

While aggregate functions allow you to nest functions, you can't do the same thing with window functions.

However, you can specify a window function inside a subquery, and then perform another window function on that column inside your main query.

### Can You Use Multiple Window Functions in the Same Query?

Yes, you can.

You can have different window functions in the same SELECT statement, and they can have the same query_partition_clause or different query_partition_clause values.

You can also have the same window functions but use different query_partition_clause values as well.

### What Is The ORDER_BY_Clause Within Window Functions?

The order_by_clause within a window function is different from the ORDER BY clause for the entire query.

This clause specifies how data is ordered within a partition.

For some analytic functions, such as [COUNT](https://www.databasestar.com/sql-count/) and [MAX](https://www.databasestar.com/sql-max/), the order does not matter.

However, in other functions such as [LEAD](https://www.databasestar.com/sql-lead/), LAG, and [RANK](https://www.databasestar.com/sql-rank/), the order does matter. So, this is how the ordering is done for those functions.

The order_by_clause looks like this:

```sql
ORDER BY expression [ASC | DESC] [NULLS [FIRST | LAST ] ]
```

In this clause:

- **expression**: This is the expression or column to order by.
- **ASC|DESC**: This specifies that the expr should be ordered in ascending or descending order. The default is ascending.
- **NULLS FIRST|LAST**: This specifies where rows with NULL values should appear – either first in the list, or last. For ascending order sorts, NULLS LAST is the default. For descending order sorts, NULLS FIRST is the default.

### What Is The Windowing Clause?

The windowing_clause allows you to specify a range of rows that are used to perform the calculations for the current row. This is part of the [window function syntax](https://www.databasestar.com/sql-window-functions/).

The syntax of the windowing_clause is quite complicated, but here it is:

```sql
 ROWS|RANGE BETWEEN start_expression AND end_expression
```

The start_expression can be any of:

- UNBOUNDED_PRECEDING
- CURRENT ROW
- expression PRECEDING|FOLLOWING

And the end_expression can be any of:

- UNBOUNDED_FOLLOWING
- CURRENT ROW
- expression PRECEDING|FOLLOWING

The ROWS and RANGE keywords specify the window for each row for calculating the result of the function. ROWS specifies the window using rows, and RANGE specifies the window as a logical offset.

Let's take a look at an example using the ROW type syntax.

```sql
SELECT first_name,
last_name,
address_state,
COUNT(*) OVER (PARTITION BY address_state
ORDER BY address_state ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING) AS state_count
FROM student;
```

| **FIRST_NAME** | **LAST_NAME** | **ADDRESS_STATE** | **STATE_COUNT** |
| -------------- | ------------- | ----------------- | --------------- |
| Robert         | Pickering     | Colorado          | 2               |
| Susan          | Johnson       | Colorado          | 2               |
| Michelle       | Randall       | Florida           | 1               |
| Tom            | Capper        | Nevada            | 1               |
| Mark           | Holloway      | New York          | 2               |
| John           | Smith         | New York          | 3               |
| Steven         | Webber        | New York          | 3               |
| Andrew         | Cooper        | Texas             | 2               |
| Tanya          | Hall          | Texas             | 3               |
| Julie          | Armstrong     | Texas             | 3               |

You can see here that the state_count column is a little different. It only counts the records in the range that has been mentioned in the ROWS clause.

The ROWS BETWEEN 2 PRECEDING AND 1 FOLLOWING means that rows are only counted where the address_state equals the current records address_state, and only for the two rows before it and the one row after it.

This is why some of the Texas rows have a state_count of 2 and others are 3.

## Conclusion

SQL window functions are quite powerful once you know how they work. It's not something you'll use in every query, but once you know what they can be used for, you'll find yourself remembering them when you need to use them for a query.
