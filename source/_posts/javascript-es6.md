---
title: es6
tags: js
---

#### destructing

```js
let a = 'world',
  b = ('hello'[(a, b)] = [b, a])
console.log(a) // -> hello
console.log(b) // -> world

let cat = 'ken'
let dog = 'lili'
let zoo = { cat, dog }
console.log(zoo)

let dog = { type: 'animal', many: 2 }
let { type, many } = dog
console.log(type, many)
```

#### debug

```js
const a = 5,
  b = 6,
  c = 7
console.log({ a, b, c })
console.table({ a, b, c, m: { name: 'xixi', age: 27 } })
```

#### lambda

```js
// 寻找数组中的最大值
const max = arr => Math.max(...arr)
max([123, 321, 32]) // outputs: 321
// 计算数组的总和
const sum = arr => arr.reduce((a, b) => a + b, 2)
sum([1, 2, 3, 4]) // output: 12
```

#### array concat

```js
const one = ['a', 'b', 'c']
const two = ['d', 'e', 'f']
const three = ['g', 'h', 'i']
const result = [...one, ...two, ...three]
```

#### copy

```js
const person01 = { name: 'name01', age: 1 }
const person02 = { name: 'name01', age: 2 }
const person03 = { name: 'name03', age: 3 }

const arr = [person01, person02, person03]
const newArr = [...arr]
console.log(arr == newArr)
// false
console.log(newArr[0] === person01)
// true
```

#### named params

```js
const getStuffAwesome = ({id, name, force, verbose}) => {
  ...do stuff
}
getStuffAwesome({ id: 150, force: true, verbose: true })
```

#### default, rest

```js
//default
function animal(type) {
  type = type || 'cat'
  console.log(type)
}
animal() // ES5

function animal(type = 'cat') {
  console.log(type)
}
animal() // ES6

//reset
function animals(...types) {
  console.log(types)
}
animals('cat', 'dog', 'fish') //["cat", "dog", "fish"]
```

#### async/await

```js
const [user, account] = await Promise.all([fetch('/user'), fetch('/account')])
```

#### let, const

```js
//ES5只有全局作用域和函数作用域，没有块级作用域,使用var两次输出都是obama
var name = 'zach'
while (true) {
  var name = 'obama'
  console.log(name) //obama
  break
}
console.log(name) //obama

//let 新增块级作用域，用它所声明的变量，只在let命令所在的代码块内有效。
let name = 'zach'
while (true) {
  let name = 'obama'
  console.log(name) //obama
  break
}
console.log(name) //zach

//var會导致for循环变量泄露为全局变量
//变量i是var声明的，在全局范围内都有效。
//所以每一次循环，新的i值都会覆盖旧值，
//导致最后输出的是最后一轮的i的值
var a = []
for (var i = 0; i < 10; i++) {
  a[i] = function() {
    console.log(i)
  }
}
a[6]() // 10

//let不会导致for循环变量泄露
var a = []
for (let i = 0; i < 10; i++) {
  a[i] = function() {
    console.log(i)
  }
}
a[6]() // 6

//javascript中常见的一个问题
//我们本来希望的是点击不同的clickBox，显示不同的i，
//但事实是无论我们点击哪个clickBox，输出的都是5
var clickBoxs = document.querySelectorAll('.clickBox')
for (var i = 0; i < clickBoxs.length; i++) {
  clickBoxs[i].onclick = function() {
    console.log(i)
  }
}
//用闭包处理
//用函数参数保持变量的值
function iteratorFactory(i) {
  var onclick = function(e) {
    console.log(i)
  }
  return onclick
}
var clickBoxs = document.querySelectorAll('.clickBox')
for (var i = 0; i < clickBoxs.length; i++) {
  clickBoxs[i].onclick = iteratorFactory(i)
}

//const也用来声明变量，但是声明的是常量。一旦声明，常量的值就不能改变。
const PI = Math.PI
PI = 23 //Module build failed: SyntaxError: /es6/app.js: "PI" is read-only

//const有一个很好的应用场景，就是当我们引用第三方库的时声明的变量，
//用const来声明可以避免未来不小心重命名而导致出现bug：
const monent = require('moment')
```

#### class, extends, super

```js
class Animal {
  constructor() {
    this.type = 'animal'
  }
  says(say) {
    console.log(this.type + ' says ' + say)
  }
}

let animal = new Animal()
animal.says('hello') //animal says hello

class Cat extends Animal {
  constructor() {
    super()
    this.type = 'cat'
  }
}

let cat = new Cat()
cat.says('hello') //cat says hello

//super关键字，它指代父类的实例（即父类的this对象）。
//子类必须在constructor方法中调用super方法，否则新建实例时会报错。
//这是因为子类没有自己的this对象，而是继承父类的this对象，然后对其进行加工。
//如果不调用super方法，子类就得不到this对象。

//ES6的继承机制，实质是先创造父类的实例对象this（所以必须先调用super方法），
//然后再用子类的构造函数修改this。
```

#### arrow function

```js
function(i){ return i + 1; } //ES5
(i) => i + 1 //ES6

function(x, y) {
    x++;
    y--;
    return x + y;
} //ES5
(x, y) => {x++; y--; return x+y} //ES6



class Animal {
    constructor(){
        this.type = 'animal'
    }
    says(say){
        setTimeout(function(){
            console.log(this.type + ' says ' + say)
        }, 1000)
    }
}

var animal = new Animal()
animal.says('hi')  //undefined says hi
// 运行上面的代码会报错，这是因为setTimeout中的this指向的是全局对象。
// 所以为了让它能够正确的运行，传统的解决方法有两种：

// 第一种是将this传给self,再用self来指代this
says(say){
    var self = this;
    setTimeout(function(){
        console.log(self.type + ' says ' + say)
    }, 1000)

// 第二种方法是用bind(this),即
says(say){
    setTimeout(function(){
    console.log(self.type + ' says ' + say)
}.bind(this), 1000)

// 但现在我们有了箭头函数，就不需要这么麻烦了：
class Animal {
    constructor(){
        this.type = 'animal'
    }
    says(say){
        setTimeout( () => {
            console.log(this.type + ' says ' + say)
        }, 1000)
    }
}
var animal = new Animal()
animal.says('hi')  //animal says hi
// 当我们使用箭头函数时，函数体内的this对象，就是定义时所在的对象，而不是使用时所在的对象。
// 并不是因为箭头函数内部有绑定this的机制，实际原因是箭头函数根本没有自己的this，
// 它的this是继承外面的，因此内部的this就是外层代码块的this。
```

#### template string

```js
$('#result').append(
  'There are <b>' +
    basket.count +
    '</b> ' +
    'items in your basket, ' +
    '<em>' +
    basket.onSale +
    '</em> are on sale!'
)

$('#result').append(`
  There are <b>${basket.count}</b> items
   in your basket, <em>${basket.onSale}</em>
  are on sale!
`)
```
