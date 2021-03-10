---
title: python yield
tags: python
date: 2019-02-28
---

### 栈帧

栈帧就是一个函数执行的环境：函数参数、函数的局部变量、函数执行完后返回到哪里等等。python 中一且皆对象，运行函数前首先会创建栈帧 (stack frame) 对象，然后在这个上下文环境中运行字节码对象，所有的栈帧都是分配在堆内存上，不去释放就会一直存在，这就决定了栈帧可以独立于调用者存在。

```python
import inspect

frame = None
def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

foo()
print(frame.f_code)
print(frame.f_code.co_name)         # bar
caller_frame = frame.f_back         # 指向调用者的栈帧
print(caller_frame.f_code.co_name)  # foo
```

### 生成器 yield

```python
def gen_func():
    yield 1
    name = "babb"
    yield 2
    age = 26
    return "test"

import dis
gen = gen_func()
# 打印字节码
print(dis.dis(gen))
# 上一次执行的字节码位置，刚开始为 None
print(gen.gi_frame.f_lasti)
# 上一次执行保存的变量，刚开始为 -1
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

'''
 18           0 LOAD_CONST               1 (1)
              2 YIELD_VALUE
              4 POP_TOP

 19           6 LOAD_CONST               2 ('babb')
              8 STORE_FAST               0 (name)

 20          10 LOAD_CONST               3 (2)
             12 YIELD_VALUE
             14 POP_TOP

 21          16 LOAD_CONST               4 (26)
             18 STORE_FAST               1 (age)

 22          20 LOAD_CONST               5 ('test')
             22 RETURN_VALUE
None
-1
{}
2
{}
12
{'name': 'babb'}
'''
```

### yield 实现大文件读取

```python
def myreadlines(f, newline):
    buf = ""

    while True:
        # 防止两个 newline 在一次读取没有切分
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos].strip()
            buf = buf[pos + len(newline):]

        # 每次读取 4096 字节数据
        chunk = f.read(4096)

        # 终止条件
        if not chunk:
            yield buf.strip()
            break

        buf += chunk

with open('test.txt') as f:
    for line in myreadlines(f, ','):
        print(line)

'''
test.txt
life is short, i use python, php is the best lanaguage of the word, www ...
'''
```