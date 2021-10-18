---
title: Python Crawler
tags: python
date: 2019-04-30
---

## 文件操作

文件访问模式

| 序号 | 文件访问模式 | 解释                            |
| ---- | ------------ | ------------------------------- |
| 01   | r            | 读                              |
| 02   | w            | 写                              |
| 03   | a            | 追加                            |
| 04   | r+           | 读写模式                        |
| 05   | w+           | 读写模式                        |
| 06   | a+           | 读写模式                        |
| 07   | b            | 二进制文件操作：图像,视频之类的 |

文件对象方法

| 序号 | 对象方法                 | 操作及解释                             |
| ---- | ------------------------ | -------------------------------------- |
| 01   | file.close()             | 关闭文件                               |
| 02   | file.read()              | 读取文件内容，一次加载所有内容至内存中 |
| 03   | file.readline(size= num) | 读取从起始位置到 num 位置的所有内容    |
| 04   | file.readlines()         | 按行读取内容                           |
| 05   | file.write()             | 向文件中写入内容                       |
| 06   | file.tell()              | 返回当前在文件中的位置                 |
| 07   | file.seek()              | 在文件中移动文件指针                   |

操作演示

```python
# read
import codecs

filename = r'G:\Python\crawl\series\test.txt'
with codecs.open(filename,'r',encoding='utf-8') as f:
    line = f.readline(20)
    print(line)

# write binary
import requests
from lxml import etree
import codecs

url = "https://alpha.wallhaven.cc/random"
content = requests.get(url).content


html = etree.HTML(content)
img_urls = html.xpath('//figure//@data-src')

i = 0
for img_url in img_urls:
    with codecs.open('%s.jpg'%i,'wb') as f:
        img = requests.get(img_url)
        f.write(img.content)
        i += 1
```

## 正则表达式

语法

| 记号     | 说明                                   | 示例           |
| -------- | -------------------------------------- | -------------- |
| literal  | 匹配字符串的值                         | wuxiaoshen     |
| .        | 匹配任意字符(除换行符之外)             | wu.iaoshen     |
| ^        | 匹配字符串的开始                       | ^wuxiaoshen    |
| \$       | 匹配字符串的结尾                       | wuxiaoshen\$   |
| \*       | 匹配前面出现 0 次或者多次的            | wu\*xiaoshen   |
| +        | 匹配前面出现 1 次或者多次              | wu+xiaoshen    |
| ?        | 匹配前面出现零次或者 1 次              | wu?xiaoshen    |
| {N}      | 匹配前面出现的正则表达式 N 次          | [0-9]{2}       |
| {M,N}    | 匹配前面出现的正则表达式 M 到 N 次之间 | [0-9]{3,8}     |
| [ ]      | 匹配里面内容的任意一个字符             | wu[xyz]iaoshen |
| [x-y]    | 匹配任意之间的一个值                   | [0-9]          |
| [^..]    | 不匹配里面内容任意值                   | [^0-9]         |
| ()       | 匹配封闭括号中正则表达式，并保存为子组 | （wuxiaoshen） |
| 特殊字符 | 特殊字符                               | 特殊字符       |
| \d       | 匹配数字                               | data\d.txt     |
| \w       | 匹配任何数字字母字符                   | [wuxiao]\w+    |
| \s       | 匹配空白符                             | of\sthe        |
| \b       | 匹配单词的边界                         | \bwuxiaoshen\b |
| \D       | 不匹配数字                             |                |
| \W       | 不匹配数字字母字符                     |                |
| \S       | 匹配任意不是空白符的字符               |                |
| \B       | 匹配不是单词开头或结束的位置           |                |

python 正则表达式模块

| 模块函数                         | 描述                                         |
| -------------------------------- | -------------------------------------------- |
| match(pattern, string, flag)     | 匹配以 pattern 开始的字符串                  |
| search(pattern, string, flag)    | 匹配第一符合要求的字符串，其他还符合，不管   |
| findall(pattern, string, flag)   | 匹配全部符合要求的字符串                     |
| split(pattern, string, flag)     | 按格式进行切分                               |
| sub(pattern, repl, string, flag) | 替换掉符合要求的字符串，常用来替换网址的组成 |

操作演示

```python
import re
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
url = "http://www.imooc.com/course/list"
resp = requests.get(url).text
# <img class="course-banner lazy" data-original="//img3.mukewang.com/5a93aa610001eb2706000338-240-# # 135.jpg" src="//img3.mukewang.com/5a93aa610001eb2706000338-240-135.jpg" style="display: inline;">
# image_urls = re.findall(r'src="(//img3.mukewang.com/[\w-]+.jpg)"',resp)
image_urls = re.findall(r'src="(//.*?.jpg)"',resp)
image_urls = ['http:' + str(i) for i in image_urls]
print(image_urls)
i = 0
for image_url in image_urls:
    with open('image\\' + str(i) + '.jpg','wb') as f:
        image = requests.get(image_url)
        f.write(image.content)
        i += 1
```

## 网页下载

urllib

| 序号 | 常用方法                 |
| ---- | ------------------------ |
| 01   | urllib.request.urlopen() |
| 02   | urllib.request.Request() |

```python
import urllib.request

url = "http://www.geekonomics10000.com/author/admin"
html = urllib.request.urlopen(url)
response = html.read().decode('utf-8')
print(response)
```

requests

传递请求参数

```python
import requests

url = "http://yanbao.stock.hexun.com/xgq/gsyj.aspx"
data = {"1": 1, "page": 4}
html = requests.get(url, params=data)
print(html.url)
```

请求头部

```python
import requests

url = "http://blog.csdn.net/pongba"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
           "Referer": 'http://blog.csdn.net/pongba/article/details/7911997'}
html = requests.get(url, headers=headers)
print(html.status_code)
```

响应内容

```python
import requests

url = "http://www.geekonomics10000.com/author/admin"
html = requests.get(url)
response_1 = html.text      # 响应字符内容
response_2 = html.content   # 以字节的方式访问请求响应体，用于非文本请求
response_3 = html.raw       # 原始响应
print(type(response_1))
print(type(response_2))
print(type(response_3))
# output
<class 'str'>
<class 'bytes'>
<class 'requests.packages.urllib3.response.HTTPResponse'>
```

## BeautifulSoup

常见的概念：

| 序号 | 概念       | 说明 |
| ---- | ---------- | ---- |
| 01   | Tag        | 标签 |
| 02   | Name       | 名字 |
| 03   | Attributes | 属性 |

常用的方法：

| 序号 | 方法       | 解释说明                 |
| ---- | ---------- | ------------------------ |
| 01   | find_all() | 搜索全部符合要求的信息   |
| 02   | get_text() | 获取文本                 |
| 03   | find()     | 返回第一个符合要求的信息 |

```python
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
cover: /img/post-cover/31.jpg
<body>
<p class="title"><b>The Dormouse's story</b></p>
cover: /img/post-cover/31.jpg

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
Soup = BeautifulSoup(html_doc,'lxml',form_encoding='utf-8')
# print(Soup.prettify())
print(Soup.title)         # <title>The Dormouse's story</title>
print(Soup.title.name)    # title
print(Soup.title.string)  # The Dormouse's story

print(Soup.p['class'])    # ['title']

print(Soup.a)   # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(Soup.find('a'))  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(Soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(Soup.get_text())    # 获取所有文字内容
'''
The Dormouse's story

The Dormouse's story
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
...
'''
```

> 作者：谢小路
> 链接：<https://www.jianshu.com/p/d0a7b59f3c29>
> 來源：简书
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
