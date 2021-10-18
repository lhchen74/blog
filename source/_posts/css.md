---
title: CSS
tags: css
date: 2020-04-18
---

### Unit

| 单位      | 含义                                                       |
| --------- | ---------------------------------------------------------- |
| px        | 一个像素点，1920 x 1080                                    |
| em        | 相对父容器的 font-size 的倍数                              |
| rem       | 相对根元素(html) font-size 的倍数                          |
| vw/vh     | 相对 viewport width/height 的百分比，100vw， 100% 视口宽度 |
| vmin/vmax | 相对荧幕较短的一边/较长的一边(一般用于手机横竖屏)          |

em，第一层 div 的 font-size 是 body font-size 的两倍，即 20px，第二层 div font-size 是第一层的两倍，即 40px, 第三层 div font-size 是第二层的两倍，即 80px.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>unit</title>
        <style>
            html {
                font-size: 30px;
            }

            body {
                font-size: 10px;
            }

            div {
                border: 2px solid black;
                margin: 4px;
                font-size: 2em;
            }
        </style>
    </head>
    <body>
        <div>
            Coding
            <div>
                Coding
                <div>Coding</div>
            </div>
        </div>
    </body>
</html>
```

![](css/c01.jpg)

rem，替换 上边 div 中的 font-size: 2em 为 font-size: 2rem, div 的 font-size 都为根元素 html font-size: 30px 的两倍即 60px

![](css/c02.jpg)

vw，vh， 100vw，100vh 可以全屏显示

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>viewport width & viewport height</title>
        <style>
            body {
                margin: 0;
                padding: 0;
            }

            .box {
                width: 50%;
            }

            .son {
                background-color: brown;
                width: 100vw;
                height: 100vh;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <div class="son"></div>
        </div>
    </body>
</html>
```

vw 和 % 区别是，vw 始终相对于视口，% 相对于父元素，将 div.son 中的 width: 100vw 替换为 width: 100%, 此时只会显示屏幕宽度的一半，因为 div.son 的父元素 div.box width: 50%.

![](css/c03.jpg)

### Shadow

css 中 shadow 包括 text-shaow 和 box-shadow, 常用形式分别为 `h-offset v-offset blur color` 和 `h-offset v-offset blur spread color` 其中 text-shadow 没有 spread 属性。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>shadow</title>
        <style>
            .box {
                width: 200px;
                height: 200px;
                background-color: yellow;
                /* h-offset v-offset blur spread color*/
                box-shadow: 20px 40px 10px 5px green;
            }

            h1 {
                font-size: 90px;
                color: red;
                /* h-offset v-offset blur color*/
                text-shadow: 4px 5px 4px #999;
            }
        </style>
    </head>
    <body>
        <div class="box"></div>
        <br />
        <h1>Hello</h1>
    </body>
</html>
```

![](css/c04.jpg)

### Center Layout

position + transform, 设置需要居中的原素 position: absolute, 然后 top: 50%, left: 50%, 此时元素的顶端距离浏览器顶端为浏览器高度的一边，左端离浏览器左端的距离为浏览器宽度的一半，最后 transform: translate(-50%, -50%); 将元素向左移动自身宽度的一半，向上移动自身高度的一半，即元素中心点距离浏览器顶端为浏览器高度的一边，离浏览器左端的距离为浏览器宽度的一半

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>center</title>
        <style>
            .box {
                width: 100px;
                height: 100px;
                position: absolute;
                /* 
                right: 50%;
                bottom: 50%;
                transform: translate(50%, 50%);
                */
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
                background-color: pink;
            }
        </style>
    </head>
    <body>
        <div class="box"></div>
    </body>
</html>
```

flex

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>center</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }

            .box {
                width: 100px;
                height: 100px;
                background-color: pink;
            }
        </style>
    </head>
    <body>
        <div class="box"></div>
    </body>
</html>
```

table

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>center</title>
        <style>
            .box {
                width: 100px;
                height: 100px;
                background-color: pink;
                display: inline-block; /*if not use inline, text-align no effect*/
            }

            body {
                display: table;
                width: 100%;
                min-height: 100vh;
            }

            .cell {
                display: table-cell;
                vertical-align: middle;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="cell">
            <div class="box">hello</div>
        </div>
    </body>
</html>
```

