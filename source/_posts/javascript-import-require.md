---
title: JS 中的 import 和 require
tags: js
date: 2019-10-29
---

> 转载: [JS 中的「import」和「require 」 - 简书](https://www.jianshu.com/p/f1e54dde30c8)

`import` 和 `require` 是 JS 模块化编程使用的，是前端开发者们在性能探索中的又一大进步。

### 对模块化的理解

模块化是一种将系统分离成独立功能部分的方法，一个模块是为完成一个功能的一段程序或子程序。"模块"是系统中**功能单一**且**可替换**的部分。
模块化思想是从 java 上衍生过来的，他将所需要的功能封装成一个类，哪里需要就在哪里调用，JS 中没有类的说法，但它引入了这种思想，在 js 中用对象或构造函数来模拟类的封装实现模块化，而在 html 上，则使用`import`和`require`

### 所属规范

**require/exports** 是 CommonJS/AMD 中为了解决模块化语法而引入的
**import/export** 是 ES6 引入的新规范，因为浏览器引擎兼容问题，需要在 node 中用`babel`将 ES6 语法编译成 ES5 语法

### 调用时间

**require** 是运行时调用，所以理论上可以运作在代码的任何地方
**import** 是编译时调用，所以必须放在文件的开头

### 本质

**require** 是赋值过程，其实`require`的结果就是对象、数字、字符串、函数等，再把结果赋值给某个变量。它是普通的值拷贝传递。
**import** 是解构过程。使用`import`导入模块的属性或者方法是引用传递。且`import`是`read-only`的，值是单向传递的。`default`是 ES6 模块化所独有的关键字，`export default {}` 输出默认的接口对象，如果没有命名，则在`import`时可以自定义一个名称用来关联这个对象

### 语法用法展示

#### | require 的基本语法

在导出的文件中使用`module.exports`对模块中的数据导出，内容类型可以是字符串，变量，对象，方法等不予限定。使用`require()`引入到需要的文件中即可

在模块中，将所要导出的数据存放在`module`的`export`属性中，在经过 CommonJs/AMD 规范的处理，在需要的页面中使用`require`指定到该模块，即可导出模块中的`export`属性并执行赋值操作（值拷贝）

```jsx
// module.js
module.exports = {
    a: function () {
        console.log("exports from module");
    },
};
// sample.js
var obj = require("./module.js");
obj.a(); // exports from module
```

当我们不需要导出模块中的全部数据时，使用大括号包含所需要的模块内容。

```jsx
// module.js
function test(str) {
    console.log(str);
}
module.exports = {
    test,
};
// sample.js
let { test } = require("./module.js");
test("this is a test");
```

#### | import 的基本语法

使用`import`导出的值与模块中的值始终保持一致，即引用拷贝，采用 ES6 中解构赋值的语法，`import`配合`export`结合使用

```jsx
// module.js
export function test(args) {
    console.log(args);
}
// 定义一个默认导出文件, 一个文件只能定义一次
export default {
    a: function () {
        console.log("export from module");
    },
};

export const name = "gzc";
// 使用_导出export default的内容
import _, { test, name } from "./a.js";

test(`my name is ${name}`); // 模板字符串中使用${}加入变量
```

### 写法形式

#### | require/exports 方式的写法比较统一

```jsx
// require
const module = require('module')
// exports
export.fs = fs
module.exports = fs
```

#### | import/export 方式的写法就相对丰富些

```jsx
// import
import fs  from 'fs';
import { newFs as fs } from 'fs';  // ES6语法, 将fs重命名为newFs, 命名冲突时常用
import { part } from fs;
import fs, { part } from fs;
// export
export default fs;
export const fs;
export function part;
export { part1, part2 };
export * from 'fs';
```

### 要点总结

-   通过`require`引入基础数据类型时,属于复制该变量
-   通过`require`引入复杂数据类型时, 属于浅拷贝该对象
-   出现模块之间循环引用时, 会输出已执行的模块, 未执行模块不会输出
-   CommonJS 规范默认`export`的是一个对象,即使导出的是基础数据类型
