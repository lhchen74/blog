---
title: Node Koa
tags: node
date: 2019-07-14
---

### 基本用法

#### Context 对象

Context 对象，表示一次对话的上下文（包括 HTTP 请求和 HTTP 回复）

```js
const Koa = require('koa')
const app = new Koa()

const main = ctx => {
  ctx.response.body = 'Hello World'
}

app.use(main)
app.listen(3000)
```

#### HTTP Response 的类型

Koa 默认的返回类型是`text/plain`，如果想返回其他类型的内容，可以先用`ctx.request.accepts`判断一下，客户端希望接受什么数据（根据 HTTP Request 的`Accept`字段），然后使用`ctx.response.type`指定返回类型。

```js
const Koa = require('koa')
const app = new Koa()

const main = ctx => {
  if (ctx.request.accepts('xml')) {
    ctx.response.type = 'xml'
    ctx.response.body = '<data>Hello World</data>'
  } else if (ctx.request.accepts('json')) {
    ctx.response.type = 'json'
    ctx.response.body = { data: 'Hello World' }
  } else if (ctx.request.accepts('html')) {
    ctx.response.type = 'html'
    ctx.response.body = '<p>Hello World</p>'
  } else {
    ctx.response.type = 'text'
    ctx.response.body = 'Hello World'
  }
}

app.use(main)
app.listen(3000)
```

#### 网页模板

实际开发中，返回给用户的网页往往都写成模板文件。可以让 Koa 先读取模板文件，然后将这个模板返回给用户

```js
const fs = require('fs')

const main = ctx => {
  ctx.response.type = 'html'
  ctx.response.body = fs.createReadStream('./demos/template.html')
}
```

### 路由

#### 原生路由

```js
const main = ctx => {
  if (ctx.request.path !== '/') {
    ctx.response.type = 'html'
    ctx.response.body = '<a href="/">Index Page</a>'
  } else {
    ctx.response.body = 'Hello World'
  }
}
```

#### koa-route 模块

```js
const route = require('koa-route')

const about = ctx => {
  ctx.response.type = 'html'
  ctx.response.body = '<a href="/">Index Page</a>'
}

const main = ctx => {
  ctx.response.body = 'Hello World'
}

app.use(route.get('/', main))
app.use(route.get('/about', about))
```

#### 静态资源

```js
const path = require('path')
const serve = require('koa-static')

const main = serve(path.join(__dirname))
app.use(main)

// 运行这个 Demo。
// $ node demos/12.js
// 访问 http://127.0.0.1:3000/12.js，在浏览器里就可以看到这个脚本的内容。
```

#### 重定向

`ctx.response.redirect()` 方法可以发出一个 302 跳转，将用户导向另一个路由

```js
const redirect = ctx => {
  ctx.response.redirect('/')
  ctx.response.body = '<a href="/">Index Page</a>'
}

app.use(route.get('/redirect', redirect))
```

### 中间件

#### 中间件的概念

代码中的`logger`函数就叫做”中间件”（middleware），因为它处在 HTTP Request 和 HTTP Response 中间，用来实现某种中间功能。`app.use()`用来加载中间件。基本上，Koa 所有的功能都是通过中间件实现的。每个中间件默认接受两个参数，第一个参数是 Context 对象，第二个参数是`next`函数。只要调用`next`函数，就可以把执行权转交给下一个中间件。

```js
const logger = (ctx, next) => {
  console.log(`${Date.now()} ${ctx.request.method} ${ctx.request.url}`)
  next()
}
app.use(logger)
```

#### 中间件栈

多个中间件会形成一个栈结构（middle stack），以”先进后出”（first-in-last-out）的顺序执行。

```js
const one = (ctx, next) => {
  console.log('>> one')
  next()
  console.log('<< one')
}

const two = (ctx, next) => {
  console.log('>> two')
  next()
  console.log('<< two')
}

const three = (ctx, next) => {
  console.log('>> three')
  next()
  console.log('<< three')
}

app.use(one)
app.use(two)
app.use(three)
/*
>> one
>> two
>> three
<< three
<< two
<< one
*/
```

