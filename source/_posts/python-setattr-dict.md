---
title: Python Setattr And Dict Update
tags: python
date: 2020-08-17
---

### 简化 __init__

你写了很多仅仅用作数据结构的类，不想写太多烦人的 `__init__()` 函数

```python
class Structure:

    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        for name, value in zip(self._fields, args):
            self.__dict__.update(zip(self._fields, args))

        extra_keys = kwargs.keys() - self._fields
        for name in extra_keys:
            self.__dict__.update({name: kwargs.pop(name)})

        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure):
    _fields = ['name', 'shares']

s = Stock('ACME', 50, price=100)
print(s.__dict__)
print(s.name, s.shares, s.price)
# {'name': 'ACME', 'shares': 50, 'price': 100}
# ACME 50 100
```

### 问题

- 当一个子类定义了 `__slots__` 时, 其实例 `__dict__` 中存在 name, 实例中没有 name 属性

- 通过property(或描述器)来包装某个属性, 通过 dict.update 无法应用到 property

```python
class Structure:

    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        self.__dict__.update(zip(self._fields, args))

        extra_keys = kwargs.keys() - self._fields
        for name in extra_keys:
            self.__dict__.update({name: kwargs.pop(name)})

        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure):
    _fields = ['name', 'shares']
    __slots__ = ['name']


s = Stock('ACME', 50, shares=100)
print(s.__dict__) # {'name': 'ACME', '_shares': 50, 'shares': 100}
print(s.name)  # AttributeError: name
print(s.shares, s._shares) # 40.0 50
```

使用 setattr 替换 dict update

```python
class Structure:

    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        # self.__dict__.update(zip(self._fields, args))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_keys = kwargs.keys() - self._fields
        for name in extra_keys:
            setattr(self, name, kwargs.pop(name))
            # self.__dict__.update({name: kwargs.pop(name)})

        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure):
    _fields = ['name', 'shares']
    __slots__ = ['name']


s = Stock('ACME', 50, price=100)

print(s.__dict__) # {'_shares': 100}
print(s.name)  # ACME
print(s.shares, s._shares) # 80.0 100
```



