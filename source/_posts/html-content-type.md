---
title: HTML Content Type
tags: html
date: 2019-04-30
---

### application/x-www-form-urlencoded

浏览器的原生 form 表单，如果不设置 enctype 属性，那么最终就会以 application/x-www-form-urlencoded 方式提交数据。请求如下面形式：

```
POST http://www.example.com HTTP/1.1
Content-Type: application/x-www-form-urlencoded;charset=utf-8

title=test&sub%5B%5D=1&sub%5B%5D=2&sub%5B%5D=3
```

该种方式提交的数据放在 body 里面，数据按照 key1=val1&key2=val2 的方式进行编码，key 和 val 都进行了 URL 转码。

### multipart/form-data

该种方式也是一个常见的 POST 提交方式，通常表单上传文件时使用该种方式。请求类似下面形式

```
POST http://www.example.com HTTP/1.1
Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryrGKCBY7qhFd3TrwA

------WebKitFormBoundaryrGKCBY7qhFd3TrwA
Content-Disposition: form-data; name="text"

title
------WebKitFormBoundaryrGKCBY7qhFd3TrwA
Content-Disposition: form-data; name="file"; filename="chrome.png"
Content-Type: image/png

PNG ... content of chrome.png ...
------WebKitFormBoundaryrGKCBY7qhFd3TrwA--
```

首先 Content-Type 指明数据以 multipart/form-data 方式编码，同时后面跟一个 boundary 标识分隔符。
body 里字段分多个部分，每部分以 –boundary 开始，然后是内容描述信息，回车空行(CRLF)之后是字段的具体内容，内容可以是文本或者二进制形式。如果传输文件，需要包含文件名和文件类型信息。最后加上–表示数据结束。

### application/json

application/json 作为响应头大家都不陌生，现在越来越多的人把其作为请求头，用来告诉服务器消息主体是序列化后的 JSON 字符串。请求类似下面形式

```
POST http://www.example.com HTTP/1.1
Content-Type: application/json;charset=utf-8

{"title":"test","sub":[1,2,3]}
```

该种形式支持比普通键值对复杂的多的结构化数据，一般用于 RESTful 接口。一般服务端对 JSON 数据都有很好的支持。

### text/xml

该种方式主要用来提交 XML 格式的数据，请求形式如下：

```
POST http://www.example.com HTTP/1.1
Content-Type: text/xml

<?xml version="1.0"?>
<methodCall>
    <methodName>examples.getStateName</methodName>
    <params>
        <param>
            <value><i4>41</i4></value>
        </param>
    </params>
</methodCall>
```

虽然在 API 方面现在 JSON 大有取代 XML 的意思，但是 XML 依然有其不可代替的领域。

> 引用: https://honglu.me/2015/07/13/%E5%B8%B8%E7%94%A8%E7%9A%84%E5%87%A0%E7%A7%8DContent-Type/
