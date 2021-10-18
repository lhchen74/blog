---
title: Python Sqlalchemy
tags: python
date: 2019-10-30
---

> 转载: [Python 编程：orm 之 sqlalchemy 模块 - 彭世瑜的博客 - CSDN 博客](https://blog.csdn.net/mouday/article/details/)

### 常用操作

```python
"""
MySQL-Python
mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

pymysql
mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

MySQL-Connector
mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

cx_Oracle
oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]

SQLite
driver://user:pass@host/database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func


# 创建数据库引擎
engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/sqlalchemy-tutorial", encoding="utf-8", echo=False)

# 声明基类
Base = declarative_base()


# 创建 User 模型
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))  # varchar(32)
    password = Column(String(64))

    def __repr__(self):
        return "<%s name: %s >" % (self.id, self.name)


# 创建表结构
Base.metadata.create_all(engine)


# 创建会话类
SessionClass = sessionmaker(bind=engine)
# 实例化
session = SessionClass()


# 生成数据对象
user = User(name="Tom", password="")
print(user.name, user.id)  # id=None

# 添加数据
session.add(user)
print(user.name, user.id)  # id=None

# 提交事务
session.commit()
print(user.name, user.id)  # id=1


# 查询
data = session.query(User).filter(User.id == 1).first()  # 或者 all()
print(data)

# 多条件查询
data = session.query(User).filter(User.id >= 1).filter(
    User.name == "Tom").first()  # 或者 all()
print(data)

# 修改
data.name = "Alex"
data.password = "xxx"
session.commit()

# 回滚
user = User(name="xiaobai", password="xxx")
session.add(user)
data = session.query(User).filter(User.name == "xiaobai").all()
print(data)
session.rollback()
data = session.query(User).filter(User.name == "xiaobai").all()
print(data)

# 统计
count = session.query(User).filter(User.name.like("a%")).count()
print(count)

# 分组
data = session.query(User.name, func.count(
    User.name)).group_by(User.name).all()
print(data)
```

### 外键关联

```python
from datetime import date
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func


engine = create_engine("mysql+pymysql://root:root@localhost:3306/sqlalchemy-tutorial",
                       encoding="utf-8", echo=False)

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name: %s >" % (self.id, self.name)


class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("student.id"))

    # student = relationship("student") 可以通过 StudyRecord 找到 Student, study_record.student
    # backref = "study_record", 可以通过 Student 找到 StudyRecord, student.study_record
    student = relationship("Student", backref="study_record")

    def __repr__(self):
        return "<%id day: %s, status: %s >" % (self.id, self.day, self.status)


Base.metadata.create_all(engine)


SessionClass = sessionmaker(bind=engine)
session = SessionClass()

student = Student(name="babb", register_date=date.today())
study_record = StudyRecord(day=10, status="Good", student=student)

session.add(student)
session.add(study_record)

session.commit()

study_record = session.query(Student).filter(
    Student.name == "babb").first().study_record
print(study_record)

student = session.query(StudyRecord).first().student
print(student)
```

### 一对多关系

```python
class User(Base):
	__tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多, user.books
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方 book 表是通过外键关联到user表的, 外键引用 user 表的 id 主键:
    user_id = Column(String(20), ForeignKey('user.id'))

```

### 创建多外键表结构

orm_mfk_api.py, 为使用者提供统一的数据结构接口

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    bill_address_id = Column(Integer, ForeignKey("address.id"))
    ship_address_id = Column(Integer, ForeignKey("address.id"))

    # 一对多:
    bill_address = relationship("Address", foreign_keys=[bill_address_id])
    ship_address = relationship("Address", foreign_keys=[ship_address_id])

    def __repr__(self):
        return "id: %s, name: %s, bill: %s, ship: %s" % (self.id, self.name, self.bill_address_id, self.ship_address_id)

class Address(Base):
	__tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String(20), nullable=False)

# 设置引擎，创建表
engine = create_engine("mysql+pymysql://root:@.../test", encoding="utf-8", echo=False)
Base.metadata.create_all(engine)
```

调用多外键关联的 api，对数据进行增删改查

```python
from orm_mfk_api import engine, User, Address
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()

# 插入地址
addr = Address(city="beijing")
addr = Address(city="wuhang")
addr = Address(city="lanzhou")
addr = Address(city="dali")

session.add_all([addr, addr, addr, addr])

# 插入用户
user = User(name="Tom", bill_address=addr, ship_address=addr)
user = User(name="Jack", bill_address=addr, ship_address=addr)
user = User(name="Jimi", bill_address=addr, ship_address=addr)

session.add_all([user, user, user])

session.commit()

# 查询
result =session.query(User).filter(User.name=="Jimi").first()
print(result)
```

### 多对多关系

orm_mm_api.py, 图书与作者多对多关系的统一接口

```python
from sqlalchemy import Integer, String, Column, Table, DATE, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:root@localhost:3306/sqlalchemy-tutorial",
                       encoding="utf-8", echo=False)
Base = declarative_base()

# 创建关系表，第三张表连接 book 和 author
bookauthor = Table("bookauthor", Base.metadata,
                  Column("book_id", Integer, ForeignKey("books.id")),
                  Column("author_id", Integer, ForeignKey("authors.id")))

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(20))

    def __repr__(self):
        return self.name

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    pub_date = Column(DATE)

    authors = relationship("Author", secondary=bookauthor, backref="books")

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)
```

调用多对多接口，管理作者与图书的数据

```python
# 调用多对多接口，管理作者与图书的数据

import orm_m2m_api
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(orm_m2m_api.engine)
session = Session()

# 作者
a1 = orm_m2m_api.Author(name="Tom")
a2 = orm_m2m_api.Author(name="Jack")
a3 = orm_m2m_api.Author(name="Jimi")
a4 = orm_m2m_api.Author(name="Ben")

# 图书
b1 = orm_m2m_api.Book(name="lear python", pub_date="2018-12-13")
b2 = orm_m2m_api.Book(name="lear java", pub_date="2018-12-14")
b3 = orm_m2m_api.Book(name="lear cpp", pub_date="2018-12-15")
b4 = orm_m2m_api.Book(name="中文书籍", pub_date="2018-12-15")

# 设置图书与作者的关系
b1.authors = [a1, a2]
b2.authors = [a1, a3]
b3.authors = [a4]

# 提交数据
session.add_all([a1, a2, a3, a4, b1, b2, b3])
session.commit()

# 书查询作者
result = session.query(orm_m2m_api.Book).filter(
    orm_m2m_api.Book.id == 2).first()
print(result, result.authors)  # lear java [Tom, Jimi]


# 作者查询书
result = session.query(orm_m2m_api.Author).filter(
    orm_m2m_api.Author.id == 1).first()
print(result, result.books)  # Tom [lear python, lear java]

# 删除书的作者
a5 = session.query(orm_m2m_api.Author).filter(
    orm_m2m_api.Author.id == 1).first()
b5 = session.query(orm_m2m_api.Book).filter(orm_m2m_api.Book.id == 1).first()
b5.authors.remove(a5)
session.commit()

# 删除作者
a6 = session.query(orm_m2m_api.Author).filter(
    orm_m2m_api.Author.id == 4).first()
session.delete(a6)
session.commit()
```

————————————————
版权声明：本文为 CSDN 博主「彭世瑜」的原创文章，遵循 CC . BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/mouday/article/details/
