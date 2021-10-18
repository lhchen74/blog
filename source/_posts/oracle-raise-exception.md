---
title: oracle raise exception
tags: db
date: 2020-01-20
---

> 转载: [PL/SQL RAISE Exceptions By Practical Examples](https://www.oracletutorial.com/plsql-tutorial/plsql-raise/)

**Summary**: in this tutorial, you will learn how to use the PL/SQL `RAISE` statement to raise a user-defined exception, internally defined exception, and reraising an exception.

To raise an [exception](https://www.oracletutorial.com/plsql-tutorial/plsql-exception/) explicitly, you use the `RAISE` statement. The `RAISE` statement allows you to:

-   Raise a user-defined exception.
-   Raise an internally defined exception.
-   Reraising the current exception.

## Raising a user-defined exception

A user-defined exception is defined by users like you or other developers in the declaration section of a block or subprogram.

### Declaring a user-defined exception

To define a user-defined exception, you use the following syntax:

```plsql
DECLARE
	exception_name EXCEPTION;
```

Similar to the [variable declaration](https://www.oracletutorial.com/plsql-tutorial/plsql-variables/), you declare an exception in the declaration section of a block.

A user-defined exception must have assigned `error_code` . To do it, you use the `EXCEPTION_INIT` pragma as follows:

```plsql
PRAGMA EXCEPTION_INIT(exception_name, error_code)
```

In this syntax, the `error_code` is an integer that ranges from `-20,999` to `-20,000`. And the `message` is a character string with a maximum length of `2,048` bytes.

The entire syntax for declaring a user-defined exception is as follows:

```plsql
DECLARE
	exception_name EXCEPTION;
 	PRAGMA EXCEPTION_INIT(exception_name, error_number);
```

### Raising a user-defined exception example

The following example illustrates how to declare a user-defined exception and associate it with an error code.

```plsql
DECLARE
    e_credit_too_high EXCEPTION;
    PRAGMA exception_init(e_credit_too_high, -20001);
    l_max_credit customers.credit_limit %TYPE;
    l_customer_id customers.customer_id %TYPE : = &customer_id;
    l_credit customers.credit_limit %TYPE : = &credit_limit;
BEGIN -- get the max credit limit
    SELECT MAX(credit_limit)
    INTO l_max_credit
    FROM customers;
    -- check if input credit is greater than the max credit
    IF l_credit > l_max_credit THEN
    	RAISE e_credit_too_high;
    END IF;
    -- if not, update credit limit
    UPDATE customers
    SET credit_limit = l_credit
    WHERE customer_id = l_customer_id;
    COMMIT;
END;
/
```

In this example,

-   First, declare a user-defined exception e_credit_too_high and associates it with the error number `-20001`.
-   Second, select maximum credit from the `customers` table using the `MAX()` function and assign this value to the `l_max_credit` variable.
-   Third, check if the input credit with the maximum credit, if the input credit is greater than the max, then raise the `e_credit_too_high` exception.
-   Finally, update the customer whose id is entered by the user with the new credit limit.

Here is the output if you enter customer id 100 and credit limit `20000`:

```plsql
ORA-20001:
```

If you want to include a custom message, you can replace the line:

```plsql
RAISE e_credit_too_high;
```

by the following line:

```plsql
raise_application_error(-20001,'Credit is too high');
```

And execute the code block again, you will receive the following error:

```plsql
ORA-20001:Creditistoohigh
```

## Raising an internally defined exception

Typically, the runtime system raises internally defined exceptions implicitly when they occur. Besides, you can explicitly raise an internally defined exception with the `RAISE` statement if the exception has a name:

```plsql
RAISE exception_name;
```

This example shows how to raise an internally defined exception `INVALID_NUMBER`:

```plsql
DECLARE
    l_customer_id customers.customer_id%TYPE := &customer_id;
BEGIN
    -- get the meax credit limit
    IF l_customer_id < 0 THEN
        RAISE invalid_number;
    END IF;
END;
/
```

If you execute the block and enter the customer id -10, you will get the following error:

```plsql
ORA-01722:invalidnumber
```

## Reraising the current exception

You can re-raise the current exception with the `RAISE` statement. Reraising an exception passes it to the enclosing block, which later can be handled further. To reraise an exception, you don’t need to specify the exception name.

```plsql
DECLARE
    e_credit_too_high EXCEPTION;
    PRAGMA exception_init( e_credit_too_high, -20001 );
    l_max_credit customers.credit_limit%TYPE;
    l_customer_id customers.customer_id%TYPE := &customer_id;
    l_credit customers.credit_limit%TYPE     := &credit_limit;
BEGIN
    BEGIN
        -- get the max credit limit
        SELECT MAX(credit_limit)
        INTO l_max_credit
        FROM customers;

        -- check if input credit is greater than the max credit
        IF l_credit > l_max_credit THEN
            RAISE e_credit_too_high;
        END IF;
        EXCEPTION
            WHEN e_credit_too_high THEN
                dbms_output.put_line('The credit is too high' || l_credit);
                RAISE; -- reraise the exception
    END;
EXCEPTION
    WHEN e_credit_too_high THEN
        -- get average credit limit
        SELECT avg(credit_limit)
        into l_credit
        from customers;

        -- adjust the credit limit to the average
        dbms_output.put_line('Adjusted credit to ' || l_credit);

        --  update credit limit
        UPDATE customers
        SET credit_limit = l_credit
        WHERE customer_id = l_customer_id;

        COMMIT;
END;
/
```

In this example:

-   First, get the max credit limit from the `customers` table.
-   Second, compare the max credit with the user-input credit. If the user-input credit is greater than the max credit, then raise the `e_credit_too_high` exception.
-   Third, display a message and reraise the exception in the exception-handling section in the inner block.
-   Finally, in the outer block, reassign the average credit to the `l_credit` variable and update the customer with the newly adjusted credit.

If you enter the customer id 100 and credit limit 10000, the credit limit of the customer will be updated to the average credit.

```plsql
SELECT * FROM customers WHERE customer_id=100;
```

In this tutorial, you have learned how to use the PL/SQL `RAISE` statement to explicitly raise a user-defined exception, internally defined exception, and reraising an exception.
