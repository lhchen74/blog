---
title: Oracle Over
date: 2018-08-08
tags: db
---

> 守着天空，大海和你的回忆

### 开窗函数

oracle 从 8.1.6 开始提供的分析函数，分析函数用于计算基于组的某种聚合值，它和聚合函数的不同之处是：对于每个组返回多行，而聚合函数对于每个组只返回一行。
over 后的写法 `over (order by salary)` 按照 salary 排序进行累计，`over(partition by deptno)` 按照部门分区。

测试数据：

t2 表信息如下：
name class s
cfe 2 74
dss 1 95
ffd 1 95
fda 1 80
gds 2 92
gf 3 99
ddd 3 99
adf 3 45
asdf 3 55
3dd 3 78

#### 开窗的窗口范围

`over (order by salary range between 5 preceding and 5 following)` 窗口范围为当前行数据幅度减 5 加 5 后的范围内的。

```sql
 select name,
        class,
        s,
        sum(s) over(order by s range between 2 preceding and 2 following) mm
   from t2

adf        3        45        45  --45加2减2即43到47，但是s在这个范围内只有45
asdf       3        55        55
cfe        2        74        74
3dd        3        78        158 --78加2减2即76到80，在76到80范围内有78，80，求和得158
fda        1        80        158
gds        2        92        92
ffd        1        95        190
dss        1        95        190
ddd        3        99        198
gf         3        99        198
```

`over (order by salary rows between 5 preceding and 5 following)` 窗口范围为当前行前后各移动 5 行。

```sql
select name,
       class,
       s,
       sum(s) over(order by s rows between 2 preceding and 2 following) mm
  from t2

adf        3        45        174     (45+55+74=174)
asdf       3        55        252     (45+55+74+78=252)
cfe        2        74        332     (74+55+45+78+80=332)
3dd        3        78        379     (78+74+55+80+92=379)
fda        1        80        419
gds        2        92        440
ffd        1        95        461
dss        1        95        480
ddd        3        99        388
gf         3        99        293
```

#### 与 over 函数结合的几个函数

```sql
select *
  from (select name,
               class,
               s,
               rank() over(partition by class order by s desc) mm
          from t2)
 where mm = 1;

dss        1        95        1
ffd        1        95        1
gds        2        92        1
gf         3        99        1
ddd        3        99        1

--在求第一名成绩的时候，不能用row_number()，因为如果同班有两个并列第一，row_number()只返回一个结果;
select *
  from (select name,
               class,
               s,
               row_number() over(partition by class order by s desc) mm
          from t2)
 where mm = 1;

1        95        1  --95有两名但是只显示一个
2        92        1
3        99        1  --99有两名但也只显示一个

--rank()和dense_rank()可以将所有的都查找出来，
--rank()和dense_rank()区别：
--rank()是跳跃排序，有两个第二名时接下来就是第四名；
select name,class,s,rank()over(partition by class order by s desc) mm from t2
dss        1        95        1
ffd        1        95        1
fda        1        80        3 --直接就跳到了第三
gds        2        92        1
cfe        2        74        2
gf         3        99        1
ddd        3        99        1
3dd        3        78        3
asdf       3        55        4
adf        3        45        5

--dense_rank()是连续排序，有两个第二名时仍然跟着第三名
select name,class,s,dense_rank()over(partition by class order by s desc) mm from t2
dss        1        95        1
ffd        1        95        1
fda        1        80        2 --连续排序（仍为2）
gds        2        92        1
cfe        2        74        2
gf         3        99        1
ddd        3        99        1
3dd        3        78        2
asdf       3        55        3
adf        3        45        4

--sum() over() 的使用
select name,class,s, sum(s) over(partition by class order by s desc) mm from t2 --根据班级进行分数求和
dss        1        95        190  --由于两个95都是第一名，所以累加时是两个第一名的相加
ffd        1        95        190
fda        1        80        270  --第一名加上第二名的
gds        2        92        92
cfe        2        74        166
gf         3        99        198
ddd        3        99        198
3dd        3        78        276
asdf       3        55        331
adf        3        45        376
```
