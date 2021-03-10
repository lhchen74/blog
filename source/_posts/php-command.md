---
title: php command
tags: php
date: 2019-10-25
---

1. PHP 运行指定文件 `php -f test.php (-f 可省略)`
2. 命令行直接运行 PHP 代码 `php -r "phpinfo();"`, 如果结果太长，还可以 `php -r "phpinfo();" | less` 分页展示
3. 交互模式运行 PHP, `php -a`, control + c/z 或者 exit 退出交互模式

```php
$ php -a
Interactive shell

php > echo 2 + 3
php > echo 2 + 3;
PHP Parse error:  syntax error, unexpected 'echo' (T_ECHO), expecting ',' or ';' in php shell code on line 2

Parse error: syntax error, unexpected 'echo' (T_ECHO), expecting ',' or ';' in php shell code on line 2
php > echo 2 + 3;
5
php > echo pow(2, 3)
php > ;
8
```

4. PHP 脚本作为 shell 脚本运行, 没有权限则切换到 root 用户 sudo su, `echo '#!/usr/bin/php\n<?php var_dump($argv); ?>' > phpscript`; 注意，我们在该 PHP 脚本的第一行使用 `#!/usr/bin/php`，就像在 shell 脚本中那样（/bin/bash）。第一行的#!/usr/bin/php 告诉 Linux 命令行用 PHP 解释器来解析该脚本文件。确定 phpscript 有可执行权限 `chmod u+x phpscript`

```php
./phpscript -h --foo

array(3) {
[0]=>
string(11) "./phpscript"
[1]=>
string(2) "-h"
[2]=>
string(5) "--foo"
}
```

5. 其他常用命令
   php -m 内置及 Zend 加载的模块
   php -i 等价于 phpinfo()
   php -i | grep php.ini 查看 php 配置文件加载路径
   php –ini 同上
   php -v 查看 php 版本
   php –re 查看是否安装相应的扩展 如 php –re gd
   php –help

**版权声明：本文为 CSDN 博主「野蛮秘籍」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。**
**原文链接：https://blog.csdn.net/fationyyk/article/details/70159416**
