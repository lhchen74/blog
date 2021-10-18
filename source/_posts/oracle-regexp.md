---
title: oracle regexp
date: 2018-08-08
tags: db
---

> 你眼中看似落叶纷飞、变化无常的世界,实际只是躺在上帝怀中一份早已谱好的乐章。

### REGEXP_REPLACE 参数说明

-   第一个是输入的字符串
-   第二个是正则表达式
-   第三个是要替换成的字符
-   第四个是标识从第几个字符开始正则表达式匹配。（默认为 1）
-   第五个是标识第几个匹配组。（默认为全部都替换掉）
-   第六个是是取值范围：
    i：大小写不敏感；
    c：大小写敏感；
    n：点号 . 不匹配换行符号；
    m：多行模式；
    x：扩展模式，忽略正则表达式中的空白字符。

### 测试数据

```sql
create table babb_reg_test(
  a varchar2(30)
);
insert into babb_reg_test values('ABC123XYZ');
insert into babb_reg_test values('ABC123XYZ456');
insert into babb_reg_test values('Edward');
select * from babb_reg_test;

A
-----------------------------------
ABC123XYZ
ABC123XYZ456
Edward
```

### 替换数字

```sql
SELECT REGEXP_REPLACE (a,'[0-9]+','QQQ') AS A
  FROM babb_reg_test;

A
-----------------------------------------------
ABCQQQXYZ
ABCQQQXYZQQQ
Edward
```

### 替换数字（从第一个字母开始匹配，替换第 2 个匹配项目）

```sql
SELECT REGEXP_REPLACE (a,'[0-9]+','QQQ',1,2) AS A
  FROM babb_reg_test;

---------------------------------------------------
ABC123XYZ
ABC123XYZQQQ
Edward

```

### 查找字符出现的次数

```sql
SELECT LENGTH(REGEXP_REPLACE(REPLACE('aa\bb\cc', '\', '@'), '[^@]+', ''))
  FROM DUAL;

^ 匹配输入字符串的开始位置。 如果在方括号表达式中使用，此时它表示不接受该字符集合。 要匹配 ^ 字符本身，请使用 \^。

----------------------------------------------------
2
```

### REGEXP_INSRT 参数说明

-   第一个是输入的字符串
-   第二个是正则表达式
-   第三个是标识从第几个字符开始正则表达式匹配。（默认为 1）
-   第四个是标识第几个匹配组。（默认为 1）
-   第五个是指定返回值的类型，如果该参数为 0，则返回值为匹配位置的第一个字符，如果该值为非 0 则返回匹配值的最后一个位置的下一个位置。
-   第六个是是取值范围：
    i：大小写不敏感；
    c：大小写敏感；
    n：点号 . 不匹配换行符号；
    m：多行模式；
    x：扩展模式，忽略正则表达式中的空白字符。

### 找数字

```sql
SELECT REGEXP_INSTR(a,'[0-9]+') AS A
  FROM babb_reg_test;

A
----------
4
4
0

```

### 找数字（从第一个字母开始匹配，找第 1 个匹配项目的最后一个字符的位置）

```sql
SELECT REGEXP_INSTR (a,'[0-9]+', 1, 1, 1) AS A
  FROM babb_reg_test;

A
----------
4
4
0
```

### 找数字（从第一个字母开始匹配，找第 2 个匹配项目）

```sql
SELECT
REGEXP_INSTR (a,'[0-9]+', 1,2) AS A
FROM
babb_reg_test;

A
----------
0
10
0
```

### 找数字（从第一个字母开始匹配，找第 2 个匹配项目的最后一个字符的位置）

```sql
SELECT
REGEXP_INSTR (a,'[0-9]+', 1, 2, 1) AS A
FROM
babb_reg_test;

A
----------
0
13
0
```
