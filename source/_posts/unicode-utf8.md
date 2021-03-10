---
title: unicode and utf8
tags: other
date: 2019-06-06
---

Unicode 是一个囊括了世界上所有字符的字符集，其中每一个字符都对应有唯一的编码值（code point），然而它并不是一种什么编码格式，仅仅是字符集而已。 Unicode 字符要存储要传输怎么办，它不管，具体怎么编码，你们可以自己去实现，可以用 UTF-8、UTF-16、甚至用 GBK 来编码也是可以的。

| 原字符 | Unicode  | UTF-8           |
| ------ | -------- | --------------- |
| 好     | '\u597d' | b'\xe5\xa5\xbd' |

```python
a = '好'
b = '\u597d'

print(a.encode('utf-8'), b.encode('utf-8'))
print(a.encode('utf-8') == b.encode('utf-8'))

# b'\xe5\xa5\xbd' b'\xe5\xa5\xbd'
# True
```

> 引用: https://foofish.net/unicode_utf-8.html
