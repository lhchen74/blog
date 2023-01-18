---
title: Oracle Call Java
date: 2018-08-08
tags: db
---

## Create Java Source

可以在 PL/SQL 中直接编译 Java 源代码

```java
create or replace and compile java source named babb as
public class Babb
{
  public static String getStrMsg(String str){
    return str+"\t 共有字符:"+str.length()+"个";
  }
}
```

也可以使用 `loadjava`工具加载 Class 文件

```java
// Babb.java
public class Babb
{
  public static String getStrMsg(String str){
    return str+"\t 共有字符:"+str.length()+"个";
  }
}
```

`javac Babb.java` 编译生成 `Babb.class` (注意编译的 java 版本要和数据库版本对应)

`loadjava.bat -user xxx/xxx@DEV -force -oci8 D:/study/java/oracle_call_java/Babb.class`

## Create Call Function

```sql
create or replace function javaTest(str varchar2)
return varchar2 as
LANGUAGE JAVA NAME 'Babb.getStrMsg(java.lang.String) return java.lang.String';
```

## Test

```sql
select javatest('abcd') from dual;

-- abcd 共有字符:4个
```

## Drop Java Source

```sql
drop java source babb;
```

## Comments

### Clean CSV Line

Java Code

```java
package com.jbn;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EDIJavaUtils {

    public static String cleanCSVLine(String content, String separator) {
        String contentWithSeparator = separator + content + separator;
        // Java Backreference in pattern need use \\N
        String regexStr = separator + "(\"?)(.*?)\\1(?=" + separator + ")";
        // (?=pattern) zero-width positive lookahead assertion
        // Pattern pattern = Pattern.compile("/(\"?)(.*?)\\1(?=/)");
        Pattern pattern = Pattern.compile(regexStr);
        Matcher matcher = pattern.matcher(contentWithSeparator);
        // Java Backreference in replacement need use $N
        String result = matcher.replaceAll("$2\n");
        return result.substring(0, result.length() - 2);
    }

    public static void main(String[] args) {
        String content = "a/\"b \" c\"/\"d\"";
        String result = cleanCSVLine(content, "/");
        System.out.println(result);
    }
}

// a
// b " c
// d
```

Compile Java Source

```sql
create or replace and compile java source named som_edi_java_utils as
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EDIJavaUtils {
    public static String cleanCSVLine(String content, String separator) {
        String contentWithSeparator = separator + content + separator;
        String regexStr = separator + "(\"?)(.*?)\\1(?=" + separator + ")";
        // Pattern pattern = Pattern.compile("/(\"?)(.*?)\\1(?=/)");
        Pattern pattern = Pattern.compile(regexStr);
        Matcher matcher = pattern.matcher(contentWithSeparator);
        String result = matcher.replaceAll("$2\n");
        return result.substring(0, result.length() - 2);
    }
}
```

Create Call Function in Package

```sql
create or replace package body som_edi_morrison_pkg is
  function clean_csv_line(content varchar2, separator varchar2) return varchar2;
end som_edi_custom_utils_pkg;

create or replace package body som_edi_custom_utils_pkg is
  function clean_csv_line(content varchar2, separator varchar2) return varchar2 
  as
  LANGUAGE JAVA NAME 'EDIJavaUtils.cleanCSVLine(java.lang.String, java.lang.String) return java.lang.String';
end som_edi_custom_utils_pkg;
```

Test

```sql
select som_edi_custom_utils_pkg.clean_csv_line('ab/95"508/"AP"PLE""/"10/FEB/12"', '/') 
  from dual;

-- ab
-- 95"508
-- AP"PLE"
-- 10/FEB/12
```

