---
title: JavaScript Core
tags: js
date: 2019-07-10
---

### IIFE

Immediately Invoked Function Expression, 立即执行函数表达式。

```js
(function () {
    console.log("IIFE");
})();
```

### closure

闭包: 外部函数返回后，内部函数仍然可以访问外部函数变量。

```js
function outer() {
    let n = 0;

    function inner() {
        n += 1;
        console.log(n);
    }

    return inner;
}

f = outer();
f();
f();
f();
```

使用闭包定义私有变量。

```js
function Product() {
    let name;

    this.setName = function (value) {
        name = value;
    };

    this.getName = function () {
        return name;
    };
}

let q = Product();
let p = new Product();
console.log(typeof q, typeof p); // undefined object
p.setName("orange");
console.log(p.name, p.getName()); // undefined orange
```

### prototype

```js
function Rectangle(x, y) {
    this._length = x;
    this._breadth = y;
}

Rectangle.prototype.getDimensions = function () {
    return {
        length: this._length,
        breadth: this._breadth,
    };
};

r1 = new Rectangle(3, 4);
r2 = new Rectangle(2, 2);
console.log(r1.getDimensions(), r2.getDimensions());
```

### module

```javascript
const myModule = (function () {
    let n = 5;

    function print(x) {
        console.log(`The result is ${x}`);
    }

    function add(a) {
        let x = a + n;
        print(x);
    }

    return {
        description: "This is description",
        add: add,
    };
})();

console.log(myModule.description);
myModule.add(5);
```

### variable hoisting

```js
// in browser
var y;
console.log(y); // 2
y = 2;

// in node
// ReferenceError: y is not defined
```

### currying

```js
const add = (x) => (y) => x + y;

console.log(add(1)(2));
add1 = add(1);
console.log(add1(2));
```

### apply, call, bind

call, apply 指定 this 值调用函数, apply 第二个参数需要传递数组， bind 为函数绑定 this 值，然后作为一个新的函数返回。

```js
// const user = {
//     name: 'babb',
//     whatIsYourName: function () {
//         console.log(this.name)
//     }
// }

// user.whatIsYourName()
// const user2 = {
//     name: 'Babb'
// }
// user.whatIsYourName.call(user2)

const user = {
    greet: "Hello",
    greetUser: function (username) {
        console.log(this.greet + " " + username);
    },
};

const greet1 = {
    greet: "Hi",
};

user.greetUser.call(greet1, "Babb");
user.greetUser.apply(greet1, ["Babb"]);

greetHi = user.greetUser.bind(greet1);
greetHi("Babb");
```

### memoization

```js
function memoizeFunction(func) {
    let cache = {};
    return function () {
        let key = arguments[0];
        console.log(key);
        if (cache[key]) {
            return cache[key];
        } else {
            // console.log(this)
            let val = func.apply(this, arguments);
            // let val = func(arguments)
            cache[key] = val;
            return val;
        }
    };
}

const fabonacci = memoizeFunction(function (n) {
    return n === 0 || n === 1 ? n : fabonacci(n - 1) + fabonacci(n - 2);
});

console.log(fabonacci(3));
```
