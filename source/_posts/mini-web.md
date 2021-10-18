---
title: Mini Web
tags:
  - node
  - python
  - go
date: 2019-07-10
---

> 来源： https://www.bilibili.com/video/av67118491

web 中的基本功能:

1. 获取路径参数，查询字符串，form 表单数据(body)，json 数据(body)
2. 返回纯文本，json 数据
3. static 静态文件访问
4. 获取 header, 设置 header

### node express

```js
var express = require('express')
var app = express()
// 使 express 可以解析 body 数据
app.use(express.urlencoded({ extended: false }))
app.use(express.json())
// static
app.use('/static', express.static('static'))

app.get('/', function(req, res) {
  console.log(req.headers.a) // get header
  res.header('b', 'c') // set header
  res.send('hello express')
})
// 路径参数
app.get('/path/:id', function(req, res) {
  console.log(req.params.id)
  res.send(req.params.id)
})
// 查询字符串
app.get('/querystring', function(req, res) {
  console.log(req.query)
  res.send(req.query.username)
})
// form 表单数据
app.post('/form', function(req, res) {
  console.log(req.body)
  res.send(req.body.username)
})
// json 数据
app.post('/json', function(req, res) {
  console.log(req.body)
  res.json({ a: 12, b: 'bb' }) // 返回 json
})
app.listen(3001)
```

### python flask

```python
from flask import Flask,request
import json

app = Flask(__name__)
# flask 默认 项目下的 static 为静态目录，可以直接访问

# 路径参数
@app.route('/path/<id>')
def f1(id):
    return id

# 查询字符串
@app.route('/querystring')
def f2():
    a = request.args.to_dict().get("a")
    return a

# form 表单
@app.route('/form',methods=['post'])
def f3():
    b = request.form.to_dict().get("b")
    return b

# json
@app.route('/json',methods=['post'])
def f4():
    jsonstr = request.data.decode('utf-8')
    c = json.loads(jsonstr).get("c")
    return str(c)

@app.route('/')
def hello():
    print(request.headers.get('a'))  # get header
    return {'a':11,'b':'bb'},200,{"f":"g"}  # json data, statuscode, header


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3002)
```

### go gin

```go
package main

import "github.com/gin-gonic/gin"
import "fmt"

func main() {
	r := gin.Default()
    // static 前缀访问，对应到当前目录下的 static 目录下文件
	r.Static("/static","./static")

	r.GET("/", func(c *gin.Context) {
		fmt.Println(c.GetHeader("a")) // get header
		c.Header("k","l") // set header
		c.String(200,"hello gin")
    })

    // 路径参数
	r.GET("/path/:id",func(c *gin.Context) {
		c.String(200,c.Param("id"))
    })

    // 查询字符串
	r.GET("/querystring",func(c *gin.Context) {
		c.String(200,c.Query("username"))
    })

    // form 表单
	r.POST("/form",func(c *gin.Context) {
		c.String(200,c.PostForm("username"))
    })

    // json
	r.POST("/json",func(c *gin.Context) {
		var amap interface{}
		c.BindJSON(&amap)
		c.JSON(200,amap) // return json
	})
	r.Run(":3003")
}
```

