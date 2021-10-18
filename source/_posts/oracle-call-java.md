---
title: Oracle Call Java
date: 2018-08-08
tags: db
---

### 1. 创建 java source

```java
create or replace and compile java source named babb as
public class Babb
{
  public static String getStrMsg(String str){
    return str+"\t 共有字符:"+str.length()+"个";
  }
}
```

也可以使用 loadjava 工具加载 class 文件

Babb.java

```java
public class Babb
{
  public static String getStrMsg(String str){
    return str+"\t 共有字符:"+str.length()+"个";
  }
}
```

`javac Babb.java` 编译生成 `Babb.class` (注意编译的 java 版本要和数据库版本对应)

`loadjava.bat -user xxx/xxx@DEV -force -oci8 D:/study/java/oracle_call_java/Babb.class`

### 2. 创建调用函数

```sql
create or replace function javaTest(str varchar2)
return varchar2 as
LANGUAGE JAVA NAME 'Babb.getStrMsg(java.lang.String) return java.lang.String';
```

### 3. 执行测试

```sql
select javatest('abcd') from dual;

-- abcd 共有字符:4个
```
