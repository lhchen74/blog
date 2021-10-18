---
title: 使用原生 JS Drag & Drop API 实现元素拖拽和文件拖放
tags: js
date: 2021-08-31
---

> 转载：[使用原生 JS Drag & Drop API 实现元素拖拽和文件拖放 - 峰华前端工程师](https://zxuqian.cn/docs/videos/browser/native-drag-drop)

有时候经常会好奇那些可视化拖拽的工具，还有拖放文件上传是怎么实现的，是不是得监听鼠标点击，移动和释放事件，然后同时计算新位置的坐标？其实不用那么麻烦，浏览器提供了内置的 Drag & Drop API，能很方便的实现拖拽功能。

<iframe src="https://player.bilibili.com/player.html?aid=459257162&amp;bvid=BV1i5411E7hk&amp;cid=299756621&amp;page=1" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="" class="videoFrame_d6vX" style="box-sizing: border-box; height: 500px; margin-top: 2vh; width: 754.75px; color: rgb(40, 61, 87); font-family: Raleway, &quot;PingFang SC&quot;, &quot;Microsoft Yahei&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"></iframe>

## 原理

Drag Drop API 的工作原理是：

-   给需要拖拽的元素添加 draggable 属性并设置为 true，然后添加 ondrag 事件。
-   给接收拖拽元素的放置元素同时设置 ondragover 和 ondrop 事件，必须在里边阻止默认事件，因为浏览器对拖拽事件默认的处理方式是禁止拖拽。

ondrag 事件是用于拖拽开始时，给事件添加一些数据，例如拖拽元素的 id。ondragover() 是当拖拽元素进入到放置区域时所触发的事件， ondrop 是元素放置后触发的事件。

## 示例

假设我们有一个需要拖拽的元素，使用一个蓝色的矩形表示，放在左边，还有一个放置区域，使用蓝色虚线表示，里边文案写着“请拖放到此区域”，放在右边。当拖拽左边元素到右边放置区域时，虚线变为橙色，放置成功后虚线变为绿色。现在来看一下怎么实现它。

### 结构与样式

首先定义 HTML 结构：

```html
<main>
    <div class="draggable-container">
        <div id="draggable" class="draggable" draggable="true"></div>
    </div>
    <div id="droppable" class="droppable"></div>
</main>
```

main 元素用于把页面划分为两列的栅格，并且这两列居中对齐：

```css
main {
    width: 100vw;
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr 1fr;
    place-items: center;
    background-color: hsl(0deg, 0%, 10%);
}
```

然后可拖拽的元素 id 为 draggable 放在了 draggable-container 容器中，这个容器是为了防止元素被拖走之后，栅格布局被破坏，所以需要它把第 1 列撑开，它也使用 grid 布局，把可拖拽的元素放到中间：

```css
.draggable-container {
    width: 100%;
    height: 100%;
    display: grid;
    place-items: center;
}
```

可拖拽的元素设置了 draggable 属性为 true，它的样式就是简单的设置了宽高、圆角和背景：

```css
.draggable,
.droppable {
    border-radius: 4px;
}
.draggable {
    width: 25vw;
    height: 25vw;
    background: #00d9ff;
}
```

droppable 为放置区域，它的样式与 draggable 类似，只是使用了虚线边框，且使用了相对定位，用于定位其中的文案。文案使用的是 ::before 伪元素设置的：

```css
.droppable {
    width: 30vw;
    height: 30vw;
    border: 8px dashed #00d9ff;
    position: relative;
    display: grid;
    place-items: center;
}
.droppable::before {
    display: block;
    content: "请拖放到此区域";
    position: absolute;
    color: white;
    font-family: sans-serif;
    font-size: 3vw;
    color: hsl(0, 0%, 30%);
}
```

使用 content 设置文本，并设置为 absolute 布局。接下来设置拖拽元素进入放置区域的边框样式和放置后的边框样式，最后设置文案的样式，在把拖拽元素放置好后，通过 z-index 把文案放在元素的下方：

```css
.dragover {
    border: 8px dashed #ffae00;
}
.dropped {
    border: 8px dashed #48ff00;
}
.dropped::before {
    z-index: -1;
}
```

### 拖拽事件

接下来看拖拽事件，首先获取 draggable 和 droppable 元素对象：

```javascript
const draggable = document.getElementById("draggable");
const droppable = document.getElementById("droppable");
```

给 draggable 可拖拽元素添加 dragstart 事件监听：

```javascript
draggable.addEventListener("dragstart", handleDragStart);
```

handleDragStart 监听器中使用事件中的 dataTransfer 属性，调用它的 setData() 方法添加了一个普通文本类型的数据，就是拖拽元素的 id。这里第 1 个参数可以是 MIME Type（text/html、image/png、text/uri-list） 也可以是自定义的类型。

```javascript
function handleDragStart(e) {
    e.dataTransfer.setData("text/plain", e.target.id);
}
```

接着给 droppable 放置区域添加 dragover 事件监听，在里边调用 preventDefault() 阻止默认事件，然后添加 dragover 样式把虚线设置为橙色：

```javascript
droppable.addEventListener("dragover", handleDragover);
function handleDragover(e) {
    e.preventDefault();
    droppable.classList.add("dragover");
}
```

再添加 dragleave 事件监听，当拖拽元素离开放置区域时，去掉 dragover 样式把边框颜色还原成蓝色：

```javascript
droppable.addEventListener("dragleave", handleDragLeave);
function handleDragLeave(e) {
    droppable.classList.remove("dragover");
}
```

最后添加 drop 事件监听，先阻止默认事件，然后通过 dataTransfer 的 getData() 方法获取拖拽元素的 id，这里的参数就是之前 setData() 中设置的 MIME Type，每种 MIME Type 只能设置一次，如果多次设置会覆盖前边的值，之后使用 document.getElementById() 获取到该元素并添加到放置区域中，把放置区域的边框设置为绿色：

```javascript
droppable.addEventListener("drop", handleDrop);
function handleDrop(e) {
    e.preventDefault();
    const draggedId = e.dataTransfer.getData("text/plain");
    droppable.appendChild(document.getElementById(draggedId));
    droppable.classList.add("dropped");
}
```

这样就完成了元素的拖拽功能。拖拽也支持从外部拖拽文件进来，例如拖进来的是一张图片，那么可以在 drop 事件监听中获取图片文件对象，然后生成 img 元素放置到预览区域中。例如把 droppable 改为接收拖拽的图片，先把 handleDrop() 事件处理函数中的代码注释掉，除了 e.preventDefault()，然后遍历 dataTransfer.items 属性，通过 item 中的 kind 属性判断是不是文件，如果是就调用 getAsFile() 方法获取文件对象，然后调用 createPreview() 生成预览。

```javascript
[...e.dataTransfer.items].forEach((item) => {
    if (item.kind === "file") {
        const file = item.getAsFile();
        createPreview(file);
    }
});
```

createPreview() 中首先判断文件的 MIME type 是否以 image/ 开头，不是就直接返回，这样它只接收图片类型的文件。接着创建一个 img 元素，并使用 URL.createObjectURL() 根据文件对象创建一个 object url，用作 image 的 src 属性，当图片加载之后这个 Object url 就没用了，所以监听 image 的 onload 事件，使用 URL.revokeObjectURL 把这个 url 回收掉，最后把图片追加到放置区域：

```javascript
function createPreview(imageFile) {
    if (!imageFile.type.startsWith("image/")) {
        return;
    }
    const image = document.createElement("img");
    image.src = URL.createObjectURL(imageFile);
    image.onload = function () {
        URL.revokeObjectURL(this.src);
    };
    droppable.appendChild(image);
}
```

图片也有一些 CSS 样式设置宽高和缩放形式：

```css
.droppable img {
    width: 80%;
    height: 80%;
    object-fit: contain;
}
```
