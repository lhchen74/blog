---
title: shell
tags: shell
---

### shell 能做什么

将一些复杂的命令简单化(平时我们提交一次 github 代码可能需要很多步骤，但是可以用 shell 简化成一步)
可以写一些脚本自动实现一个工程中自动更换最新的sdk(库)
自动打包、编译、发布等功能
清理磁盘中空文件夹
总之一切有规律的活脚本都可以尝试一下

### shell 不能做什么

需要精密的运算的时候
需要语言效率很高的时候
需要一些网络操作的时候
总之 shell 就是可以快速开发一个脚本简化开发流程，并不可以用来替代高级语言

### shell 的工作原理

shell 可以被称作是脚本语言，因为它本身是不需要编译的，而是通过解释器解释之后再编译执行，和传统语言相比多了解释的过程所以效率会略差于传统的直接编译的语言。

### 变量

```bash
#变量'='前后不能有空格
myText="hello world"
muNum=100
echo $myText
echo muNum
```

### 四则运算

```bash
# shell的乘法(*)有时需要转义
echo "Hello World !"
a=3
b=5
val=`expr $a + $b`
echo "Total value : $val"

val=`expr $a - $b`
echo "Total value : $val"

val=`expr $a \* $b`
echo "Total value : $val"

val=`expr $a / $b`
echo "Total value : $val"
```

### 关系运算符

| 运算符 | 含义                         |
| ------ | ---------------------------- |
| -eq    | 两个数相等返回true           |
| -ne    | 两个数不相等返回true         |
| -gt    | 左侧数大于右侧数返回true     |
| -lt    | 左侧数小于右侧数返回true     |
| -ge    | 左侧数大于等于右侧数返回true |
| -le    | 左侧数小于等于右侧数返回true |

```bash
#!/bin/sh
a=10
b=20
if [ $a -eq $b ]
then
   echo "true"
else
   echo "false"
fi

if [ $a -ne $b ]
then
   echo "true"
else
   echo "false"
fi
```

### 字符串运算符

| 运算符  | 含义                                                   |
| ------- | ------------------------------------------------------ |
| =       | 两个字符串相等返回true                                 |
| !=      | 两个字符串不相等返回true                               |
| -z      | 字符串长度为0返回true                                  |
| -n      | 字符串长度不为0返回true                                |
| -d file | 检测文件是否是目录，如果是，则返回 true                |
| -r file | 检测文件是否可读，如果是，则返回 true                  |
| -w file | 检测文件是否可写，如果是，则返回 true                  |
| -x file | 检测文件是否可执行，如果是，则返回 true                |
| -s file | 检测文件是否为空（文件大小是否大于0，不为空返回 true） |
| -e file | 检测文件（包括目录）是否存在，如果是，则返回 true      |

### 字符串

```bash
#!/bin/sh
mtext="hello"  #定义字符串
mtext2="world"
mtext3=$mtext" "$mtext2  #字符串的拼接
echo $mtext3  #输出字符串
echo ${#mtext3}  #输出字符串长度
echo ${mtext3:1:4}  #截取字符串
```

### 数组

```bash
#!/bin/sh
array=(1 2 3 4 5)  #定义数组
array2=(aa bb cc dd ee)  #定义数组
value=${array[3]}  #找到某一个下标的数，然后赋值
echo $value  #打印
value2=${array2[3]}  #找到某一个下标的数，然后赋值
echo $value2  #打印
length=${#array[*]}  #获取数组长度
echo $length
```

### 输出程序

```bash
#!/bin/sh
echo "hello world"  
echo hello world  

text="hello world"
echo $text

echo -e "hello \nworld"  #输出并且换行

echo "hello world" > a.txt  #重定向到文件

echo `date`  #输出当前系统时间

###printf同c语言
```

### 判断语句

```bash
if [ $a == $b ]
then
   echo "a is equal to b"
elif [ $a -gt $b ]
then
   echo "a is greater than b"
elif [ $a -lt $b ]
then
   echo "a is less than b"
else
   echo "None of the condition met"
fi
```

### test命令

```bash
test $[num1] -eq $[num2]  #判断两个变量是否相等
test num1=num2  #判断两个数字是否相等
```

### 循环

```bash
#!/bin/sh
#for循环
for i in {1..5}
do
    echo $i
done

for i in 5 6 7 8 9
do
    echo $i
done

for FILE in $HOME/.bash*
do
   echo $FILE
done
#while循环
#!/bin/sh
###普通while循环
COUNTER=0
while [ $COUNTER -lt 5 ]
do
    COUNTER=`expr $COUNTER + 1`
    echo $COUNTER
done
###获取键盘数据，然后把用户输入的文字输出出来。
echo '请输入。。。'
echo 'ctrl + d 即可停止该程序'
while read FILM
do
    echo "Yeah! great film the $FILM"
done

#跳出循环
break     #跳出所有循环
break n   #跳出第n层f循环
continue  #跳出当前循环
```

### 函数

```bash
#无返回值
sysout(){
    echo "hello world"
}
sysout

#有返回值
test(){
    aNum=3
    anotherNum=5
    return $(($aNum+$anotherNum))
}
test
result=$?
echo $result

#多个参数
test(){
    echo $1  #接收第一个参数
    echo $2  #接收第二个参数
    echo $3  #接收第三个参数
    echo $#  #接收到参数的个数
    echo $*  #接收到的所有参数
}
test aa bb cc
```

### 重定向

```bash
#将结果写入文件，结果不会在控制台展示，而是在文件中，覆盖写
$echo result > file 
#将结果写入文件，结果不会在控制台展示，而是在文件中，追加写
$echo result >> file  
#获取输入流
echo input < file  
```

### 自动提交github仓库的脚本

```bash
#test.sh
#!/bin/bash
echo "-------Begin-------"
git add .
git commit -m $1
echo $1
git push origin master
echo "--------End--------"
#test.sh  'first commit'
```

> 作者：关玮琳linSir
> 链接：<https://www.jianshu.com/p/71cb62f08768>
> 來源：简书
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。