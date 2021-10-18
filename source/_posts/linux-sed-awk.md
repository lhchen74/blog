---
title: Linux Grep Sed And Awk
tags: linux
date: 2021-03-14
---

## grep

grep 是文本查找命令，可以通过正则查找匹配。

```shell
$ grep 'root' passwd
root:x:0:0:root:/root:/bin/bash


$ grep '^\w\{4\}:' passwd
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
```

## sed

流处理编辑器， sed 一次处理一行内容，不改变文件内容（除非重定向）。

1. 文本或管道输入
2. 读入一行到**模式空间**（临时缓存区）
3. sed 命令处理
4. 输出到屏幕
5. 重复 2

### sed 格式

-   命令行格式

    `sed [options] 'command' file(s)`

    options:

    -   -n: -n, --quiet, --silent suppress automatic printing of pattern space
    -   -e: -e script, --expression=script add the script to the commands to be executed

    command: 行定位（正则） + sed 命令（操作）

-   脚本格式

    `sed -f scriptfile file(s)`

### p 打印

sed 读入一行自动输出打印一行，p 打印命令也会打印一行，所以 `sed 'p' passwd ` 每行会打印两遍。使用 `-n` option 关闭自动打印。

```shell
$ sed 'p' passwd
root:x:0:0:root:/root:/bin/bash
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
......

$ sed -n 'p' passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
......
```

行定位

定位一行：行号`x` , 正则表达式 `/pattern/`

定位间隔行：行号`x,y` , 正则表达式 `/pattern1/,/pattern2/` , 混合 `/pattern/,x`

取反：`x,y!`

定位间隔几行：`first ~ step`

```shell
$ nl passwd | sed -n '10p'
    10  news:x:9:9:news:/var/spool/news:/usr/sbin/nologin

$ nl passwd | sed -n '/news/p'
    10  news:x:9:9:news:/var/spool/news:/usr/sbin/nologin

$ nl passwd | sed -n '1,2p'
    1  root:x:0:0:root:/root:/bin/bash
    2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

$ nl passwd | sed -n '/root/,/daemon/p'
     1  root:x:0:0:root:/root:/bin/bash
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

$ nl passwd | sed -n '1,/daemon/p'
     1  root:x:0:0:root:/root:/bin/bash
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin

$ nl passwd | sed -n '1,/daemon/!p'
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
     4  sys:x:3:3:sys:/dev:/usr/sbin/nologin
     5  sync:x:4:65534:sync:/bin:/bin/sync
     6  games:x:5:60:games:/usr/games:/usr/sbin/nologin

$ nl passwd | sed -n '1~2p'
     1  root:x:0:0:root:/root:/bin/bash
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
     5  sync:x:4:65534:sync:/bin:/bin/sync
     7  man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
     9  mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
......
```

### a、i、c、d 行处理

-   a 新增行(之后) i 插入行(之前)
-   c 替代行 `sed '1,3 c =========='` 范围替换时整体替换，不是单行替换， 1-3 行都替换为 `==========`
-   d 删除行

```shell
$ nl passwd | sed '2a =========='
     1  root:x:0:0:root:/root:/bin/bash
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
==========
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
......

$ nl passwd | sed '2,3a =========='
     1  root:x:0:0:root:/root:/bin/bash
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
==========
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
==========
     4  sys:x:3:3:sys:/dev:/usr/sbin/nologin
......

$ nl passwd | sed '2i =========='
     1  root:x:0:0:root:/root:/bin/bash
==========
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
......


$ nl passwd | sed '1c =========='
==========
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
......


$ nl passwd | sed '1,3c =========='
==========
     4  sys:x:3:3:sys:/dev:/usr/sbin/nologin
     5  sync:x:4:65534:sync:/bin:/bin/sync
......

$ nl passwd | sed '1d'
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
......

$ nl passwd | sed '/root/d'
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
......
```

优化服务器配置，在 ssh 的配置 ssh_config 文件中加入相应的文本。

```
#   port123
#   permitrootlogin no
```

因为命令和文本使用空格分隔，如果在开头使用空格需要添加转义符。

