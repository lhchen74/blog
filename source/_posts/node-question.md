---
title: node question
tags: node
date: 2019-07-15
description: node 和 js 中的一些比较疑惑的问题
---

### fetch & axios

为什么 axios 中可以通过 `res.data` 获取 json 数据，而 fetch 不可以直通过 `res.json()` 获取 json 数据 ?
因为 axios 和 fetch 实现不一样，fetch 中的第一个 then 返回的 res.json() 也是一个 promise。

```js
// chrome
fetch('https://jsonplaceholder.typicode.com/users')
  .then(res => res.json())
  .then(data => console.log(data))

// chrome/node
const axios = require('axios')

axios.get('https://jsonplaceholder.typicode.com/users').then(res => {
  console.log(res.data)
})
```
