---
title: Python Faker
tags: python
date: 2020-06-10
---

> 转载: [求求你，别再手工造假数据了，fake 了解一下 - FooFish-Python 之禅](https://foofish.net/python-fake-data.html)

项目开发初期，为了测试方便，我们总要造不少假数据到系统中，尽量模拟真实环境。

比如要创建一批用户，创建一段文本，或者是电话号码，抑或着是街道地址或者 IP 地址等等。

以前要么就是键盘一顿乱敲，随便造个什么字符串出来，当然最后谁也不认识谁。

现在你不要这样做了。

用 faker 就能满足你的一切需求。

先安装 faker

```python
pip install Faker
```

创建 faker 对象

```python
from faker import Faker
fake = Faker()
```

fake 一个名字

```python
>>> fake.name()
'Joshua Reed'
```

fake 一个地址

```python
>>> fake.address()
'554 Hoffman Locks Suite 216\nElizabethstad, RI 23081'
```

fake 一个浏览器 UA

```python
>>> fake.chrome()
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/35.0.870.0 Safari/532.0'
```

fake 一个日期

```python
>>> fake.date()
'1984-08-17'
>>> fake.date_object()
datetime.date(1980, 9, 27)
```

但凡是你需要的东西他都能帮你 fake，如果你不知道它能 fake 哪些东西，可以用 dir(fake)查看一下。

它能 fake 近 300 种东西出来，如果还有你满足不了需求的，你可以像它的 Github 提交 PR 或者自己扩展

上面 fake 的东西，比如名字，街道都是英文的，他支不支持中文呢？

可以的

只要在创建 Faker 对象的时候，指定语言就可以

```python
>>> fake = Faker("zh_CN")
>>> fake.name()
'庄阳'
>>> fake.address()
'浙江省台北县沈北新北京街i座 285123'
>>> fake.phone_number()
'13223924289'
```

你会发现，fake 的假数据还挺真实的。除了中文，它还支持日语、韩语、德语等上百种语言

当然，它还支持命令行模式

-h 查看帮助文档

```python
faker [-h] [--version] [-o output]
      [-l {bg_BG,cs_CZ,...,zh_CN,zh_TW}]
      [-r REPEAT] [-s SEP]
      [-i {package.containing.custom_provider otherpkg.containing.custom_provider}]
      [fake] [fake argument [fake argument ...]]
```

我可不可以创建属于自己的 fake 数据呢？比如我想随机生成一个基于 Android 设备的 User-Agent

```python
from faker import Faker
fake = Faker()

from faker.providers import BaseProvider

# 创建自定义的provider
class MyProvider(BaseProvider):
    def android_ua(self):
        return 'xxxxxx'

# 添加一个provider
fake.add_provider(MyProvider)

>>>fake.android_ua()
>>>'xxxxxx'
```

是不是太简单了。另外，faker 还是一个非常值得作为源码研究的库。
