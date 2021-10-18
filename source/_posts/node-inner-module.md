---
title: Node Inner Module
tags: node
date: 2019-07-15
description: node 常用内置模块
---

### process

```javascript
var arr = process.argv
if (arr.length == 3) {
    console.log(arr[2])
}
console.log(process.argv)
// aaa
// [ '/usr/local/Cellar/node/9.11.1/bin/node',
//   '/Users/jbn/Desktop/study/node/node_guide/test_process.js',
//   'aaa' ]

process.stdout.write("请输入用户名:");
process.stdin.on('data', (input) => {
    let username = input.toString().trim();
    process.stdout.write("请输入密码:");
    process.stdin.on('data',(input) => {
        let password = input.toString().trim()
        if (username === "babb" && password === "123") {
            console.log("success")
        }
    });
});
```

### http

```javascript
var http = require("http")
var fs = require("fs")

var server = http.createServer()

server.on("request", (req, res) => {
    var url = req.url

    if (url === "/plain") {
        // Content-Type 设置相应内容格式和编码方式
        res.setHeader("Content-Type", "text/plain; charset=utf-8")
        res.end("你好，世界！")
    } else if (url === "/html") {
        res.setHeader("Content-Type", "text/html; charset=utf-8")
        res.end("<h1>Hello, World!</h1>")
    } else if (url === "/file") {
        fs.readFile('./05.jpg', (err, data) => {
            if (err) {
                res.setHeader("Content-Type", "text/plain; charset=utf-8")
                res.end("文件读取失败！")
            } else {
                res.setHeader("Content-Type", "image/jpeg")
                res.end(data)
            }
        })
    }
})

server.listen(3000, () => {
    console.log("server is listening in port 3000...")
})
```
