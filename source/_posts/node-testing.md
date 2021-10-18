---
title: Node Test
tags: node
date: 2019-07-15
---

### Need test func

src/fn.js

```js
module.exports = {
  num1: n => parseInt(n),
  num2: n => Number(n)
}
```

src/math.js

```js
function sumOne(a, b) {
  const c = 1
  return a + b + c
}

module.exports = {
  add: (...args) => {
    return args.reduce((prev, cur) => {
      return prev + cur
    })
  },
  mul: (...args) => {
    return args.reduce((prev, cur) => {
      return prev * cur
    })
  },
  cover: (a, b) => {
    if (a > b) {
      return a - b - 1
    } else {
      return sumOne(a, b)
    }
  }
}
```

### assert

断言失败会抛出异常

test/assert_test.js

```js
const { add, mul } = require('../src/math')

const assert = require('assert')

assert.equal(add(2, 3), 5)
assert.equal(mul(2, 4), 6)

//   throw new AssertionError(obj);
//   ^

// AssertionError [ERR_ASSERTION]: 8 == 6
```

### chai

chai 不仅包含 assert 这种 TDD (测试驱动方式)，还包含 BDD (行为驱动方式)

test/chai_test.js

```js
const { add, mul } = require('../src/math')
const { should, expect, assert } = require('chai')

should()

// BDD
add(2, 3).should.equal(5)
expect(add(2, 3)).to.equal(5)

// TDD
assert.equal(add(2, 3), 5)
```

### mocha

test/mocha_test.js

```js
const { add, mul, cover } = require('../src/math')

const { should, expect, assert } = require('chai')

describe('#math', () => {
  describe('add', () => {
    it('should return 5 when 2 + 3', () => {
      expect(add(2, 3), 5)
    })

    it('should return 0 when -1 + 1', () => {
      expect(add(-1, 1), 0)
    })
  })
  describe('mul', () => {
    it('should return 6 when 2 * 3', () => {
      expect(mul(2, 3), 6)
    })

    it('should return 0 when 0 * 1', () => {
      expect(mul(0, 1), 0)
    })
  })

  describe('cover', () => {
    it('should retrun 0 when cover(3, 2)', () => {
      expect(cover(3, 2), 0)
    })

    it('should retrun 0 when cover(2, 3)', () => {
      expect(cover(2, 3), 6)
    })
  })
})

// mocha mocha_test.js

//   #math
//     add
//       √ should return 5 when 2 + 3
//       √ should return 0 when -1 + 1
//     mul
//       √ should return 6 when 2 * 3
//       √ should return 0 when 0 * 1
//     cover
//       √ should retrun 0 when cover(3, 2)
//       √ should retrun 0 when cover(2, 3)
```

### benchmark

test/benchmark_test.js

```js
const Benchmark = require('benchmark')
const suite = new Benchmark.Suite()
const { num1, num2 } = require('../src/fn')

suite
  .add('parseInt', () => {
    num1('123456')
  })
  .add('Number', () => {
    num2('123456')
  })
  .on('cycle', event => {
    console.log(String(event.target))
  })
  .on('complete', function() {
    console.log('Fastest is ' + this.filter('fastest').map('name'))
  })
  .run({ async: true })

// parseInt x 246,356,980 ops/sec ±2.37% (87 runs sampled)
// Number x 696,671,582 ops/sec ±1.12% (88 runs sampled)
// Fastest is Number

suite
  .add('RegExp#test', function() {
    ;/o/.test('Hello World!')
  })
  .add('String#indexOf', function() {
    'Hello World!'.indexOf('o') > -1
  })
  .add('String#match', function() {
    !!'Hello World!'.match(/o/)
  })
  // add listeners
  .on('cycle', function(event) {
    console.log(String(event.target))
  })
  .on('complete', function() {
    console.log('Fastest is ' + this.filter('fastest').map('name'))
  })
  // run async
  .run({ async: true })

// RegExp#test x 36,726,524 ops/sec ±2.85% (84 runs sampled)
// String#indexOf x 705,320,555 ops/sec ±0.99% (89 runs sampled)
// String#match x 13,646,421 ops/sec ±8.66% (63 runs sampled)
// Fastest is String#indexOf
```
