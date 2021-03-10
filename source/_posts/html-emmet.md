---
title: html emmet
tags: html
date: 2019-10-28
---

> 转载: [前端html、CSS快速编写代码插件-Emmet使用方法技巧详解 - 恩恩先生 - 博客园](https://www.cnblogs.com/engeng/articles/5955167.html)

Emmet 的前身是大名鼎鼎的 Zen coding，如果你从事 Web 前端开发的话，对该插件一定不会陌生。它使用仿 CSS 选择器的语法来生成代码，大大提高了 HTML/CSS 代码编写的速度，而且作为一款插件能够大部分的代码编辑器，文章后面列出了支持的代码编辑器类型。请看下面演示：

### 快速编写 HTML 代码

**1. 初始化**

HTML 文档需要包含一些固定的标签，比如<html>、<head>、<body>等，现在你只需要 1 秒钟就可以输入这些标签。比如输入“!”或“html:5”，然后按 Tab 键：

- html:5 或!：用于 HTML5 文档类型
- html:xt：用于 XHTML 过渡文档类型
- html:4s：用于 HTML4 严格文档类型

**2. 轻松添加类、id、文本和属性**

连续输入元素名称和 ID，Emmet 会自动为你补全，比如输入 p#foo：

连续输入类和 id，比如 p.bar#foo，会自动生成：

```html
<p class="bar" id="foo"></p>
```

下面来看看如何定义 HTML 元素的内容和属性。你可以通过输入 h1{foo}和 a[href=#]，就可以自动生成如下代码：

```html
<h1>foo</h1>
<a href="#"></a>
```

**3. 嵌套**

现在你只需要 1 行代码就可以实现标签的嵌套。

- \>：子元素符号，表示嵌套的元素
- +：同级标签符号
- ^：可以使该符号前的标签提升一行

**4. 分组**

你可以通过嵌套和括号来快速生成一些代码块，比如输入(.foo>h1)+(.bar>h2)，会自动生成如下代码：

```html
<div class="foo">
  <h1></h1>
</div>
<div class="bar">
  <h2></h2>
</div>
```

**5. 隐式标签**

声明一个带类的标签，只需输入 div.item，就会生成 `<div class="item"></div>`。

在过去版本中，可以省略掉 div，即输入.item 即可生成`<div class="item"></div>`。现在如果只输入.item，则 Emmet 会根据父标签进行判定。比如在`<ul>`中输入.item，就会生成`<li class="item"></li>`。

下面是所有的隐式标签名称：

- li：用于 ul 和 ol 中
- tr：用于 table、tbody、thead 和 tfoot 中
- td：用于 tr 中
- option：用于 select 和 optgroup 中

**6. 定义多个元素**

要定义多个元素，可以使用*符号。比如，ul>li*3 可以生成如下代码：

```html
<ul>
  <li></li>
  <li></li>
  <li></li>
</ul>
```

**7. 定义多个带属性的元素**

如果输入 ul>li.item\$\*3，将会生成如下代码：

```html
<ul>
  <li class="item1"></li>
  <li class="item2"></li>
  <li class="item3"></li>
</ul>
```

### CSS 缩写

**1. 值**

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

- p 表示%
- e 表示 em
- x 表示 ex

**2. 附加属性**

可能你之前已经了解了一些缩写，比如 @f，可以生成：

```css
@font-face {
  font-family: ;
  src: url();
}
```

一些其他的属性，比如 background-image、border-radius、font、@font-face,text-outline、text-shadow 等额外的选项，可以通过“+”符号来生成，比如输入@f+，将生成：

```css
@font-face {
  font-family: 'FontName';
  src: url('FileName.eot');
  src: url('FileName.eot?#iefix') format('embedded-opentype'), ​
      url('FileName.woff') format('woff'),
    ​ url('FileName.ttf') format('truetype'), ​ url('FileName.svg#FontName')
      format('svg');
  font-style: normal;
  font-weight: normal;
}
```

**3. 模糊匹配**

如果有些缩写你拿不准，Emmet 会根据你的输入内容匹配最接近的语法，比如输入 ov:h、ov-h、ovh 和 oh，生成的代码是相同的：

```css
overflow: hidden;
```

**4. 供应商前缀**

如果输入非 W3C 标准的 CSS 属性，Emmet 会自动加上供应商前缀，比如输入 trs，则会生成：

```css
-webkit-transform: ;
-moz-transform: ;
-ms-transform: ;
-o-transform: ;
transform: ;
```

你也可以在任意属性前加上“-”符号，也可以为该属性加上前缀。比如输入-super-foo：

```css
-webkit-super-foo: ;
-moz-super-foo: ;
-ms-super-foo: ;
-o-super-foo: ;
super-foo: ;
```

如果不希望加上所有前缀，可以使用缩写来指定，比如-wm-trf 表示只加上-webkit 和-moz 前缀：

```css
-webkit-transform: ;
-moz-transform: ;
transform: ;
```

前缀缩写如下：

- w 表示 -webkit-
- m 表示 -moz-
- s 表示 -ms-
- o 表示 -o-

**5. 渐变**

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

### 附加功能

**生成 Lorem ipsum 文本**

Lorem ipsum 指一篇常用于排版设计领域的拉丁文文章，主要目的是测试文章或文字在不同字型、版型下看起来的效果。通过 Emmet，你只需输入 lorem 或 lipsum 即可生成这些文字。还可以指定文字的个数，比如 lorem10，将生成：

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero delectus.

### 定制

你还可以定制 Emmet 插件：

- 添加新缩写或更新现有缩写，可修改 snippets.json 文件
- 更改 Emmet 过滤器和操作的行为，可修改 preferences.json 文件
- 定义如何生成 HTML 或 XML 代码，可修改 syntaxProfiles.json 文件

### 语法及标签缩写方法

```html
语法及标签缩写方法如下：

后代：>
缩写：nav>ul>li

<nav>
    <ul>
        <li></li>
    </ul>
</nav>
兄弟：+
缩写：div+p+bq

<div></div>
<p></p>
<blockquote></blockquote>
上级：^
缩写：div+div>p>span+em^bq

<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
缩写：div+div>p>span+em^^bq

<div></div>
<div>
    <p><span></span><em></em></p>
</div>
<blockquote></blockquote>
分组：()
缩写：div>(header>ul>li*2>a)+footer>p

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
缩写：(div>dl>(dt+dd)*3)+footer>p

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
乘法：*
缩写：ul>li*5

<ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
</ul>
自增符号：$
缩写：ul>li.item$*5

<ul>
    <li class="item1"></li>
    <li class="item2"></li>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
</ul>
缩写：h$[title=item$]{Header $}*3

<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>
缩写：ul>li.item$$$*5

<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
    <li class="item004"></li>
    <li class="item005"></li>
</ul>
缩写：ul>li.item$@-*5

<ul>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>
缩写：ul>li.item$@3*5

<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>
ID和类属性
缩写：#header

<div id="header"></div>
缩写：.title

<div class="title"></div>
缩写：form#search.wide

<form id="search" class="wide"></form>
缩写：p.class1.class2.class3

<p class="class1 class2 class3"></p>
自定义属性
缩写：p[title="Hello world"]

<p title="Hello world"></p>
缩写：td[rowspan=2 colspan=3 title]

<td rowspan="2" colspan="3" title=""></td>
缩写：[a='value1' b="value2"]

<div a="value1" b="value2"></div>
文本：{}
缩写：a{Click me}

<a href="">Click me</a>
缩写：p>{Click }+a{here}+{ to continue}

<p>Click <a href="">here</a> to continue</p>
隐式标签
缩写：.class

<div class="class"></div>
缩写：em>.class

<em><span class="class"></span></em>
缩写：ul>.class

<ul>
    <li class="class"></li>
</ul>
缩写：table>.row>.col

<table>
    <tr class="row">
        <td class="col"></td>
    </tr>
</table>
HTML
所有未知的缩写都会转换成标签，例如，foo → <foo></foo>

缩写：!

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

</body>
</html>
缩写：a

<a href=""></a>
缩写：a:link

<a href="http://"></a>
缩写：a:mail

<a href="mailto:"></a>
缩写：abbr

<abbr title=""></abbr>
缩写：acronym

<acronym title=""></acronym>
缩写：base

<base href="" />
缩写：basefont

<basefont />
缩写：br

<br />
缩写：frame

<frame />
缩写：hr

<hr />
缩写：bdo

<bdo dir=""></bdo>
缩写：bdo:r

<bdo dir="rtl"></bdo>
缩写：bdo:l

<bdo dir="ltr"></bdo>
缩写：col

<col />
缩写：link

<link rel="stylesheet" href="" />
缩写：link:css

<link rel="stylesheet" href="style.css" />
缩写：link:print

<link rel="stylesheet" href="print.css" media="print" />
缩写：link:favicon

<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />
缩写：link:touch

<link rel="apple-touch-icon" href="favicon.png" />
缩写：link:rss

<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml" />
缩写：link:atom

<link rel="alternate" type="application/atom+xml" title="Atom" href="atom.xml" />
缩写：meta

<meta />
缩写：meta:utf

<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
缩写：meta:win

<meta http-equiv="Content-Type" content="text/html;charset=windows-1251" />
缩写：meta:vp

<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0" />
缩写：meta:compat

<meta http-equiv="X-UA-Compatible" content="IE=7" />
缩写：style

<style></style>
缩写：script

<script></script>
缩写：script:src

<script src=""></script>
缩写：img

<img src="" alt="" />
缩写：iframe

<iframe src="" frameborder="0"></iframe>
缩写：embed

<embed src="" type="" />
缩写：object

<object data="" type=""></object>
缩写：param

<param name="" value="" />
缩写：map

<map name=""></map>
缩写：area

<area shape="" coords="" href="" alt="" />
缩写：area:d

<area shape="default" href="" alt="" />
缩写：area:c

<area shape="circle" coords="" href="" alt="" />
缩写：area:r

<area shape="rect" coords="" href="" alt="" />
缩写：area:p

<area shape="poly" coords="" href="" alt="" />
缩写：form

<form action=""></form>
缩写：form:get

<form action="" method="get"></form>
缩写：form:post

<form action="" method="post"></form>
缩写：label

<label for=""></label>
缩写：input

<input type="text" />
缩写：inp

<input type="text" name="" id="" />
缩写：input:hidden

别名：input[type=hidden name]

<input type="hidden" name="" />
缩写：input:h

别名：input:hidden

<input type="hidden" name="" />
缩写：input:text, input:t

别名：inp

<input type="text" name="" id="" />
缩写：input:search

别名：inp[type=search]

<input type="search" name="" id="" />
缩写：input:email

别名：inp[type=email]

<input type="email" name="" id="" />
缩写：input:url

别名：inp[type=url]

<input type="url" name="" id="" />
缩写：input:password

别名：inp[type=password]

<input type="password" name="" id="" />
缩写：input:p

别名：input:password

<input type="password" name="" id="" />
缩写：input:datetime

别名：inp[type=datetime]

<input type="datetime" name="" id="" />
缩写：input:date

别名：inp[type=date]

<input type="date" name="" id="" />
缩写：input:datetime-local

别名：inp[type=datetime-local]

<input type="datetime-local" name="" id="" />
缩写：input:month

别名：inp[type=month]

<input type="month" name="" id="" />
缩写：input:week

别名：inp[type=week]

<input type="week" name="" id="" />
缩写：input:time

别名：inp[type=time]

<input type="time" name="" id="" />
缩写：input:number

别名：inp[type=number]

<input type="number" name="" id="" />
缩写：input:color

别名：inp[type=color]

<input type="color" name="" id="" />
缩写：input:checkbox

别名：inp[type=checkbox]

<input type="checkbox" name="" id="" />
缩写：input:c

别名：input:checkbox

<input type="checkbox" name="" id="" />
缩写：input:radio

别名：inp[type=radio]

<input type="radio" name="" id="" />
缩写：input:r

别名：input:radio

<input type="radio" name="" id="" />
缩写：input:range

别名：inp[type=range]

<input type="range" name="" id="" />
缩写：input:file

别名：inp[type=file]

<input type="file" name="" id="" />
缩写：input:f

别名：input:file

<input type="file" name="" id="" />
缩写：input:submit

<input type="submit" value="" />
缩写：input:s

别名：input:submit

<input type="submit" value="" />
缩写：input:image

<input type="image" src="" alt="" />
缩写：input:i

别名：input:image

<input type="image" src="" alt="" />
缩写：input:button

<input type="button" value="" />
缩写：input:b

别名：input:button

<input type="button" value="" />
缩写：isindex

<isindex />
缩写：input:reset

别名：input:button[type=reset]

<input type="reset" value="" />
缩写：select

<select name="" id=""></select>
缩写：option

<option value=""></option>
缩写：textarea

<textarea name="" id="" cols="30" rows="10"></textarea>
缩写：menu:context

别名：menu[type=context]>

<menu type="context"></menu>
缩写：menu:c

别名：menu:context

<menu type="context"></menu>
缩写：menu:toolbar

别名：menu[type=toolbar]>

<menu type="toolbar"></menu>
缩写：menu:t

别名：menu:toolbar

<menu type="toolbar"></menu>
缩写：video

<video src=""></video>
缩写：audio

<audio src=""></audio>
缩写：html:xml

<html xmlns="http://www.w3.org/1999/xhtml"></html>
缩写：keygen

<keygen />
缩写：command

<command />
缩写：bq

别名：blockquote

<blockquote></blockquote>
缩写：acr

别名：acronym

<acronym title=""></acronym>
缩写：fig

别名：figure

<figure></figure>
缩写：figc

别名：figcaption

<figcaption></figcaption>
缩写：ifr

别名：iframe

<iframe src="" frameborder="0"></iframe>
缩写：emb

别名：embed

<embed src="" type="" />
缩写：obj

别名：object

<object data="" type=""></object>
缩写：src

别名：source

<source></source>
缩写：cap

别名：caption

<caption></caption>
缩写：colg

别名：colgroup

<colgroup></colgroup>
缩写：fst, fset

别名：fieldset

<fieldset></fieldset>
缩写：btn

别名：button

<button></button>
缩写：btn:b

别名：button[type=button]

<button type="button"></button>
缩写：btn:r

别名：button[type=reset]

<button type="reset"></button>
缩写：btn:s

别名：button[type=submit]

<button type="submit"></button>
```
