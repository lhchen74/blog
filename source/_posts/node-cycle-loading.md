---
title: Node Cors
tags: node
date: 2019-07-10
---

### commonjs

commonjs 模块第一次加载之后就会被缓存起来，不会再加载第二次

a.js

```js
exports.done = false // 2
var b = require('./b.js') // 3
console.log('in a.js, b.done = %j', b.done) // 8 第三次
exports.done = true // 9
console.log('a.js process finish') // 10 第四次
```

b.js

```js
exports.done = false // 4
var a = require('./a.js') // 不会再重复加载，使用 main.js 加载过后缓存的模块
console.log('in b.js, a.done = %j', a.done) // 5  第一次
exports.done = true // 6
console.log('b.js process finish') // 7 第二次
```

main.js

```js
var a = require('./a.js') // 1
var b = require('./b.js') // 不会再重复加载，使用 a.js 加载过后缓存的模块

console.log('in main.js a.done=%j, b.done=%j', a.done, b.done) // 11 第五次
```

out conosle

```
in b.js, a.done = false
b.js process finish
in a.js, b.done = true
a.js process finish
in main.js a.done=true, b.done=true
```
