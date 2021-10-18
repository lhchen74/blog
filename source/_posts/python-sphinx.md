---
title: Python Sphinx
tags: python
date: 2019-10-31
---

### 安装 Sphinx

```
pip install Sphinx
```

### 快速创建

```
sphinx_quickstart
```

文档根目录(Root path for the documentation)，默认为当前目录(.)
是否分离文档源代码与生成后的文档(Separate source and build directories): y
模板与静态文件存放目录前缀(Name prefix for templates and static dir):\_
项目名称(Project name) : sphinx-note
作者名称(Author name)：jbn
项目版本(Project version) : 1.0.0
文档默认扩展名(Source file suffix) : .rst
默认首页文件名(Name of your master document):index
是否添加 epub 目录(Do you want to use the epub builder):n
启用 autodoc|doctest|viewcode（autodoc 可以根据 python doc 生成文档，viewcode 可以查看源码） ：y
生成 Makefile (Create Makefile)：y
生成 windows 用命令行(Create Windows command file):y

### 配置

配置文件位于 source 文件夹下的 conf.py

修改默认主题

```python
# pip install sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
```

添加 markdown 支持

```python
# pip install recommonmark
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
```

### 添加普通文档

在 source 的 index.rst 中添加 reStructuredText

```rst
.. note documentation master file, created by
   sphinx-quickstart on Fri Sep 27 17:48:58 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to jbn's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reStructuredText



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

source 文件夹下 reStructuredText.rst内容如下:

```rst
reStructuredText 语法
=======================

行内样式
----------

斜体
>>>>>>>
重点、解释文字

*重点(emphasis)通常显示为斜体* *

