---
title: python pymysql
tags: python
date: 2019-07-15
description: python 使用 pymysql 操作 mysql 数据库
---

### basic

```python
import pymysql
import sys

# 打开数据库连接
db = pymysql.connect("localhost","root","root","testdb" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)

# 关闭数据库连接
db.close()
```

### 执行sql

```python
db = pymysql.connect("localhost","root","root","testdb" )
cursor = db.cursor()
row = cursor.execute('select * from employee')
print(row)
row = cursor.execute('insert into employee(first_name) values(%s)','babb')
print(row)
db.commit()
cursor.close()
db.close()
```

### 获取数据

```python
# 获取查询数据
cursor.execute('select * from employee')
row1 = cursor.fetchone()
print(row1)
row2 = cursor.fetchmany(2)
print(row2)
row3 = cursor.fetchall()
print(row3)

# 获取新创建数据自增 ID
row = cursor.execute('insert into employee (first_name) values (%s)','owen')
db.commit()
new_id = cursor.lastrowid
print(new_id)

# 获取到的数据为 Dict
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('select * from employee where first_name = %s','Zara')
row = cursor.fetchone()
print(row)
```

### 调用存储过程

```python
# 调用无参存储过程
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
cursor.callproc('test_no_proc')

row = cursor.fetchmany(2)
print(row)

# 调用有参存储过程
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
cursor.callproc('test_proc',args=['Zara'])
# cursor.callproc('test_proc',args=('Zara'))  # 这种情况下参数其实是 Z,a,r,a
# cursor.execute("call test_proc('Zara')")
row = cursor.fetchall()
print(row)
```
