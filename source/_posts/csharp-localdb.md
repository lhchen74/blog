---
title: SqlServer LOCALDB 安装和连接
tags: csharp
date: 2019-10-25
---

关于 LOCALDB 的详细[文档说明](https://technet.microsoft.com/zh-cn/hh510202),包含安装,连接,共享连接等操作 **https://technet.microsoft.com/zh-cn/hh510202**

> 目的

调试程序没有安装 sql server 时, 可以使用 localdb.这是一个简易的 sql server 数据库,用于本地测试是很方便,省去安装 SQL SERVER 的工作

> 安装 localdb

安装 VS2015 之后,就有了 localdb2016 VS2013 大概是 2014 ,

另外 localdb2014 有单独的安装包,而 2016 则没找到.VS2015 的安装包里有 LOCALDB2016 的 MSI 文件,但是安装之后却无法使用. 使用命令查看版本,如下:

![](csharp-localdb/540771-20170314154618620-1044166666.jpg)

> sqllocaldb 使用

打开 CMD,使用 sqllocaldb.exe 这个命令

sqllocaldb.exe i // 查看已经有的 localdb 的实例

sqllocaldb.exe v // 电脑上安装的 localdb 的所有版本

sqllocaldb.exe s [实例名] // 启动这个实例

sqllocaldb.exe -? // 这个命令的帮助信息

![](csharp-localdb/540771-20161010173121446-1241040689.jpg)

> 使用 MSSM 连接 sqllocaldb

打开 MSSM,服务器名称那里输入`(localdb)\MSSQLLocalDB` ,括号里面是 localdb 这个可能是固定的, **反斜杠后面就是实例的名字**.

然后就连接上了,可以建库建数据了

![](csharp-localdb/540771-20161010180111305-661520541.jpg)

> ASP.NET 程序中使用

-   指定连接到这个数据库文件 MDF

    `Server=(LocalDB)\MSSQLLocalDB; Integrated Security=true;AttachDbFileName=D:\Data\MyDB1.mdf`

-   不指定到 MDF 文件路径,指定默认数据库名

    `Server=(LocalDB)\MSSQLLocalDB; Integrated Security=true;Initial Catalog=MyDB1"`

*   指定用户名和密码(目前使用这是这种,简单明了

    `Server=(localdb)\MSSQLLocalDB;uid=sa;pwd=123456;Initial Catalog=MyDB1`

**使用这几种连接串在 VS 中使用 IISEXPRESS 调试时,没有问题,但是发布到 IIS 中,却连接不上数据库.因为访问权限的问题.细节请看文章第一行链接.**

解决办法是:

1. 将应用程序池的权限改为 localsystem 这个投机的办法,比较省事.但是问题还是很多.

2. 打开**LocalDB** 实例共享:(这个总结起来就是,给 LOCALDB 开共享实例,给 LOCALDB 设定连接帐号)

**给 LOCALDB 开共享实例**

MSSQLLocalDB:实例名 mylocaldb, 为实例名取的共享实例别名,其它帐户连接时通过这个别名 (命令窗口要使用管理员权限那种)

`sqllocaldb h "MSSQLLocalDB" "mylocaldb"`

使用 MSSM 连接工具连接时,也要使用管理员权限打开.实例名变成`(localdb)\.\mylocaldb` 第一个`\`后面的`.\mylocaldb`就是共享实例别名

为什么上面的 MSSM 要使用管理员工具打开,因为下面的验证方式是帐号密码形式的,如果使用 WINDOWS 验证,则不需要.

![](D:\study\jbn\source_posts\csharp-localdb/540771-20170124111204691-1671264676.jpg)

**给 LOCALDB 设定连接帐号**

到这步之后,将 WEB 程序的连接字符串写成指定帐号和密码的这种,结果依然不能访问,还是没有权限,

server=(localdb)\.\mylocaldb;uid=sa;pwd=123456;AttachDbFileName=D:\Data\MyDB1.mdf

**查看数据库帐号,发现 LOCALDB 并没有 SA 这个帐号**,于是加上它,并且给予 DB_OWNER

![](csharp-localdb/540771-20170124112301300-1557512723.jpg)

最后,在浏览器中打开程序,发现连接成功,网页打开了..

> [LOCALDB 安装和连接 - mirrortom - 博客园](https://www.cnblogs.com/mirrortom/p/5946817.html)
