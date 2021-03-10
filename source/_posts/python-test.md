---
title: python test
tags: python
---

> As for those people, the truth doesn't count, what they only care is that the accepted truth must be advantageous to them - Strive to live in this world

### doctest 文档测试

Python 内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。doctest 严格按照 Python 交互式命令行的输入和输出来判断测试结果是否正确。

```python
def fabonacci(n):
    '''
    fabonacci: 1 1 2 3 5
    >>> fabonacci(2)
    1
    >>> fabonacci(5)
    5
    >>> fabonacci(-5)
    Traceback (most recent call last):
        ...
    ValueError: param can not < 1
    '''

    if n < 1:
        raise ValueError("param can not < 1")
    elif n <= 2:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

### unittest 单元测试

单元测试（unit testing），是指对软件中的最小可测试单元进行检查和验证。
python 单元测试可以通过在 main 函数中运行 `unittest.main()`, 也可以以模块的方式运行 `python -m unittest mydict_test`

```python
# mydict.py
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"Dict has no key {key}")

    def __setattr__(self, key, value):
        self[key] = value


# mydict_test.py
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 模块方式运行: python -m unittest mydict_test
if __name__ == '__main__':
    unittest.main()
```
