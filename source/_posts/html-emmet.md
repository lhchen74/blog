---
title: HTML Emmet
tags: html
date: 2019-10-28
---

> 转载: [前端 html、CSS 快速编写代码插件-Emmet 使用方法技巧详解 - 恩恩先生 - 博客园](https://www.cnblogs.com/engeng/articles/5955167.html)

Emmet 的前身是大名鼎鼎的 Zen coding，如果你从事 Web 前端开发的话，对该插件一定不会陌生。它使用仿 CSS 选择器的语法来生成代码，大大提高了 HTML/CSS 代码编写的速度，而且作为一款插件能够大部分的代码编辑器，文章后面列出了支持的代码编辑器类型。请看下面演示：

## 快速编写 HTML 代码

### 初始化

HTML 文档需要包含一些固定的标签，比如`<html>、<head>、<body>`等，现在你只需要 1 秒钟就可以输入这些标签。比如输入 "!" 或 "html:5"，然后按 Tab 键:

-   html:5 或 !: 用于 HTML5 文档类型
-   html:xt: 用于 XHTML 过渡文档类型
-   html:4s: 用于 HTML4 严格文档类型

### id、class、自定义属性和文本

连续输入元素名称和 id，Emmet 会自动为你补全，连续输入 class 和 id，比如 `p.bar#foo`，会自动生成：

```html
<p class="bar" id="foo"></p>
```

下面来看看如何定义 HTML 元素的内容和属性。你可以通过输入 `h1{foo}` 和 `a[href=#]`，就可以自动生成如下代码：

```html
<h1>foo</h1>
<a href="#"></a>
```

### 嵌套

现在你只需要 1 行代码就可以实现标签的嵌套。

-   \>：子元素符号，表示嵌套的元素
-   +：同级标签符号
-   ^：可以使该符号前的标签提升一行

连续输入 `div+div>p>span+em^bq` 会自动生成：

```html
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```

### 分组

你可以通过嵌套和括号来快速生成一些代码块，比如输入(.foo>h1)+(.bar>h2)，会自动生成如下代码：

```html
<div class="foo">
    <h1></h1>
</div>
<div class="bar">
    <h2></h2>
</div>
```

### 隐式标签

声明一个带类的标签，只需输入 div.item，就会生成 `<div class="item"></div>`。在过去版本中，可以省略掉 div，即输入 .item 即可生成`<div class="item"></div>`。现在如果只输入 .item，则 Emmet 会根据父标签进行判定。比如在`<ul>`中输入.item，就会生成`<li class="item"></li>`。

下面是所有的隐式标签名称：

-   li：用于 ul 和 ol 中
-   tr：用于 table、tbody、thead 和 tfoot 中
-   td：用于 tr 中
-   option：用于 select 和 optgroup 中

### 定义多个元素

要定义多个元素，可以使用`*`符号。比如，`ul>li*3` 可以生成如下代码：

```html
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

### 定义多个带属性的元素

如果输入 `ul>li.item$*3`，将会生成如下代码：

```html
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
</ul>
```

## CSS 缩写

### 值

比如要定义元素的宽度，只需输入 w100，即可生成

```css
width: 100px;
```

除了 px，也可以生成其他单位，比如输入 h10p+m5e，结果如下：

```css
height: 10%;
margin: 5em;
```

单位别名列表：

-   p 表示%
-   e 表示 em
-   x 表示 ex

### 附加属性

可能你之前已经了解了一些缩写，比如 @f，可以生成：

```css
@font-face {
    font-family: ;
    src: url();
}
```

一些其他的属性，比如 background-image、border-radius、font、@font-face、text-outline、text-shadow 等额外的选项，可以通过"+"符号来生成，比如输入@f+，将生成：

```css
@font-face {
    font-family: "FontName";
    src: url("FileName.eot");
    src: url("FileName.eot?#iefix") format("embedded-opentype"), url("FileName.woff")
            format("woff"), url("FileName.ttf") format("truetype"), url("FileName.svg#FontName")
            format("svg");
    font-style: normal;
    font-weight: normal;
}
```

### 模糊匹配

如果有些缩写你拿不准，Emmet 会根据你的输入内容匹配最接近的语法，比如输入 ov:h、ov-h、ovh 和 oh，生成的代码是相同的：

```css
overflow: hidden;
```

### 供应商前缀

如果输入非 W3C 标准的 CSS 属性，Emmet 会自动加上供应商前缀，比如输入 trs，则会生成：

```css
-webkit-transform: ;
-moz-transform: ;
-ms-transform: ;
-o-transform: ;
transform: ;
```

你也可以在任意属性前加上"-"符号，也可以为该属性加上前缀。比如输入-super-foo：

```css
-webkit-super-foo: ;
-moz-super-foo: ;
-ms-super-foo: ;
-o-super-foo: ;
super-foo: ;
```

如果不希望加上所有前缀，可以使用缩写来指定，比如 -wm-trf 表示只加上 -webkit 和 -moz 前缀：

```css
-webkit-transform: ;
-moz-transform: ;
transform: ;
```

前缀缩写如下：

-   w 表示 -webkit-
-   m 表示 -moz-
-   s 表示 -ms-
-   o 表示 -o-

### 渐变

输入 lg(left, #fff 50%, #000)，会生成如下代码：

```css
background-image: -webkit-gradient(
    linear,
    0 0,
    100% 0,
    color-stop(0.5, #fff),
    to(#000)
);
background-image: -webkit-linear-gradient(left, #fff 50%, #000);
background-image: -moz-linear-gradient(left, #fff 50%, #000);
background-image: -o-linear-gradient(left, #fff 50%, #000);
background-image: linear-gradient(left, #fff 50%, #000);
```

## 附加功能

### Lorem ipsum 文本

Lorem ipsum 指一篇常用于排版设计领域的拉丁文文章，主要目的是测试文章或文字在不同字型、版型下看起来的效果。通过 Emmet，你只需输入 lorem 或 lipsum 即可生成这些文字。还可以指定文字的个数，比如 lorem10，将生成：

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero delectus.

## 定制

你还可以定制 Emmet 插件：

-   添加新缩写或更新现有缩写，可修改 snippets.json 文件
-   更改 Emmet 过滤器和操作的行为，可修改 preferences.json 文件
-   定义如何生成 HTML 或 XML 代码，可修改 syntaxProfiles.json 文件

## 语法及标签缩写方法

### 后代 >, 兄弟 +, 上级 ^

```html
<!-- nav>ul>li -->
<nav>
    <ul>
        <li></li>
    </ul>
</nav>

<!-- div+p+bq -->
<div></div>
<p></p>
<blockquote></blockquote>

<!-- div+div>p>span+em^bq -->
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>

<!-- div+div>p>span+em^^bq -->
<div></div>
<div>
    <p><span></span><em></em></p>
</div>
<blockquote></blockquote>
```

### 分组 ()

```html
<!-- div>(header>ul>li*2>a)+footer>p -->

<div>
    <header>
        <ul>
            <li><a href=""></a></li>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>

<!-- (div>dl>(dt+dd)*3)+footer>p -->
<div>
    <dl>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
        <dt></dt>
        <dd></dd>
    </dl>
</div>
<footer>
    <p></p>
</footer>
```

### 乘法 \*

```html
<!-- ul>li*5 -->
<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

### 自增符号 $

```html
<!-- ul>li.item$*5 -->
<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
</ul>

<!-- h$[title=item$]{Header $}*3 -->
<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>

<!-- ul>li.item$$$*5 -->
<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
    <li class="item004"></li>
    <li class="item005"></li>
</ul>

<!-- ul>li.item$@-*5 -->
<ul>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>

<!-- ul>li.item$@3*5 -->
<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>
```

### id 和 class 属性

```html
<!-- #header -->
<div id="header"></div>

<!-- .title -->
<div class="title"></div>

<!-- form#search.wide -->
<form id="search" class="wide"></form>

<!-- p.class1.class2.class3 -->
<p class="class1 class2 class3"></p>
```

### 自定义属性

```html
<!-- p[title="Hello world"] -->
<p title="Hello world"></p>

<!-- td[rowspan=2 colspan=3 title] -->
<td rowspan="2" colspan="3" title=""></td>

<!-- [a='value1' b="value2"] -->
<div a="value1" b="value2"></div>
```

### 文本 {}

```html
<!-- a{Click me} -->
<a href="">Click me</a>

<!-- p>{Click }+a{here}+{ to continue} -->
<p>Click <a href="">here</a> to continue</p>
```

### 隐式标签

```html
<!-- .class -->
<div class="class"></div>

<!-- em>.class -->
<em><span class="class"></span></em>

<!-- ul>.class -->
<ul>
    <li class="class"></li>
</ul>

<!-- table>.row>.col -->
<table>
    <tr class="row">
        <td class="col"></td>
    </tr>
</table>
```

### CSS

```css
body {
    /* df+w100p+h100vh+p10-20+m0-auto+fz12+bgc:pink+color:white */
    display: flex;
    width: 100%;
    height: 100vh;
    padding: 10px 20px;
    margin: 0 auto;
    font-size: 12px;
    background-color: pink;
    color: white;
}
```
