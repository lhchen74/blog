---
title: Node Pm2
tags: node
date: 2020-06-28
---

PM2 is a daemon process manager that will help you manage and keep your application online 24/7

### 命令行启动程序

`pm2 start .\flask-app.py --name flask-app --log .\log\flask-app.log --time --watch`

-   --name application name
-   --log output log path
-   --time log with time
-   --watch watch and restart app when files change

flask-app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World !"

# ! if debug=True, cmd will launch and listening the request
app.run('127.0.0.1', 5000, debug=False)
```

### 根据配置文件启动程序

```
pm2 start/restart/reload/delete ecosystem.config.js --env production --only koa-app
```

- cosystem.config.js launch by config file
- --env assign environment
- --only only launch assigned app

ecosystem.config.js

```js
module.exports = {
  apps: [{
    name: 'koa-app',
    script: 'koa-app.js',

    // Options reference: https://pm2.io/doc/en/runtime/reference/ecosystem-file/
    error_file: './log/koa-app-err.log',
    out_file: './log/koa-app.log',
    merge_logs: true,   // ! if not merged, log will add id as suffix, such as koa-app-err-1.log, koa-app-1.log
    args: 'one two',
    instances: 1,
    autorestart: true,
    watch: true,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    },
    ignore_watch: ['./node_modules', './log']
  }],

  // deploy: {
  //   production: {
  //     user: 'node',
  //     host: '212.83.163.1',
  //     ref: 'origin/master',
  //     repo: 'git@github.com:repo.git',
  //     path: '/var/www/production',
  //     'post-deploy': 'npm install && pm2 reload ecosystem.config.js --env production'
  //   }
  // }
};
```

koa-app.js

```js
const Koa = require('koa')
const app = new Koa()

console.log('Koa2 App')

app.use(async (ctx, next) => {
    ctx.body = 'Hello Koa2'
})

app.listen(3000)
```

### 后台启动监听程序

`pm2 start .\watch.js --log log\watch.log`

watch.js

```js
const chokidar = require('chokidar');
// Example of a more typical implementation structure:

// Initialize watcher.
const watcher = chokidar.watch('./input', {
    ignored: /(^|[\/\\])\../, // ignore dotfiles
    persistent: true
});

// Something to use when events are received.
const log = console.log.bind(console);
// Add event listeners.
watcher
    .on('add', path => log(`File ${path} has been added`))
    .on('change', path => log(`File ${path} has been changed`))
    .on('unlink', path => log(`File ${path} has been removed`));
```

