---
title: Singular vs Plural and Other Database Table Naming Conventions
tags: db
date: 2022-12-15
---

> 转载：[Singular vs Plural and Other Database Table Naming Conventions - Database Star](https://www.databasestar.com/database-table-naming-conventions/)

Are you wondering if you should name your SQL database tables in the singular form or plural form?

Learn what the preferred convention is and some reasoning behind it, as well as other database table naming conventions, in this article.

## Why Do We Need SQL Table Naming Conventions?

You might be wondering why we need conventions or best practices for naming SQL tables in the first place.

Can't we just name it what we want, and move on?

We could do that… but it's better to have naming conventions for several reasons:

- **Consistency for developers**. If the developers are working with their own coding standards, using the same conventions for table names and object names in their code will make life easier for the team. There's a lot of time and effort wasted trying to work out if your table is called Customer or Customers, or if it's your object in your source code that's called Customers and your table called Customer.
- **Databases may outlive applications**. A well-designed database can stand for a long time – longer than many applications. I've worked on databases where the application has been redesigned or replaced, but the database has stayed the same. It's important to get it right at the start and follow conventions.
- **Saving time**. If you set up table naming conventions at the start, you can save time later on when you need to create new tables or enhance the database in other ways.

Setting up a naming convention for your database tables will take a bit of time at the start, but it will save time for the developers.

(Related – [How to Become a Database Developer: The Definitive Guide](https://www.databasestar.com/database-developer-guide/))

So, let's move on to what I think are good SQL database table naming conventions.

## Singular vs Plural Table Names: Should Database Table Names Be Singular or Plural?

I've done some research on this topic from a variety of sources. I've also used my own experience in deciding whether singular or plural table names are better.

If you have existing standards within your team or project, use those. It's better to be consistent than to use one convention in particular.

If you don't have standards, then you'll need to decide on singular vs plural table names.

**In my opinion, singular table names are better than plural.**

I have several reasons for this, which I'll mention shortly.

But first, let me show you several different sources who have different opinions on this topic.

The number of articles for each opinion shouldn't matter. I've just added them to demonstrate that there are different views on the topic and which pages/websites have each of these views.

### Who Says Singular Table Names are Better?

There are several sources that I found that believe singular table names are better.

- The top voted answer relating to singular vs plural on [this popular Stack Overflow question](https://stackoverflow.com/questions/338156/table-naming-dilemma-singular-vs-plural-names).
- Vertabelo's [blog post](http://www.vertabelo.com/blog/technical-articles/naming-conventions-in-database-modeling).
- Launch By Lunch's [blog post](https://launchbylunch.com/posts/2014/Feb/16/sql-naming-conventions/).
- Team Ten's [blog post](https://www.teamten.com/lawrence/programming/use-singular-nouns-for-database-table-names.html).
- Microsoft SQL Server's [built-in AdventureWorks database](https://sqlserversamples.codeplex.com/)

### Who Says Plural Table Names are Better?

There are several sources that state they prefer plural table names:

- Les Hazlewood's [blog post](http://leshazlewood.com/software-engineering/sql-style-guide/).
- SQLStyle [website](http://www.sqlstyle.guide/).
- Tim Hall from [Oracle-Base](https://oracle-base.com/articles/misc/naming-conventions).
- [This post](http://www.gplivna.eu/papers/naming_conventions.htm) from gplivna.eu.
- Don Burleson from [dba-oracle.com](http://www.dba-oracle.com/standards_schema_object_names.htm).

## Why I Prefer Singular Database Table Names

There are **several reasons** why I prefer singular table names over plural table names. I've written more about them here in my [SQL Best Practices and Style Guide post](https://www.databasestar.com/sql-best-practices/).

### Consistency Throughout Your System

The biggest reason why I prefer singular table names instead of plural table names when it comes to database table naming conventions is that it ensures consistency between all areas of your application.

Developers work with SQL code, database tables, and their own application code. In object-oriented programming, classes are singular nouns (e.g. Bike, Car, Student).

This means that if we use singular table names (such as car or student), we can ensure that the same convention is easily followed for all types:

- Database tables (including [views](https://www.databasestar.com/sql-views/) and [synonyms](https://www.databasestar.com/oracle-synonym/))
- SQL statements that query these tables
- Functions and APIs that use this SQL or tables
- Objects in source code in all languages and technologies being used in the application

This way, a developer knows that their student class uses a getStudent() function and returns a Student object using a SELECT query on the student table.

Well, maybe that's not the exact method they would use, but the point is that the class and database table and everything else are all singular.

This is a big time saver and prevents developers from trying to work out which form they used when naming tables.

### The Concept of a Table is a Container of Single Rows

The second reason relates to what a table is. A table stores rows. It can store zero, one, or many rows. **The name should not imply the number of items in the table.**

A table is, therefore, a container. **And a container is a single object**. Whether it contains multiple rows or a single row does not impact its name, and therefore the name should be singular.

A good example is the AppleBag example used in the top-rated singular/plural answer in [this Stack Overflow question](https://stackoverflow.com/questions/338156/table-naming-dilemma-singular-vs-plural-names).

A bag containing apples can be called an AppleBag, regardless of how many apples it contains. Tables are the same thing.

### Singular Names are Easier to Create

It's easy to come up with singular names for SQL table names. Well, it might not be that easy, but it's easier than plural names.

You might have a "person" table. This is a singular name. What would you call the plural version of the table? People? Persons?

The pluralisation of words is an English language concept to help with speaking. SQL and databases don't need to know about plurals of words.

### There Are Many Non-English Developers

The number of non-English-speaking developers is rising. These non-English native speaking developers may not understand the concept of pluralisation of words. It's easier for these developers to understand singular versions of words.

Whether your team contains all English-speaking developers, or has some non-English native developers, it's better to plan for the future and make your code as easy to understand as possible for all developers.

### The Concept of Master and Detail is Easier to Understand

If you've seen examples of databases where a master and detail record is used, or even when you've created some yourself, you might have found it easier to understand to use singular names.

A master-detail relationship example could be an order for many products.

The main order can contain many order line items.

To represent this in tables, they could be named using singular form:

- Order
- OrderDetail

Or, the table names using the plural form:

- Orders
- OrderDetails

The plural version is a little inconsistent as it uses a different term.

For master-detail tables, it's easier to use a singular table name.

## Other Database Table Naming Conventions

In addition to using singular or plural words for SQL table names, there are several other conventions that I would recommend when working with database tables.

### Use Underscores To Separate Words Instead Of Camel Case

Several sources recommend using CamelCase to separate words.

This isn't a good idea when working with SQL, for several reasons.

It's harder to read when skimming down an SQL file.

For example:

```sql
SELECT * FROM ApplicationUsers;
```

Or

```sql
SELECT * FROM applicationUsers;
```

It's better to use an underscore to separate words, to improve readability.

```sql
SELECT * FROM application_users;
```

This way it's clearer what the name of the table is.

The second reason, and probably the more important one, is that **SQL is case-insensitive**.

It doesn't care what case your table names are in.

This matters because the objects are stored in the database in the same case, so naming them using camel case will be lost.

Also, when you use SQL formatters (and you should, especially the built-in one in SQL Developer), it may cause you to lose the camel case.

The SQL database doesn't need camel case and doesn't differentiate, so neither should you.

So, using underscores to separate words in SQL table names is easier to distinguish and will be stored as expected in the database.

### Don't Use Quotes

If you want to store a table name in a certain case or in a certain format, you could use quotes to store the name.

For example:

```sql
CREATE TABLE "ApplicationUser" ...
```

This will store the table name as ApplicationUser.

However, this means that every time you want to refer to the table, you'll need to use quotes.

And sometimes you'll forget, and get an error.

Or other developers won't know or won't remember, and they will get an error or get incorrect results.

So, avoiding quotes is a good SQL table naming convention to use.

This also means you should avoid spaces in database table names. The only way to add spaces is to enclose the entire name in quotes (such as "Application User"), which will cause the same issues.

### Use Full Words

It might be tempting to save a few keystrokes and abbreviate your table names.

So, instead of creating a customer table, you decide to call it cust.

Now, it's a little less clear as to what that table means. It's probably customer, but are you sure?

There's no need to abbreviate words just for the sake of it. Use the full words when naming tables. It's one of the easier database table naming conventions to follow.

The exception to this is if you've reached Oracle's 30 character limit for table names. Other database vendors may not have this restriction.

If you have, then you can play around with the name of the table to ensure it is less than or equal to 30 characters. You can do this by:

- Removing vowels from words (e.g. customer_historic_invoice_billed (32 characters) could become customer_historic_invc_blld (27 characters))
- Abbreviating words in the table name using commonly known abbreviations (e.g. customer_historic_invoice_billed (32 characters) could become cust_hist_invoice_billed (24 characters))

### Avoid Reserved Words

There are several words in SQL that are reserved for use by the database. These words should not be used to create tables with.

A common example is User. Creating a table with the name of User will probably cause an error, because user is a reserved word. If you create it without an error (for example, by enclosing it in quotes), then it will still cause confusion.

So, in general, it's a good idea to avoid using reserved words for table names in SQL.

### Don't Add Prefix of Object Type to the Name

In the earlier days of database development, it was a common practice to add a prefix to an object name that signals what kind of object it is.

For example, tbl_customer for a table, or vw_all_customers for a view.

The idea is that developers could see the object name and immediately know it was a view or a table, and develop on it accordingly.

However, **using prefixes on an object name not only wastes valuable characters**, but it also **makes maintenance worse**.

What if you needed to change the table to a view of the same name? If you keep using this standard, you'd have to rename it from tbl* to vw*, causing your code to break unless you changed the code.

If you avoid using prefixes in your SQL table names, it makes maintenance easier. It's a good SQL table naming convention to follow.

### Avoid Concatenating Table Names in Many-to-Many Relationships If Possible

Let's say you had a student table and a subject table as I've used in many of my [SQL function examples](https://www.databasestar.com/oracle-sql-functions/).

A student can have many subjects, and a subject can have many students.

This is a many-to-many relationship. In relational database design, this needs to be reflected using a joining table – a table that captures this relationship.

This table also needs a name.

Common suggestions of table name conventions would be to name the table the concatenation of the [two tables that join to it](https://www.databasestar.com/sql-joins/). In this case, it would be student_subject (or subject_student)

This is not a good idea as it doesn't effectively describe the object you're referring to. Giving it a better name will improve the developer's code and improve understanding of the database.

In this example, I could name the table subject_enrolment or class_enrolment or something, which reflects the fact a student has enrolled in a subject.

## Conclusion – Singular Table Names are Preferred

I hope you've learned something from this post and understand the benefits of using singular table names in your database.

The main point here is that you should be consistent. If your team already uses plural names, then stick with it. If there is no table naming convention, then choose singular.

What are your thoughts? Are you pro-singular or pro-plural? Are there any other naming conventions for tables that I've missed out? Do you have any other questions? Let me know in the comments below.

Lastly, if you enjoy the information and career advice I've been providing, **sign up to my newsletter below** to stay up-to-date on my articles. You'll also receive a fantastic bonus. Thanks!
