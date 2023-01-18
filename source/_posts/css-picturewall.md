---
title: CSS3 Picuturewall
tags: css
date: 2019-04-30
---

### css3 简介

CSS 用于控制网页的样式和布局。CSS3 是最新的 CSS 标准。

### css3 实现照片墙

#### index.html 主页

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>PictureWall</title>
        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <body>
        <h1>The Gril Of Anime</h1>
        <div id="container">
            <img class="pic1" src="image/103528_0.jpeg" />
            <img class="pic2" src="image/103528_1.jpeg" />
            <img class="pic3" src="image/103528_2.jpeg" id="music" />
            <img class="pic4" src="image/103528_3.jpeg" />
            <img class="pic5" src="image/103528_4.jpeg" />
            <img class="pic6" src="image/103528_5.jpeg" />
            <img class="pic7" src="image/103528_6.jpeg" />
            <img class="pic8" src="image/103528_7.jpeg" />
            <img class="pic9" src="image/103528_8.jpeg" />
            <img class="pic10" src="image/103528_9.jpeg" />
        </div>
        <div>
            <audio id="audio">
                <source src="audio/童话镇.mp3" type="audio/mpeg" />
                Your browser does not support the audio element.
            </audio>
        </div>
        <script>
            var arr = [
                "audio/童话镇.mp3",
                "audio/鸟之诗.mp3",
                "audio/犬夜叉.mp3",
            ];
            var audio = document.getElementById("audio");
            function playEndedHandler() {
                // 一首歌播放完毕后切换到下一首
                audio.src = arr.pop();
                audio.play();
                // 没有歌曲时解除事件监听
                !arr.length &&
                    audio.removeEventListener("ended", playEndedHandler, false);
            }

            document.getElementById("music").onclick = function () {
                // 监听音乐播放完毕事件
                audio.addEventListener("ended", playEndedHandler, false);
                // 点击 'music' 元素播放音乐暂停音乐
                if (audio.paused) {
                    audio.play();
                } else {
                    audio.pause();
                }
            };
        </script>
    </body>
</html>
```

#### style.css 样式表

```css
body {
    background: #eee;
    background-image: url("image/main.jpg");
}
h1 {
    text-align: center;
    color: #ccc;
    font-family: 华文行楷;
    word-spacing: 15px;
    font-size: 40px;
}
#container {
    width: 960px;
    height: 450px;
    margin: 50px auto;
    position: relative;
}
#container img {
    padding: 5px 5px 8px;
    background: #fff;
    border: 1px solid #ddd;
    position: absolute;
    width: 144px;
    height: 128px;
    -webkit-transition: 0.5s;
    -moz-transition: 0.5s;
    transition: 0.5s;
}
#container img:hover {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    transform: rotate(0deg);
    -webkit-transform: scale(1.5);
    -moz-transform: scale(1.5);
    transform: scale(1.5);
    box-shadow: 10px 10px 10px #ccc;
    z-index: 2;
}
.pic1 {
    top: 50px;
    left: 50px;
    -webkit-transform: rotate(20deg);
    -moz-transform: rotate(20deg);
    transform: rotate(20deg);
}
.pic2 {
    top: 50px;
    left: 200px;
    -webkit-transform: rotate(-20deg);
    -moz-transform: rotate(-20deg);
    transform: rotate(-20deg);
}
.pic3 {
    top: 50px;
    left: 350px;
    -webkit-transform: rotate(10deg);
    -moz-transform: rotate(10deg);
    transform: rotate(10deg);
}
.pic4 {
    top: 50px;
    left: 500px;
    -webkit-transform: rotate(-15deg);
    -moz-transform: rotate(-15deg);
    transform: rotate(-15deg);
}
.pic5 {
    top: 50px;
    left: 650px;
    -webkit-transform: rotate(50deg);
    -moz-transform: rotate(50deg);
    transform: rotate(50deg);
}
.pic6 {
    top: 200px;
    left: 650px;
    -webkit-transform: rotate(20deg);
    -moz-transform: rotate(20deg);
    transform: rotate(20deg);
}
.pic7 {
    top: 200px;
    left: 500px;
    -webkit-transform: rotate(-20deg);
    -moz-transform: rotate(-20deg);
    transform: rotate(-20deg);
}
.pic8 {
    top: 200px;
    left: 350px;
    -webkit-transform: rotate(-10deg);
    -moz-transform: rotate(-10deg);
    transform: rotate(-10deg);
}
.pic9 {
    top: 200px;
    left: 200px;
    -webkit-transform: rotate(-50deg);
    -moz-transform: rotate(-50deg);
    transform: rotate(-50deg);
}
.pic10 {
    top: 200px;
    left: 50px;
    -webkit-transform: rotate(10deg);
    -moz-transform: rotate(10deg);
    transform: rotate(10deg);
}
```

### 渲染效果

点击第三张图片播放音乐

![picture-wall](css-picturewall/picture-wall.png)

> [慕课网] https://www.imooc.com/
