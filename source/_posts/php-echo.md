---
title: PHP：echo、print、print_r() 和 var_dump()
tags: php
date: 2019-11-06
---

> 转载: [PHP：echo、print、print_r() 和 var_dump() - Teraflopst - SegmentFault 思否](https://segmentfault.com/a/1190000005968434)

### echo 和 print

`echo` 和 `print` 都不是函数，而是 **语言结构**，所以圆括号都不是必需的。两者十分相似，功能几乎是完全一样。

1、echo 可以输出多个字符串，使用 `,` 连接

```php
echo 'a','b','c';
```

输出：abc

如果你非要加上圆括号，需要注意

```php
echo ('a','b','c');      //错误
echo ('a'),('b'),('c');  //正确
```

2、print 只能输出一个字符串

```php
print 'a','b','c';  //错误
print 'abc';        //正确
print 'a'.'b'.'c';  //正确
```

注意：上面的 `'a'.'b'.'c'` 并不是多个字符串，而是 PHP 中拼接（concat）多个字符串后的一个字符串。

3、echo 没有返回值，print 有返回值 1

因此 print 能用在表达式中：

```php
$ret = print 'abc';
echo $ret + 1;
```

输出：abc2

4、echo 输出的速度比 print 快

### print_r() 和 var_dump()

`print_r()` 显示关于一个变量的易于理解的信息。如果给出的是 string、integer 或 float，将打印变量值本身。如果给出的是 array，将会按照一定格式显示键和元素。object 与数组类似。

`print_r()` 会舍弃掉小数位末尾的 “0”；布尔值 true 输出 1，false 不输出；空字符串 和 null 不输出。如果给出的是 array，将会按照一定格式显示键和元素。object 与数组类似。

`var_dump()` 方法是判断一个变量的类型与长度，并输出变量的值和数据类型。`var_dump()` 输出比 `print_r()` 更详细，一般调试时用得多。两者区别如下：

```
$arr = array(5, 5.0, 'hello', '', true, false, null);
var_dump($arr);
print_r($arr);
```

输出：

```php
array(7) {
  [0]=>
  int(5)
  [1]=>
  float(5)
  [2]=>
  string(5) "hello"
  [3]=>
  string(0) ""
  [4]=>
  bool(true)
  [5]=>
  bool(false)
  [6]=>
  NULL
}
Array
(
    [0] => 5
    [1] => 5
    [2] => hello
    [3] =>
    [4] => 1
    [5] =>
    [6] =>
)
```

题外：如果想捕捉 `print_r()` 的输出，可添加一个 true 参数。此时 `print_r()` 将不打印结果，而是返回其输出。

```php
$str = "hello";
$result = print_r($str, true);
echo $result;
```
