---
title: JavaScript Create Object
tags: js
date: 2019-07-10
---

javascript 对象创建方式

### prototype

```js
function Cat() {
    this.name = "mm";
}

Cat.prototype.makeSound = function () {
    console.log("o(∩_∩)o");
};

var cat = new Cat();
cat.makeSound();
```

### Object.create()

不能实现私有属性和私有方法，实例对象之间也不能共享数据

```js
var Cat = {
    name: "mm",
    makeSound: function () {
        console.log("o(∩_∩)o");
    },
};

var cat = Object.create(Cat);
cat.makeSound();
var cat1 = Object.create(Cat);
cat1.name = "mm1";
var cat2 = Object.create(Cat);
cat2.name = "mm2";
console.log(cat1.name, cat2.name); // mm1 mm2

// 有的浏览器不支持 create, 使用原型链定义 Object.create
if (!Object.create) {
    Object.create = function (o) {
        function F() {}
        F.prototype = o;
        return new F();
    };
}
```

### 调用函数返回对象

可以实现私有属性和私有方法，实例对象之间可以共享数据无，但是无法使用 instanceof 检查继承关系

```js
var Animal = {
    createNew: function () {
        var animal = {};
        animal.makeSound = function () {
            console.log("o(∩_∩)o");
        };
        return animal;
    },
};

var Cat = {
    sound: "喵喵",
    createNew: function () {
        var cat = Animal.createNew();
        // var sound = '喵喵'
        cat.name = "mm";
        cat.makeSound = function () {
            console.log(Cat.sound);
        };
        cat.changeSound = function (sound) {
            Cat.sound = sound;
        };
        return cat;
    },
};

var cat = Cat.createNew();
var cat2 = Cat.createNew();
cat.changeSound("呜呜");
console.log(cat.sound); // undefined
cat.makeSound(); // 呜呜
cat2.makeSound(); // 呜呜
// console.log(cat instanceof Cat) // Right-hand side of 'instanceof' is not callable
```
