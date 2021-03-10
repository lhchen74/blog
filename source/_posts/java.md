---
title: java
tags: java
date: 2019-10-19
---

### 数据类型

boolean 只有 true, false; null, 0 不能表示 false

### 基本数据类型转换

byte, short, char 之间不会相互转换，它们在计算时会首先转换为 int 类型.

```java
short s = 2;
// 变量参与运算时,java 程序不知道具体设个变量在做完运算后会不会超出当前变量范围
// 所以先把变量转化为一个更大的长度,short 短整型数据会默认转换为 int 整型数据
// s = s + 3; // error
short s = (short)(s + 3) 
s1 += 3 // 在使用扩展运算符时, 变量在参与运算时会把结果自动强制转换为当前变量类型
int s2 = s + 3
```



boolean 类型不可以转换为其它数据类型

### 数据运算

char 类型数据可以做数学运算,在做数学运算的时候把字符转换为 ASCII 码进行计算

 字符串与其它数据类型相加时,实际上时把其它数据转换为字符串,做字符串的拼接

```java
// char 类型数据可以做数学运算,在做数学运算的时候把字符转换为 ASCII 码进行计算
System.out.println('*' + '\t' + '*') // 93
// 字符串与其它数据类型相加时,实际上时把其它数据转换为字符串,做字符串的拼接
System.out.println("*" + '\t' + '*') // *	*
```

逻辑运算符

`& `逻辑与, `| `逻辑或 , `!`逻辑非, `^`逻辑异或

`&&`短路与, `||`短路或

|   a   |   b   |  a&b  | a\|b  |  !a   |  a^b  | a&&b  | a\|\|b |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :----: |
| true  | true  | true  | true  | false | false | true  |  true  |
| true  | false | false | true  | false | true  | false |  true  |
| false | true  | false | true  | true  | true  | false |  true  |
| false | false | false | false | true  | false | false | false  |

位运算

`& | ^` 也可以参与位运算

|  a   |  b   | a&b  | a\|b | a^b  |
| :--: | :--: | :--: | :--: | :--: |
|  1   |  1   |  1   |  1   |  0   |
|  1   |  0   |  0   |  1   |  1   |
|  0   |  1   |  0   |  1   |  1   |
|  0   |  0   |  0   |  0   |  0   |

```
-15 : 11111111 11111111 11111111 11110001 &
 15 : 00000000 00000000 00000000 00001111
  1 : 00000000 00000000 00000000 00000001
  
-15 : 11111111 11111111 11111111 11110001 |
 15 : 00000000 00000000 00000000 00001111
 -1 : 11111111 11111111 11111111 11111111
      10000000 00000000	00000000 00000000     // 1 最高位符号位, 其余按位取反
      10000000 00000000 00000000 00000001     // 加 1
```

`<< >> >>> ` 有符号左移, 有符号右移, 无符号右移

- `<<`左移 空位补0, 被移除的高位丢弃, 空缺位补 0
- `>>`被移位的二进制最高位是 0, 右移后,空缺位补 0; 最高位是 1, 空缺位补 1
- `>>>` 被移位二进制最高位无论是 0 或者是 1, 空缺位都补 0

负数二进制

15 二进制 `00000000 00000000 00000000 00001111`

反码(按位取反) `11111111 1111111 1111111 11110000`

补码(加1) `11111111 1111111 1111111 11110001`

-15 二进制 `11111111 11111111 11111111 11110001`

```java
System.out.println(0b11111111111111111111111111110001); // -15
// 11111111111111111111111111110001
// 10000000000000000000000000001110  // 1 最高位符号位, 其余按位取反
// 10000000000000000000000000001111  // 加 1 -15
```
