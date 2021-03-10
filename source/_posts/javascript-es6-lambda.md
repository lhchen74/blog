---
title: es6 lambda
tags: js
date: 2019-10-29
---

> 转载：[ES6 语法学习-JS 中的 lambda:箭头函数 - 胡飞飞的学习笔记 - CSDN 博客](https://blog.csdn.net/holmofy/article/details/79554611)

1.最基本的写法

使用=>操作符，简化匿名函数的定义

```js
(param1,param2,...,paramN) => {
// 函数体
}

// 参数列表与箭头符号不能换行
var func = ()
=> 1;
// SyntaxError: expected expression, got '=>'

// 注意解析的优先级
let callback;
callback = callback || function() {}; // ok
callback = callback || () => {};
// SyntaxError: invalid arrow-function arguments
// 需要加括号提高解析优先级
callback = callback || (() => {}); // ok
```

2.如果函数体只有一条语句，可以省略函数体的大括号

```js
(param1,param2,...,paramN) => expression
// 等价于
(param1,param2,...,paramN) => {
  return expression;
}
```

3.如果参数只有一个，可以省略参数列表的小括号

```js
singleParam => {
  statements
}
// 等价于
(singleParam) => {
  statements
}
```

4.如果函数没有参数，参数列表的小括号不能省略

```js
// 参数列表的小括号不能省略
() => {
  statements
}
```

5.当返回值是对象字面量时，为了避免函数体的大括号与对象字面量的大括号冲突，必须在字面量上加一对小括号

```js
params => ({ foo: bar })
```

6.使用可变参数

```js
(param1, param2, ...rest) => {
  statements
}
```

7.参数默认值

默认情况下参数默认值为 undefined，可以使用 param=defaultValue 的方式指定参数的默认值。

```js
(param1 = defaultValue1, param2 = defaultValue2, paramN = defaultValueN) => {
  statements
}
```

8.在参数列表中使用解构赋值

```js
// a+b+c = a+b+a+b
var f = ([a = 5, b = 6] = [1, 2], { x: c } = { x: a + b }) => a + b + c

f() // 6
f([3, 4]) // 14
f([3]) // 18
f([3, 4], { x: 5 }) // 12
```

9.对象解构赋值

```js
var materials = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium']

materials.map(function(material) {
  return material.length
}) // [8, 6, 7, 9]
// 等价于
materials.map(material => {
  return material.length
}) // [8, 6, 7, 9]
// 等价于
// 在参数列表中直接解构数组对象的 length 属性
materials.map(({ length }) => length) // [8, 6, 7, 9]
```

10.箭头函数没有绑定 this 变量

```js
// this 作用域问题

function Person() {
  // 构造函数中的 this 表示对象本身
  this.age = 0;

  setInterval(function growUp() {
    // 在 non-strict 模式中, growUp()函数中的 this 是全局对象
    // growUp 是全局函数，不是对象的方法
    this.age++;
    // 浏览器环境中全局对象为 window
    // window.age=undefined
    // undefined++ -> NAN
    // NAN++ -> NAN
    // 一直都是 NAN
    }, 1000);
}

var p = new Person();

// ES3/5 中，可以定义一个变量指向外部对象

function Person() {
  var that = this
  that.age = 0

  setInterval(function growUp() {
    // that 暂存了对象的引用
    that.age++
  }, 1000)
}

// 还有一种方式直接绑定函数的 this 对象
function Person() {
  this.age = 0

  setInterval(
    function growUp() {
      // 这时的 this 就是 Person 对象
      this.age++
    }.bind(this),
    1000
  )
}


// ES6 有了箭头函数，就不用这么麻烦了，因为箭头函数中没有 this 变量
function Person(){
  this.age = 0;

  setInterval(() => {
    // 这里的 this 对象就是 Person 对象
    this.age++;
  }, 1000);
}

var p = new Person();
```

11.箭头函数使用 call 和 apply 方法

```js
var func = (a, b) => a + b
func.call(null, 1, 2) // 3
func.apply(null, [1, 2]) // 3
```

12.箭头函数没有绑定 arguments 变量

```js
var arr = () => arguments[0]
arr() // ReferenceError: arguments is not defined

var arguments = [1, 2, 3]
// 因为箭头函数没有自己的 arguments
// 所以访问的是父作用域中的 arguments
var arr = () => arguments[0]
arr() // 1

// 使用可变参数作为 arguments 使用
var f = (...args) => args[0] + n

// 普通函数有自己的 arguments 变量
function foo(n) {
  var f = () => arguments[0] + n
  return f()
}

foo(1) // 2
```

13.箭头函数作为对象的方法，注意 this 的问题

```js
var obj = {
  i: 10,
  // 箭头函数没有 this,所以访问的是全局 this
  b: () => console.log(this.i, this),
  c: function() {
    console.log(this.i, this)
  }
}

obj.b() // undefined, Window {...} (or the global object)
obj.c() // 10, Object {...}
```

14.箭头函数不能作为构造函数

```js
var Foo = () => {
  this.age = 18
}
var foo = new Foo() // TypeError: Foo is not a constructor
```

15.箭头函数没有 prototype 属性

```js
var Foo = () => {}
console.log(Foo.prototype) // undefined
```

————————————————
版权声明：本文为 CSDN 博主「Holmofy」的原创文章，遵循 CC 4. BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/holmofy/article/details/79554611
