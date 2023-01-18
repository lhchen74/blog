---
title: JavaScript Apply
tags: js
date: 2019-07-15
---

### apply

`Function.apply(obj, args)`

-   obj：这个对象将代替 Function 类里 this 对象
-   args：这个是类数组，它将作为参数传给 Function(args->arguments)

call 和 apply 的意思一样, 只不过是参数列表不一样.

`Function.call(obj, param1, param2...)`

-   obj：这个对象将代替 Function 类里 this 对象
-   params：这个是一个参数列表

如下在 Student 中 `Person.apply(this, arguments)` 调用 Person, 但是 `Person 中的 this 是 new 出来的 Student 对象`，所以 student 对象上就有了 name, age 属性

```js
function Person(name, age) {
    this.name = name;
    this.age = age;
}

function Student(name, age, grade) {
    Person.apply(this, arguments);
    this.grade = grade;
}

let student = new Student("babb", 21, "一年级");
console.log(student.name, student.age);
// babb 21
```

缓存函数运行结果

```js
let memoize = function (f) {
    let cache = {};

    return function () {
        // console.log(arguments) // [Arguments] { '0': 1, '1': 2 }
        let arg_str = JSON.stringify(arguments);
        // console.log(arg_str) // {"0":1,"1":2}
        // arguments 是个类数组对象(有 length 属性) f.apply(f, [Arguments] { '0': 1, '1': 2 }) <=> f(1, 2)
        // ES6 中可以使用 f(...argumnets)
        cache[arg_str] = cache[arg_str] || f.apply(f, arguments);
        return cache[arg_str];
    };
};

function add(a, b) {
    console.log("call add");
    return a + b;
}

let addFunc = memoize(add);
console.log(addFunc(1, 2));
console.log(addFunc(1, 2));
console.log(addFunc(3, 4));
console.log(addFunc(3, 4));

// call add
// 3
// 3
// call add
// 7
// 7
```

### apply 的巧妙应用

#### 将一个数组传递给一个不接受数组作为参数的函数

ES6 中 可以使用 `...` 代替，例如 `let max = Math.max.apply(null,array) <=> let max = Math.max(...array)`

a) Math.max 可以实现得到数组中最大的一项

因为 Math.max 参数里面不支持 Math.max([param1,param2]) 也就是数组，但是它支持 Math.max(param1,param2,param3…)，所以可以根据刚才 apply 的那个特点来解决 `let max = Math.max.apply(null,array)`, 这样轻易的可以得到一个数组中最大的一项(apply 会将一个数组装换为一个参数接一个参数的传递给方法)，这块在调用的时候第一个参数给了一个 null,这个是因为没有对象去调用这个方法,我只需要用这个方法帮我运算,得到返回的结果就行,所以直接传递了一个 null 过去

注意: Math.max 方法的参数中只要有一个值被转为 NaN,则该方法直接返回 NaN

```js
> Math.max(1,null) //相当于 Math.max(1,0)
> 1
> Math.max(1,undefinded) //相当于 Math.max(1,NaN)
> NaN

> Math.max(0,-0) //正零比负零大,和==不同
> 0
> Math.max(-0,-1) //负零比-1 大
> -0
```

b) Array.prototype.push 可以实现两个数组合并

同样 push 方法没有提供 push 一个数组,但是它提供了 push(param1,param,…paramN) 所以同样也可以通过 apply 来装换一下这个数组,即:

```js
let arr1 = new Array("1", "2", "3");

let arr2 = new Array("4", "5", "6");

Array.prototype.push.apply(arr1, arr2);
```

3. 转换类数组对象为数组

```js
let a = Array("1", "2");
console.log(a); // [ '1', '2' ]

let b = Array.apply(null, [1, 2]);
console.log(b); // [ '1', '2' ]

// apply 第二个参数只要是个类数组对象就可以了，比如 {length: 2} 就可以看作一个类数组对象，长度是 2，每个元素是 undefined; 所以，Array.apply(null, { length: 2}) 相当于 Array(undefined, undefined)
Array(undefined, undefined, undefined, undefined, undefined);
let c = Array.apply(null, { length: 2 });
console.log(c); // [ undefined, undefined ]

let d = Array.apply(null, { 0: "a", 1: "b" });
console.log(d); // []
let e = Array.apply(null, { 0: "a", 1: "b", length: 2 });
console.log(e); // ['a', 'b']
```

#### 填补稀疏数组

apply 配合 Array(这里不需要加 new)使用,可以将数组中的缝隙填补为 undefined 元素, 因为 apply 不会忽略数组中的缝隙,会把缝隙作为 undefined 参数传递给函数

```js
console.log(Array.apply(null, ["a", , "b"])); // [ 'a', undefined, 'b' ]
// ES6 中也可以使用如下方式
// console.log(Array.from(['a', , 'b']))
// console.log([...['a', , 'b']])
```

> https://www.cnblogs.com/chenhuichao/p/8493095.html > https://www.cnblogs.com/ziyunfei/archive/2012/09/18/2690412.html > https://segmentfault.com/q/1010000006793990