```shell
$ sed '$a    port456 \n    permitrootlogin no' ssh_config
#   port123
#   permitrootlogin no
port456
    permitrootlogin n


$ sed '$a \    port456 \n    permitrootlogin no' ssh_config
#   port123
#   permitrootlogin no
    port456
    permitrootlogin no
```

删除文本中的空行。echo -e 表示启用解释反斜杠转义。

```shell
$ echo -e 'a\n\nb\n\nc' | sed '/^$/d'
a
b
c
```

### s 替换命令

```shell
$ sed 's/:/%/' passwd
root%x:0:0:root:/root:/bin/bash
daemon%x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin%x:2:2:bin:/bin:/usr/sbin/nologin
......

$ sed 's/:/%/g' passwd
root%x%0%0%root%/root%/bin/bash
daemon%x%1%1%daemon%/usr/sbin%/usr/sbin/nologin
bin%x%2%2%bin%/bin%/usr/sbin/nologin
......
```

### {} 多个 sed 命令，用 ; 分开

```shell
$ nl passwd | sed '{1,3d;s/:/%/g}'
     4  sys%x%3%3%sys%/dev%/usr/sbin/nologin
     5  sync%x%4%65534%sync%/bin%/bin/sync
     6  games%x%5%60%games%/usr/games%/usr/sbin/nologin
......

$ nl passwd | sed -n '{p;n}'
     1  root:x:0:0:root:/root:/bin/bash
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
     5  sync:x:4:65534:sync:/bin:/bin/sync
......
```

### n 读取下一个输入行（用下一个命令处理）

```shell
$ nl passwd | sed -n '{n;p}'
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
     4  sys:x:3:3:sys:/dev:/usr/sbin/nologin
     6  games:x:5:60:games:/usr/games:/usr/sbin/nologin
......


$ nl passwd | sed -n '{n;n;p}'
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
     6  games:x:5:60:games:/usr/games:/usr/sbin/nologin
     9  mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
......


$ nl passwd | sed -n '1~2p'
     1  root:x:0:0:root:/root:/bin/bash
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
     5  sync:x:4:65534:sync:/bin:/bin/sync
......
```

### & 替换固定字符串

```shell
$ sed 's/^[a-z_-]\+/&   /'  passwd
root   :x:0:0:root:/root:/bin/bash
daemon   :x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin   :x:2:2:bin:/bin:/usr/sbin/nologin
......
```

大小写转换 `\u\l\U\L`

```shell
$ sed 's/^[a-z_-]\+/\u&/'  passwd
Root:x:0:0:root:/root:/bin/bash
Daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
Bin:x:2:2:bin:/bin:/usr/sbin/nologin
......

$ sed 's/^[a-z_-]\+/\U&/'  passwd
ROOT:x:0:0:root:/root:/bin/bash
DAEMON:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
BIN:x:2:2:bin:/bin:/usr/sbin/nologin
......
```

将文件夹下的 .txt 文件名转换为大写

```shell
$ ls *.txt | sed 's/^\w\+/\U&/'
123.txt
ABC.txt
TEST.txt
```

### () 匹配组

获取 passwd 中 USER、UID 和 GID.

```shell
$ sed 's/\(^[a-z_-]\+\):x:\([0-9]\+\):\([0-9]\+\).*$/USER:\1    UID:\2    GID:\3/' passwd
USER:root    UID:0    GID:0
USER:daemon    UID:1    GID:1
USER:bin    UID:2    GID:2
USER:sys    UID:3    GID:3
USER:sync    UID:4    GID:65534
```

### rw 读写

r: 复制指定文件插入到匹配行，不改变文件内容。

w: 复制指定行拷贝到指定文件里，会改变目标文件内容。

```shell
$ echo -e '123\n456\n789' > 123.txt
$ echo -e 'abc\ndef\nghk' > abc.txt

$ sed '1r 123.txt' abc.txt
abc
123
456
789
def
ghk


$ sed '1w abc.txt' 123.txt
123
456
789

$ cat abc.txt
123
```