#### 异步中间件

`fs.readFile`是一个异步操作，必须写成`await fs.readFile()`，然后中间件必须写成 async 函数

```js
const fs = require('fs.promised')
const Koa = require('koa')
const app = new Koa()

const main = async function(ctx, next) {
  ctx.response.type = 'html'
  ctx.response.body = await fs.readFile('./demos/template.html', 'utf8')
}

app.use(main)
app.listen(3000)
```

#### 中间件的合成

```js
const compose = require('koa-compose')

const logger = (ctx, next) => {
  console.log(`${Date.now()} ${ctx.request.method} ${ctx.request.url}`)
  next()
}

const main = ctx => {
  ctx.response.body = 'Hello World'
}

const middlewares = compose([logger, main])
app.use(middlewares)
```

### 错误处理

#### 500 错误

```js
const main = ctx => {
  ctx.throw(500)
}
```

#### 404 错误

```js
const main = ctx => {
  ctx.response.status = 404 // <=> ctx.throw(404)
  ctx.response.body = 'Page Not Found'
}
```

#### 处理错误的中间件

```js
const handler = async (ctx, next) => {
  try {
    await next()
  } catch (err) {
    // 让最外层的中间件，负责所有中间件的错误处理
    ctx.response.status = err.statusCode || err.status || 500
    ctx.response.body = {
      message: err.message
    }
  }
}
const main = ctx => {
  ctx.throw(500)
}

app.use(handler)
app.use(main)
```

#### error 事件的监听

运行过程中一旦出错，Koa 会触发一个`error`事件。监听这个事件，也可以处理错误

```js
const main = ctx => {
  ctx.throw(500);
};

app.on('error', (err, ctx) =>
  console.error('server error', err);
);
```

#### 释放 error 事件

如果错误被`try...catch`捕获，就不会触发`error`事件。这时，必须调用`ctx.app.emit()`，手动释放`error`事件，才能让监听函数生效。

```js
const handler = async (ctx, next) => {
  try {
    await next()
  } catch (err) {
    ctx.response.status = err.statusCode || err.status || 500
    ctx.response.type = 'html'
    ctx.response.body = '<p>Something wrong, please contact administrator.</p>'
    ctx.app.emit('error', err, ctx)
  }
}

const main = ctx => {
  ctx.throw(500)
}

app.on('error', function(err) {
  console.log('logging error ', err.message)
  console.log(err)
})
```

### Web App 的功能

#### cookies

```js
const main = function(ctx) {
  const n = Number(ctx.cookies.get('view') || 0) + 1
  ctx.cookies.set('view', n)
  ctx.response.body = n + ' views'
}
//访问 http://127.0.0.1:3000，你会看到1 views。刷新一次页面，就变成了2 views。再刷新，每次都会计数增加1。
```

#### 表单

```js
const koaBody = require('koa-body')

const main = async function(ctx) {
  const body = ctx.request.body
  if (!body.name) ctx.throw(400, '.name required')
  ctx.body = { name: body.name }
}

app.use(koaBody())

// curl -X POST --data "name=Jack" 127.0.0.1:3000
// {"name":"Jack"}
```

#### 文件上传

```js
const os = require('os')
const path = require('path')
const koaBody = require('koa-body')

const main = async function(ctx) {
  const tmpdir = os.tmpdir() //系统默认存储目录
  const filePaths = []
  const files = ctx.request.body.files || {}

  for (let key in files) {
    const file = files[key]
    const filePath = path.join(tmpdir, file.name)
    const reader = fs.createReadStream(file.path)
    const writer = fs.createWriteStream(filePath)
    reader.pipe(writer)
    filePaths.push(filePath)
  }

  ctx.body = filePaths
}

app.use(koaBody({ multipart: true }))

//curl --form upload=@db.json http://127.0.0.1:3000
//["C:\\Users\\hp-hp\\AppData\\Local\\Temp\\db.json"]
```
