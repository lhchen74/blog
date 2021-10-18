---
title: Html5
tags: html
date: 2020-07-17
---

> [路飞学城-学习文档](https://book.apeland.cn/details/489/#新的操作方法)

### HTML5 简介

HTML5 是 HTML 最新的修订版版，2014 年 10 月由 W3C 完成标准制定。它的设计的目的是为了在移动设备上支持多媒体。并且 HTML5 简单易学。

#### 什么是 HTML5

HTML5 是下一代标准。HTML4.01 的上个版本诞生于 1999 年,HTML5 目前为止仍然处于完善之中。然而，大部分现代浏览器已经具备了某些 HTML5 支持

#### HTML5 有趣的新特性

-   用于媒体播放的 video 和 audio 元素
-   新的特殊内容元素：比如`article`,`footer`,`header`,`nav`,`section`
-   新的表单控件：比如`calendar`、`date`、`time`、`email`、`url`、`search`
-   2D/3D 绘图&效果
-   支持对本地离线存储

#### HTML5 的文档声明

<!doctype> 声明必须位于 HTML5 文档中的第一行,使用非常简单:

```html
<!DOCTYPE html>
```

之前我们所编写的网页其实都是 HTML5 的文档，为了向后兼容。如果我们编写 HTML4 的文档声明，那么就可能不会兼容 HTML5 的新的标签支持。

#### HTML5 浏览器支持

最新版本的五个主流浏览器都支持某些 HTML5 特性，IE9 以上浏览器支持 HTML5 新特性。但是 IE8 以下的浏览器不支持

IE8 以下(包含 IE8)以下版本浏览器兼容 HTML5 的方法，我们必须使用 htmlshiv 垫片包，让其支持 HTML5 新特性

```html
<!--[if lt IE 9]>
<script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
<![endif]-->
```

### HTML5 新标签

#### 8 个新语义元素和新属性

`header`,`section`,`footer`,`aside`,`nav`,`main`,`article`,`figure`所有的这些元素都是**块级**元素

##### 所有的标签都支持 HTML5 新属性

| 属性            | 描述                                                                                                                           | 浏览器支持性                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| contenteditable | 规定是否可编辑元素的内容                                                                                                       | All                              |
| contextmenu     | 指定一个元素的上下文菜单。当用户右击该元素，出现上下文菜单                                                                     | 只有 Firefox 浏览器支持          |
| data-\*         | 嵌入自定义数据                                                                                                                 | All                              |
| draggable       | 规定元素是否可拖动。链接和图像默认是可拖动的。经常用它实现拖放操作                                                             | ie8 以下浏览器都支持，其它不支持 |
| hidden          | 规定对元素进行隐藏。如果使用该属性，则会隐藏元素，隐藏的元素不会被显示，可以通过 js 来设置 hidden 属性为 true,使得元素变得可见 | All                              |

##### 1.nav 标签

`<nav>` 标签定义导航链接的部分。

并不是所有的 HTML 文档都要使用到`<nav>`元素。`<nav>`元素只是作为标注一个导航链接的区域。

比如之前 HTML4 中我们定义导航的时候通常都这样写

```html
<div class="nav">
    <a href="#">python</a>
    <a href="#">linux</a>
    <a href="#">web前端</a>
    <a href="#">Java</a>
    <a href="#">Go</a>
</div>
```

通过 HTML5 的`nav`标签我们可以这样表示：

```html
<nav>
    <a href="#">python</a>
    <a href="#">linux</a>
    <a href="#">web前端</a>
    <a href="#">Java</a>
    <a href="#">Go</a>
</nav>
```

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702121619942.png)

##### 2.header 标签

`header`标签定义文档的头部区域，它是作为网页的头部介绍内容或者是导航链接栏的容器。在一个文档中，你可以定义多个`header`元素

> 注意：header 标签不能被放在`footer`、`address`或者另一个`header`元素内部

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702121522178.png)

##### 3.main 标签

标签规定文档的主要内容。一个文档中只有一个 main 元素。

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702122038020.png)

你会发现，把整个文档作为了主要内容。

##### 4.aside 标签

`aside`标签定义`article`标签外的内容。aside 的内容应该与附近的内容相关

比如像稀土掘金网站上

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702121436193.png)

##### 5.section 标签

section 标签定义了文档的某个区域。比如章节、头部、顶部或者文档的其他区域

```html
<section>
    <h2>小猿圈重大新闻</h2>
    <p>
        本阶段讲解HTML5+CSS3部分，下个阶段老师开始做直播课。欢迎大家光临。小猿圈上的视频全部免费
    </p>
</section>
```

比如这个网站 aside 侧边栏中定制了三个 section
![](https://book.apeland.cn/media/images/2019/07/15/image-20190702122333918.png)

##### 6.article 标签

定义页面独立的内容。必须是独立于文档的其余部分。

article 通常都应用在：

-   论坛帖子
-   博客文档
-   新闻故事
-   评论

##### 7.figure 标签

`figure`标签规定独立的流内容(图像、图标、照片、代码等)

`figure`元素的内容应该与主内容有关，同时元素的位置相对于主内容是独立的。如果被删除，则不应对文档流产生影响。

```html
<figure>
    <img src="flower.jpg" alt="My 女神" width="304" height="228" />
    <figcaption>我的女神照</figcaption>
</figure>
```

##### 8.footer 标签

定义文档或者文档一部分区域的页脚。该元素会包含文档闯作业的姓名、文档的版权信息、使用条款的链接、联系信息等等。在一个文档中，可以定义多个 footer。

比如小猿圈的底部就是用 footer

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702141520625.png)

#### 其它的新语义化标签

##### mark

高亮文本标签

```html
<p><mark> 元素用于 <mark>高亮</mark> 文本</p>
```

##### progress

用来显示一项任务的完成进度。

属性：

-   max 最大值
-   value 当前进度

```html
<progress value="70" max="100">70 %</progress>
```

##### address

个人或者某个组织的联系信息等等

```html
<address>
    <a href="mailto:jim@rock.com">mjj67890@163.com</a><br />
    <a href="tel:+13115552368">(311) 555-2368</a>
</address>
```

以上标签都是我们在网页中常见到的。还有很少可以在网页中见到的 HTML5 新标签。在这里我就不一一赘述了。大家可以参考这个链接去查阅相关资料：[新标签](https://developer.mozilla.org/zh-CN/docs/Web/Guide/HTML/HTML5/HTML5_element_list)

#### 新的表单特性

HTML5 新增了新的表单元素

-   datalist
-   keygen
-   output

##### datalist

该元素规定输入域的选项列表。规定了 form 或 input 应该拥有自动完成功能，都能够用户在自动完成域中开始输入是，浏览器应该在该域中显示填写的选项：

```html
<form action="">
    <input type="text" list="class" />
    <datalist id="class">
        <option value="hello world"></option>
        <option value="hello web"></option>
        <option value="hello Go"></option>
        <option value="hello python"></option>
    </datalist>
    <input type="submit" />
</form>
```

> 注意：input 中的 list 跟 datalist 中的 id 必须关联。

##### kegen(了解)

是提供一种验证用户的可靠方法，当提交表达时，会生成两个键，一个是私钥，一个是公钥。

私钥存储于客户端，公钥则被发送给服务器。公钥可用于之后验证用户的客户端证书

```html
<form action="hello.asp" method="get">
用户名: <input type="text" name="usr_name">
加密: <keygen name="security">
<input type="submit">
</form>>
```

##### output

用于不同类型的输出，比如计算或脚本输出

```html
<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
<input type="range" id="a" value="50">100 +
<input type="number" id="b" value="50">=
<output name="x" for="a b"></output>
</form>
```

#### HTML5 新的表单属性

##### form 新属性

**autocomplete 属性**

此属性规定 form 或 input 应该拥有自动完成功能

当用户在自动完成域中开始输入时，浏览器应该在该域中显示填写的选项

```html
<form action="" autocomplete="on">
    用户名: <input type="text" name="usr_name" >
    <input type="submit">
</form>
```

当刷新网页，再次输入内容，查看效果

**novalidate 属性**

是一个布尔值，当为 true 时，表示规定在提交表单时，不应该验证 form 或 input 域

如果给 input 的 type 改成 email。则我们在输入邮箱时通常自动验证。如图所示

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702154639700.png)

