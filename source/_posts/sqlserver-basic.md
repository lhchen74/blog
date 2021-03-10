---
title: SqlServer 基本语法
tags: db
date: 2019-11-2
---

> 转载：[sql(SqlServer)编程基本语法- lipan -博客园](https://www.cnblogs.com/lipan/archive/2010/12/09/1892516.html)

### 一、定义变量

```mssql
--简单赋值
declare @a int
set @a=5
print @a

--使用select语句赋值
declare @user1 nvarchar(50)
select @user1='张三'
print @user1
declare @user2 nvarchar(50)
select @user2 = Name from ST_User where ID=1
print @user2

--使用update语句赋值
declare @user3 nvarchar(50)
update ST_User set @user3 = Name where ID=1
print @user3
```

### 二、表、临时表、表变量

```mssql
--创建临时表1
create table #DU_User1
(
     [ID] [int]  NOT NULL,
     [Oid] [int] NOT NULL,
     [Login] [nvarchar](50) NOT NULL,
     [Rtx] [nvarchar](4) NOT NULL,
     [Name] [nvarchar](5) NOT NULL,
     [Password] [nvarchar](max) NULL,
     [State] [nvarchar](8) NOT NULL
);
--向临时表1插入一条记录
insert into #DU_User1 (ID,Oid,[Login],Rtx,Name,[Password],State) values (100,2,'LS','0000','临时','321','特殊');

--从ST_User查询数据，填充至新生成的临时表
select * into #DU_User2 from ST_User where ID<8

--查询并联合两临时表
select * from #DU_User2 where ID<3 union select * from #DU_User1

--删除两临时表
drop table #DU_User1
drop table #DU_User2
```

```mssql
--创建临时表
CREATE TABLE #t
(
    [ID] [int] NOT NULL,
    [Oid] [int] NOT NULL,
    [Login] [nvarchar](50) NOT NULL,
    [Rtx] [nvarchar](4) NOT NULL,
    [Name] [nvarchar](5) NOT NULL,
    [Password] [nvarchar](max) NULL,
    [State] [nvarchar](8) NOT NULL,
)

--将查询结果集（多条数据）插入临时表
insert into #t select * from ST_User
--不能这样插入
--select * into #t from dbo.ST_User

--添加一列，为int型自增长子段
alter table #t add [myid] int NOT NULL IDENTITY(1,1)
--添加一列，默认填充全球唯一标识
alter table #t add [myid1] uniqueidentifier NOT NULL default(newid())

select * from #t
drop table #t
```

```mssql
--给查询结果集增加自增长列

--无主键时：
select IDENTITY(int,1,1)as ID, Name,[Login],[Password] into #t from ST_User
select * from #t

--有主键时：
select (select SUM(1) from ST_User where ID<= a.ID) as myID,* from ST_User a order by myID
```

```mssql
--定义表变量
declare @t table
(
    id int not null,
    msg nvarchar(50) null
)
insert into @t values(1,'1')
insert into @t values(2,'2')
select * from @t
```

### 三、循环

```mssql
--while循环计算1到100的和
declare @a int
declare @sum int
set @a=1
set @sum=0
while @a<=100
begin
    set @sum+=@a
    set @a+=1
end
print @sum
```

### 四、条件语句

```mssql
--if,else条件分支
if(1+1=2)
begin
    print '对'
end
else
begin
    print '错'
end

--when then条件分支
declare @today int
declare @week nvarchar(3)
set @today=3
set @week=case
    when @today=1 then '星期一'
    when @today=2 then '星期二'
    when @today=3 then '星期三'
    when @today=4 then '星期四'
    when @today=5 then '星期五'
    when @today=6 then '星期六'
    when @today=7 then '星期日'
    else '值错误'
end
print @week
```

### 五、游标

```mysql
declare @ID int
declare @Oid int
declare @Login varchar(50)

--定义一个游标
declare user_cur cursor for select ID,Oid,[Login] from ST_User
--打开游标
open user_cur
while @@fetch_status=0
begin
--读取游标
    fetch next from user_cur into @ID,@Oid,@Login
    print @ID
    --print @Login
end
close user_cur
--摧毁游标
deallocate user_cur
```

### 六、触发器

触发器中的临时表：

Inserted
　　存放进行 insert 和 update 操作后的数据
　　 Deleted
　　存放进行 delete 和 update 操作前的数据

```mssql
--创建触发器
Create trigger User_OnUpdate
    On ST_User
    for Update
As
    declare @msg nvarchar(50)
    --@msg记录修改情况
    select @msg = N'姓名从“' + Deleted.Name + N'”修改为“' + Inserted.Name + '”' from Inserted,Deleted
    --插入日志表
    insert into [LOG](MSG)values(@msg)

--删除触发器
drop trigger User_OnUpdate
```

### 七、存储过程

```mssql
--创建带output参数的存储过程
CREATE PROCEDURE PR_Sum
    @a int,
    @b int,
    @sum int output
AS
BEGIN
    set @sum=@a+@b
END

--创建Return返回值存储过程
CREATE PROCEDURE PR_Sum2
    @a int,
    @b int
AS
BEGIN
    Return @a+@b
END

--执行存储过程获取output型返回值
declare @mysum int
execute PR_Sum 1,2,@mysum output
print @mysum

--执行存储过程获取Return型返回值
declare @mysum2 int
execute @mysum2= PR_Sum2 1,2
print @mysum2
```

### 八、自定义函数

函数的分类：

1）标量值函数

2）表值函数

a:内联表值函数

b:多语句表值函数

3）系统函数

```mssql
--新建标量值函数
create function FUNC_Sum1
(
    @a int,
    @b int
)
returns int
as
begin
    return @a+@b
end

--新建内联表值函数
create function FUNC_UserTab_1
(
    @myId int
)
returns table
as
return (select * from ST_User where ID<@myId)

--新建多语句表值函数
create function FUNC_UserTab_2
(
    @myId int
)
returns @t table
(
    [ID] [int] NOT NULL,
    [Oid] [int] NOT NULL,
    [Login] [nvarchar](50) NOT NULL,
    [Rtx] [nvarchar](4) NOT NULL,
    [Name] [nvarchar](5) NOT NULL,
    [Password] [nvarchar](max) NULL,
    [State] [nvarchar](8) NOT NULL
)
as
begin
    insert into @t select * from ST_User where ID<@myId
    return
end

--调用表值函数
select * from dbo.FUNC_UserTab_1(15)
--调用标量值函数
declare @s int
set @s=dbo.FUNC_Sum1(100,50)
print @s

--删除标量值函数
drop function FUNC_Sum1
```

### 自定义函数与存储过程的区别

一、自定义函数：

1. 可以返回表变量

2. 限制颇多，包括

   不能使用 output 参数；

   不能用临时表；

   函数内部的操作不能影响到外部环境；

   不能通过 select 返回结果集；

   不能 update，delete，数据库表；

3. 必须 return 一个标量值或表变量

自定义函数一般用在复用度高，功能简单单一，争对性强的地方。

二、存储过程

1. 不能返回表变量

2. 限制少，可以执行对数据库表的操作，可以返回数据集

3. 可以 return 一个标量值，也可以省略 return

存储过程一般用在实现复杂的功能，数据操纵方面。
