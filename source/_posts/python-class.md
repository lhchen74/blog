---
title: python class
tags: python
date: 2019-02-28
---

### 多继承顺序

super() 会沿着`__mro__` 顺序调用

```python
class D:
    pass

class E:
    pass

class B(D):
    pass

class C(E):
    pass

class A(B, C):
    pass

# D   E
#  B C
#   A

print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)

class D:
    pass

class B(D):
    pass

class C(D):
    pass

class A(B, C):
    pass

#  D
# B C
#  A
print(A.__mro__)
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
```

### abstract class

```python
import abc

class BaseCache(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

class RedisCache(BaseCache):
    pass


# TypeError: Can't instantiate abstract class RedisCache with abstract methods get
# redis_cache = RedisCache()


class BaseCache2:
    
    def get(self, key):
        raise NotImplementedError

class RedisCache2(BaseCache2):
    pass

redis_cache2 = RedisCache2()
# 在使用的时候才会报错，实例化的时候不会报错
# NotImplementedError
redis_cache2.get('name')
```



### new & init

new 用来控制对象的生成过程，在对象生成之前，init 用来完善对象，如果 new 方法不返回对象不会调用 init

```python
class User:

    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('__init__')

u = User('babb')
# __new__
# __init__


class User:

    def __new__(cls, *args, **kwargs):
        print('__new__')
        print('args: ', args)
        print('kwargs: ', kwargs)

    def __init__(self, name):
        # __new__ 没有返回不会调用 __init__
        print('__init__')

u = User('babb')
# __new__
# args:  ('babb',)
# kwargs:  {}

u = User(name='babb')
# __new__
# args:  ()
# kwargs:  {'name': 'babb'}
```

### type

type 可以用来创建类

```python
def say(self):
    print(f'i am {self.name}')


class BaseClass:

    def hello(self):
        print('hello world')


User = type('User', (BaseClass, ), {'name': 'babb', 'say': say})
u = User()
print(u.__dict__, User.__dict__, u.name)
u.say()
u.hello()

# {} {'name': 'babb', 'say': <function say at 0x00000000020D3E18>, '__module__': '__main__', '__doc__': None} babb
# i am babb
# hello word
```

### metaclass

python 类实例化时会首先寻找 metaclass, 通过 metaclass 创建类，元类是用来创建类的类，需要继承 type，因为 type 可以用来创建类

```python
class MetaClass(type):
    # 将类的创建委托给元类
    def __new__(cls, *args, **kwargs):
        print('meta __new__')
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'user'


u = User('babb')
print(u)
```