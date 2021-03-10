---
title: node async
tags: node
date: 2019-07-10
---

### Promise

#### resolve，reject

```js
function test(resolve, reject) {
  var timeOut = Math.random() * 2
  console.log('timeOut: ' + timeOut)
  setTimeout(function() {
    if (timeOut < 1) {
      console.log('resolve...')
      resolve('resolve')
    } else {
      console.log('reject...')
      reject('reject')
    }
  }, timeOut * 1000)
}

var p1 = new Promise(test)
var p2 = p1.then(function(result) {
  console.log('成功：' + result)
})
var p3 = p2.catch(function(reason) {
  console.log('失败：' + reason)
})

// timeOut: 0.2448595166188703
// resolve...
// 成功：resolve
```

#### Promise.all()，Promise.race()

Promise.all() 接受一个 Promise 的数组，数组中所有 Promise 都执行完毕后，才会返回结果
Promise.all() 接受一个 Promise 的数组，数组中只要一个 Promise 执行完毕后，就会返回结果

```js
var p1 = new Promise(function(resolve, reject) {
  // setTimeout(resolve, 500, 'P1');
  setTimeout(resolve('P1'), 500)
})
var p2 = new Promise(function(resolve, reject) {
  setTimeout(resolve, 600, 'P2')
})
// 同时执行p1和p2，并在它们都完成后执行then:
Promise.all([p1, p2]).then(function(results) {
  console.log(results) // 获得一个Array: ['P1', 'P2']
})

Promise.race([p1, p2]).then(function(results) {
  console.log(results)
})

// P1   // 因为异步， 并且 Promise.race([p1, p2]) 比 Promise.all([p1, p2]) 先执行完
// [ 'P1', 'P2' ]
```

#### Get Youdao translate

```js
var XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest
var fs = require('fs')

function search(term) {
  var url = `http://dict.youdao.com/w/${term}/#keyfrom=dict2.top`
  var xhr = new XMLHttpRequest()
  var result

  var p = new Promise(function(resolve, reject) {
    xhr.open('GET', url, true)
    xhr.onload = function(e) {
      if (this.status === 200) {
        result = this.responseText
        resolve(result)
      }
    }
    xhr.onerror = function(e) {
      reject(e)
    }
    xhr.send()
  })

  return p
}

// search('Hello').then(console.log, console.error);

search('hello').then(result => {
  matches = result.match(/<div class="trans-container">([^]*?)<\/div>/)
  console.log(matches[1])
}, console.error)
```

### async

async 函数（包含函数语句、函数表达式、Lambda 表达式）会返回一个 Promise 对象，如果在函数中 return 一个直接量，async 会把这个直接量通过 Promise.resolve() 封装成 Promise 对象。Promise 的特点一—无待，所以在没有 await 的情况下执行 async 函数，它会立即执行，返回一个 Promise 对象，并且，并且不会阻塞后面的语句。

```js
async function testAsync() {
  return 'hello, async'
}

const result = testAsync()

console.log(result)

testAsync().then(v => {
  console.log(v)
})

// Promise { 'hello, async' }
// hello, async
```

await 不仅仅用于等 Promise 对象，它可以等任意表达式的结果，所以，await 后面实际是可以接普通函数调用或者直接量的。

如果它等到的不是一个 Promise 对象，那 await 表达式的运算结果就是它等到的东西。

如果它等到的是一个 Promise 对象，await 就忙起来了，它会阻塞后面的代码，等着 Promise 对象 resolve，然后得到 resolve 的值，作为 await 表达式的运算结果。

这就是 await 必须用在 async 函数中的原因。async 函数调用不会造成阻塞，它内部所有的阻塞都被封装在一个 Promise 对象中异步执行。

```js
function getSomething() {
  return 'something'
}

async function testAsync() {
  return Promise.resolve('hello async')
}

async function test() {
  const v1 = await getSomething()
  const v2 = await testAsync()
  console.log(v1, v2)
}

test()

// something hello async
```

#### Promise compare async

```js
function takeLongTime(n) {
  return new Promise(resolve => {
    setTimeout(() => resolve(n + 200), n)
  })
}

function step1(n) {
  console.log(`step1 with ${n}`)
  return takeLongTime(n)
}

function step2(n) {
  console.log(`step2 with ${n}`)
  return takeLongTime(n)
}

function step3(n) {
  console.log(`step3 with ${n}`)
  return takeLongTime(n)
}

function doIt() {
  const time1 = 100
  step1(time1)
    .then(time2 => step2(time2))
    .then(time3 => step3(time3))
    .then(result => {
      console.log(`doIt result is ${result}`)
    })
}

doIt()

async function doIt2() {
  const time1 = 100
  const time2 = await step1(time1)
  const time3 = await step2(time2)
  const result = await step3(time3)
  console.log(`doIt2 result is ${result}`)
}

doIt2()

// step1 with 100
// step1 with 100
// step2 with 300
// step2 with 300
// step3 with 500
// step3 with 500
// doIt result is 700
// doIt2 result is 700
```

#### async error

await

```js
function f1() {
  f2()
}

async function f2() {
  try {
    console.log(await f3())
  } catch (error) {
    console.log('******error******')
  }
}

// 不能直接用 async, await 返回 promise
// 必须返回异步函数 function () { throw new Error('error') } 的 promise 包装
async function f3() {
  await setTimeout(function() {
    throw new Error('error')
  }, 1000)
}

f1()

// D:\study\node\test.js:19
//     throw new Error('error')
//     ^

// Error: error
//     at Timeout._onTimeout (D:\study\node\test.js:19:11)
//     at listOnTimeout (internal/timers.js:531:17)
//     at processTimers (internal/timers.js:475:7)
```

promise

```js
function f1() {
  f2()
}

async function f2() {
  try {
    // 函数返回 promise 需要使用 await 调用
    // 否则: (node:16348) UnhandledPromiseRejectionWarning: Unhandled promise rejection
    // console.log(f3())
    console.log(await f3())
  } catch (error) {
    console.log('******error******')
  }
}

async function f3() {
  return new Promise((resolve, reject) => {
    setTimeout(function() {
      reject('error')
    }, 1000)
  })
}

f1()
// ******error******
```