如果将 form 设置此属性，则可以直接提交。

```html
<form action="" autocomplete="on" novalidate="">
    用户名: <input type="text" name="usr_name" >
    email: <input type="email">
    <input type="submit">
</form>
```

##### input 新属性

**autofocus 属性**

在页面加载时，是否自动获得焦点

```
用户名: <input type="text" name="usr_name" autofocus>
```

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702155007003.png)

**formaction 属性**

该属性用于描述表单提交的 URL 地址。会覆盖 form 元素中的 action 属性。该属性用于`type='submit'`。

```html
<form action="" autocomplete="on" novalidate="">
    用户名: <input type="text" name="usr_name" autofocus>
    email: <input type="email">
    <input type="submit" value='提交到当前服务器'>
    <input type="submit" formaction="http://www.baidu.com" value='提交到百度服务器'>
</form>
```

**formenctype 属性**

该属性描述了表单提交到服务器的数据编码(只对 form 表单中 method=’post‘表单)

第一个提交按钮已默认编码发送表单数据，第二个提交按钮以 “multipart/form-data” 编码格式发送表单数据:

```html
<form action="" autocomplete="on" novalidate="" method='post'>
    用户名: <input type="text" name="usr_name" autofocus>
    email: <input type="email">
    <input type="submit" value='提交到当前服务器'>
    <input type="submit" formenctype="multipart/form-data" value="以 Multipart/form-data 提交">
</form>
```

**formmethod 属性**

formmethod 属性定义了表单提交的方式。

formmethod 属性覆盖了 `<form>`元素的 method 属性。

**注意:** 该属性可以与 type=”submit” 和 type=”image” 配合使用。

```html
<form action="" autocomplete="on" novalidate="" method='get'>
    用户名: <input type="text" name="usr_name" autofocus>
    email: <input type="email">
    <input type="submit" value='get提交'>
    <input type="submit" method= 'post' formenctype="multipart/form-data" value="post提交">
</form>
```

**formnovalidate 属性**

novalidate 属性是一个 boolean 属性.

novalidate 属性描述了 `<input>` 元素在表单提交时无需被验证。

formnovalidate 属性会覆盖 `<form>` 元素的 novalidate 属性.

**注意:** formnovalidate 属性与 type=”submit 一起使用

```html
<form action="">
    E-mail: <input type="email" name="userid" />
    <input type="submit" value="提交" />
    <input type="submit" formnovalidate value="不验证提交" />
</form>
```

**formtarget 属性**

formtarget 属性指定一个名称或一个关键字来指明表单提交数据接收后的展示。

```html
<form action="">
    用户名: <input type="text">
    密码: <input type="password">
    <input type="submit" formtarget="_blank" value="提交到一个新的页面上"> 
</form>
```

**height 和 width 属性**

定义一个图像提交按钮，使用 width 和 height 属性

```html
<input type="image" src="img_submit.gif" width="30" height="30" />
```

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702160933241.png)

**list 属性**

规定输入域的 datalist。datalist 是输入域的选项列表。前面有介绍

**multiple 属性**

规定`input`元素可以选择多个值。适用于像 input 标签：file

```
上传多个文件:选择图片:<input type='file' name= 'img' multiple>
```

**pattern 属性**

描述了一个正则表达式用于验证`input`元素的值

注意：适用于以下类型`input`标签:text,search,url,tel,email,passworld

```html
<form action="">
    请输入正确的账号:
    <input
        type="text"
        style="width: 200px;"
        placeholder="由字母,数字,下划线 组成,以字母开头 4-16位"
        pattern="^[a-zA-Z]\w{3,15}$"
        title="输入的账号不合法"
    />
    <input type="submit" value="提交" />
</form>
```

