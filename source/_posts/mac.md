---
title: Mac Tools & Commands
tags: mac
date: 2019-07-10
---

### say

基本用法：say hello

查看播音员名单：say -v '?'

指定播音员：say -v Ting-Ting 你好

### dictionary

鼠标悬浮在单词上方按 ctrl + command + d 查询单词

配置翻译可以在 dictionary.app 中设定

### iina

播放器

### the unarchiver

解压软件

### calculator

C: 清除上一步操作

AC: 清除所有操作

配置可以在 calculator.app 中设定

### voice memos

录音软件

### finder

目录结构

/ 根目录

​ /Application

​ /Library

​ /System/Library/Desktop Pictures

​ /Users/jbn

​ /Desktop | /Documnets | / Downloads | /Movies ...

Finder -> 前往文件件，快捷键 Shift + Command + G

Command + N: 打开一个新的 Finder 窗口

Command + W: 关闭一个 Finder 窗口

Shift + Command + N: 新建文件夹

Enter:修改文件夹文件名称

Command + D: Command + C & Command + V

Command + delete: 删除文件夹文件

Command + C & Command + option + V: 移动文件夹文件

Command + O: 进入文件夹

Command + [ : 进入上层目录

Command + ]: 进入下层目录

Shift + Command + D: 进入桌面

Shift + Command + H: 进入用户目录

Command + Option + C:  复制路径

### 退出程序

Command + Q

Command + Option + Esc: 强制退出

Activity Monitor.app: 活动监视器相当于 window 的任务管理器


### tree

输出目录树结构

| 命令                     | 含义                     |
| ------------------------ | ------------------------ |
| `tree --help`            | 显示帮助                 |
| `tree -L n`              | 指定遍历层级为 n         |
| `tree -L 2 > test.txt`   | 将目录树写到 test.txt    |
| `tree -d`                | 只显示文件夹             |
| `tree -I "node_modules"` | 过滤不想要的文件或文件夹 |

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