### Table

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>table</title>
    </head>
    <style>
        #customers {
            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
            width: 100%;
            border-collapse: collapse;
        }

        #customers td,
        #customers th {
            font-size: 1em;
            border: 1px solid #98bf21;
            padding: 3px 7px 2px 7px;
        }

        #customers th {
            font-size: 1.1em;
            text-align: left;
            padding-top: 5px;
            padding-bottom: 4px;
            background-color: #a7c942;
            color: #ffffff;
        }

        #customers tr.alt td {
            color: #000000;
            background-color: #eaf2d3;
        }
    </style>
    <body>
        <table id="customers">
            <tr>
                <th>Company</th>
                <th>Contact</th>
                <th>Country</th>
            </tr>
            <tr>
                <td>Alfreds Futterkiste</td>
                <td>Maria Anders</td>
                <td>Germany</td>
            </tr>
            <tr class="alt">
                <td>Berglunds snabbköp</td>
                <td>Christina Berglund</td>
                <td>Sweden</td>
            </tr>
            <tr>
                <td>Centro comercial Moctezuma</td>
                <td>Francisco Chang</td>
                <td>Mexico</td>
            </tr>
            <tr class="alt">
                <td>Ernst Handel</td>
                <td>Roland Mendel</td>
                <td>Austria</td>
            </tr>
            <tr>
                <td>Island Trading</td>
                <td>Helen Bennett</td>
                <td>UK</td>
            </tr>
            <tr class="alt">
                <td>Königlich Essen</td>
                <td>Philip Cramer</td>
                <td>Germany</td>
            </tr>
            <tr>
                <td>Laughing Bacchus Winecellars</td>
                <td>Yoshi Tannamuri</td>
                <td>Canada</td>
            </tr>
            <tr class="alt">
                <td>Magazzini Alimentari Riuniti</td>
                <td>Giovanni Rovelli</td>
                <td>Italy</td>
            </tr>
            <tr>
                <td>North/South</td>
                <td>Simon Crowther</td>
                <td>UK</td>
            </tr>
            <tr class="alt">
                <td>Paris spécialités</td>
                <td>Marie Bertrand</td>
                <td>France</td>
            </tr>
        </table>
    </body>
</html>
```

![](css/c05.jpg)

### Float and Overflow

float 元素父容器未设定高度

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>overflow</title>
        <style>
            .container {
                border: 1px solid green;
            }

            .container img {
                float: left;
                height: 100px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="../images/404.jpg" />
        </div>
    </body>
</html>
```

![](css/c06.jpg)

div.container 设定 height: 200px

![](css/c07.jpg)

div.container 设定 overflow: hidden, 删除 height: 200px, 在不给元素设置高度的情况下，将 overflow 设置为 hidden 时，它会显示内部元素的高度。

![](css/c08.jpg)

float + overflow 实现 navbar

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>page</title>
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 0;
            }

            ul.topmenu {
                list-style: none;
                margin: 0;
                padding: 0;
                /* 
                  Anything inside that might be floating does not get clipped unless you have the overflow set to either hidden, scroll or auto. 
                  The real magic of the method is that without having given the element a set height, when you set overflow to hidden it takes on the height of the inner elements.
                */
                overflow: hidden;
                background-color: #666;
            }

            ul.topmenu li {
                float: left;
            }

            ul.topmenu li a {
                display: inline-block;
                color: white;
                padding: 16px;
                text-decoration: none;
                text-align: center;
            }

            ul.topmenu li a:hover {
                background-color: #333;
            }

            ul.topmenu li a.active {
                background-color: #4caf50;
            }
        </style>
    </head>

    <body>
        <ul class="topmenu">
            <li><a class="active" href="">Home</a></li>
            <li><a href="">News</a></li>
            <li><a href="">Contact</a></li>
            <li><a href="">About</a></li>
        </ul>
    </body>
