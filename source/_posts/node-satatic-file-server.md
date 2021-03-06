---
title: node static file server
tags: node
date: 2019-07-15
---

```js
var http = require('http')
var fs = require('fs')
var path = require('path')
var mime = require('mime')

var cache = {}

/**
 * send 404 error
 * @param {} response
 */
function send404(response) {
  response.writeHead(404, { 'Content-Type': 'text/plain' })
  response.write('Error 404: resource not found')
  response.end()
}

/**
 * send 静态文件内容
 * @param {*} response
 * @param {*} filePath 文件路径包含名称
 * @param {*} fileContents 文件内容
 */
function sendFile(response, filePath, fileContents) {
  response.writeHead(200, {
    // mime.lookup 获取文件的 mime 类型, mime.getType('package.json') => application/json
    'Content-Type': mime.getType(path.basename(filePath))
  })
  response.end(fileContents)
}

/**
 * 提供静态文件服务
 * @param {*} response
 * @param {*} cache 静态文件缓存对象
 * @param {*} absPath 文件绝对路径
 */
function serveStatic(response, cache, absPath) {
  if (cache[absPath]) {
    sendFile(response, absPath, cache[absPath])
  } else {
    fs.exists(absPath, function(exists) {
      if (exists) {
        fs.readFile(absPath, function(err, data) {
          if (err) {
            send404(response)
          } else {
            cache[absPath] = data
            sendFile(response, absPath, data)
          }
        })
      } else {
        send404(response)
      }
    })
  }
}

// 创建 HTTP 服务器

var server = http.createServer(function(request, response) {
  var filePath = false

  if (request.url == '/') {
    filePath = 'public/index.html'
  } else {
    filePath = 'public' + request.url
  }

  var absPath = './' + filePath
  serveStatic(response, cache, absPath)
})

// 启动服务器

server.listen(3000, function() {
  console.log('Server listening on port 3000')
})
```
