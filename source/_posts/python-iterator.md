---
title: Python Iterable
tags: python
date: 2019-02-28
---

### Iterator & Iterable

Iterable: 实现了 `__iter__` 方法的对象
Iterator: 实现了 `__iter__` 和 `__next__` 方法的对象

Python 中关于迭代有两个概念，第一个是 Iterable，第二个是 Iterator，协议规定 Iterable 的 `__iter__`方法会返回一个 Iterator, Iterator 的 `__next__`方法（Python 2 里是 next）会返回下一个迭代对象，如果迭代结束则抛出 StopIteration 异常。同时，Iterator 自己也是一种 Iterable，所以也需要实现 Iterable 的接口，也就是`__iter__`，这样在 for 当中两者都可以使用。Iterator 的`__iter__`只需要返回自己就行了。

```python
a = [1, 2, 3]
print(isinstance(a, Iterable))  # True
print(isinstance(a, Iterator))  # False

# list 实现了 __iter__ 方法，返回一个迭代器
iterator_a = iter(a)
print(isinstance(iterator_a, Iterator))  # True

for i in a:
    print(i, end=' ')

# 1 2 3

print()

for i in iterator_a:
    print(i, end=' ')

# 1 2 3
```

### for 循环后备机制

for 为了兼容性有两种机制，如果对象有`__iter__`会使用迭代器，但是如果对象没有`__iter__`，但是实现了`__getitem__`，会改用下标迭代的方式。

```python
class Company:

    def __init__(self, employees):
        self.employees = employees

    def __getitem__(self, index):
        return self.employees[index]

companies = Company(['A', 'B', 'C'])
#  __iter__ => __getitem__
for c in companies:
    print(c)
```

###  为什么存在 Iterable 和 Iterator

Python 中许多方法直接返回 Iterator，如果 Iterator 自己不是 Iterable 的话，就很不方便，需要先返回一个 Iterable 对象，再让 Iterable 返回 Iterator。

生成器表达式也是一个 Iterator，显然对于生成器表达式直接使用 for 是非常重要的。那么为什么不只保留 Iterator 的接口而还需要设计 Iterable 呢？

许多对象比如 list、dict，是可以重复遍历的，甚至可以同时并发地进行遍历，通过 `__iter__` 每次返回一个独立的迭代器，就可以保证不同的迭代过程不会互相影响。

而生成器表达式之类的结果往往是一次性的，不可以重复遍历，所以直接返回一个 Iterator 就好。让 Iterator 也实现 Iterable 的兼容就可以很灵活地选择返回哪一种。

总结来说 Iterator 实现的`__iter__` 是为了兼容 Iterable 的接口，从而让 Iterator 成为 Iterable 的一种实现。

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)   
print(c, type(c)) # <zip object at 0x0000026580247648> <class 'zip'>
print(isinstance(c, Iterator)) # True
for i in c:
    print(i)
for i in c:
    print(i)
print('*' * 10)
c_list = list(zip(a, b))
for i in c_list:
    print(i)
for i in c_list:
    print(i)
    
# (1, 4)
# (2, 5)
# (3, 6)
# **********
# (1, 4)
# (2, 5)
# (3, 6)
# (1, 4)
# (2, 5)
# (3, 6)
```

### 自定义迭代器

```python
from collections.abc import Iterator, Iterable

class Company:

    def __init__(self, employees):
        self.employees = employees

    def __iter__(self):
        return MyIterator(self.employees)


class MyIterator(Iterator):

    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.index = 0

    # 继承 Iterator 会自动实现
    # def __iter__(self):
    #     return self

    def __next__(self):

        try:
            iter_item = self.iter_list[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return iter_item


company = Company(['A', 'B', 'C'])
for c in company:
    print(c)

company_iter = iter(company)
while True:
    try:
        print(next(company_iter))
    except StopIteration:
        break
```