</html>
```

![](css/c09.jpg)

### Selector Specificity

(A, B, C, D) 前面的越大优先级越高

A: 行内样式 (可以被 !important 覆盖, !important 可以用来覆盖 bootstrap 等的行内样式 )

B: ID 选择器 #container

C: Class, 属性和伪类选择器 .title, input[type='text'], :hover

D: 类型和伪元素择器 div, ::before

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>priority</title>
        <style>
            html {
                font-size: 40px;
            }

            #container .menu.menu li.item2 {
                /* (0, 1, 3, 1) */
                color: purple;
            }
            #container li:nth-child(2).item2 {
                /* (0, 1, 2, 1) */
                color: yellow;
            }
            #container li.item2 {
                /* (0, 1, 1, 1) */
                color: green;
            }
            li.item2 {
                /* (0, 0, 1, 1) */
                color: blue;
            }
            item2 {
                /* (0, 0, 1, 0) */
                color: red;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <ul class="menu">
                <li id="item1" class="item1">项目1</li>
                <li class="item2">项目2</li>
                <li class="item3">项目3</li>
            </ul>
        </div>
    </body>
</html>
```

![](css/c10.jpg)

### Inline、Block and Inline-block

block 元素不设定宽度默认会占据一整行，inline, inline-block 会占据内容的宽度

block 元素水平居中使用 margin: 0 auto, inline, inline-block 水平居中使用 text-align:center

block, inline-block 元素可以设置宽度高度，inline 元素宽度高度设置无效

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>inline block</title>
        <style>
            * {
                margin: 0;
                padding: 0;
            }

            div {
                width: 50%;
                margin: 0 auto; /* 设置 block 元素水平居中*/
            }

            strong {
                display: inline-block;
            }

            div,
            span,
            strong {
                background-color: black;
                color: white;
            }

            body {
                text-align: center; /*设定 inline, inline-block 元素水平居中*/
            }

            span,
            strong {
                height: 100px;
            }
        </style>
    </head>
    <body>
        <div>Block</div>
        <span>Inline</span>
        <br />
        <strong>Inline-Block</strong>
    </body>
</html>
```

![](css/c11.jpg)

inline 元素的上下外边距无效，如果需要为 inline 元素设置上下外边距，需要将 dispaly 设置为 inline-block

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>box model</title>
        <style>
            strong {
                background-color: red;
                opacity: 0.6;
                margin: 10px;
                padding: 20px;
            }
        </style>
    </head>
    <body>
        <p>
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Doloribus,
            corrupti similique. Iste, minus modi?
            <strong>Aspernatur</strong> asperiores maxime aliquam repellat ea?
            Tenetur, deleniti repellendus et distinctio tempore error ab officia
            debitis? Lorem ipsum, dolor sit amet consectetur adipisicing elit.
            Laborum beatae dolor, maxime inventore, natus repellat vitae
            repellendus ex esse sit itaque dolorum deserunt totam ducimus cum,
            quas perferendis quia nulla!
        </p>
    </body>
</html>
```

![](css/c12.jpg)

为 strong 添加 disply: inline-block

![](css/c13.jpg)

### Grayscale

设置网页灰度

```html
<!DOCTYPE html>
<html lang="en" class="gray">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>grayscale</title>
        <style>
            html {
                filter: grayscale(100%);
            }
        </style>
    </head>
    <body>
        <img src="./grayscale.jpg" />
    </body>
</html>
```

![](css/c14.jpg)

### CSS image resize percentage of itself

