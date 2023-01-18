---
title: DB Dialect
tags: db
date: 2019-10-11
---

> [数据库方言（dialect）是什么？ - FooFish-Python 之禅](https://foofish.net/what-is-db-dialect.html)

抛开数据库，生活中的方言是什么？方言就是某个地方的特色语言，是一种区别于其它地方的语言，只有你们这一小块地方能听懂，出了这个地方又是另一种方言。

数据库方言也是如此，MySQL 是一种方言，Oracle 也是一种方言，MSSQL 也是一种方言，他们之间在遵循 SQL 规范的前提下，都有各自的扩展特性。

拿分页来说，MySQL 的分页是用关键字 `limit`， 而 Oracle 用的是 `rownum`，MSSQL 又是另一种分页方式。

```sql
# MySQL
select * from t_user limit 10;
# Oracle
select * from t_user where rownum <10;
# MSSQL
select top 10 * from t_user;
```

这对于 ORM 框架来说，为了在上层的 ORM 层做了无差别调用，比如分页，对使用者来说，不管你底层用的是 MySQL 还是 Oracle，他们用的都是一样的接口，但是底层需要根据你使用的数据库方言不同而调用不同的 DBAPI。用户只需要在初始化的时候指定用哪种方言就好，其它的事情 ORM 框架帮你完成了

![layers.png](db-dialect/layers.png)