`解释文字(interpreted text)通常显示为斜体`  `

粗体
>>>>>>
重点强调

**重点强调(strong emphasis)通常显示为粗体** **

等宽
>>>>>>

``行内文本(inline literal)通常显示为等宽文本，空格可以保留，但是换行不可以。`` ``

段落
-------
段落是被空行分割的文字片段，左侧必须对齐（没有空格，或者有相同多的空格）。

缩进的段落被视为引文。

列表
------

符号列表(Bullet Lists)
>>>>>>>>>>>>>>>>>>>>>>

符号列表可以使用 -、 \*、 + 来表示

不同的符号结尾需要加上空行，下级列表需要有空格缩进。

- 符号列表1-
- 符号列表2-

  + 二级符号列表1+

  - 二级符号列表2-

  * 二级符号列表3*

* 符号列表3*

+ 符号列表4+

枚举(顺序)列表(Enumerated Lists)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
枚举列表算即顺序(序号)列表，可以使用不同的枚举序号来表示列表。

可以使用的枚举有：

阿拉伯数字: 1, 2, 3, ... (无上限)。
大写字母: A-Z。
小写字母: a-z。
大写罗马数字: I, II, III, IV, ..., MMMMCMXCIX (4999)。
小写罗马数字: i, ii, iii, iv, ..., mmmmcmxcix (4999)。
可以为序号添加前缀和后缀，下面的是被允许的。

. 后缀: "1.", "A.", "a.", "I.", "i."。
() 包起来: "(1)", "(A)", "(a)", "(I)", "(i)"。
) 后缀: "1)", "A)", "a)", "I)", "i)"。

枚举列表可以结合 # 自动生成枚举序号。

1. 枚举列表1 1.
#. 枚举列表2 #.
#. 枚举列表3 #.

(I) 枚举列表1 (I)
(#) 枚举列表2 (#)
(#) 枚举列表3 (#)

A) 枚举列表1 A)
#) 枚举列表2 #)
#) 枚举列表3 #)

定义列表(Definition Lists)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
定义列表可以理解为解释列表，即名词解释。

条目占一行，解释文本要有缩进；多层可根据缩进实现。

定义1
 这是定义1的内容

定义2
 这是定义2的内容

字段列表(Field Lists)
>>>>>>>>>>>>>>>>>>>>>>

:标题: reStructuredText语法说明

:作者:
     - Seay
     - Seay1
     - Seay2

:时间: 2016年06月21日

:概述: 这是一篇
     关于reStructuredText

     语法说明。

选项列表(Option Lists)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
选项列表是一个类似两列的表格，左边是参数，右边是描述信息。当参数选项过长时，参数选项和描述信息各占一行。

选项与参数之间有一个空格，参数选项与描述信息之间至少有两个空格。

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too


块(Blocks)
-----------
文字块(Literal Blocks)
>>>>>>>>>>>>>>>>>>>>>>>
文字块就是一段文字信息，在需要插入文本块的段落后面加上 ::，接着一个空行，然后就是文字块了。

文字块不能定顶头写，要有缩进，结束标志是，新的一段文本贴开头，即没有缩进。

下面是文字块内容：

::

   这是一段文字块
   同样也是文字块
   还是文字块

这是新的一段。


行块(Line Blocks)
>>>>>>>>>>>>>>>>>>>>>
行块对于地址、诗句以及无装饰列表是非常有用的。行块是以 | 开头，每一个行块可以是多段文本。

| 前后各有一个空格。

下面是行块内容：
 | 这是一段行块内容
 | 这同样也是行块内容
   还是行块内容


块引用(Block Quotes)
>>>>>>>>>>>>>>>>>>>>>
块引用是通过缩进来实现的，引用块要在前面的段落基础上缩进。

通常引用结尾会加上出处(attribution)，出处的文字块开头是 --、--- 、—，后面加上出处信息。

块引用可以使用空的注释 .. 分隔上下的块引用。

注意在新的块和出处都要添加一个空行。

下面是引用的内容：

    “真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。”

    --- 鲁迅

..

      “人生的意志和劳动将创造奇迹般的奇迹。”

      — 涅克拉索

文档测试块(Doctest Blocks)
>>>>>>>>>>>>>>>>>>>>>>>>>>>
文档测试块是交互式的Python会话，以 >>> 开始，一个空行结束。

>>> print "This is a doctest block."
This is a doctest block.
>>> print "This is a doctest block."
This is a doctest block.

表格(Tables)
--------------
reStructuredText提供两种表格：网格表（Grid Tables），简单表（Simple Tables）。

网格表(Grid Tables)
>>>>>>>>>>>>>>>>>>>>
网格表中使用的符号有：\-、\=、\|、\+。

- 用来分隔行， = 用来分隔表头和表体行，| 用来分隔列，+ 用来表示行和列相交的节点。

Grid table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

简单表(Simple Tables)
>>>>>>>>>>>>>>>>>>>>>
简单表相对于网格表，少了 | 和 + 两个符号，只用 - 和 = 表示。

Simple table:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

分隔符
------------
分隔符就是一条水平的横线，是由 4 个 - 或者更多组成，需要添加换行。

上面部分

------------

下面部分

超链接
--------
介绍各类带有链接性质的超链接

自动超链接
>>>>>>>>>>>
reStructuredText会自动将网址生成超链接。

https://github.com/SeayXu/

外部超链接(External Hyperlink)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
引用/参考(reference)，简单的形式，只能是一个词语，引用的文字不能带有空格。

这篇文章来自我的Github,请参考 reference_。

.. _reference: https://github.com/SeayXu/

引用/参考(reference)，行内形式，引用的文字可以带有空格或者符号。

这篇文章来自我的Github,请参考 `lh chen <https://github.com/lhchen74/>`_。

内部超链接|锚点(Internal Hyperlink)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
更多信息参考 引用文档_

这里是其他内容

.. _引用文档:

这是引用部分的内容

匿名超链接(Anonymous hyperlink)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
词组(短语)引用/参考(phrase reference)，引用的文字可以带有空格或者符号，需要使用反引号引起来。

这篇文章参考的是：`Quick reStructuredText`__

.. __: http://docutils.sourceforge.net/docs/user/rst/quickref.html

间接超链接(Indirect Hyperlink)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
间接超链接是基于匿名链接的基础上的，就是将匿名链接地址换成了外部引用名。

SeayXu_ 是 `我的 GitHub 用户名`__。

.. _SeayXu: https://github.com/SeayXu/

__ SeayXu_


隐式超链接(Implicit Hyperlink)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
小节标题、脚注和引用参考会自动生成超链接地址，使用小节标题、脚注或引用参考名称作为超链接名称就可以生成隐式链接。
隐式链接到 `表格(Tables)`_，即可生成超链接。


替换引用(Substitution Reference)
---------------------------------
替换引用就是用定义的指令替换对应的文字或图片，和内置指令(inline directives)类似。