> 引用：[html - CSS image resize percentage of itself? - Stack Overflow](https://stackoverflow.com/questions/8397049/css-image-resize-percentage-of-itself)

I am trying to resize an img with a percentage of itself. For example, I just want to shrink the image by half by resizing it to 50%. But applying `width: 50%;` will resize the image to be 50% of the container element (the parent element which maybe the `<body>` for example).

Question is, can I resize the image with a percentage of itself without using javascript or server side? (I have no direct information of the image size)

1. This method resize image only visual not it actual dimensions in DOM, and visual state after resize centered in middle of original size. you can use `transform-origin: top left` adjust scale origin.

    **html:**

    ```html
    <img src="example.png" />
    ```

    **css:**

    ```css
    .fake {
        transform-origin: top left;
        -webkit-transform: scale(0.5); /* Saf3.1+, Chrome */
        -moz-transform: scale(0.5); /* FF3.5+ */
        -ms-transform: scale(0.5); /* IE9 */
        -o-transform: scale(0.5); /* Opera 10.5+ */
        transform: scale(0.5);
        /* IE6–IE9 */
        filter: progid:DXImageTransform.Microsoft.Matrix(M11=0.9999619230641713, M12=-0.008726535498373935, M21=0.008726535498373935, M22=0.9999619230641713,SizingMethod='auto expand');
    }
    ```

2. The trick is to let the container element shrinkwrap the child image, so it will have a size equal to that of the unsized image. Thus, when setting `width` property of the image as a percentage value, the image is scaled relative to its original scale.

    **html:**

    ```html
    <span>
        <img src="example.png" />
    </span>
    ```

    **css:**

    ```css
    span {
        display: inline-block;
    }
    img {
        width: 50%;
        height: 50%;
    }
    ```

3. you can also take advantage of the newly introduced CSS3 `fit-content`. However, not all popular browser versions support it at the time of writing.

    **html:**

    ```html
    <figure>
        <img src="example.png" />
    </figure>
    ```

    **css:**

    ```css
    figure {
        height: fit-content;
        width: fit-content;
    }

    img {
        height: 50%;
        width: 50%;
    }
    ```

### Select not first child

-   使用 `not` 伪类选择器。

    ```css
    p:not(:first-child) {
        color: red;
    }
    ```

-   使用 `nth-child` 选择器，`nth-child(n + 2)` 中的 n 代表从 0 开始的自然数，n + 2 表示 `>= 2`的自然数。

    ```css
    p:nth-child(n + 2) {
        color: red;
    }
    ```

-   使用 `+ ` 选择器，表示选择紧跟着的兄弟元素。`p + p` 表示 p 元素相邻后面的 p 元素, 第一个 p 元素不会选中。`~` 表示选择所有后面所有的兄弟元素。

```css
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>CSS Not First Child</title>
        <style>
            p + p {
                color: red;
            }
        </style>
    </head>
    <body>
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
    </body>
</html>
```

Result:

![1629868296182](css/1629868296182.png)

### Tooltip by title attribute

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <style>
            div {
                width: 100px;
                height: 100px;
                background-color: violet;
            }
        </style>
    </head>
    <body>
        <div title="This is a violet div"></div>
    </body>
</html>
```

![1629869873425](css/1629869873425.png)

### offsetWidth, clientWidth, scrollWidth

offsetWidth: 包括所有边框的大小。如果元素有 display: block，则可以通过 width/height 和 padding 和 border 的和来计算

width(130px) + padding(10px _ 2) + border(5px _ 2) = 160px

clientWidth: 框内容的可视部分，不包括边框或滚动条，但包括填充。不能直接从 CSS 中计算，取决于系统的滚动条大小。

width(130px) + padding(10px \* 2) - scrollBarWidth(17px) = 133px

```js
const scrollbarWidth =
    ele.offsetWidth -
    ele.clientWidth -
    parseInt(getComputedStyle(ele).borderLeftWidth.replace("px", "")) -
    parseInt(getComputedStyle(ele).borderRightWidth.replace("px", ""));
```

scrollWidth: 框中所有内容的大小，包括当前隐藏在滚动区域之外的部分。不能直接从 CSS 计算，取决于内容。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use of offsetWidth, clientWidth and scrollWidth property</title>

        <style>
            #box {
                height: 100px;
                width: 130px;
                border: 5px black solid;
                padding: 10px;
                margin: 5px;
                overflow: scroll;
                background-color: aqua;
                /* box-sizing: border-box; */
                white-space: nowrap;
            }
        </style>
    </head>

    <body>
        <div id="box">
            Understanding offsetWidth, clientWidth, scrollWidth and -Height,
            respectively
        </div>

        <p>Click on button to get result</p>

        <button onClick="display()">Click Here!</button>

        <div id="result"></div>

        <script>
            function display() {
                const ele = document.getElementById("box");
                const osw = ele.offsetWidth;
                const sw = ele.scrollWidth;
                const cw = ele.clientWidth;

                document.getElementById("result").innerHTML =
                    "offsetWidth: " +
                    osw +
                    "px<br>clientWidth: " +
                    cw +
                    "px<br>scrollWidth : " +
                    sw +
                    "px";

                const scrollbarWidth =
                    ele.offsetWidth -
                    ele.clientWidth -
                    parseInt(
                        getComputedStyle(ele).borderLeftWidth.replace("px", "")
                    ) -
                    parseInt(
                        getComputedStyle(ele).borderRightWidth.replace("px", "")
                    );

                console.log(scrollbarWidth);
            }
        </script>
    </body>
</html>
```

![](css/c16.jpg)

### getComputedStyle

getcomputedstyle()方法在应用活动样式表并解决这些值可能包含的任何基本计算之后，返回一个对象，其中包含元素的所有 CSS 属性的值。单个 CSS 属性值可以通过对象提供的 api 访问，或者通过对 CSS 属性名称进行索引访问。

```
const style = window.getComputedStyle(element [, pseudoElt]);
```

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>getComputedStyle</title>
        <style>
            p {
                width: 400px;
                margin: 0 auto;
                padding: 20px;
                font: 2rem/2 sans-serif;
                text-align: center;
                background: purple;
                color: white;
            }

            h3::after {
                content: " rocks!";
            }
        </style>
    </head>
    <body>
        <p>Hello</p>

        <h3>Generated content</h3>
        <script>
            const paragraph = document.querySelector("p");
            const computedStyles = window.getComputedStyle(paragraph);
            console.log(computedStyles);

            paragraph.textContent = `font-size: ${computedStyles.getPropertyValue(
                "font-size"
            )}, line-height: ${computedStyles.getPropertyValue("line-height")}`;

            const h3 = document.querySelector("h3");
            const result = window.getComputedStyle(h3, ":after");
            console.log("the generated content is: ", result.content);
            console.log("font-size: " + result.fontSize);
        </script>
    </body>
</html>
```

![](css/c15.jpg)

### requestAnimationFrame

**window.requestAnimationFrame()** 告诉浏览器——你希望执行一个动画，并且要求浏览器在下次重绘之前调用指定的回调函数更新动画。该方法需要传入一个回调函数作为参数，该回调函数会在浏览器下一次重绘之前执行

**注意：若你想在浏览器下次重绘之前继续更新下一帧动画，那么回调函数自身必须再次调用 window.requestAnimationFrame()**

```
window.requestAnimationFrame(callback);
```

-   `callback`

    下一次重绘之前更新动画帧所调用的函数(即上面所说的回调函数)。该回调函数会被传入[`DOMHighResTimeStamp`](https://developer.mozilla.org/zh-CN/docs/Web/API/DOMHighResTimeStamp)参数，该参数与[`performance.now()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Performance/now)的返回值相同，它表示`requestAnimationFrame()` 开始去执行回调函数的时刻。