![](https://book.apeland.cn/media/images/2019/07/15/image-20190702162408170.png)

**required 属性**

规定必须在提交之前输入框不能为空。

```
用户名: <input type="text" name="usrname" required>
```

##### 新的 input 类型

HTML5 拥有多个表单的输入类型。这些新特性提供了更好的输入控制和验证

新的输入类型

```html
color : 取色
date : 日期选择器
datetime ：选择UTC时间
datetime-local: 选择一个日期和时间(无时区)
email：提交表单时。自动验证email的值是否有效
month：选择月份
number:输入数值
range：包含一定范围内数字值的输入域
search:搜索域
tel:输入电话号码字段
time:选择一个时间
url:输入包含URL地址
week:选择周和年
```

### HTM5 中的 API

#### 新的操作方法

##### 1.获取元素的方法

获取单个元素,参数可以是我们任意的选择器。

```html
document.querySelect('选择器');
```

获取多个元素，参数是任意的选择器

```html
document.querySelectAll('选择器');
```

##### 2.类的操作

**添加类**

```html
oDiv.classList.add('类名');
```

**移除类**

```html
oDiv.classList.remove('类名');
```

**检测类**

```html
oDiv.classList.contains('类名');
```

**切换类**

```html
oDiv.classList.toggle('类名');//有则删除，无则添加
```

##### 3.自定义属性

我们可以通过`data-自定义属性名`来给元素添加自定义的属性名。一旦添加完成之后。通过 JS 可以获取以及设置自定义属性。

比如定义一个`data-test`属性名

**获取自定义的属性名**

```html
oDiv.dataset.test
```

**设置自定义属性**

```html
oDiv.dataset.自定义属性名 = 值
```

#### 文件读取

读取文件，首先先得将文件上传，可以通过 input 的 type 为 file 的表单控件实现

```html
<input type="file" name="" />
```

其次，通过 FileReader 读取文件。读取完文件之后，会将结果存储在 result 属性中，而不是直接返回

##### FileReader 常用方法

```html
1.readAsBinaryString: 将文件读取为二进制编码
2.readAsDataURL: 将文件读取为DataURL
3.readAsText:将文件读取为文本
```

##### FileReader 提供的事件

```html
1.onabort
读取文件中断时触发
2.onerror
读取文件出错时触发
3.onload
读取文件完成时触发，只在读取成功后触发
4.onloadend
读取文件完成时触发，无论读取成功或失败都会触发
5.onloadstart
读取文件开始时触发
6.onprogress
正在读取文件
```

##### 读取文件实例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>read file</title>
</head>
<body>
    <input type="file" name="">
    <script type="text/javascript">
    var input = document.querySelector("input");
    input.onchange = function() {
        // 获取到文件
        var file = this.files[0];
        // 创建读取器
        var reader = new FileReader();
        // 开始读取
        reader.readAsText(file);
        // 文件读取完成后，获取读取的结果
        reader.onload = function() {
            console.log(reader.result);
        }
    }
    </script>
</body>
</html>
```

#### 获取网络状态

`window.navigator.onlione`返回浏览器的网络状态。联网状态返回 true,断网状态时返回 false。

**实例代码**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>network status</title>
</head>
<body>
    <script type="text/javascript">
    // 获取当前网络状态
    var state = window.navigator.onLine;
    if (state) {
        alert("联网状态");
    }
    else {
        alert("断网状态");
    }
    </script>
</body>
</html>
```

#### 地理位置定位

地理位置 api 允许用户向 web 应用程序提供他们的位置。处于隐私考虑，报告地理位置前会先请求用户许可

##### geolocation 对象

地理位置 API 通过`navigator.geolocation`提供

```html
if(navigator.geolocation){
    /*地理位置服务可用*/    
}else{
    /*地理位置服务不可用*/
}
```

##### 获取当前定位

```html
if(navigator.geolocation){
    /*地理位置服务可用*/
    navigator.geolocation.getCurrentPosition(function(postion){
        position.coords.latitude;//经度
        position.coords.longitude;//纬度
    })
}else{
    /*地理位置服务不可用*/
}
```

据我最近测试，目前原生获取经纬的度的方法已不起作用，多次测试，猜测可能导致的问题是因为国内对浏览器定位有限制。

##### 百度地图定位

所以，为了实现定位，我们还是用第三方的好啊。比如 [百度地图开发平台](http://lbsyun.baidu.com/index.php?title=jspopular3.0)，真的！！这个平台上想要什么都有。

```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
    body, html,#allmap {width: 100%;height: 100%;overflow: hidden;margin:0;font-family:"微软雅黑";}
    </style>
    <script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=您的密钥"></script>
    <title>地图展示</title>
</head>
<body>
    <div id="allmap"></div>
</body>
</html>
<script type="text/javascript">
    // 百度地图API功能
    var map = new BMap.Map("allmap");    // 创建Map实例
    map.centerAndZoom(new BMap.Point(116.404, 39.915), 11);  // 初始化地图,设置中心点坐标和地图级别
    //添加地图类型控件
    map.addControl(new BMap.MapTypeControl({
        mapTypes:[
            BMAP_NORMAL_MAP,
            BMAP_HYBRID_MAP
        ]}));      
    map.setCurrentCity("北京");          // 设置地图显示的城市 此项是必须设置的
    map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
</script>
```

效果显示:

![](https://book.apeland.cn/media/images/2019/07/15/image-20190704114429773.png)

> 注意：一定要去申请自己的密钥。

注册该网站完成之后，去这[申请密钥](http://lbsyun.baidu.com/apiconsole/key/create)

![](https://book.apeland.cn/media/images/2019/07/15/image-20190704114633680.png)

在这提供了大量的[Web 服务 API](http://lbsyun.baidu.com/index.php?title=webapi)

百度地图 Web 服务 API 为开发者提供 http/https 接口，即开发者通过 http/https 形式发起检索请求，获取返回 json 或 xml 格式的检索数据。用户可以基于此开发 JavaScript、C#、C++、Java 等语言的地图应用。

不过下面的服务都是一些接口。目前我们没有学习 Ajax 技术。大家可以关注一下这个技术。非常重要的。等咱们学到 Ajax 技术之后我们就可以使用此些服务。

![](https://book.apeland.cn/media/images/2019/07/15/image-20190704114838543.png)

#### 本地存储

HTML5 web 存储，一个比 cookie 更好的本地存储方式。

随着互联网的快速发展，基于网页的应用越来越普遍，同时也变得越来越复杂。为了满足各种各样的需求，会经常在本地存储大量的数据，传统方式我们会以 document.cookie 来进行存储，但是由于其存储大小只有 4k 左右，并且解析也相当的复杂，给开发带来诸多不便，HTML5 规范提出解决方案，使用 sessionStorage 和 localStorage 存储数据

##### localStorage

特点：

1. 永久存储
2. 多窗口共享
3. 容量大约为 20M

###### 常用方法

```html
window.localStorage.setItem(key,value); //设置存储的内容
window.localStorage.getItem(key); //获取内容
window.localStorage.removeItem(key);//删除内容
window.localStorage.clear(); //清空内容
```

##### sessionStorage

1. 生命周期为关闭当前浏览器窗口
2. 可以在同一个窗口下访问
3. 数据大小为 5M 左右

```html
window.sessionStorage.setItem(key,value); //设置存储的内容
window.sessionStorage.getItem(key); //获取内容
window.sessionStorage.removeItem(key);//删除内容
```

#### 音频 audio

HTML5 提供了播放音频文件的标准。直到现在，仍然不存在在网页上播放音频的标准。今天，大多数音频都是通过插件(比如 Flash)来播放的。然而，并非所有浏览器都拥有同样的插件。

##### 音频 audio

##### 基本使用

```html
<audio controls="controls">
    <source src="my.mp3" type="audio/mp3" />
    您的刘看齐不支持audio元素
</audio>
```

![](https://book.apeland.cn/media/images/2019/07/17/image-20190702171528902.png)

-   controls 属性添加音频的控件，播放、暂停和音量控件
-   autoplay:使音频自动播放
-   loop:使音频自动重复播放

在`<audio>`与`</audio>`之间插入浏览器不支持的提示文本。`audio`元素允许使用多个`source`标签，`source`标签可以链接不同的音频文件，浏览器将使用第一个支持的音频文件。

##### 浏览器支持

目前，此标签支持三种音视频格式文件：MP3/Wav 和 Ogg;

| 浏览器               | MP3 | Wav | Ogg |
| -------------------- | --- | --- | --- |
| Internet Explorer 9+ | YES | NO  | NO  |
| Chrome 6+            | YES | YES | YES |
| Firefox 3.6+         | YES | YES | YES |
| Safari 5+            | YES | YES | NO  |
| Opera 10+            | YES | YES | YES |

同样，audio 可以配合 JS 来实现自己的音乐播放器

大家可以参考 MDN`video`和`audio`标签的相关事件：[媒体对象相关事件](https://developer.mozilla.org/zh-CN/docs/Web/Guide/Events/Media_events),[DOM 相关事件](http://www.w3school.com.cn/tags/html_ref_audio_video_dom.asp)

##### 纯 js 实现古风音乐播放器

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>音乐播放器</title>
        <link type="text/css" href="css/style.css" rel="stylesheet" />
    </head>
    <body>
        <div class="btns-bg">
            <div class="PlayEy"></div>
            <div class="Btn"></div>
            <div class="Play">
                <audio
                    id="audios"
                    src="http://music.163.com/song/media/outer/url?id=504924216.mp3"
                ></audio>
            </div>
        </div>
        <script type="text/javascript" src="js/script.js"></script>
    </body>
</html>
```

style.css

```css
body {
    margin:0;
    background-repeat:no-repeat;
    background-position:50%;
    background-image:url(../img/page-bg.png);
    background-size:100% auto;
    background-color:#efebcb
}
.PlayEy {
    display:flex;
    justify-content:center;
    align-items:center;
    width:653px;
    height:653px;
    background:url(../img/bg_circle.png), url(../img/bg_center.png) no-repeat center;
    background-size:100% % auto
}
.Btn {
    position:absolute;
    display:flex;
    justify-content:center;
    align-items:center;
    width:95px;
    height:95px;
    background-color:#ff0;
    background:url(../img/btn-bg.png) no-repeat;
    animation:Btn-bg 3s linear infinite
}
.Play {
    position:absolute;
    width:29px;
    height:36px;
    background:red;
    background:url(../img/pause.png) no-repeat;
    transition:.5s
}
.btns-bg {
    display:flex;
    justify-content:center;
    align-items:center;
    margin:30px auto;
    width:653px;
    height:653px
}
@keyframes Btn-bg {
    from {
    }
    to {
        transform:rotate(360deg)
    }
}
```

script.js

```js
var i = 0;
var oPlayEy = document.getElementsByClassName("PlayEy")[0];
var oPlay = document.getElementsByClassName("Play")[0];
var audios = document.getElementById('audios');
oPlay.onclick = function () {
    var seii = setInterval(function () {
        (i == 360) ? i = 0: i++;
        oPlayEy.style.transform = "rotate(" + i + "deg)";
        if (audios.paused) {
            clearInterval(seii)
        }
    }, 30);
    if (audios.paused) {
        audios.play();
        oPlay.style.backgroundImage = "url(img/play.png)";
        oPlay.style.width = 32 + "px";
        oPlay.style.height = 32 + "px";
    } else {
        audios.pause();
        oPlay.style.backgroundImage = "url(img/pause.png)";
        oPlay.style.width = 29 + "px";
        oPlay.style.height = 36 + "px";
    }
}
```

#### 视频 video

##### 基本使用

```html
<video width="800" height="" controls="">
    <source src="Hero.mp4" type="video/mp4"></source>
<source src="Hero.ogv" type="video/ogg"></source>
<source src="Hero.webm" type="video/webm"></source>
当前浏览器不支持 video直接播放
</video>
```

![](https://book.apeland.cn/media/images/2019/07/17/image-20190702174917166.png)

<video>  元素提供了 播放、暂停和音量控件来控制视频。

同时`<video>` 元素也提供了 width 和 height 属性控制视频的尺寸.如果设置的高度和宽度，所需的视频空间会在页面加载时保留。如果没有设置这些属性，浏览器不知道大小的视频，浏览器就不能再加载时保留特定的空间，页面就会根据原始视频的大小而改变。

<video>  与</video>  标签之间插入的内容是提供给不支持 video 元素的浏览器显示的。
<video>  元素支持多个  <source>  元素. <source>  元素可以链接不同的视频文件。浏览器将使用第一个可识别的格式。

##### 浏览器支持

| 浏览器            | MP4                  | WebM | Ogg |
| ----------------- | -------------------- | ---- | --- |
| Internet Explorer | YES                  | NO   | NO  |
| Chrome            | YES                  | YES  | YES |
| Firefox           | YES                  | YES  | YES |
| Safari            | YES                  | NO   | NO  |
| Opera             | YES (从 Opera 25 起) | YES  | YES |

##### 简单视频的 DOM 操作

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <div class="box">
            <button id="playOrStop">播放/暂停</button>
        </div>
        <video width="800" height="">
            <source src="Hero.mp4" type="video/mp4"></source>
            <source src="Hero.ogv" type="video/ogg"></source>
            <source src="Hero.webm" type="video/webm"></source>
            当前浏览器不支持 video直接播放
        </video>
        <script type="text/javascript">
            var playOrStop  = document.getElementById('playOrStop');
            var video  = document.querySelector('video');
            console.dir(video);
            console.dir(playOrStop);
            playOrStop.onclick = function(){
                console.log(video.paused);
                if(video.paused){
                    video.play();
                }else{
                    video.pause();
                }
            }
        </script>
    </body>
</html>
```

#### HTML5 实现调用摄像头

要想实现调用摄像头，使用了 html5 的`getUserMedia()`API

代码如下：

```html
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title></title>
    </head>
    <body>
        <video id="video" autoplay style="width: 480px;height: 320px;"></video>
        <div>
            <button id="capture">拍照</button>
        </div>
        <!-- 展示拍摄的照片 -->
        <canvas id="canvas" width="480" height="320"></canvas>
        <script type="text/javascript">
            window.onload = function() {
                // 1.获取标签
                var video = document.getElementById('video');
                var capture = document.getElementById('capture');
                var ctx = document.getElementById('canvas').getContext('2d');
                // 调用媒体对象
                // 参数为constraints 一个约束对象  是video还是audio
                navigator.mediaDevices.getUserMedia({
                    video: {
                        width: 480,
                        height: 320
                    }
                }).then(function(stream) {
                    // 获取到window.URL对象
                    var URL = window.URL || window.webkitURL;
                    // 创建一个video的url字符串
                    try {
                        video.src = URL.createObjectURL(stream);
                    } catch (e) {
                        video.srcObject = stream;
                    }
                    // 视频播放
                    video.play();
                }).catch(function(err) {
                    console.log(err);
                })
                // 点击拍照按钮事件
                capture.onclick = function() {
                    ctx.drawImage(video,0,0,480,320);
                }
            }
        </script>
    </body>
</html>
```

### Canvas 画布

#### 基本用法

```html
<canvas id="canvas" width="150" height="150"></canvas>
```

`<canvas>`看起来跟`img`标签有点像，唯一不同的是它没有 src 属性和 alt 属性。实际上，canvas 标签只有两个属性:`width`和`height`。

如果没有设置宽度和高度，默认的 canvas 会初始化`width：300px,height:150px`

##### 渲染上下文对象

`canvas`标签创造了一个固定大小的画布，它有一个或者多个**渲染上下文对象**，用它可以绘制和处理要展示的内容。接下来我们把注意力放在 2D 渲染上下文中。

canvas 起初是空白的。为了展示，首先脚本需要找到渲染上下文，然后在它的上面绘制。`canvas`元素有一个叫做 `getContext()`的方法，这个方法是用来获得渲染上下文和它的绘画功能。`getContext()`只有一个参数，上下文的格式。

```html
var canvas = document.getElementById('myCanvas');//获取绘画上下文对象var ctx =
canvas.getContext('2d');
```

打印结果：

![](https://book.apeland.cn/media/images/2019/07/15/image-20190703092814320.png)

#### 绘制形状

在这里你将学会如何绘制矩形、三角形、直线、圆弧和曲线。如果想绘制比较复杂的图形，我们需要掌握路径。

##### 栅格(了解)

![](https://book.apeland.cn/media/images/2019/07/15/image-20190703093242883_85zZ35d.png)

##### 绘制矩形常用 API

绘制一个填充的矩形

```html
fillRect(x,y,width,height);
```

绘制一个矩形的边框

```html
strokeRect(x, y, width, height)
```

清除指定矩形区域，让清除部分完全透明。

```html
clearRect(x, y, width, height)
```

上面提供的方法之中每个都包含了相同的参数。x 和 y 指定了 canvas 画布上所绘制的矩形的左上角(相对于原点)的坐标。width 和 height 设置矩形的尺寸。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title></title>
    </head>
    <body>
        <canvas
            id="myCanvas"
            width="300"
            height="300"
            style="border:1px solid #666;"
        ></canvas>
        <script type="text/javascript">
            var canvas = document.getElementById("myCanvas");
            var ctx = canvas.getContext("2d");
            ctx.fillRect(25, 25, 100, 100);
            ctx.clearRect(45, 45, 60, 60);
            ctx.strokeRect(50, 50, 50, 50);
        </script>
    </body>
</html>
```

效果显示:

![](https://book.apeland.cn/media/images/2019/07/15/image-20190703094320517.png)

##### 填充颜色和描边颜色设置

```html
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');
ctx.fillStyle = 'red';//填充颜色
ctx.strokeStyle = 'green';//描边颜色
```

#### 使用路径绘制图形

图形的基本元素是路径。路径是通过不同颜色和宽度的线段或曲线相连形成的不同形状的点的集合。一个路径，甚至一个子路径，都是闭合的。使用路径绘制图形我们需要做以下几步。

1. **创建路径起始点**
2. **使用画布的各种方法划出路径**
3. **然后把路径封闭**
4. **一旦路径生成，你就能通过描边或填充路径区域来渲染图形**

##### 绘制路径常用 api

###### beginPath()

```
新建一条路径，生成之后，图形绘制api被指向到路径上生成路径。无参数
```

###### closePath()

```
闭合路径之后图形绘制api又重新指向了上下文中
```

###### stroke()

```
 通过线条来绘制图形轮廓
```

###### fill()

```
通过填充路径的内容区域生成实心的图形
```

###### moveTo(x,y)

```
:将画笔移动到指定的坐标x以及y上
```

当 canvas 初始化或者`beginPath()`调用后，你通常会使用`moveTo()`函数设置起点。我们也能够使用`moveTo()`绘制一些不连续的路径

###### lineTo(x,y)

```
:绘制直线，绘制一条从当前位置到指定x以及y位置的直线
```

该方法有两个参数：x 以及 y ，代表坐标系中直线结束的点。开始点和之前的绘制路径有关，之前路径的结束点就是接下来的开始点，等等。。。开始点也可以通过`moveTo()`函数改变。

看个例子：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="myCanvas" width="300" height="300" style="border:1px solid #666;"></canvas>
        <script type="text/javascript">
            var canvas = document.getElementById('myCanvas');
            var ctx = canvas.getContext('2d');
            // 填充三角形
            ctx.beginPath();
            ctx.moveTo(25, 25);
            ctx.lineTo(105, 25);
            ctx.lineTo(25, 105);
            ctx.fill();
            // 描边三角形
            ctx.beginPath();
            ctx.moveTo(125, 125);
            ctx.lineTo(125, 45);
            ctx.lineTo(45, 125);
            ctx.closePath();
            ctx.stroke();
        </script>
    </body>
</html>
```

效果展示：
![](https://book.apeland.cn/media/images/2019/07/15/image-20190703103427898.png)

###### arc()

绘制圆弧或者圆

```html
arc(x,y,radius,startAngle,endAngle,anticlockwise);
```

圆心在 (x, y) 位置，半径为 radius ，根据 anticlockwise （默认为顺时针）指定的方向从 startAngle 开始绘制，到 endAngle 结束。

anticlockwise:可选的，布尔值，如果为 true，逆时针绘制圆弧，反之，顺时针绘制

**笑脸例子**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="myCanvas" width="300" height="300" style="border:1px solid #666;"></canvas>
        <script type="text/javascript">
            var canvas = document.getElementById('myCanvas');
            var ctx = canvas.getContext('2d');
            ctx.beginPath();
            ctx.arc(75, 75, 50, 0, Math.PI * 2, true); // 绘制
            ctx.moveTo(110, 75);
            ctx.arc(75, 75, 35, 0, Math.PI, false); // 口(顺时针)
            ctx.moveTo(65, 65);
            ctx.arc(60, 65, 5, 0, Math.PI * 2, true); // 左眼
            ctx.moveTo(95, 65);
            ctx.arc(90, 65, 5, 0, Math.PI * 2, true); // 右眼
            ctx.stroke();
        </script>
    </body>
</html>
```

效果展示：

![](https://book.apeland.cn/media/images/2019/07/15/image-20190703104809071.png)

###### quadraticCurveTo(cp1x,cp1y,x,y)

```
绘制二次贝塞尔曲线,cp1x,cp1y为一个控制点，x,y为结束点
```

###### bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)

```
绘制三次贝塞尔曲线，cp1x,cp1y为控制点一，cp2x,cp2y为控制点二，x,y为结束点。
```

看图：
![](https://book.apeland.cn/media/images/2019/07/15/image-20190703102603167.png)

参数 x、y 在两个方法中都是结束点坐标。cp1x,cp1y 为坐标的第一个控制点(上图中的红色点)，cp2x,cp2y 为坐标中的第二个控制点

**二次贝赛尔曲线绘制对话气泡**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title></title>
    </head>
    <body>
        <canvas
            id="myCanvas"
            width="300"
            height="300"
            style="border:1px solid #666;"
        ></canvas>
        <script type="text/javascript">
            var canvas = document.getElementById("myCanvas");
            var ctx = canvas.getContext("2d");
            ctx.beginPath();
            ctx.moveTo(75, 25);
            ctx.quadraticCurveTo(25, 25, 25, 62.5);
            ctx.quadraticCurveTo(25, 100, 50, 100);
            ctx.quadraticCurveTo(50, 120, 30, 125);
            ctx.quadraticCurveTo(60, 120, 65, 100);
            ctx.quadraticCurveTo(125, 100, 125, 62.5);
            ctx.quadraticCurveTo(125, 25, 75, 25);
            ctx.stroke();
        </script>
    </body>
</html>
```

效果展示:

![](https://book.apeland.cn/media/images/2019/07/15/image-20190703103214627.png)

三次贝塞尔曲线绘制

```
//三次贝塞尔曲线 ctx.beginPath(); ctx.moveTo(75,40); ctx.bezierCurveTo(75,37,70,25,50,25); ctx.bezierCurveTo(20,25,20,62.5,20,62.5); ctx.bezierCurveTo(20,80,40,102,75,120); ctx.bezierCurveTo(110,102,130,80,130,62.5); ctx.bezierCurveTo(130,62.5,130,25,100,25); ctx.bezierCurveTo(85,25,75,37,75,40); ctx.fill();
```

效果展示:

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703105124830.png)

###### rect(x,y,width,height)

```
绘制矩形
```

> 注意：当你调用 fill()函数时，所有没有闭合的形状都会自动闭合，所以你需要调用 closePath()函数。但是调用 stroke()时不会自动闭包

#### 样式和颜色

-   fillStyle = color:设置图形的填充颜色
-   strokeStyle = color: 设置图形边框的颜色
-   globalAlpha :设置透明度值，取值范围为 0~1 之间的数值
-   lineWidth = value:设置线条宽度，数值无单位
-   lineCap = type 设置线段末端的样式
    -   type:butt 默认值，方形
    -   type:round 圆形
    -   type:square 以方形结束，但是增加一个宽度和线段相同，宽度是线段宽度一半的矩形区域
-   lineJoin = type:设定线条和线条连接的样式
    -   type:round 通过填充一个额外的，圆心在相连部分末端的扇形，绘制拐角的形状。 圆角的半径是线段的宽度。
    -   type:bevel 在相连部分的末端填充一个额外的以三角形为底的区域， 每个部分都有各自独立的矩形拐角。
    -   type: miter 通过延伸相连部分的外边缘，使其相交于一点，形成一个额外的菱形区域

#### 绘制文本

canvas 提供了两种方法来渲染文本

-   `filleText(text,x,y,[,maxWidth])`

在指定的(x,y)位置填充指定的文本，绘制的最大宽度是可选的

-   `strokeText(text,x,y,[,maxWidth])`

在指定的(x,y)位置绘制文本边框，绘制的最大宽度是可选的

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="canvas" width="500" height="200" style="border: 1px solid #666;"></canvas>
        <script type="text/javascript">
            var canvas = document.getElementById('canvas');
            var ctx = canvas.getContext('2d');
            // 设置字体大小和字体
            ctx.font = '30px 微软雅黑';
            ctx.fillText('hello world',50,50);
            ctx.strokeText('hello world',50,80);
        </script>
    </body>
</html>
```

效果：

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703111440124.png)

##### 有样式的文本

-   `font = value`

当前我们用来绘制文本的样式. 这个字符串使用和 `CSS font`属性相同的语法. 默认的字体是 `10px sans-serif`。

-   `textAlign = value`

文本对齐选项. 可选的值包括：`start`, `end`, `left`, `right` or `center`. 默认值是 `start`。

-   `textBaseline = value`

基线对齐选项. 可选的值包括：`top`, `hanging`, `middle`, `alphabetic`, `ideographic`, `bottom`。默认值是 `alphabetic。`

-   `direction = value`

文本方向。可能的值包括：`ltr`, `rtl`, `inherit`。默认值是 `inherit。`

#### 使用图片

canvas 更有意思的一项特性就是图像操作能力。可以用于动态的图像合成或者作为图形的背景，以及游戏界面（Sprites）等等。浏览器支持的任意格式的外部图片都可以使用，比如 PNG、GIF 或者 JPEG。 你甚至可以将同一个页面中其他 canvas 元素生成的图片作为图片源。

引入图像到 canvas 里需要以下两步基本操作：

1. 获得一个指向`HTMLImageElement`的对象或者另一个 canvas 元素的引用作为源，也可以通过提供一个 URL 的方式来使用图片
2. 使用`drawImage()`函数将图片绘制到画布上

##### 核心方法

`drawImage(imgObj,x,y,width,height,dx,dy,dWith,dHeight)`

其中 imgObj 是 image 或者 canvas 对象，x 和 y 是在 canvas 里的起始坐标。后面两个参数是可选的，默认是当前画布设置的大小。这两个参数用来控制当前 canvas 缩放的大小。

如果是 8 个参数，用来控制做切片显示，前四个参数是定义图像源后的切片位置和大小，后四个参数是定义切片的目标显示的位置和大小

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703121156876.png)

**例子：一个简单的线图**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="canvas" width="500" height="500"></canvas>
        <script type="text/javascript">
            var ctx = document.getElementById('canvas').getContext('2d');
            var img = new Image();
            img.onload = function() {
                ctx.drawImage(img, 0, 0);
                ctx.beginPath();
                ctx.moveTo(123, 400);
                ctx.lineTo(198, 350);
                ctx.lineTo(300, 200);
                ctx.lineTo(500, 150);
                ctx.stroke();
            }
            img.src = 'image-20190703114102416.png';
        </script>
    </body>
</html>
```

效果展示：

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703114728769.png)

#### 状态的保存和恢复

`save()`

保存画布的所有状态

`restore()`

save 和 restore 方法是用来保存和恢复 canvas 状态的。都没有参数。

**栗子：**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="canvas" width="200" height="200"></canvas>
        <script type="text/javascript">
            function draw(){
                var ctx = document.getElementById('canvas').getContext('2d');
                ctx.fillRect(0,0,150,150);//默认绘制一个矩形
                ctx.save();//保存当前状态
                ctx.fillStyle = 'red'; //在原有配置基础上对颜色发生改变
                ctx.fillRect(15,15,120,120);
                ctx.save();//保存当前状态
                ctx.fillStyle = 'green'; //再次改变颜色
                ctx.globalAlpha = 0.5; //改变透明度
                ctx.fillRect(30,30,90,90);//使用新的配置绘制一个矩形
                ctx.restore(); //重载之前的颜色状态 (红色)
                ctx.fillRect(45,45,60,60); //使用上一次的配置绘制一个矩形
                ctx.restore(); //加载默认的颜色配置
                ctx.fillRect(60,60,30,30); //使用默认配置绘制矩形
            }
            draw();
        </script>
    </body>
</html>
```

效果展示：

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703141914667.png)

##### 移动 translate

`translate(x,y)`

translate 方法接收两个参数。x 是左右偏移量，y 是上下偏移量。**在做变形之前先保存状态是良好的一个习惯**

**栗子**

```html
function draw() {
  var ctx = document.getElementById('canvas').getContext('2d');
  for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
      ctx.save();
      ctx.fillStyle = 'rgb(' + (51 * i) + ', ' + (255 - 51 * i) + ', 255)';
      ctx.translate(10 + j * 50, 10 + i * 50);
      ctx.fillRect(0, 0, 25, 25);
      ctx.restore();
    }
  }
}
```

效果：

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703143629007.png)

##### 旋转

`rotate(angle)`

只接受一个参数：选装的角度。顺时针方向

#### 基本动画

如何通过 canvas 来制作动画呢？

步骤：

1. **清空 canvas**

    通过`clearReact()`来清空 canvas，保证自己的画布是干净的

2. **保存 canvas 状态**

3. **绘制动画图形**

4. **恢复 canvas**状态

##### 操控动画的方法

`setInterval(functuon,delay)`

在设定好间隔时间后，function 会定期执行

`setTimeout(function,delay)`

在设定好的时间之后执行函数

`requestAnimationFrame(callback)`

此方法一般每秒钟回到函数执行 60 次。告诉浏览器你希望执行一个动画，并在重绘之前，请求浏览器执行一个特定的函数来更新动画。

**做三个案例效果**

**1.太阳系动画**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="canva" width="500" height="500"></canvas>
        <script type="text/javascript">
            window.onload = function() {
                var sun = new Image();
                var moon = new Image();
                var earth = new Image();
                /* 初始化方法 */
                function init() {
                    sun.src = "sun.png";
                    moon.src = "moon.png";
                    earth.src = "earth.png";
                    window.requestAnimationFrame(draw);
                }
                function draw() {
                    // 1.获取上下文
                    var ctx = document.getElementById('canva').getContext('2d');
                    ctx.globalCompositeOperation = 'destination-over';
                    // 2.清空canvas
                    ctx.clearRect(0, 0, 500, 500);
                    // 3.设置背景填充色和边框色
                    ctx.fillStyle = "rgba(0,0,0,0.4)";
                    ctx.strokeStyle = "rgba(0,153,255,0.4)";
                    // 4.保存状态
                    ctx.save();
                    // 5.设置位移
                    ctx.translate(150, 150);
                    // 6.地球
                    var time = new Date();
                    // 6.1 地球选装
                    ctx.rotate(((2 * Math.PI) / 60) * time.getSeconds() + ((2 * Math.PI) / 60000) * time.getMilliseconds());
                    // 6.2 地球位移
                    ctx.translate(105, 0);
                    // 6.3 填充图形
                    ctx.fillRect(0, -12, 50, 24); // Shadow
                    ctx.drawImage(earth, -12, -12);
                    // Moon
                    ctx.save();
                    ctx.rotate(((2 * Math.PI) / 6) * time.getSeconds() + ((2 * Math.PI) / 6000) * time.getMilliseconds());
                    ctx.translate(0, 28.5);
                    ctx.drawImage(moon,-2.5,-2.5);
                    ctx.restore();
                    ctx.restore();//恢复到初始的状态
                    // 开始画圆
                    ctx.beginPath();
                    // 画圆
                    ctx.arc(150, 150, 105, 0, Math.PI * 2, false); // Earth orbit
                    // 描边
                    ctx.stroke();
                    ctx.drawImage(sun, 0, 0, 300, 300);
                    window.requestAnimationFrame(draw);
                }
                init();
            }
        </script>
    </body>
</html>
```

效果展示：

![](https://book.apeland.cn/media/images/2019/07/18/3.gif)

#### 高级动画

**制作高级动画小球**

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <canvas id="canvas" width="600" height="300" style="border: 1px solid #000000;"></canvas>
        <script type="text/javascript">
            var canvas = document.getElementById('canvas');
            var ctx = canvas.getContext('2d');
            var raf;
            var running = false;
            var ball = {
                x: 100, //x坐标
                y: 100, //y坐标
                vx: 5, //x轴方向步伐
                vy: 2, //y轴方向步伐
                radius: 25, //半径
                color: 'blue', //颜色
                drawBall: drawBall // 画的动作
            }
            // 画球的方法
            function drawBall() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
                ctx.closePath();
                ctx.fillStyle = this.color;
                ctx.fill();
            }
            function clear() {
                ctx.fillStyle = 'rgb(255,255,255,0.3)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            }
            function draw() {
                clear();
                // 之前用clearReact()方法来清除前一帧动画,换成filleReact()方法来实现长尾效果
                // ctx.clearRect(0, 0, canvas.width, canvas.height);
                ball.drawBall();
                ball.x += ball.vx;
                ball.y += ball.vy;
                // 处理边界
                if (ball.y + ball.vy > canvas.height || ball.y + ball.vy < 0) {
                    ball.vy = -ball.vy;
                }
                if (ball.x + ball.vx > canvas.width || ball.x + ball.vx < 0) {
                    ball.vx = -ball.vx;
                }
                raf = window.requestAnimationFrame(draw);
            }
            // canvas.addEventListener('mouseover', function() {
            //     raf = window.requestAnimationFrame(draw);
            // });
            canvas.addEventListener('mousemove', function(e) {
                if(!running){
                    clear();
                    ball.x = e.clientX;
                    ball.y = e.clientY;
                    ball.drawBall();
                }
            });
            canvas.addEventListener('click', function() {
                if(!running){
                    window.requestAnimationFrame(draw);
                    running = true;
                }
            });
            canvas.addEventListener('mouseout', function() {
                window.cancelAnimationFrame(raf);
                running = false;
            });
            ball.drawBall();
        </script>
    </body>
</html>
```

效果显示:

![](https://book.apeland.cn/media/images/2019/07/18/4.gif)

### SVG

SVG 是一种基于 XML 语法的图像格式，全称是可缩放矢量图（Scalable Vector Graphics）。其他图像格式都是基于像素处理的，SVG 则是属于对图像的形状描述，所以它本质上是文本文件，体积较小，且不管放大多少倍都不会失真。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703180548964.png)

#### 语法以及常用标签

##### 1.svg 标签

SVG 代码都放在顶层标签`SVG`之中

```html
<svg width="100%" height="100%">
    <circle id="mycircle" cx="50" cy="50" r="50" />
</svg>
```

`svg`的`width`属性和`height`属性，指定 SVG 图像在 HTML 元素中所占据的宽度和高度。如果不指定，默认大小是 300px 宽，150px 高

##### 2.circle 标签

`circle`标签代表圆形

```html
<svg width="300" height="180">
    <circle cx="30" cy="50" r="25" />
    <circle cx="90" cy="50" r="25" class="red" />
    <circle cx="150" cy="50" r="25" class="fancy" />
</svg>
```

上面代码定义了三个圆。`circle`标签`cx`,`cy`,`r`属性分别为横坐标、纵坐标和半径，单位为像素。坐标都是相对于`svg`画布的左上角原点。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184136878.png)

`class`属性用来指定对应的 css 类

```
.red {    fill: red;}.fancy {    fill: none;    stroke: black;    stroke-width: 3pt;}
```

SVG 的 CSS 属性与网页元素有所不同。

-   fill：填充色
-   stroke：描边色
-   stroke-width：边框宽度

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184122130.png)

##### 3.line 标签

`line`标签用来绘制直线

```html
<line x1="0" y1="0" x2="200" y2="0" style="stroke:rgb(0,0,0);stroke-width:5" />
```

-   x1：线段起点的横坐标
-   y1：起点纵坐标
-   x2： 终点的横坐标
-   y2：终点的纵坐标
-   style：线段的样式

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184106728.png)

##### 4.polyline 标签

绘制一根折线

```html
<polyline points="3,3 30,28 3,53" fill="none" stroke="black" />
```

`<polyline>`的`points`属性指定了每个端点的坐标，横坐标与纵坐标之间与逗号分隔，点与点之间用空格分隔。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184032294.png)

##### 5.rect 标签

绘制矩形

```
 <rect x="0" y="0" height="100" width="200" style="stroke: #70d5dd; fill: #dd524b" />
```

`<rect>`的`x`属性和`y`属性，指定了矩形左上角端点的横坐标和纵坐标；`width`属性和`height`属性指定了矩形的宽度和高度（单位像素）。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184018489.png)

##### 6.ellipse 标签

绘制椭圆

```html
<ellipse
    cx="60"
    cy="60"
    ry="20"
    rx="40"
    stroke="black"
    stroke-width="5"
    fill="silver"
/>
```

`<ellipse>`的`cx`属性和`cy`属性，指定了椭圆中心的横坐标和纵坐标（单位像素）；`rx`属性和`ry`属性，指定了椭圆横向轴和纵向轴的半径（单位像素）。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184003935.png)

##### 7.polygon 标签

绘制多边形

```html
<polygon
    fill="green"
    stroke="orange"
    stroke-width="1"
    points="0,0 100,0 100,100 0"
/>
```

`<polygon>`的`points`属性指定了每个端点的坐标，横坐标与纵坐标之间与逗号分隔，点与点之间用空格分隔。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703183951130.png)

##### 8.path 标签

制作路径

```html
<path
    d="  M 18,3  L 46,3  L 46,40  L 61,40  L 32,68  L 3,40  L 18,40  Z"
></path>
```

`<path>`的`d`属性表示绘制顺序，它的值是一个长字符串，每个字母表示一个绘制动作，后面跟着坐标

-   M：移动到（moveto）
-   L：画直线到（lineto）
-   Z：闭合路径

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703183915762.png)

##### 9.text 标签

绘制文本

```html
<text x="50" y="25">Hello World</text>
```

`<text>`的`x`属性和`y`属性，表示文本区块基线（baseline）起点的横坐标和纵坐标。文字的样式可以用`class`或`style`属性指定。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703183854326.png)

##### 10.use 标签

复制一个形状

```html
<circle id="myCircle" cx="5" cy="5" r="4" /><use
    href="#myCircle"
    x="10"
    y="0"
    fill="blue"
/><use href="#myCircle" x="20" y="0" fill="white" stroke="blue" />
```

`<use>`的`href`属性指定所要复制的节点，`x`属性和`y`属性是`<use>`左上角的坐标。另外，还可以指定`width`和`height`坐标。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703183805232.png)

##### 11.g 标签

用于将多个形状组成一个组(group),方便复用

```html
<g id="myCircle">
    <text x="25" y="20">圆形</text> <circle cx="50" cy="50" r="20" /></g
><use href="#myCircle" x="100" y="0" fill="blue" /><use
    href="#myCircle"
    x="200"
    y="0"
    fill="white"
    stroke="blue"
/>
```

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703183727008.png)

##### 12.defs 标签

用于自定义形状。它内部的代码不会显示，仅供引用

##### 13.image 标签

用于插入图片文件

```html
<image xlink:href="img_submit.gif" width="20%" height="20%" />
```

`<image>`的`xlink:href`属性表示图像的来源。

![](https://book.apeland.cn/media/images/2019/07/18/image-20190703184914061.png)

##### 14.animate 标签

产生动画效果

```html
<rect x="0" y="0" width="100" height="100" fill="#feac5e">
    <animate
        attributeName="x"
        from="0"
        to="500"
        dur="2s"
        repeatCount="indefinite"
/></rect>
```

矩形会在水平反向上不断移动，产生动画效果。

-   attributeName：发生动画效果的属性名。
-   from：单次动画的初始值。
-   to：单次动画的结束值。
-   dur：单次动画的持续时间。
-   repeatCount：动画的循环模式。

![](https://book.apeland.cn/media/images/2019/07/18/5.gif)

定制多个 animate

```html
<animate
    attributeName="x"
    from="0"
    to="500"
    dur="2s"
    repeatCount="indefinite"
/><animate attributeName="height" to="500" dur="2s" repeatCount="indefinite" />
```

![](https://book.apeland.cn/media/images/2019/07/18/6.gif)

##### 15.animateTransform 标签

```html
<rect x="250" y="250" width="50" height="50" fill="#4bc0c8">
    <animateTransform
        attributeName="transform"
        type="rotate"
        begin="0s"
        dur="10s"
        from="0 200 200"
        to="360 400 400"
        repeatCount="indefinite"
/></rect>
```

`<animateTransform>`的效果为旋转（`rotate`），这时`from`和`to`属性值有三个数字，第一个数字是角度值，第二个值和第三个值是旋转中心的坐标。`from="0 200 200"`表示开始时，角度为 0，围绕`(200, 200)`开始旋转；`to="360 400 400"`表示结束时，角度为 360，围绕`(400, 400)`旋转。

![](https://book.apeland.cn/media/images/2019/07/18/7.gif)

关于 SVG 其实跟 canvas 差不了多少，都是可以做一下复杂的图形和动画效果。SVG 的入门教学先写到这里。如果有同学在公司用到了 SVG 的高级特效，可以参考 MDN[SVG](https://developer.mozilla.org/zh-CN/docs/Web/SVG)。

### 拖拽/拖放

拖放(drap&drop)在我们平时的工作中，经常遇到。它表示：抓取对象以后拖放到另一个位置。目前，它是 HTML5 标准的一部分。

#### 拖放的基本操作

```
选中=>拖动=>释放
```

##### 选中

在 H5 标准中，为了使元素克拖动，把`draggable`属性设置为`true`。文本、图片和链接式默认可以拖放的，它们的`draggable`属性默认被设置了 true。

图片和链接按住鼠标左键选中，就可以拖放。

文本只有在被选中的情况下才能拖放。如果显示设置为恩本的`draggable`属性为`true`,按住鼠标左边也可以直接拖放。

**语法**

```html
<element draggle="true|false|auto"></element>
```

-   true: 可以拖动
-   false: 禁止拖动
-   auto: 跟随浏览器定义是否可以拖动

##### 拖动

每个可拖动的元素，在拖动过程中，都会经历三个过程：

```
拖动开始=>拖动过程中=>拖动结束
```

| 对象             | 事件名称  | 描述                     |
| ---------------- | --------- | ------------------------ |
| 被拖动的元素对象 | dragstart | 在元素开始被拖动时候触发 |
|                  | drag      | 在元素被拖动时反复触发   |
|                  | dragend   | 在拖动操作完成时触发     |

| 对象     | 事件名称  | 描述                                         |
| -------- | --------- | -------------------------------------------- |
| 目标对象 | dragenter | 当被拖动元素进入目标元素占据的屏幕空间时触发 |
|          | dragover  | 当被拖动元素在目标元素内时触发               |
|          | dragleave | 当被拖动元素没有放下就离开目标元素时触发     |

> 注意:dragenter 和 dragover 事件的默认行为是拒绝接受任何被拖放的元素。因此，我们必须阻止浏览器这种默认行为。e.prevenDefault();

##### 释放

到达目的地之后，释放元素事件

| 对象     | 事件名称 | 描述                                                               |
| -------- | -------- | ------------------------------------------------------------------ |
| 目标对象 | drop     | 当被拖动元素在目标元素里放下时触发，一般需要取消浏览器的默认行为。 |

看个例子演示每个 API

```html
<!DOCTYPE HTML>
<html>
    <head>
        <title>拖放示例-文本</title>
    </head>
    <style>
        #current{
            border: 1px solid #000;
            padding: 20px;
            margin-bottom: 20px;
        }
        #target{
            border: 1px solid #f00;
            width: 400px;
            height: 400px;
        }
        .box{
            width: 100px;
            height: 100px;
            border: 1px solid #FF6700;
        }
    </style>
    <body>
        <p>不能被拖拽的文字</p>
        <div id="current">
            <div class="text" id="text">
                <p draggable="true">可拖拽的文字</p>
                <img src="img_submit.gif" alt="">
                <div class="box" draggable="true"></div>
            </div>
        </div>
        <div id="target"></div>
        <script>
            var text = document.getElementById('text');
            var target = document.getElementById('target');
            text.ondragstart = function(event){
                console.log('元素开始被拖动');
            }
            text.ondrag = function(e){
                // console.log('一直被拖拽着');
            }
            text.ondragend = function(e){
                console.log('拖拽操作完成时触发');
            }
            target.ondragenter = function(e){
                console.log('进入了所要的目标对象中');
                e.preventDefault()
            }
            target.ondragover = function(e){
                console.log('在目标元素内触发');
                e.preventDefault();
            }
            target.ondragleave = function(e){
                console.log('拖拽着元素没有放下，并离开目标对象时');
                // e.preventDefault();
            }
            target.ondrop = function(event){
                console.log('被拖拽元素在目标元素里放下是触发');
                event.preventDefault();
            }
        </script>
    </body>
</html>
```

效果展示:

![](https://book.apeland.cn/media/images/2019/07/18/8.gif)

由上个例子我们可以看出我们确实实现了拖放的功能，猜想：能否让我们拖拽的元素放到指定的目标对象上呢？答案是可以的，如果想实现该功能，就要学一下`DataTransfer`对象了

#### DataTransfer 对象

在进行拖放操作时，`DataTransfer`对象用来保存，通过拖放操作，拖动到浏览器的数据。它可以保存一项或多项数据、一种或者多种数据类型。

```html
event.DataTransfer
```

##### 方法

【1】`DataTransfer.setData()`

该方法用来设置拖动操作的当前数据

语法：

```html
DataTransfer.setData(format,data);
```

-   format 拖动数据的 MIME 类型，通常`text/plain`和`text/uri-list`
-   data 要添加的数据

【2】`DataTransfer.getData()`

接收指定类型的拖放数据。如果拖放行为没有操作任何数据，则返回一个空字符串。返回值是字符串类型

语法:

```html
dataTransfer.getData(format);
```

-   format 拖动数据的 MIME 类型，通常`text/plain`和`text/uri-list`

【3】`DataTransfer.clearData()`

删除给定类型拖动操作的数据。

【4】`DataTransfer.setDragImage()`

可以使用该方法来拖拽图片

语法：

```html
DataTransfer.setDragImage(img,xOffset,yOffset)
```

-   img:拖拽图像的当前元素
-   xOffset :图片的横向偏移量
-   yOffset: 图片的纵向偏移量

#### 定义拖动效果

`dropEffect`属性可以定义完成具体的效果

我们可以定义三种效果：

1. `copy` 表示拖动的数据将从其当前位置复制到放置位置。
2. `move` 表示拖动的数据将从其当前位置移动到放置位置。
3. `link` 表示将在源位置和放置位置之间创建某种形式的关系或连接。

#### 例子:实现复制和移动元素

```html
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title></title>
        <style>
            #copy,#move{
                border: 1px solid #000;
                width: 300px;
                height: 200px;
            }
            #copyTarget,#moveTarget{
                width: 300px;
                height: 200px;
                border: 1px solid #FF0000;
            }
            #newId{
                width: 200px;
                height: 50px;
                border: 1px solid darkcyan;
            }
        </style>
    </head>
    <body>
        <h2>使用拖拽实现移动和复制功能</h2>
        <div draggable="true" id="copy">要复制的元素</div>
        <div id="copyTarget"></div>
        <div draggable="true" id="move">要移动的元素</div>
        <div id="moveTarget"></div>
        <script type="text/javascript">
            window.onload = function() {
                // 复制
                $('copy').ondragstart = handler_dragstart;
                $('copy').ondragend = handler_dragend;
                $('copyTarget').ondragover = hander_dragover;
                $('copyTarget').ondragleave = handler_dragLeave
                $('copyTarget').ondrop = handler_drop;
                // 移动
                $('move').ondragstart = handler_dragstart;
                $('move').ondragend = handler_dragend;
                $('moveTarget').ondragover = hander_dragover;
                $('moveTarget').ondragleave = handler_dragLeave
                $('moveTarget').ondrop = handler_drop;
                function handler_dragstart(event) {
                    console.log('拖拽开始');
                    // 设置数据
                    event.dataTransfer.setData('text/plain', event.target.id);
                    // 设置拖动效果 设置既复制又移动
                    event.effectAllowed = 'copyMove';
                }
                function handler_dragend(event) {
                    // 拖动操作完成时 清空设置的数据
                    // event.target.style.borderColor = 'black';
                    event.dataTransfer.clearData();
                }
                // 当被拖动元素在目标元素内时触发
                function hander_dragover(event) {
                    event.target.style.background = 'lightblue';
                    event.preventDefault();
                }
                function handler_drop(event) {
                    event.preventDefault();
                    // 获取设置的数据
                    var id = event.dataTransfer.getData('text/plain');
                    if (id === 'copy' && event.target.id == 'copyTarget') {
                        var nodeCopy = document.getElementById(id).cloneNode(true);
                        nodeCopy.id = 'newId';
                        event.target.appendChild(nodeCopy);
                    }
                    if(id === 'move' && event.target.id == 'moveTarget'){
                        event.target.appendChild(document.getElementById(id));
                        console.log(event.target.children);
                    }
                }
                function handler_dragLeave(event) {
                    event.target.style.background = 'white';
                    event.preventDefault();
                }
                function $(ele) {
                    return document.getElementById(ele);
                }
            }
        </script>
    </body>
</html>
```

效果展示：

![](https://book.apeland.cn/media/images/2019/07/18/9.gif)

#### 例子:实现简单拖拽购物车功能

```html
<html>
    <head>
        <meta charset="utf-8" />
        <title>使用拖放API将商品拖入购物车</title>
        <style>
            body {
                font-size: 12px
            }
            .liT {
                border-bottom: solid 1px #ccc;
                background-color: #eee;
                font-weight: bold
            }
            .liF {
                float: left;
                margin-right: 5px;
            }
            ul {
                list-style-type: none;
                padding: 0px;
                height: 106px;
                width: 330px
            }
            ul li {
                overflow: hidden;
            }
            ul li img {
                width: 68px;
                height: 96px;
                border: solid 1px #ccc;
                padding: 3px
            }
            ul li span {
                float: left;
                width: 70px;
                padding: 5px;
            }
        </style>
    </head>
    <body>
        <ul>
            <li class="liF">
                <img src="image01.png" id="img02" alt="42" title="2006作品" draggable="true">
            </li>
            <li class="liF">
                <img src="image02.png" id="img03" alt="56" title="2008作品" draggable="true">
            </li>
            <li class="liF">
                <img src="image03.png" id="img04" alt="52" title="2010作品" draggable="true">
            </li>
        </ul>
        <ul id="ulCart">
            <li class="liT">
                <span>书名</span>
                <span>定价</span>
                <span>数量</span>
                <span>总价</span>
            </li>
        </ul>
        <script type="text/javascript">
            pageload();
            function $$(id) {
               return document.getElementById(id);
            }
            //自定义页面加载时调用的函数
            function pageload() {
                //获取全部的图书商品
                var Drag = document.getElementsByTagName("img");
                //遍历每一个图书商品
                for (var intI = 0; intI < Drag.length; intI++) {
                    console.log(Drag[intI]);
                    //为每一个商品添加被拖放元素的dragstart事件
                    Drag[intI].addEventListener("dragstart", function(e) {
                        e.dataTransfer.clearData();
                        var objDtf = e.dataTransfer;
                        console.log(objDtf);
                        objDtf.setData("text/plain", addCart(this.title, this.alt, 1));
                    },true);
                }
                var Cart = $$("ulCart");
                //添加目标元素的drop事件
               Cart.addEventListener("drop",function(e) {
                    var objDtf = e.dataTransfer;
                    var strHTML = objDtf.getData("text/plain");
                    var num = top_();
                    Cart.innerHTML += strHTML;
                    var lists = document.getElementsByClassName('liC');
                    for(var i = 0; i < lists.length; i++){
                        var spans = lists[i].children;
                        console.log(spans);
                        spans[2].innerHTML = num;
                        spans[3].innerHTML = num * spans[1].innerHTML;
                    }
                    e.preventDefault();
                    e.stopPropagation();
                },false);
            }
            //添加页面的dragover事件
            document.ondragover = function(e) {
                //阻止默认方法,取消拒绝被拖放
                e.preventDefault();
            }
            //添加页面drop事件
            document.ondrop = function(e) {
                //阻止默认方法,取消拒绝被拖放
                e.preventDefault();
            }
            //自定义向购物车中添加记录的函数
            function addCart(a, b, c) {
                var strHTML = `<li class = 'liC'>
                <span>${a}</span>
                <span class="price">${b}</span>
                <span class="num">${c}</span>
                <span class="sum">${b*c}</span>
            </li>`
                return strHTML;
            }
            //提示输入框
            function top_() {
                var str = prompt("请输入要购买的数量", 1);
                return str;
            }
        </script>
    </body>
</html>

```
