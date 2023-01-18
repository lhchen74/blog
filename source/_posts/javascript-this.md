---
title: JavaScript This
tags: js
date: 2020-11-29
---

### this 是什么

this 是执行当前函数的对象(The object that is executing the current function)

-   以对象方法的形式调用 this 就是调用方法的对象
-   以普通函数的形式调用, this 在浏览器中是 window 对象, 在 node 中是 global 对象 (实际也是 window / global 对象的方法)
-   以构造函数的形式调用, this 是构造函数创建返回的对象
-   回调函数也是以普通函数的形式调用

#### 对象方法和普通函数中的 this

```js
const video = {
    title: "a",
    play() {
        console.log(this);
    },
};

video.stop = function () {
    console.log(this);
};

video.stop(); // { title: 'a', play: [Function: play], stop: [Function] }
video.play(); // { title: 'a', play: [Function: play], stop: [Function] }
stop = video.stop;
stop(); // Object [global] {}

function playVideo() {
    console.log(this);
}

playVideo(); // Object [global] {}
```

#### 构造函数中的 this

构造函数创建对象的过程 `const v = new Video("b");`

1. 创建空的对象 {}
2. this 指向空的对象 {}, 为 this 即 {} 设定属性
3. 返回 this

```js
function Video(title) {
    this.title = title;
    console.log(this);
}

const v = new Video("b"); // Video { title: 'b' }
```

#### 回调函数中的 this

如下 forEach 回调函数不是 video 的方法，是由 global/window 调用的普通函数，global 和 window 中没有定义 title，所以值是 undefined.

```js
const video = {
    title: "a",
    tags: ["a", "b", "c"],
    showTags() {
        this.tags.forEach(function (tag) {
            console.log(this.title, tag);
        });
    },
};

video.showTags();
// undefined a
// undefined b
// undefined c
```

### 回调函数 this 绑定问题解决方式

#### 函数参数指定 this

有些函数参数可以指定 this, 例如 forEach 第二个参数可以指定 this

```js
const video = {
    title: "a",
    tags: ["a", "b", "c"],
    showTags() {
        this.tags.forEach(function (tag) {
            console.log(this.title, tag);
        }, this);
    },
};

video.showTags();
// a a
// a b
// a c
```

#### 中间变量保存 this

使用变量存储容器对象中的 this, 如下使用 self 存储对象方法 showTags 中的 this, 在回调中使用 self 而不是 this.

```js
const video = {
    title: "a",
    tags: ["a", "b", "c"],
    showTags() {
        const self = this;
        this.tags.forEach(function (tag) {
            console.log(self.title, tag);
        });
    },
};

video.showTags();

// a a
// a b
// a c
```

#### bind/call/apply

使用 bind 函数返回的新函数不论以何种方式调用 this 都不会变是 bind 时指定的对象

```js
function playVideo(a, b) {
    console.log(this, a, b);
}
playVideo.call({ name: "Babb" }, 1, 2); // { name: 'Babb' } 1 2
playVideo.apply({ name: "Babb" }, [1, 2]); // { name: 'Babb' } 1 2
const fn = playVideo.bind({ name: "Babb" }); // { name: 'Babb' } 1 2
fn(1, 2);

const video = {
    title: "a",
    tags: ["a", "b", "c"],
    showTags() {
        this.tags.forEach(
            function (tag) {
                console.log(this.title, tag);
            }.bind(this)
        );
    },
};

video.showTags();

// a a
// a b
// a c
```

#### arrow function

箭头函数会从容器方法中继承 this

```js
const video = {
    title: "a",
    tags: ["a", "b", "c"],
    showTags() {
        this.tags.forEach((tag) => {
            console.log(this.title, tag);
        });
    },
};

video.showTags();

// a a
// a b
// a c
```
