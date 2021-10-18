---
title: Python Func Args
tags: python
date: 2019-04-30
---

### 位置参数

调用函数时根据函数定义的参数位置来传递参数。

```python
def print_hello(name, sex):
    sex_dict = {1: '先生', 2: '女士'}
    print('hello %s %s, welcome to python world!' %(name, sex_dict.get(sex, '先生')))

# 两个参数的顺序必须一一对应，且少一个参数都不可以
print_hello('tanggu', 1)
```

### 关键字参数

用于函数调用，通过“键-值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。

```python
# 以下是用关键字参数正确调用函数的实例
print_hello('tanggu', sex=1)
print_hello(1, name='tanggu')
print_hello(name='tanggu', sex=1)
print_hello(sex=1, name='tanggu')

# 以下是错误的调用方式 (位置参数必须在关键字参数前面)
print_hello(name='tanggu', 1)
print_hello(sex=1, 'tanggu')
```

通过上面的代码，我们可以发现：有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序的

### 默认参数

用于定义函数，为参数提供默认值，调用函数时可传可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）

```python
# 正确的默认参数定义方式--> 位置参数在前，默认参数在后
def print_hello(name, sex=1):
    pass

# 错误的定义方式
def print_hello(sex=1, name):
    pass

# 调用时不传sex的值，则使用默认值1
print_hello('tanggu')

# 调用时传入sex的值，并指定为2
print_hello('tanggu', 2)
```

### 可变参数

定义函数时，有时候我们不确定调用的时候会传递多少个参数(不传参也可以)。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。

- 包裹位置传递

```python
def func(*args):
    pass

# func()
# func(a)
# func(a, b, c)
```

我们传进的所有参数都会被 args 变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args 是元组类型，这就是包裹位置传递。

- 包裹关键字传递

```python
def func(**kargs):
    pass

# func(a=1)
# func(a=1, b=2, c=3)
```

kargs 是一个字典(dict)，收集所有关键字参数

### 解包裹参数

\*和\*\*，也可以在函数调用的时候使用，称之为解包裹(unpacking)

- 在传递元组时，让元组的每一个元素对应一个位置参数

```python
def print_hello(name, sex):
    print(name, sex)

# args = ('tanggu', '男')
# print_hello(*args)
# tanggu 男
```

- 在传递词典字典时，让词典的每个键值对作为一个关键字参数传递给函数

```python
def print_hello(kargs):
    print kargs

# kargs = {'name': 'tanggu', 'sex', u'男'}
# print_hello(**kargs)
# {'name': 'tanggu', 'sex', u'男'}
```

### 位置参数、默认参数、可变参数的混合使用

基本原则是：先位置参数，默认参数，包裹位置，包裹关键字(定义和调用都应遵循)

```python
def func(name, age, sex=1, *args, **kargs):
    print name, age, sex, args, kargs

# func('tanggu', 25, 2, 'music', 'sport', class=2)
# tanggu 25 1 ('music', 'sport') {'class'=2}

def foo(x,a = 4,**kwargs):  #混合使用参数
    print(x)
    print(a)
    print(kwargs)

foo(1,y=2,z=3)　  　        #使用默认参数
# 1　　
# 4
# {'y': 2, 'z': 3}

foo(1,5,y=2,z=3)　　        #修改默认参数
# 1
# 5
# {'y': 2, 'z': 3}
```

### 小结

- 位置参数：调用函数时所传参数的位置必须与定义函数时参数的位置相同
- 关键字参数：使用关键字参数会指定参数值赋给哪个形参，调用时所传参数的位置可以任意
- 可变参数
  - 包裹位置：可接受任意数量的位置参数(元组)；只能作为最后一个位置参数出现，其后参数均为关键字参数
  - 包裹关键字：可接受任意数量的关键字参数(字典)；只能作为最后一个参数出现
- 默认参数：默认参数的赋值只会在函数定义的时候绑定一次，默认值不会再被修改

> 作者: devops1992
> 来源: <https://www.cnblogs.com/bingabcd/p/6671368.html>
