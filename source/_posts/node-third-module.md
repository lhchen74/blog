---
title: Node Third Module
tags: node
date: 2019-07-15
description: node 常用第三方模块
---

### [cheerio](https://www.npmjs.com/package/cheerio)

Fast, flexible & lean implementation of core jQuery designed specifically for the server.

Parse HTML Content to File

```javascript
const http = require("http");
const cheerio = require("cheerio");
const fs = require("fs");
const url = "http://sports.sina.com.cn/nba/1.shtml";

function httpGet(url, cb) {
    let html = "";
    http.get(url, function (res) {
        res.on("data", function (chunk) {
            html += chunk;
        });
        res.on("end", function () {
            cb(html);
        });
    }).on("error", function (e) {
        console.log(e.message);
    });
    return html;
}

httpGet(url, function (html) {
    const $ = cheerio.load(html);
    $("#right a").each(function (index) {
        const newUrl = $(this).attr("href");
        httpGet(newUrl, function (body) {
            const jq = cheerio.load(body);
            fs.writeFile(
                `./news/${index}.txt`,
                jq("#artibody").text(),
                function (err) {
                    if (err) {
                        console.log(err.message);
                    }
                    console.log("success");
                }
            );
        });
    });
});
```

### [Chart.js](https://www.chartjs.org/docs/latest/)

Simple yet flexible JavaScript charting for designers & developers

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>chartjs</title>
        <script src="bower_components/chart.js/dist/Chart.js"></script>
    </head>
    <body>
        <div
            class="chart-container"
            style="position: relative; height:40vh; width:80vw"
        >
            <canvas id="myChart"></canvas>
        </div>
    </body>
    <script>
        var ctx = document.getElementById("myChart");
        var myChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
                datasets: [
                    {
                        label: "# of Votes",
                        data: [12, 19, 3, 5, 2, 3],
                        backgroundColor: [
                            "rgba(255, 99, 132, 0.2)",
                            "rgba(54, 162, 235, 0.2)",
                            "rgba(255, 206, 86, 0.2)",
                            "rgba(75, 192, 192, 0.2)",
                            "rgba(153, 102, 255, 0.2)",
                            "rgba(255, 159, 64, 0.2)",
                        ],
                        borderColor: [
                            "rgba(255,99,132,1)",
                            "rgba(54, 162, 235, 1)",
                            "rgba(255, 206, 86, 1)",
                            "rgba(75, 192, 192, 1)",
                            "rgba(153, 102, 255, 1)",
                            "rgba(255, 159, 64, 1)",
                        ],
                        borderWidth: 1,
                    },
                ],
            },
            options: {
                scales: {
                    yAxes: [
                        {
                            ticks: {
                                beginAtZero: true,
                            },
                        },
                    ],
                },
            },
        });
    </script>
</html>
```

![chart](node-module/chart.png)

### [colors](https://www.npmjs.com/package/colors)

get color and style in your node.js console.

### [chalk](https://www.npmjs.com/package/chalk)

Terminal string styling done right.

### [mockjs](http://mockjs.com/)

生成随机数据，拦截 Ajax 请求

### [pm2](http://pm2.keymetrics.io/)

Advanced, production process manager for Node.js

### [lowdb](https://www.npmjs.com/package/lowdb)

Small JSON database for Node, Electron and the browser. Powered by Lodash.

### [chokidar](https://www.npmjs.com/package/chokidar)

A neat wrapper around Node.js fs.watch / fs.watchFile / FSEvents.

### [yrm](https://www.npmjs.com/package/yrm)

`yrm` can help you easy and fast switch between different npm registries, now include: `npm`, `cnpm`, `taobao`, `nj(nodejitsu)`, `rednpm`, `yarn`.

```
Usage: yrm [options] [command]

  Commands:

    ls                           List all the registries
    use <registry>               Change registry to registry
    add <registry> <url> [home]  Add one custom registry
    del <registry>               Delete one custom registry
    home <registry> [browser]    Open the homepage of registry with optional browser
    test [registry]              Show the response time for one or all registries
    help                         Print this help

  Options:

    -h, --help     output usage information
    -V, --version  output the version number
```

### [Prism](https://prismjs.com/)

Prism is a lightweight, extensible syntax highlighter, built with modern web standards in mind. It’s used in millions of websites, including some of those you visit daily.

### [furigana-markdown-it](https://www.npmjs.com/package/furigana-markdown-it)

furigana-markdown-it  A markdown-it plugin which adds furigana support

### [case-police: 🚨](https://github.com/antfu/case-police)

Make the case correct, PLEASE!

- Git**H**ub, not *Github*
- Type**S**cript, not *Typescript*
- **m**acOS, not *MacOS*
- **VS C**ode, not *Vscode*
- [...](https://github.com/antfu/case-police/blob/main/dict)

### [Slidev](https://sli.dev/)

Presentation **Sli**des for **Dev**elopers