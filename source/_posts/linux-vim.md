---
title: Vim
tags: linux
categories: manual
date: 2019-10-12
---

### normal (普通模式)

普通模式下可以进行各种命令操作和移动。

进入 vim 默认是 normal 模式（大部分情况是浏览而不是编辑）。使用 `Esc` 从 insert 模式回到 normal 模式

#### 光标移动

-   h 向左移动光标
-   j 向下移动光标
-   k 向上移动光标
-   l 向右移动光标

#### 单词移动

-   `w/W` 移动到下一个 word/WORD 开头, `e/E` 移动到下一个 word/WORD 结尾
-   `b/B` 回到上一个 word/WORD 开头（back word)
-   word 指以非空白字符分割的单词，WORD 以空白字符分割的单词

#### 行间搜索移动

同一行快速移动的方式是搜索一个字符并且移动到该字符

-   使用 `f{char}`可以移动到 char 字符上, `t`移动到 char 的前一个字符
-   使用`;或,`继续搜索该行`下一个或上一个`
-   大写的 `F` 表示反过来搜索前面的字符

#### 水平移动

快速移动到一行的行首或行尾

-   `0`移动到行首第一个字符, `^`移动到第一个非空白字符
-   `$`移动到行尾, `g_`移动到行尾非空白字符

#### 页面移动

-   `gg/G` 移动到文件开头和结尾，可以使用 `Ctrl + o`快速返回
-   `H/M/L`跳转到文件开头（Head），中间（Middle)和结尾（Lower)
-   `Ctrl + u、Ctrl + f` 上下翻页（upward/forward)
-   `zz` 把光标所在位置移动到屏幕中间

#### 快速删除

-   `x` 快速删除一个字符
-   `d`配合文本对象快速删除一个单词 `daw/dw`(delete around word)
-   `dd` 删除一行， `d0`删除到行首，`d$`删除到行尾，`dt;dt)`删除到 `;或者)`
-   d 和 x 可以搭配数字执行，表示重复执行， `4dd`删除 4 行，`4x`删除 4 个字符

#### 快速修改

-   `r` replace 替换一个字符, `R`连续向下替换
-   `s` substitute 删除当前字符并进入插入模式，`4s` 删除 4 个字符进入插入模式， `S` 整行删除进入插入模式
-   `c` change 配合文本对象修改，`cw`删除当前单词进入插入模式，`ct"`删除到`"`进入插入模式，`C` 整行删除进入插入模式

#### 查询

-   `/或者？`进行前向或者反向搜索(需要使用`enter` 退出搜索，才能使用 `n/N `跳转到下一个或者上一个匹配 )
-   `n/N`跳转到下一个或者上一个匹配。
-   `*/#`进行当前单词的前向和后向匹配。

#### 复制/剪切/黏贴

-   `d` cut
-   `y` copy
-   `P` paste before the cursor
-   `p` paste after the cursor

### insert (插入模式)

normal -> insert

| a   | append              |
| --- | ------------------- |
| i   | insert              |
| A   | append after line   |
| I   | insert before line  |
| o   | append a line below |
| O   | append a line above |

#### 删除操作

如下命令也可以在 Terminal 中使用

-   `Ctrl + h` 删除上一个字符
-   `Ctrl + w` 删除上一个单词
-   `Ctrl + u` 删除当前行

### command(命令模式)

| :wq/:x         | 写入并退出              |
| -------------- | ----------------------- |
| :vs            | vertical split 垂直分屏 |
| :sp            | split 水平分屏          |
| :set nu        | 设置行号                |
| :% s/foo/bar/g | 全局替换 foo -> bar     |

### visual(可视模式)

Visual 模式一般用来块状选择文本。

Normal 模式下使用 `v` 进入 visual 选择

使用 `V` 选择行

使用 `Ctrl + v`进行方块选择

### 快速切换 insert 和 normal 模式

使用 `Ctrl + c` 代替 `Esc`(但是会中断某些插件) 或者 `Ctrl + [`

`gi` 快速跳转到最后一次编辑的地方并进入插入模式

### Terminal

-   `Ctrl + h` 删除上一个字符
-   `Ctrl + w` 删除上一个单词
-   `Ctrl + u` 删除当前行
-   `Ctrl + a` 移动到行首
-   `Ctrl + e` 移动到行尾
-   `Ctrl + b` 向前移动一个字符
-   `Ctrl + f` 向后移动一个字符
