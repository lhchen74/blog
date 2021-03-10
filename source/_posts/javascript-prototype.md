---
title: javascript prototype
tags: js
---

```js
Number.prototype.add = function(x) {
  return this + x
}

Number.prototype.subtract = function(x) {
  return this - x
}

Number.prototype.iterate = function() {
  var result = []
  for (var i = 0; i < this; i++) {
    result.push(i)
  }
  return result
}

Number.prototype = Object.defineProperty(Number.prototype, 'double', {
  get: function() {
    return this + this
  }
})

Number.prototype = Object.defineProperty(Number.prototype, 'square', {
  get: function() {
    return this * this
  }
})

console.log((8)['add'](2), (8).add(2), 8..add(2))
console.log((8).add(2).subtract(2))
console.log((8).iterate())
console.log((8).double.square)
```