### q 退出 sed

```shell
$ nl passwd | sed '3q'
     1  root:x:0:0:root:/root:/bin/bash
     2  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
     3  bin:x:2:2:bin:/bin:/usr/sbin/nologin
```

## awk

文本与数据处理工具，与 sed 相比可以编程，处理灵活，功能强大。更侧重于复杂逻辑处理。

### awk 处理方式与格式

#### awk 处理方式

-   awk 一次处理一行内容。
-   awk 对每行可以切片处理。

`awk '{print $1}'` 输出首个单词。

#### awk 格式

-   命令行格式

    `awk [options] 'command' file(s)`

    基本格式: command: `pattern {awk 操作命令}`

    pattern: 正则表达式；逻辑判断式。

    awk 操作命令: 内置函数 print(), printf(), getline...; 控制指令：if(){} else{}, while() {}。

    扩展格式：command: `BEGIN {print "start"} pattern {awk 操作命令} END {print "end"}`

-   脚本格式

    `awk -f awk-script-file file(s)`

### awk 内置参数

-   awk 内置变量 1

    $0: 表示整个当前行

    $1: 每行第一个字段

    $2: 每行第二个字段

    ......

-   awk 内置参数：分隔符

    options: -F field-separator (默认为空格)

    例如：`awk -F ':' '{print $3}' /etc/passwd`

    ```shell
    $ echo 'babb:28:170' | awk -F ':' '{print $1,$2}'
    babb 28

    $ echo 'babb:28:170' | awk -F ':' '{print $1" "$2}'
    babb 28

    $ echo 'babb:28:170' | awk -F ':' '{print "name:" $1 "\t" "age:" $2}'
      name:babb       age:28
    ```

-   awk 内置变量 2

    NR: 每行的记录号

    NF: 字段数量的变量

    FILENAME: 正在处理的文件名

    例如： `awk -F ':' '{print FILENAME,NR,NF}' /etc/passwd`

    显示 /etc/passwd 每行的行号，每行的列数，对应的用户名（prrint, printf）

    ```shell
    $ awk -F ':' '{print "Line: "NR, "Col: "NF, "User: "$1}' passwd
    Line: 1 Col: 7 User: root
    Line: 2 Col: 7 User: daemon
    Line: 3 Col: 7 User: bin
    ......
    
    $ awk -F ':' '{printf("Line: %s Col: %s User: %s\n",NR,NF,$1)}' passwd
    Line: 1 Col: 7 User: root
    Line: 2 Col: 7 User: daemon
    Line: 3 Col: 7 User: bin
    ......
    
    $ awk -F ':' '{printf("Line: %3s Col: %s User: %s\n",NR,NF,$1)}' passwd
    Line: 1 Col: 7 User: root
    Line: 2 Col: 7 User: daemon
    Line: 3 Col: 7 User: bin
    ......
    Line: 9 Col: 7 User: mail
    Line: 10 Col: 7 User: news
    Line: 11 Col: 7 User: uucp
    ......
    ```

显示 /etc/passwd中用户ID大于100 的行号和用户名（if ... else ...）

````shell
$ awk -F ':' '{if ($3>100) print "Line: "NR, "User: "$1}' passwd
Line: 18 User: nobody
Line: 20 User: syslog
Line: 21 User: messagebus
......
````

在服务器 log 中找出 'Error' 的发生日期

```shell
$ sed -n '/Error/p' fresh.log | awk '{print $1}'
2016-11-01T10:39:04.09558300+08:00
2016-11-02T10:39:04.09558300+08:00
2016-11-03T08:39:04.09558300+08:00

$ awk '/Error/{print $1}' fresh.log
2016-11-01T10:39:04.09558300+08:00
2016-11-02T10:39:04.09558300+08:00
2016-11-03T08:39:04.09558300+08:00
```

### awk 逻辑判断式

`~, !~` : 匹配正则表达式。

```shell
$ awk -F ':' '$1~/^m.*/{print $1}' passwd
man
mail
messagebus
myths

$ awk -F ':' '$1!~/^m.*/{print $1}' passwd
root
daemon
bin
sys
......
```

