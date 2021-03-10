---
title: node call python
tags: node
date: 2019-07-15
---

### call cmd

#### chid_process.exec

```js
var exec = require('child_process').exec
var cmdStr = 'curl http://www.weather.com.cn/data/sk/101010100.html'
exec(cmdStr, function(err, stdout, stderr) {
  if (err) {
    console.log('get weather api error:' + stderr)
  } else {
    /*
     这个stdout的内容就是上面curl出来的这个东西：
     {"weatherinfo":{"city":"北京","cityid":"101010100","temp":"3","WD":"西北风","WS":"3级","SD":"23%","WSE":"3","time":"21:20","isRadar":"1","Radar":"JC_RADAR_AZ9010_JB","njd":"暂无实况","qy":"1019"}}
    */
    var data = JSON.parse(stdout)
    console.log(data)
  }
})
```

#### chid_process.spawn

```js
var spawn = require('child_process').spawn
netstat = spawn('netstat', ['-a'])

// 捕获标准输出并将其打印到控制台
netstat.stdout.on('data', function(data) {
  console.log('standard output:\n' + data)
})

// 捕获标准错误输出并将其打印到控制台
netstat.stderr.on('data', function(data) {
  console.log('standard error output:\n' + data)
})

// 注册子进程关闭事件
netstat.on('exit', function(code, signal) {
  console.log('child process eixt ,exit:' + code)
})
```

### call c/c++

```js
var JSCPP = require('JSCPP')
var code =
  '#include <iostream>' +
  'using namespace std;' +
  'int main() {' +
  '    int a;' +
  '    cin >> a;' +
  '    cout << a << endl;' +
  '    return 0;' +
  '}'
var input = '4321'
var exitcode = JSCPP.run(code, input)
console.info('program exited with code ' + exitcode)

// 4321
// program exited with code 0
```

### call python

```js
const exec = require('child_process').exec
const arg1 = 'hello'
const arg2 = 'node'

// # py_test.py
// import sys
// print(sys.argv)

exec('python py_test.py ' + arg1 + ' ' + arg2, function(error, stdout, stderr) {
  if (stdout.length > 1) {
    console.log('you offer args:', stdout)
  } else {
    console.log("you don't offer args")
  }
  if (error) {
    console.info('stderr : ' + stderr)
  }
})
```
