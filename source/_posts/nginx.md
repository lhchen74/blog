---
title: nginx simple
tags: nginx
date: 2019-07-14
---

### command

在 window 上如果使用 git shell，需要在 nginx 前加 start，例如 `start nginx -s stop` 会停止 nginx 服务。

启动 nginx 服务

```bash
nginx
```

检查配置文件是否正确

```bash
nginx -t -c conf/nginx.conf
```

重新加载配置文件并重启

```bash
nginx -s reload
```

停止 nginx 服务

```bash
nginx -s stop
```

### nginx 作为静态文件服务器

将 `D:/study/nginx/resource` 作为静态文件根目录，启动 nginx， 访问 `http://localhost:8081`，会显示 D:/study/nginx/resource 下的静态资源。

```nginx
server {
    listen 8081;
    server_name resource;
    root D:/study/nginx/resource;
    autoindex on;
    location / {
        add_header Access-Control-Allow-Origin *;
    }
    add_header Cache-Control "no-cache, must-revalidate";
}
```