`==, !=, <, >`: 判断逻辑表达式。

```shell
$ awk -F ':' '$3>100 {print $1}' passwd
nobody
syslog
messagebus
usbmux
```

### awk 扩展格式

扩展格式：command: `BEGIN {print "start"} pattern {awk 操作命令} END {print "end"}` 可以在整个循环开始和结尾做一些操作。

制表显示 /etc/passwd 每行的行号，每行的列数，对应的用户名。

```shell
$ awk -F ':' 'BEGIN {print "Line\tCol\t User"}{print NR"\t"NF"\t"$1}END{print "----------"FILENAME"----------"}' passwd
Line    Col      User
1       7       root
2       7       daemon
3       7       bin
4       7       sys
5       7       sync
......
----------passwd----------
```

统计当前文件夹下的文件/文件夹占用的大小。

```shell
$ ls -l
total 12
-rw-r--r-- 1 11435 1049089   24  3月 14 16:00 123.txt
-rw-r--r-- 1 11435 1049089   22  3月 14 16:04 abc.txt
-rw-r--r-- 1 11435 1049089  531  3月 14 17:21 fresh.log
-rw-r--r-- 1 11435 1049089 2463  3月 11 14:02 index.html
-rw-r--r-- 1 11435 1049089 2202  3月 14 16:55 passwd
-rw-r--r-- 1 11435 1049089  127  3月 14 15:57 ssh_config


$ ls -l | awk 'BEGIN{size=0}{size+=$5}END{print " size is " size}'
 size is 5369
```

统计显示 /etc/passwd 的账户总人数。

```shell
$ awk -F ':' 'BEGIN{count=0}$1!~/^$/{count++}END{print " count = " count}' passwd
 count = 17
```

统计显示 UID 大于 10 的用户名。

```shell
$ awk -F ':' 'BEGIN{count=0}{if ($3>10) name[count++]=$1}END{for (i=0;i<count;i++) print i, name[i]}' passwd
0 proxy
1 www-data
2 backup
3 list
4 irc
5 gnats
```

统计 netstat -anp 状态下为 LISTEN 和 CONNECTED 的连接数量。

! 需要在 Linux 下测试

```shell
$ netstat -anp | awk '$6~/CONNECTED|LISTEN/{sum[$6]++}END{for(i in sum) print i, sum[i]}'
```

### etc/passwd 文件样例

用户名:口令:用户标识号:组标识号:注释性描述:主目录:登录 Shell

```shell
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System
```

### fresh.log 文件样例

```
2016-10-31T10:39:04.09558300+08:00 Fresh token in 7199 seconds later...
2016-10-31T12:39:04.09558300+08:00 Fresh token in 7199 seconds later...
2016-11-01T10:39:04.09558300+08:00 Fresh token in 7199 seconds later...
2016-11-01T10:39:04.09558300+08:00 Error in genToken()
2016-11-01T12:39:04.09558300+08:00 Fresh token in 7199 seconds later...
2016-11-01T20:39:04.09558300+08:00 Fresh token in 7199 seconds later...
2016-11-02T10:39:04.09558300+08:00 Error in genToken()
2016-11-03T08:39:04.09558300+08:00 Error in genToken()
```

## 应用

### 查找不包含 TEST 的文件夹

-v, --invert-match: select non-matching lines

```shell
$ ls | grep -v '.*\?TEST.*\?'

$ ls | awk '!/TEST/'
```

### 批量替换文件名

| src                     | dest          |
| ----------------------- | ------------- |
| AAA-o60807012@76027.xml | o60807012.out |
| BBB-o60466251@75842.xml | o60466251.out |

```shell
$ ls *.xml | sed 's/.*\?-\(.*\?\)@.*\?/mv & \1.out/'
mv AAA-o60807012@76027.xml o60807012.out
mv BBB-o60466251@75842.xml o60466251.out

# 需要添加 sh 才会执行 shell 命令
$ ls *.xml | sed 's/.*\?-\(.*\?\)@.*\?/mv & \1.out/' | sh
```