-   返回值

    一个 `long` 整数，请求 ID ，是回调列表中唯一的标识。是个非零值，没别的意义。你可以传这个值给 [`window.cancelAnimationFrame()`](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/cancelAnimationFrame) 以取消回调函数。

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>requestAnimationFrame</title>
    </head>
    <body>
        <div
            id="box"
            style="width: 200px; height: 200px; background-color: red;"
        ></div>

        <script>
            const element = document.getElementById("box");
            let start;

            function step(timestamp) {
                if (start === undefined) start = timestamp;

                console.log(timestamp);

                const elapsed = timestamp - start;

                element.style.transform =
                    "translateX(" + Math.min(0.1 * elapsed, 200) + "px";

                if (elapsed < 2000) {
                    window.requestAnimationFrame(step);
                }
            }

            window.requestAnimationFrame(step);
        </script>
    </body>
</html>
```

### Change Theme Schema

反转网站主题色

1 将背景设置为与原来相反的黑色，使用滤镜反转整个网页中的元素

```css
 {
    background: black;
    filter: invert(1) hue-rotate(180deg);
}
```

![](css/1593832966231.png)

2 图片需要保持原来的模样

```js
document.querySelectorAll("img").forEach((item) => {
    item.style.filter = "invert(1) hue-rotate(189deg)";
});
```

![](css/1593833238141.png)
