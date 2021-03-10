---
title: node record
tags: node
date: 2019-07-15
description: 记录一些有意思的程式
---

### random story

```js
// rss_feeds.txt
// http://lambda-the-ultimate.org/rss.xml
// http://lambda-the-ultimate.org/rss.xml

var fs = require('fs')
var request = require('request')
var htmlparser = require('htmlparser')

var configFilename = './rss_feeds.txt'

function checkForRSSFile() {
  fs.exists(configFilename, function(exists) {
    if (!exists) return next(new Error('Missing RSS file: ' + configFilename))
    next(null, configFilename)
  })
}

function readRSSFile(configFilename) {
  fs.readFile(configFilename, function(err, feedList) {
    if (err) return next(err)

    feedList = feedList
      .toString()
      .replace('/^s+|s+$/g', '') // 去掉前后的空白字符，\s 匹配空白字符
      .split('\n')
    var random = Math.floor(Math.random() * feedList.length)
    next(null, feedList[random])
  })
}

function downloadRSSFeed(feedUrl) {
  request({ uri: feedUrl }, function(err, res, body) {
    if (err) return next(err)
    if (res.statusCode != 200) {
      return next(new Error('Abnormal response status code'))
    }
    next(null, body)
  })
}

function parseRSSFeed(rss) {
  var handler = new htmlparser.RssHandler()
  var parser = new htmlparser.Parser(handler)
  parser.parseComplete(rss)
  if (!handler.dom.items.length) return next(new Error('No RSS items found'))
  var item = handler.dom.items.shift()
  console.log(item.title)
  console.log(item.link)
}

tasks = [checkForRSSFile, readRSSFile, downloadRSSFeed, parseRSSFeed]

function next(err, result) {
  if (err) throw err

  var currentTask = tasks.shift()

  if (currentTask) {
    currentTask(result)
  }
}

next()
```

### word count

```js
var fs = require('fs')
var completedTasks = 0
var tasks = []
var wordCounts = {}
var filesDir = './text'

function checkIfComplete() {
  completedTasks++
  if (completedTasks == tasks.length) {
    for (var index in wordCounts) {
      console.log(index + ': ' + wordCounts[index])
    }
  }
}

function countWordsInText(text) {
  var words = text
    .toString()
    .toLowerCase()
    .split(/\W+/)
    .sort()
  // console.log(words)
  for (var index in words) {
    var word = words[index]
    if (word) {
      wordCounts[word] = wordCounts[word] ? wordCounts[word] + 1 : 1
    }
  }
}

fs.readdir(filesDir, function(err, files) {
  if (err) throw err
  for (var index in files) {
    var task = (function(file) {
      fs.readFile(file, function(err, text) {
        if (err) throw err
        countWordsInText(text)
        checkIfComplete()
      })
    })(filesDir + '/' + files[index])
    tasks.push(task)
  }
})
```

### todo rest

```js
var http = require('http')
var url = require('url')
var items = ['learn node']
var server = http.createServer(function(req, res) {
  switch (req.method) {
    case 'POST':
      var item = ''
      req.setEncoding('utf8')
      // 默认情况下，data 事件会提供 Buffer 对象，这是 Node 版的字节数组。
      // 而对于文本格式的待办事项而言，并不需要二进制数据，所以最好将流编码设定为 ascii 或 utf8；
      // 这样 data 事件会给出字符串。这可以通过调用 req.setEncoding(encoding) 方法设定。
      req.on('data', function(chunk) {
        item += chunk
      })
      req.on('end', function() {
        items.push(item)
        res.end('OK\n')
      })
      break
    case 'GET':
      items.forEach(function(item, i) {
        res.write(i + ') ' + item + '\n')
      })
      res.end()
      break
    case 'DELETE':
      var path = url.parse(req.url).pathname
      var i = parseInt(path.slice(1), 10)
      if (isNaN(i)) {
        res.statusCode = 400
        res.end('Invalid item id')
      } else if (!items[i]) {
        res.statusCode = 404
        res.end('Item not found')
      } else {
        items.splice(i, 1)
        res.end('OK\n')
      }
      break
    default:
      break
  }
})

server.listen(3000)
```
