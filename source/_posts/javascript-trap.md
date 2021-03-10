---
title: node trap
tags: node
date: 2019-07-15
---

### 1 / 0

在 node 中除以 0 不会产生异常

```js
console.log(0 / 0, 1 / 0, -1 / 0)
// NaN Infinity -Infinity
```

### undefined compare

undefined 可以和其它类型比较

```js
console.log(undefined < 1, undefined > 1, undefined < '1')
// false false false
```