这是 |logo| github的Logo，我的github用户名是:|name|。

.. |logo| image:: https://help.github.com/assets/images/site/favicon.ico
.. |name| replace:: SeayXu


脚注引用(Footnote Reference)
--------------------------------
脚注引用，有这几个方式：有手工序号(标记序号123之类)、自动序号(填入#号会自动填充序号)、自动符号(填入*会自动生成符号)。

手工序号可以和#结合使用，会自动延续手工的序号。

# 表示的方法可以在后面加上一个名称，这个名称就会生成一个链接。

脚注引用一 [1]_
脚注引用二 [#]_
脚注引用三 [#链接]_
脚注引用四 [*]_
脚注引用五 [*]_
脚注引用六 [*]_

.. [1] 脚注内容一
.. [2] 脚注内容二
.. [#] 脚注内容三
.. [#链接] 脚注内容四 链接_
.. [*] 脚注内容五
.. [*] 脚注内容六
.. [*] 脚注内容七


引用参考(Citation Reference)
---------------------------------
引用参考的内容通常放在页面结尾处，比如 [One]_，[Two]_

.. [One] 参考引用一
.. [Two] 参考引用二


注释(Comments)
--------------------
注释以 .. 开头，后面接注释内容即可，可以是多行内容，多行时每行开头要加一个空格。

..
 我是注释内容
 你们看不到我


Code Block
------------------------

this is python code block::

    def chain(*iterables):
        for it in iterables:
            for i in it:
                yield i


    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))

this is ruby code block

.. code-block:: ruby
    :linenos:

        class Roulette
          def method_missing(name, *args)
            person = name.to_s.capitalize
            super unless %w[Bob Frank Bill Honda Eric].include? person
            number = 0
            3.times do
              number = rand(10) + 1
              puts "#{number}..."
            end
            "#{person} got a #{number}"
          end
        end

        number_of = Roulette.new
        puts number_of.bob
        puts number_of.kitty


    this is python code block use literalinclude

.. literalinclude:: example.py
    :language: python
    :emphasize-lines: 12,15-18
    :linenos:

指令
---------
image指令
>>>>>>>>>>>>>>>>>

.. image:: _static/girl.png
    :height: 400px
    :width: 1080px
    :scale: 100%
    :alt: alternate text
    :align: left

figure指令
>>>>>>>>>>>>>>>>>

.. figure:: _static/girl.png

   The Anime Is Fate/Grade.

csv-table指令
>>>>>>>>>>>>>>>>>>>>>

.. csv-table:: csv-table
 :widths: 15, 10, 15

 "column1", "column2", "column3"
 value1, value2, value3
 value4, value5, value6

math指令
>>>>>>>>>>>>>>>>>>>>>

.. math:: (a + b)^2 = a^2 + 2ab + b^2
```

### 添加 API 文档

`sphinx-apidoc -o ./source ./code/` 根据 python doc 生成 rst 文件 ` -o ./source`输出出文件位置，` ./code`代码所在文件位置

code 下 的 sort.py 如下:

```python
class Sort:
    '''
    this is a class for sort
    '''

    @staticmethod
    def selection_sort(arr):
        '''
        selection_sort
        :param arr: this is a arr need sort
        :return: a arr after sorted
        '''
        new_arr = []
        for _ in range(len(arr)):
            smallest_index = Sort.find_smallest(arr)
            new_arr.append(arr.pop(smallest_index))
        return new_arr

    @staticmethod
    def quick_sort(arr):
        '''
        quick_sort
        :param arr: this is a arr need sort
        :return: a arr after sorted
        '''
        if len(arr) < 2:
            return arr
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        large = [i for i in arr if i > pivot]
        return Sort.quick_sort(less) + [pivot] + Sort.quick_sort(large)

```

`sphinx-apidoc -o ./source ./code/` 命令执行后在 source 目录下产生 modules.rst, sort.rst；在 index.rst 下加入 modules.rst  引用

```rst
.. xx documentation master file, created by
   sphinx-quickstart on Wed Oct 30 20:00:26 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to jbn's documentation!
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   reStructuredText
   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

### make html

在文档根目录执行 `make html`，点击 build 下的 index.html 可以查看生成文档效果

![](python-sphinx/1572485387672.png)

### 上传文档到 github

### readdocs 网站导入 github 文档

