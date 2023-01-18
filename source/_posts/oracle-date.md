---
title: Oracle Date Functions The Complete Guide
tags: db
date: 2022-12-20
---

> 转载：[Oracle Date Functions: The Complete Guide - Database Star](https://www.databasestar.com/oracle-date-functions/#LAST_DAY)

There are many different date and time functions in Oracle, and they behave differently than other databases. Learn what they are and see some useful queries in this article.

Oracle date functions are any functions that work with date and/or time values. They often take dates as an input and return many different types of output.

I'll explain what each of the Oracle date functions is and show an example.

Let's start by taking a look at the different date-related data types in Oracle.

## Date and Time Data Types in Oracle

There are a few [different data types](https://www.databasestar.com/oracle-data-types/) in Oracle that store date values. They are:

- DATE: The "standard" date value in Oracle. It stores year, month, day, as well as hour, minute and second. Yes, even though it's called "date", it stores the time component. This is a good thing to remember.
- TIMESTAMP: This data type stores year, month, day, hour, minute, second, as well as fractional seconds.
- TIMESTAMP WITH TIME ZONE: This data type is the same as TIMESTAMP, but it stores the timezone along with it.
- TIMESTAMP WITH LOCAL TIME ZONE: This data type is similar to TIMESTAMP WITH TIME ZONE, but the timezone that's stored is the database timezone.
- INTERVAL YEAR TO MONTH: This data type stores a "period of time" (rather than a "point in time" like other data types), and represents a period of time in months up to years.
- INTERVAL DAY TO SECOND: This data type also stores a period of time, but stores a value that captures seconds all the way up to days.

So now we've looked at the different data types, let's take a look at the different Oracle date functions.

## SYSDATE Function

The Oracle SYSDATE function allows you to easily output the current date. It shows the date and time of the database server.

To use it, you simply type the word SYSDATE. It has no parameters, which means you don't need any brackets after it.

An example of the SYSDATE function is:

```sql
SELECT SYSDATE
FROM dual;
```

Result:

```
10/SEP/22
```

I've used the DUAL table because Oracle needs to select from a table in a select query, and the DUAL table is useful for this (read more about [the dual table here](https://www.databasestar.com/dual-table-in-oracle/)).

As you can see, the current date is shown. It only shows the date, though. This is because the output format for SELECT queries for dates is currently set to the DD/MM/YYYY format.

The SYSDATE function does return the time component as well though. We can see this if we change the session's date format, or surround the SYSDATE in a TO_CHAR function.

```sql
ALTER SESSION
SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';
```

Now, let's rerun the SELECT statement with the SYSDATE function.

```sql
SELECT SYSDATE
FROM dual;
```

Result:

```
2022-09-10 08:54:19
```

As you can see, the output now shows the date and time returned from SYSDATE. We changed the date format in the session to include the time.

We could use the [TO_CHAR function](https://www.databasestar.com/oracle-to_char/) to change the way this particular function is shown:

```sql
SELECT
TO_CHAR(SYSDATE, 'DD/MM/YYYY HH:MI:SS') AS sysdate_time
FROM dual;
```

Result:

```
10/09/2022 08:54:19
```

You can see that the output now includes the date and time.

## CURRENT_DATE

The CURRENT_DATE function is similar to the SYSDATE function, but it shows you the **current date and time in the session timezone**.

This is the timezone that your session is in, or the timezone you're in when you log in to the system. This can sometimes be different to the database timezone.

To use this function, simply add the word CURRENT_DATE to your query. No brackets are needed as there are no parameters.

```sql
SELECT CURRENT_DATE
FROM dual;
```

Result:

```
10/SEP/22
```

This shows the current date of your user session.

Just like with the SYSDATE function, this function **returns a DATE data type**, which actually includes a date and a time. To show the time component of this value, either use the TO_CHAR function or alter your session to include the time format.

```sql
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD HH24:MI:SS';
```

The other way is to use the TO_CHAR function to change the format.

```sql
SELECT
TO_CHAR(CURRENT_DATE, 'DD/MM/YYYY HH:MI:SS')
FROM dual;
```

Result:

```
10/09/2022 08:54:19
```

You can see that the output now includes the date and time.

### Oracle CURRENT_DATE Vs SYSDATE

The main difference between CURRENT_DATE and SYSDATE is:

- CURRENT_DATE returns the date from your **session** timezone (your timezone).
- SYSDATE returns the date from the **database** timezone.

If you're in the east coast of the United States and your database is on the west coast, these functions will show different values. If you're in Australia and the database is in London, they will show different values.

They might even _look_ the same but actually be different.

This is because the default output is DD-MON-YY, which hides the time.

This is the default output, assuming I'm in Melbourne (UTC +10) and the database is in Perth (UTC +8).

```sql
SELECT CURRENT_DATE, SYSDATE
FROM dual;
```

Result:

| **CURRENT_DATE** | **SYSDATE** |
| ---------------- | ----------- |
| 10/SEP/22        | 10/SEP/22   |

These values look the same, right?

Now, if I include the time component by using [TO_CHAR](https://www.databasestar.com/oracle-to_char/), my result shows these two values as being different.

```sql
SELECT
TO_CHAR(CURRENT_DATE, 'DD-MON-YY HH:MI:SS') AS CDATE,
TO_CHAR(SYSDATE, 'DD-MON-YY HH:MI:SS') AS SDATE
FROM dual;
```

Result:

| **CDATE**          | **SDATE**          |
| ------------------ | ------------------ |
| 10-SEP-22 05:53:33 | 10-SEP-22 03:53:33 |

### How Can I Get the Oracle CURRENT_DATE – 1 Day?

If you want to find records that are less than, greater than, or equal to the day before today (or any comparison, really), then you can do this with the Oracle CURRENT_DATE function.

You'll just have to use [TRUNC](https://www.databasestar.com/oracle-trunc/) as well.

```sql
SELECT
CURRENT_DATE,
TRUNC(CURRENT_DATE) AS trunc_today,
TRUNC(CURRENT_DATE)-1 AS trunc_yesterday
FROM dual;
```

Result:

| **CURRENT_DATE** | **TRUNC_TODAY** | **TRUNC_YESTERDAY** |
| ---------------- | --------------- | ------------------- |
| 10/SEP/22        | 10/SEP/22       | 09/SEP/22           |

You can use this TRUNC(CURRENT_DATE)-1 logic in your other SQL queries:

```sql
--Find employees hired yesterday or later.
SELECT name
FROM employee
WHERE hire_date >= TRUNC(CURRENT_DATE)-1
```

## SYSTIMESTAMP

The SYSTIMESTAMP function returns the **date and time of the database**.

The important part to remember is that it returns the time of the database, not your local time.

So, if you're accessing a database in a different time zone, it will return the time and timezone of the place where the database is stored, not your local time zone.

For example, if your database is in London but you are in New York, the SYSTIMESTAMP will return a time that is 5 hours ahead of your time.

It's similar to the SYSDATE function, however it **returns a TIMESTAMP WITH TIME ZONE** instead of a DATE data type.

This means it includes the date, time, and fractional seconds.

```sql
SELECT SYSTIMESTAMP
FROM dual;
```

Result:

```
10/SEP/22 08:57:17.067000000 AM +10:00
```

Now, because it's a TIMESTAMP WITH TIME ZONE, it shows the time by default, unlike the DATE data type.

You can see the output here shows the date, the time, the fractions of seconds, and the timezone. You don't need to format it to see the complete output.

### How Can I Insert With SYSTIMESTAMP?

You can insert the value returned by SYSTIMESTAMP in a few ways.

First, you can ensure that the column you're inserting into is of type TIMESTAMP WITH TIME ZONE.

Alternatively, if it isn't, you can use the TO_CHAR function to convert the value into a VARCHAR2 data type, and insert that.

However, it's generally not a good idea to insert dates into character fields. I would recommend inserting the value as a TIMESTAMP WITH TIME ZONE.

### Can I Find the SYSTIMESTAMP Without Timezone?

Yes, you can.

You can use SYSDATE to just get the date and time, but it won't have fractional seconds.

### Can I Use TO_CHAR With SYSTIMESTAMP?

Yes, you can. See the Examples below for more information.

You can include the SYSTIMESTAMP function inside TO_CHAR, and specify the format of the values to output.

### Example 1

This is the SYSDATE and SYSTIMESTAMP function side-by-side.

```sql
SELECT
SYSDATE,
SYSTIMESTAMP
FROM dual;
```

Result:

| **SYSDATE** | **SYSTIMESTAMP**                       |
| ----------- | -------------------------------------- |
| 10/SEP/2022 | 10/SEP/22 09:35:48.801000000 AM +11:00 |

### Example 2

This example uses the TO_CHAR function on SYSTIMESTAMP.

```sql
SELECT
SYSTIMESTAMP,
TO_CHAR(SYSTIMESTAMP, 'dd Mon yyyy') AS text_output
FROM dual;
```

Result:

| **SYSTIMESTAMP**                       | **TEXT_OUTPUT** |
| -------------------------------------- | --------------- |
| 10/SEP/22 09:36:18.196000000 AM +11:00 | 10 Sep 2022     |

## CURRENT_TIMESTAMP

The CURRENT_TIMESTAMP function returns the **date and time in the timezone of your session**, or where you have logged in from.

It's similar to the CURRENT_DATE function in that it returns the date and time of your session, instead of the database. It's also similar to the SYSTIMESTAMP function in that it returns the timestamp instead of a date.

The **return data type is a TIMESTAMP WITH TIME ZONE**, which includes date, time, fractional seconds, and a timezone.

The CURRENT_TIMESTAMP has one optional parameter: the precision or number of fractional seconds to return. If omitted, it uses 6 places.

```sql
CURRENT_TIMESTAMP([precision])
```

An example of this function is:

```sql
SELECT CURRENT_TIMESTAMP
FROM dual;
```

Result:

```
10/SEP/22 08:57:49.020000000 AM AUSTRALIA/MELBOURNE
```

You can see that the current date and time are shown here, along with the timezone.

### Can I Subtract Hours from the CURRENT_TIMESTAMP?

Yes, you can. The best way to do this is to use an interval data type, as you'll keep your original data type.

For example, if I wanted to subtract 4 hours from the current time, I would do this:

```sql
SELECT
CURRENT_TIMESTAMP,
CURRENT_TIMESTAMP - INTERVAL '4' HOUR
FROM dual;
```

Result:

| **CURRENT_TIMESTAMP**                            | **CURRENT_TIMESTAMP-INTERVAL**                   |
| ------------------------------------------------ | ------------------------------------------------ |
| 10/SEP/22 06:17:25.690000000 AM AUSTRALIA/SYDNEY | 10/SEP/22 02:17:25.690000000 AM AUSTRALIA/SYDNEY |

## LOCALTIMESTAMP

The final function that gets the current date is the LOCALTIMESTAMP function.

This function gets the **current date and time of your session**.

It's similar to the CURRENT_TIMESTAMP function, but **LOCALTIMESTAMP returns a TIMESTAMP value** and CURRENT_TIMESTAMP returns a TIMESTAMP WITH TIME ZONE VALUE.

This means that LOCALTIMESTAMP returns just the date and time, and no timezone.

The LOCALTIMESTAMP function looks like this:

```sql
SELECT LOCALTIMESTAMP
FROM dual;
```

Result:

```
10/SEP/22 08:58:25.614000000 AM
```

You can see that the output shows the date, time, and fractional seconds.

The parameters of the LOCALTIMESTAMP function are:

- timestamp_precision (mandatory): This specifies the number of digits of seconds of the return value, also known as the "fractional second precision".

## ADD_MONTHS

The ADD_MONTHS function allows you to input a date value, and a number of months, and return another date value. The value returned is the input date value plus the number of months you supply.

So, if you start with Jan 10th 2022, and add 3 months, the function will return Apr 10th, 2022.

The syntax is:

```sql
ADD_MONTHS (input_date, number_of_months)
```

An example of this function is:

```sql
SELECT
SYSDATE,
ADD_MONTHS(SYSDATE, 5) AS new_date
FROM dual;
```

| **SYSDATE** | **NEW_DATE** |
| ----------- | ------------ |
| 10/SEP/22   | 10/FEB/23    |

This query shows the SYSDATE, as well as the SYSDATE with 5 months added. You can see that it has the same day, but it is 5 months in the future.

You can also provide negative values:

```sql
SELECT
SYSDATE,
ADD_MONTHS(SYSDATE, -12) AS new_date
FROM dual;
```

| **SYSDATE** | **NEW_DATE** |
| ----------- | ------------ |
| 10/SEP/22   | 10/SEP/21    |

This will show a date of 12 months in the past.

For more information on using the ADD_MONTHS function, including some "what if" questions, read this article: [Oracle ADD_MONTHS Function with Examples](https://www.databasestar.com/oracle-add_months/).

## LAST_DAY

The LAST_DAY function returns the last day of the month of the specified date value.

You supply a date, and another date is returned which is the last day of the month.

The syntax is:

```sql
LAST_DAY (input_date)
```

Let's see an example:

```sql
SELECT
SYSDATE,
LAST_DAY(SYSDATE) AS last_of_month
FROM dual;
```

| **SYSDATE** | **LAST_OF_MONTH** |
| ----------- | ----------------- |
| 10/SEP/22   | 30/22             |

You can see here that I've shown today's date using SYSDATE, and also the last day of this month using the LAST_DAY function.

What if I wanted to specify a particular date?

You can do that as well, by entering the date in the database's default format (usually DD-MON-YY) or using the TO_DATE function.

```sql
SELECT
LAST_DAY('03-OCT-2022')
FROM dual;
```

Result:

```
31/OCT/2022
```

For more information on the LAST_DAY function, such as returning the first day of the next month (and other examples), read my article: [Oracle LAST_DAY Function with Examples](https://www.databasestar.com/oracle-next_day/).

## NEXT_DAY

The NEXT_DAY function returns the date of the next specified weekday that comes after the specified value.

It's handy for working with any business logic you have where you need to use weekdays.

It takes two parameters:

```sql
NEXT_DAY (input_date, weekday)
```

The input date is the date to start from, and the weekday is the name of the day you're looking for.

For example, running SYSDATE on today's date will show 15 Sep 2022, and it's a Tuesday.

To find the next Thursday that appears after today, use this function:

```sql
SELECT
NEXT_DAY(SYSDATE, 'THURSDAY')
FROM dual;
```

Result:

```
15/SEP/22
```

You can see it shows a date of 15th September, which is the next Thursday that comes after the date I mentioned.

If I want to find the next Monday, I change the function slightly:

```sql
SELECT
NEXT_DAY(SYSDATE, 'MONDAY')
FROM dual;
```

Result:

```
12/SEP/22
```

You can see it shows a date of 12th September, which is next Monday. It doesn't show the day before, even though it's closer. It always goes forwards.

For more information on the NEXT_DAY function, read my article here: [Oracle NEXT_DAY Function with Examples](https://www.databasestar.com/oracle-next_day/).

## MONTHS_BETWEEN

The MONTHS_BETWEEN function allows you to find the number of months between two specified dates.

You specify two dates as parameters, and a number is returned:

```sql
MONTHS_BETWEEN (date1, date2)
```

Date1 is usually the later date.

If date1 is greater than date2, the value is positive. Otherwise, it is negative.

The returned value can be a whole or a decimal number. So, it returns a partial month value.

Let's see an example:

```sql
SELECT
MONTHS_BETWEEN('12-MAY-2022', '10-FEB-2022')
FROM dual;
```

Result:

```
3.064516129
```

The value returned is 3.06 because there is approximately 3.06 months between these two dates.

## ROUND

The ROUND function allows you to round a date value to a format you specify.

This function is often used with numbers, but can also be used with dates.

If you use it with a date value, you can specify a DATE or TIMESTAMP value. You can specify any format mask, but the default is the nearest day, and is returned as a DATE.

The syntax is:

```sql
ROUND (input_date, round_to)
```

If I wanted to round a date to the nearest month, I would use something like this:

```sql
SELECT
ROUND(SYSDATE, 'MM')
FROM dual;
```

Result:

```
01/SEP/22
```

This shows a value of 1 Sep because the specified date (SYSDATE, or 10 Sep) has been rounded forwards to this date.

If we specify a different date and input:

```sql
SELECT
ROUND(SYSDATE, 'YYYY')
FROM dual;
```

Result:

```
01/JAN/23
```

We can see that the date shown is 1 Jan 2023. This is because it has rounded forward to the nearest year, and in this case, it is the start of 2023.

For more information on the ROUND function, read my article: [SQL ROUND Function with Examples](https://www.databasestar.com/sql-round/).

## TRUNC

The TRUNC function, like the round function, works with numbers as well as dates.

It truncates or removes a part of the date to the format you specify.

The syntax is:

```sql
TRUNC (input_date, format_mask)
```

If you don't specify a format mask, then the function will truncate the value to the nearest day. This is helpful if you want to remove the time part of a date value.

For example, to show only the date part of today's date:

```sql
SELECT
TRUNC(SYSDATE)
FROM dual;
```

Result:

```
10/SEP/22
```

This shows only the date part of today.

Or, you can show only the YEAR:

```sql
SELECT
TRUNC(SYSDATE, 'YYYY')
FROM dual;
```

Result:

```
01/JAN/22
```

You can see that a date is shown that matches the first day of the current year.

For more information on the TRUNC function, read my article here: [Oracle TRUNC Function with Examples](https://www.databasestar.com/oracle-trunc/).

## EXTRACT

The EXTRACT function in Oracle extracts a specific part of a date from a date or interval value.

This means that it can get the month, or year, for example, from a DATE value. I think it's easier than using a conversion function such as TO_CHAR.

The EXTRACT function looks like this:

```sql
EXTRACT (date_component FROM expression)
```

The date_component is a keyword that represents the part of the date to extract, such as MONTH, DAY, YEAR, or HOUR.

The expression is a value or column that is a date or interval data type.

An example of this function is:

```sql
SELECT
SYSDATE,
EXTRACT(MONTH FROM SYSDATE) AS extract_month
FROM dual;
```

| **SYSDATE** | **EXTRACT_MONTH** |
| ----------- | ----------------- |
| 10/SEP/22   | 9                 |

This shows the month part of the SYSDATE.

For more information on the EXTRACT function, you can read my article here: [Oracle EXTRACT Function with Examples](https://www.databasestar.com/oracle-extract/).

## TO_DATE

The TO_DATE function allows you to convert a character value into a date value. It converts any character data type (CHAR, VARCHAR2, NCHAR, or NVARCHAR2) into a DATE type.

It's useful if you have a date in a particular format in a text format or text column, and you need it in a DATE format (for a function or to insert into a column, for example).

The syntax is:

```sql
TO_DATE (date_text [, format_mask] [, nls_date_language])
```

The date_text is the date you want to convert, which is in some kind of text or character format. You can optionally specify the format mask (which is the format that this date value was provided in), and the nls_date_langauge is used for dates in different languages or countries.

An example of this function is:

```sql
SELECT
TO_DATE('21-JAN-2022', 'DD-MON-YYYY')
FROM dual;
```

Result:

```
21/JAN/22
```

This shows the specified date (21 Jan 2022) converted to a date format. It might look the same in your IDE, but that's just how dates are displayed. The value started as a character value and is converted to a date value.

If your date is in a different format:

```sql
SELECT
TO_DATE('20220115_142309', 'YYYYMMDD_HH24MISS')
FROM dual;
```

Result:

```
15/JAN/22
```

This example shows a completely different format, but it can still be converted to a date format. We have specified the format mask here, which is the format that the first parameter is in.

For more information on the TO_DATE function, read my article here: [Oracle TO_DATE Function with Examples](https://www.databasestar.com/oracle-to_date/).

## NEW_TIME

The NEW_TIME function converts a date from one timezone to another.

It's not something I've used very often, but if you need to work with different timezones, it can be very helpful.

The syntax is:

```sql
NEW_TIME (input_date, input_timezone, output_timezone)
```

To use this function, you specify the input_date, and the timezone this date is in as the input_timezone. You then specify the timezone you want to convert to in the output_timezone.

Let's see an example:

```sql
SELECT
SYSDATE,
NEW_TIME(SYSDATE, 'GMT', 'PST') AS converted_time
FROM dual;
```

| **SYSDATE** | **CONVERTED_TIME** |
| ----------- | ------------------ |
| 10/SEP/22   | 10/SEP/22          |

This converts the current date and time from a GMT timezone to a PST timezone. Note that you can only see the dates here and not times, because I haven't changed the session settings or used a function such as TO_CHAR to format the output.

I'll explain all about the TO_CHAR function and using it to format dates below, but here's a brief example:

```sql
SELECT
TO_CHAR(SYSDATE, 'dd-mm-yy hh:mi:ss AM') AS sysdate_time,
TO_CHAR(NEW_TIME(SYSDATE, 'GMT', 'PST'), 'dd-mm-yy hh:mi:ss AM') AS newtime_test
FROM dual;
```

| **SYSDATE_TIME**    | **NEWTIME_TEST**     |
| ------------------- | -------------------- |
| 10-09-2209:16:37 AM | 10-09-22 01:16:37 AM |

This now shows the date, which was in GMT but then converted to PST.

## FROM_TZ

This function converts a TIMESTAMP value and a specified TIME ZONE to a TIMESTAMP WITH TIME ZONE value.

If you need a value that's in a TIMESTAMP WITH TIME ZONE format, then this is the function to use.

The syntax is:

```sql
FROM_TZ (timestamp_value, timezone_value)
```

An example of this function is:

```sql
SELECT
FROM_TZ(TIMESTAMP '2022-04-19 07:13:50', '-9:00')
FROM dual;
```

Result:

```
19/APR/22 07:13:50.000000000 AM -09:00
```

This converts the timestamp specified (which is a date and time) into a TIMESTAMP WITH TIME ZONE, in the timezone of -9 hours from GMT.

Note the TIMESTAMP keyword in front of the date and time value, which denotes that the value is a TIMESTAMP value.

## SYS_EXTRACT_UTC

The SYS_EXTRACT_UTC will extract or convert the specified date and time into a UTC (also known as GMT) date and time.

You specify a data type that has a timezone, and a TIMESTAMP is returned that shows the time in UTC time.

For example, we can convert this date to UTC:

```sql
SELECT
SYS_EXTRACT_UTC(TIMESTAMP '2022-05-15 19:10:45 +10:00')FROM dual;
```

Result:

```
15/MAY/22 09:10:45.000000000 AM
```

This converts the specified time, which is +10 UTC, into a UTC time. The UTC time is 10 hours before the specified time.

This function will return a different day if the conversion results in the output date being a different day to the input date:

```sql
SELECT
SYS_EXTRACT_UTC(TIMESTAMP '2022-05-15 22:06:12 -7:00')
FROM dual;
```

Result:

```
16/MAY/22 05:06:12.000000000 AM
```

This moves the time forward to get to UTC time, which results in the date being on a different day.

## SESSIONTIMEZONE

The SESSIONTIMEZONE function returns the timezone offset of your session, in the format of [+|-]TZH:TZM, or a time zone region name.

This can be helpful to know, especially if you're doing a lot of work with dates and work on databases in different time zones.

The syntax for the SESSIONTIMEZONE function is quite simple.

```
SESSIONTIMEZONE
```

There is really only one way to use the SESSIONTIMEZONE function.

```sql
SELECT SESSIONTIMEZONE
FROM dual;
```

Result:

```
Australia/Sydney
```

This function shows that I am in the Sydney time zone.

### How Can You Change the Session Time Zone?

While you can't easily change the database time zone, the session time zone is something that is easy to change.

To change the session time zone, you run the ALTER SESSION command:

```sql
ALTER SESSION SET TIME_ZONE = '+8:0';
```

### What's The Difference Between SESSIONTIMEZONE and CURRENT_TIMESTAMP?

Both of these functions look at the time of the session. But there are some differences.

- CURRENT_TIMESTAMP returns the entire date and time, including the time zone.
- SESSIONTIMEZONE returns only the time zone.

Sometimes, SESSIONTIMEZONE may be easier to use than trying to perform string manipulation on the CURRENT_TIMESTAMP function.

## DBTIMEZONE

The DBTIMEZONE function returns the timezone offset of the database, in the format of [+|-]TZH:TZM, or a time zone region name.

It's helpful when working with dates to know what timezone the database is in. This is easier than using one of the other date functions, or performing an extraction from a TIMESTAMP WITH TIME ZONE value.

This DBTIMEZONE function is how to check the timezone in Oracle database 11g – and all other database versions.

The syntax for the DBTIMEZONE function is quite simple:

```
DBTIMEZONE
```

There is really only one way to use the Oracle DBTIMEZONE function.

```sql
SELECT DBTIMEZONE
FROM dual;
```

Result:

```
+00:00
```

This shows that my database is in the UTC + 0 time zone.

### How Can You Change the Database Time Zone?

The database time zone is actually the time zone of the operating system of the server it runs on.

So, you can't specifically change the time zone on the database.

You can view it by running this query:

```sql
SELECT SESSIONTIMEZONE FROM DUAL;
```

Or, this query will show the current time with timezone:

```sql
SELECT current_timestamp FROM DUAL;
```

### What's the Difference Between Oracle DBTIMEZONE and SESSIONTIMEZONE in Oracle?

The difference between these two functions is:

- DBTIMEZONE returns the time zone of the database server.
- SESSIONTIMEZONE returns the time zone of your session.

These two values may be different if you're in a different location to your database.

### What's The Difference Between Oracle DBTIMEZONE vs SYSTIMESTAMP?

The difference between DBTIMEZONE and SYSTIMESTAMP is:

- DBTIMEZONE returns just the timezone offset of the database (e.g. +7:00).
- SYSTIMESTAMP returns the timestamp with time zone of the database (e.g. 13-JUL-2022 08:49:02 AM +7:00)

So, the SYSTIMESTAMP includes more information than the DBTIMEZONE function.

## Formatting Dates

So far we're worked with date values. We've changed their data type, worked with timezones, and even extracted and truncated parts of them.

However, you might have noticed that the data types are displayed in a certain format. And, that the DATE data type doesn't show the time, even though the time is included.

Fortunately, Oracle lets you format a DATE value for your output. This can be helpful to check if your function is returning the right value in a query, or for displaying an output in your application.

You can do this with the TO_CHAR function.

For example, we show the SYSDATE like this:

```sql
SELECT SYSDATE
FROM dual;
```

Result:

```
10/SEP/22
```

If we want to see it in a different format, such as 2022-09-10, we can write this:

```sql
SELECT SYSDATE,
TO_CHAR(SYSDATE, 'YYYY-MM-DD') AS formatted_date
FROM dual;
```

| **SYSDATE** | **FORMATTED_DATE** |
| ----------- | ------------------ |
| 10/SEP/22   | 2022-09-10         |

You can see that the output is in a different format. It has 4 digits for the year, then a dash, then two digits for the month, then a dash, then two digits for the day.

You can also use the TO_CHAR function to show the time. This is a common way to use this function.

```sql
SELECT SYSDATE,
TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS AM') AS formatted_date
FROM dual;
```

| **SYSDATE** | **FORMATTED_DATE**     |
| ----------- | ---------------------- |
| 10/SEP/22   | 2022-09-10 09:21:29 AM |

This shows the same date, but in a different format. It shows the hours, minutes, seconds, and an AM/PM marker.

Now, you're probably wondering, what do all of those formatting codes mean? Some of them may seem obvious (such as YYYY means a 4-digit year). But what about the others?

Let's look at them now.

## Date Format Parameters

In many Oracle functions that deal with dates, such as TO_CHAR, you can specify a "format mask". This is a parameter that lets you specify a certain combination of characters, which allows Oracle to translate into a specific format for a date.

You can use these characters to change the way that dates are formatted.

A full list of the date format parameters is shown here:

**Year**

| **Parameter** | **Explanation**                                                                                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| YEAR          | Year, spelled out in full words                                                                                                                                                                                                                  |
| YYYY          | 4-digit year                                                                                                                                                                                                                                     |
| YYY           | Last 3 digits of year                                                                                                                                                                                                                            |
| YY            | Last 2 digits of year                                                                                                                                                                                                                            |
| Y             | Last digit of year                                                                                                                                                                                                                               |
| IYY           | Last 3 digits of ISO year                                                                                                                                                                                                                        |
| IY            | Last 2 digits of ISO year                                                                                                                                                                                                                        |
| I             | Last digit of ISO year                                                                                                                                                                                                                           |
| IYYY          | 4-digit year, which is based on the ISO standard                                                                                                                                                                                                 |
| RRRR          | This format accepts a 2-digit year, and returns a 4-digit year. If the provided value is between 0 and 49, it will return a year greater than or equal to 2000. If the provided value is between 50 and 99, it will return a year less than 2000 |

**Month**

| **Parameter** | **Explanation**                                              |
| ------------- | ------------------------------------------------------------ |
| Q             | Quarter of year, from 1 to 4. JAN to MAR = 1                 |
| MM            | Month, from 01 to 12. JAN = 01                               |
| MON           | Abbreviated name of month.                                   |
| MONTH         | Name of month, padded with blanks to length of 9 characters. |
| RM            | Roman numeral month, from I to XII. JAN = I.                 |

**Week**

| **Parameter** | **Explanation**                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------- |
| WW            | Week of year, from 1 to 53. Week 1 starts on the first day of the year, and continues to the seventh day of the year. |
| W             | Week of month, from 1 to 5. Week 1 starts on the first day of the month and ends on the seventh.                      |
| IW            | Week of year, from 1 to 52 or 1 to 53, based on the ISO standard.                                                     |

**Day**

| **Parameter** | **Explanation**                                                   |
| ------------- | ----------------------------------------------------------------- |
| D             | Day of week, from 1 to 7.                                         |
| DAY           | Name of day.                                                      |
| DD            | Day of month, from 1 to 31.                                       |
| DDD           | Day of year, from 1 to 366.                                       |
| DY            | Abbreviated name of day.                                          |
| J             | Julian day, which is the number of days since January 1, 4712 BC. |

**Time**

| **Parameter** | **Explanation**                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| HH            | Hour of day, from 1 to 12.                                                                                                        |
| HH12          | Hour of day, from 1 to 12.                                                                                                        |
| HH24          | Hour of day, from 0 to 23.                                                                                                        |
| MI            | Minute, from 0 to 59                                                                                                              |
| SS            | Second, from 0 to 59                                                                                                              |
| SSSSS         | Seconds past midnight, from 0 to 86399.                                                                                           |
| FF            | Fractional seconds. This uses a value from 1 to 9 after FF, to indicate the number of digits in the fractional seconds (e.g. FF7) |

**Indicators**

| **Parameter**         | **Explanation**              |
| --------------------- | ---------------------------- |
| AM, A.M., PM, or P.M. | Meridian indicator           |
| AD or A.D             | AD indicator                 |
| BC or B.C.            | BC indicator                 |
| TZD                   | Daylight savings information |
| TZH                   | Time zone hour.              |
| TZM                   | Time zone minute.            |
| TZR                   | Time zone region.            |

## Common Uses for Date Functions

So, we've seen explanations of all of the date functions in Oracle, and some examples for how they work.

Now, let's take a look at some common examples of date functions.

These examples will show you how to do common tasks in Oracle using dates. So, if you're looking up how to find the date one year from now, or format a date in a certain way, this is where you'd look.

Let's see the examples.

###

### Find the Number of Days Between Two Dates

To find the number of days between two dates, you can simply subtract one date from another. You don't need to use a function for this.

For example, to find the number of days between 31 Dec 2022 and today, run this query:

```sql
SELECT
TO_DATE('31-DEC-2022') - SYSDATE
FROM dual;
```

Result:

```
111.6092245
```

### Add Days To A Date

Just like subtracting two dates, you can add a number to a date to get a number of days in the future. Adding numbers to a date is treated as adding days.

```sql
SELECT
SYSDATE + 7
FROM dual;
```

Result:

```
17/SEP/22
```

This shows the date 7 days from now.

###

### Subtracting Days From A Date

To subtract days from a date, just subtract a number. A number represents the number of days.

```sql
SELECT
SYSDATE - 21
FROM dual;
```

Result:

```
20/AUG/22
```

This shows the date 21 days in the past.

### Show Today's Date and Time

To show today's date and time, you can use the SYSDATE function, along with the TO_CHAR function to format it. Alternatively, you can use the CURRENT_DATE function.

SYSDATE shows the server's date and time, and CURRENT_DATE shows your session's date and time.

You can write a query like this:

```sql
SELECT
TO_CHAR(SYSDATE, 'DD-MM-YYYY HH:MI:SS AM')
FROM dual;
```

Result:

```
10-09-2022 09:24:11 AM
```

Or, you can write the same query using CURRENT_DATE, if your session time is more important (if, for example, your database is in another timezone and you want to find the time where you are now).

```sql
SELECT
TO_CHAR(CURRENT_DATE, 'DD-MM-YYYY HH:MI:SS AM')
FROM dual;
```

Result:

```
10-09-2022 09:24:11 AM
```

### Add One Year To A Date

Earlier, I showed you how to add a number of days to a date. This is helpful for adding days, but when it comes to adding years, using days is not reliable.

This is because the number of days in each year is not consistent. Rather than using a complicated lookup table and formula, you can just use the ADD_MONTHS function.

To add one year to today's date:

```sql
SELECT
ADD_MONTHS(SYSDATE, 12)
FROM dual;
```

Result:

```
10/SEP/23
```

### Subtract Years From a Date

Similar to adding a year to a date, you can also subtract years from a date. This is best done using the ADD_MONTHS function and providing a negative number value.

To find the date 5 years before a specific date:

```sql
SELECT
ADD_MONTHS('10-JUL-2022', -60)
FROM dual;
```

Result:

```
10/JUL/17
```

Notice that I added the number 60 in there, because 5 years \* 12 months is 60.

It could be easier to read and configure if you use the number of years \* 12:

```sql
SELECT
ADD_MONTHS('10-JUL-2022', 5 * -12)
FROM dual;
```

Result:

```
10/JUL/17
```

That way, you can just change the number 5 if you ever need to change this, rather than work out how many months are in a year.

### Find the Number of Months Between Two Dates

To find the number of months between two dates in Oracle, use the MONTHS_BETWEEN function.

This is helpful to find the number of months an employee has worked at a company, or the number of months since a sale was made, for example.

```sql
SELECT
employee_id,
hire_date,
ROUND(MONTHS_BETWEEN(SYSDATE, HIRE_DATE), 1) AS months_worked
FROM employee;
```

| **EMPLOYEE_ID** | **HIRE_DATE** | **MONTHS_WORKED** |
| --------------- | ------------- | ----------------- |
| 1               | 27/AUG/11     | 72.5              |
| 2               | 2/JAN/12      | 68.3              |
| 3               | 4/DEC/16      | 9.2               |
| 4               | 12/OCT/11     | 70.9              |
| 5               | 15/NOV11      | 69.9              |
| 6               | 2/JUL/10      | 86.3              |
| 7               | 3/OCT/10      | 83.2              |
| 8               | 20/MAY10      | 87.7              |
| 9               | 15/MAR/15     | 29.9              |
| 10              | 3/JUL14       | 38.2              |

This shows the ID, the hire date, and the number of months the employee has worked at the company.

Note that I used the ROUND function, to clean up the output, as the MONTHS_BETWEEN returns a decimal number that could be quite long.

### Get the First Day of the Month

To find the first day of the month in Oracle SQL, you can use the TRUNC function.

```sql
SELECT
TRUNC(SYSDATE, 'MONTH')
FROM dual;
```

Result:

```
01/SEP/22
```

### Get the Last Day of the Month

To find the last day of the month, use a combination of the TRUNC and LAST_DAY functions.

```sql
SELECT
TRUNC(LAST_DAY(SYSDATE))
FROM dual;
```

Result:

```
30/SEP/22
```

### Get the First Day of the Year

To get the first day of the year, which is always Jan 1st, use the TRUNC function to truncate it to a year.

```sql
SELECT
TRUNC(SYSDATE, 'YEAR')
FROM dual;
```

Result:

```
01/JAN/22
```

### Get the Last Day Of The Year

The last day of the year is always 31 Dec. To find the last day of the year in SQL, use this query:

```sql
SELECT
ADD_MONTHS(TRUNC(SYSDATE, 'YEAR'), 12) - 1
FROM dual;
```

Result:

```
31/DEC/22
```

This query first truncates the current date to the first day of the year (1 Jan), then adds 12 months to it (to make it 1 Jan of the next year). Then, it subtracts 1 day from that, to find the last day of the current year.

### Get the Number of Days in a Month

To find the number of days in a particular month, whether it's the current month or a month from another date, use this query.

It uses the LAST_DAY, TO_CHAR, and CAST functions.

```sql
SELECT
CAST(TO_CHAR(LAST_DAY(SYSDATE), 'dd') AS INT)
FROM dual;
```

Result:

```
30
```

This finds the last day of the month using LAST_DAY, and then converts it to an INT value. You can use any date here instead of SYSDATE.

## Conclusion

So, this article has highlighted all of the DATE functions in Oracle. I've explained what they do, provided a small example, and covered a few common and useful ways to use these date functions.

If you have any questions about these functions, please let me know!
