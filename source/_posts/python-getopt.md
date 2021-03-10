---
title: python getopt
tags: python
---

### 参数说明

`getopt.getopt(args, shortopts, longopts=[])`

- args 指的是当前脚本接收的参数，它是一个列表，可以通过 sys.argv 获得
- shortopts 是短参数，例如 python test.py -h
- longopts 是长参数，例如 python test.py --help

### 测试一

```python
import getopt
import sys

# sys.argv[0] 是当前脚本文件名
print(sys.argv[0])  # test.py
arg = getopt.getopt(sys.argv[1:], '-h', ['help'])
print(arg)

# python .\test.py -h
# ([('-h', '')], [])
# python .\test.py --help
# ([('--help', '')], [])
```

### 测试二

```python
import getopt
import sys
# -f: 代表当前参数有值 对应长参数为 filename=
opts, args = getopt.getopt(
    sys.argv[1:], '-h-f:-v', ['help', 'filename=', 'version'])
for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
        print("[*] Help info")
        exit()
    if opt_name in ('-v', '--version'):
        print("[*] Version is 0.01 ")
        exit()
    if opt_name in ('-f', '--filename'):
        fileName = opt_value
        print("[*] Filename is ", fileName)
        # do something
        exit()

# PS G:\Python\getoptdemo> python test.py --filename='test'
# [*] Filename is  test
# PS G:\Python\getoptdemo> python test.py -f test
# [*] Filename is  test
# PS G:\Python\getoptdemo> python test.py --version
# [*] Version is 0.01
# PS G:\Python\getoptdemo> python test.py -v
# [*] Version is 0.01
# PS G:\Python\getoptdemo>
```

> 作者：倾旋
> 链接：https: // www.jianshu.com/p/a877e5b46b2d
> 來源：简书
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
