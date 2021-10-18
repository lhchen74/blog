---
title: Python Property Descriptor
tags: python
date: 2019-07-18
---

## property 属性访问器

property 用于控制访问安全类似 java 中的 get、set 方法；可以定义计算属性，例如根据半径计算直径(diameter)。

```python
from numbers import Integral
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def radius(self):
        # 不能使用 return self.radius，会造成循环引用
        # 1. 直接返会实例字典属性
        # 2. 私有化 radius, 返回 self._radius
        return self.__dict__['radius']

    @radius.setter
    def radius(self, value):
        if not isinstance(value, Integral) or value < 0:
            raise ValueError('radius must be int and gte 0, but got {}'.format(value))
        self.__dict__['radius'] = value
```

## \_\_getattr\_\_ and \_\_getattribute\_\_

`__getattr__` 和 `__getattribute__` 在属性不存在时调用，如果两个同时存在，`__getattribute__` 会首先调用，而 `__getattr__` 会在 `__getattribute__` 抛出 `AttributeError` 时调用

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __getattribute__(self, name):
        print('__getattribute__  {}'.format(name))

    def __getattr__(self, name):
        print('__getattr__ {}'.format(name))

c = Circle(1)
d = c.radius    # __getattribute__  radius
d = c.name      # __getattribute__  name


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __getattribute__(self, name):
        print('__getattribute__  {}'.format(name))
        raise AttributeError('{} not exist'.format(name))

    def __getattr__(self, name):
        print('__getattr__ {}'.format(name))

c = Circle(1)
d = c.name
# __getattribute__  name
# __getattr__ name
```

## descriptor 描述器

python 中，一个类实现了`__get__`, `__set__`, `__delete__`,三个方法中的任何一个方法就是描述器，仅实现 `__get__` 方法就是非数据描述器，同时实现`__get__`,`__set__` 就是数据描述器。python中属性的调用顺序: `__getattribute__`(data descriptor -> instance property -> nondata descriptor -> class property) -> `__getattr__`

```python
from numbers import Integral

class IntField:
    # instance 被描述的类的实例，owner 被描述的类
    def __get__(self, instance, owner):
        return self.value

    # value 为 instance 属性设置的值
    def __set__(self, instance, value):
        if not isinstance(value, Integral) or value < 0:
            raise ValueError('radius must be int and gte 0, but got {}'.format(value))
        self.value = value

class Circle:
    radius = IntField()
    def __init__(self, radius):
        self.radius = radius

c = Circle(-1)
# ValueError: radius must be int and gte 0, but got -1
```

## 使用 descriptor 实现 lazyproperty

```python
class lazyproperty:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):

        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


# def lazyproperty(func):
#     name = '_lazy_' + func.__name__
#     @property
#     def lazy(self):
#         if hasattr(self, name):
#             return getattr(self, name)
#         else:
#             value = func(self)
#             setattr(self, name, value)
#             return value
#     return lazy

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # area = lazyproperty(area)
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

c = Circle(10)
print(c.area)
print(c.area)
```
