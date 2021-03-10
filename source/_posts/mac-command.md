---
title: mac
tags: other
description: mac 常用命令记录
date: 2018-03-01
---

### tree

输出目录树结构

| 命令                     | 含义                     |
| ------------------------ | ------------------------ |
| `tree --help`            | 显示帮助                 |
| `tree -L n`              | 指定遍历层级为 n         |
| `tree -L 2 > test.txt`   | 将目录树写到 test.txt    |
| `tree -d`                | 只显示文件夹             |
| `tree -I "node_modules"` | 过滤不想要的文件或文件夹 |

### other

| 命令                 | 含义     |
| -------------------- | -------- |
| command + option + c | 复制路径 |

### 软连接

软连接文件类似于 Windows 的快捷方式，它实际上是一个特殊的文件, 其中包含的有另一文件的位置信息。

语法:

`ln -s 源文件(即：实际所在的路径及名字) 目标文件(即：希望所在的路径及名字)`

如下将 django-admin.py 连接到 bin 目录下

`ln -s /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/django/bin/django-admin.py /usr/local/bin`

### 权限

`d rwx r-x r-x`

第 1 位表示文件类型。d 是目录文件，l 是链接文件，-是普通文件，p 是管道

第 2-4 位表示这个文件的属主拥有的权限，r 是读，w 是写，x 是执行。

第 5-7 位表示和这个文件属主所在同一个组的用户所具有的权限。

第 8-10 位表示其他用户所具有的权限。
