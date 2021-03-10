---
title: php
tags: php
---

### global 关键字

global 关键字用于函数内访问全局变量，在函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字，
PHP 将所有全局变量存储在一个名为 `$GLOBALS[index]` 的数组中，index 保存变量的名称，这个数组可以在函数内部访问，也可以直接用来更新全局变量

```php
<?php
$x=5;
$y=10;

function myTest()
{
    global $x,$y;
    $y=$x+$y;
}

myTest();
echo $y; // 输出 15

// $GLOBALS
$x=5;
$y=10;

function myTest()
{
    $GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y'];
}

myTest();
echo $y;
?>
```

### include 和 require 语句

include 和 require 除了处理错误的方式不同之外，在其他方面都是相同的：

- require 生成一个致命错误（E_COMPILE_ERROR），在错误发生后脚本会停止执行。
- include 生成一个警告（E_WARNING），在错误发生后脚本会继续执行。

因此，如果您希望继续执行，并向用户输出结果，即使包含文件已丢失，那么请使用 include。否则，在框架、CMS 或者复杂的 PHP 应用程序编程中，请始终使用 require 向执行流引用关键文件。这有助于提高应用程序的安全性和完整性，在某个关键文件意外丢失的情况下。

### 常量

```php
<?php
// 区分大小写的常量名
define("GREETING", "欢迎访问 Runoob.com");
// 不区分大小写的常量名
// define("GREETING", "欢迎访问 Runoob.com", true);
echo GREETING;    // 输出 "欢迎访问 Runoob.com"
?>
```

define 定义的常量是全局的，命名空间无效。

### 关联数组

关联数组是使用您分配给数组的指定的键的数组，这里有两种创建关联数组的方法

```php
//1
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
//2
$age['Peter']="35";
$age['Ben']="37";
$age['Joe']="43";

foreach($age  as $x => $x_value)
{
    echo "key=".$x.",value=".$x_value;
    echo "<br>";
}
```

### 换行

```php
<?php

echo "aaa\n";
echo "bbb";

// $ php -f newline.php
// aaa
// bbb

// browser
// aaa bbb

// browser -> View page source
// aaa
// bbb

echo "ccc<br/>";
echo "ddd";

// $ php -f newline.php
// ccc<br/>ddd


// browser
// ccc
// ddd


// browser -> View page source
// ccc<br/>ddd


// p 标签在浏览器中会换两行，等同于两次 br 标签
echo '<p>' . 'eee' . '</p>';
echo '<p>' . 'fff' . '</p>';

// browser
// eee

// fff
```

### 单引号，双引号

```php
<?php
// 双引号解析变量, 单引号不解析变量（效率更高）
$name = "babb";
echo "$name";
echo "<br/>";
echo '$name';
// babb
// $name

// 单引号只转义 ' 和 \
$str = "1\n2\r3\t4\$5\\6\'";
echo $str;
echo '<br/>';
$str = '1\n2\r3\t4\$5\\6\'';
echo $str;

// 1 2 3 4$5\6\'
// 1\n2\r3\t4\$5\6'

```

### 花括号（brace）

```php
<?php

$name = "babb";

echo "$name";
echo '<br/>';
// Notice: Undefined variable: names in D:\study\php\str\brace.php on line 7
// echo "$names";
// echo '<br/>';
echo "${name}s";
echo '<br/>';
echo "{$name}s";
echo '<br/>';
echo "{ $name }s";

// babb
// babbs
// babbs
// { babb }s


// 字符串修改，也可以使用[]
$str = 'abcdef';
echo $str{0};
echo '<br/>';
$str{0} = 'A';
echo $str;
echo '<br/>';
echo $str[mt_rand(0, strlen($str) - 1)]; // 随机输出一个字符
// a
// Abcdef
// d
```

### 常用函数

date(format) 函数的第一个必需参数 _format_ 规定了如何格式化日期/时间。
常用的字符：

- d - 代表月中的天 (01 - 31)
- m - 代表月 (01 - 12)
- Y - 代表年 (四位数)

```php
<?php
echo date("Y/m/d") . "<br>";
echo date("Y.m.d") . "<br>";
echo date("Y-m-d");
?>
```

explode()函数：把字符串打散为数组

```php
<?php
  $str = 'hello,php,python';
  print_r (explode(",",$str));
 ?>
```

htmlspecialchars()函数： 把预定义的字符`> <` 等转换为 HTML 实体

chunk_split(string,length,end) 函数: chunk_split() 函数把字符串分割为一连串更小的部分。

```php
<?php
$str = "Hello world!";
echo chunk_split($str,6,"...");
// Hello ...world!...
?>
```

base64_encode ( string `$data` ) : string — 使用 MIME base64 对数据进行编码

```php
<?php
$str = 'This is an encoded string';
echo base64_encode($str);
?>
// VGhpcyBpcyBhbiBlbmNvZGVkIHN0cmluZw==
```

### $\$

PHP 中`$`表示一个变量的声明，`$a = 'test'`；表示变量 a 的值是 test。而`$$`表示指向一个变量值的变量。
`$$a = 'a'`; 首先取` $a` 变量的值为test，然后再将其值变成一个变量即表示为`$test='a'`;

```php
<?php
$value='test';
$$value='a';
echo $test;   # a
?>
```

### 多选下拉菜单

```php
<?php
$q = isset($_POST['q'])? $_POST['q'] : '';
if(is_array($q)) {
    $sites = array(
            'RUNOOB' => '菜鸟教程: http://www.runoob.com',
            'GOOGLE' => 'Google 搜索: http://www.google.com',
            'TAOBAO' => '淘宝: http://www.taobao.com',
    );
    foreach($q as $val) {
        // PHP_EOL 为常量，用于换行
        echo $sites[$val] . PHP_EOL;
    }

} else {
?>
<form action="" method="post">
    <select multiple="multiple" name="q[]">
    <option value="">选择一个站点:</option>
    <option value="RUNOOB">Runoob</option>
    <option value="GOOGLE">Google</option>
    <option value="TAOBAO">Taobao</option>
    </select>
    <input type="submit" value="提交">
    </form>
<?php
}
?>
```

### PHP7 新特性

```php
// NULL 合并运算符
<?php
// 获取 $_GET['site'] 的值，如果不存在返回 '菜鸟教程'
$site = $_GET['site'] ?? '菜鸟教程';
print($site);
print(PHP_EOL); // PHP_EOL 为换行符


// 以上代码等价于
$site = isset($_GET['site']) ? $_GET['site'] : '菜鸟教程';
print($site);
print(PHP_EOL);

$site = $_GET['site'] ?? $_POST['site'] ?? '菜鸟教程';

print($site);
?>


// 太空船运算符
// 用于比较两个表达式 $a 和 $b，如果 $a 小于、等于或大于 $b时，它分别返回-1、0或1。
<?php
print( 1 <=> 1);print(PHP_EOL);
?>

// 使用 define 函数来定义常量数组
<?php
define('sites', [
   'Google',
   'Runoob',
   'Taobao'
]);

print(sites[1]);
?>
```
