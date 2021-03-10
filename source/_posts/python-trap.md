---
title: python trap
tags: python
---

#### UnboundLocalError

```python
a = 1
def func():
    a += 1
    print(a)
func()
# UnboundLocalError: local variable 'a' referenced before assignment

import random
def func(ok):
    if ok:
        a = random.random()
    else:
        import random
        a = random.randint(1,10)
    return a
func(True)
# UnboundLocalError: local variable 'random' referenced before assignment

### Solve ###
import random
def func(ok):
    if ok:
        global random
        a = random.random()
    else:
        import random
        a = random.randint(1,10)
    return a
func(True)
```

#### mutable 对象作为默认参数

python 中一切皆对象，函数也是对象，默认参数是函数的一个属性，默认参数在函数定义的时候已经求值，函数的 `__defaults` 始终保持一个对默认参数的引用

```python
def f(lst = []):
    lst.append(1)
    return lst
print(f())
print(f())
# [1]
# [1, 1]


import time
def report(when = time.time()):
    return when
print(report())
print(report())
# 1521033649.5745206
# 1521033649.5745206

### Solve ###
def report(when = None):
    if when is None:
        when = time.time()
    return when
print(report())
print(report())
# 1521033793.564442
# 1521033812.377632


def func(a = [1]):
    a.append(1)
    print(a)

print(func.__defaults__) # ([1],)  默认参数在定义时就已经存在
func() # [1, 1]
func() # [1, 1, 1]
print(func.__defaults__) # ([1, 1, 1],)  func.__defaults__ 始终保持一个对默认参数的引用
func.__defaults__ = ([8],)
func() # [8, 1]
```

#### x + = y ne x = x + y

x += y 是 `inplace` 操作

```python
x = [1]
print(id(x))
x = x+[2]
print(id(x))
# 2484214337928
# 2484214326344
x = [1]
print(id(x))
x+=[2]
print(id(x))
# 2648852238728
# 2648852238728
```

#### 一个元素的 tuple

tuple 是一个元素时后面需要添加一个 `,`

```python
a =(1,2)
print(type(a))
a = (1)
print(type(a))
a = (1,)
print(type(a))
# <class 'tuple'>
# <class 'int'>
# <class 'tuple'>
```

#### 生成一个元素是可变对象的序列

```python
a = [[]] * 10
print(a)
# [[], [], [], [], [], [], [], [], [], []]
a[0].append(10)
print(a)
# [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10]]

a =[[] for _ in range(10)]
a[0].append(10)
print(a)
# [[10], [], [], [], [], [], [], [], [], []]
```

#### 在访问列表的时候，修改列表

```python
# 当删除元素3之后，6 变成lst的第2个元素（从0开始）
def modify_lst(lst):
    for idx,elem in enumerate(lst):
        print(idx,elem)
        if elem % 3 ==0:
            del lst[idx]
lst = [1,2,3,6,5,4]
modify_lst(lst)
print(lst)
# 0 1
# 1 2
# 2 3
# 3 5
# 4 4
# [1, 2, 6, 5, 4]

### Solve ###
lst = [x for x in lst if x % 3 != 0]
print(lst)
# [1, 2, 5, 4]
```

#### 闭包与 lambda

```python
# Python中的属性查找规则，LEGB（local，enclousing，global，bulitin），i就是在闭包作用域（enclousing)，
# 而Python的闭包是延迟绑定，这意味着闭包中用到的变量的值，是在内部函数被调用时查询得到的。
def create_multipliers():
    return [lambda x: i*x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))
# 8
# 8
# 8
# 8
# 8

### Solve ###
# 变闭包作用域为局部作用域。
def create_multipliers():
    return [lambda x,i=i:i*x for i in range(5)]
for multiplier in create_multipliers():
    print(multiplier(2))
# 0
# 2
# 4
# 6
# 8
```

#### except

python3 为了 Exception 对象可以及时被回收会删除 Exception 对象, 当有全局变量和其同名时, 会导致之后无法访问

```python
e = 18
try:
    1 / 0
except Exception as e:
    print(e)

print(e)

# division by zero
# Traceback (most recent call last):
#   File "test.py", line 70, in <module>
#     print(e)
# NameError: name 'e' is not defined
```

#### \_\_del\_\_

在循环引用中的对象定义的 `__del__` ，Python GC 不能进行回收，因此，存在内存泄漏的风险
