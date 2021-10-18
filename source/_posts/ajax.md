---
title: AJAX
tags: js
date: 2020-04-17
---

## XMLHttpRequest

XMLHttpRequest readyState:

0. xhr instance created, but open not called.
1. open already called, but send not called.
2. send already called and return http header and status, but not return http body.
3. receiving http body but not completed.
4. fully receive http body. 

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
        <script src="./xhr.js"></script>
    </head>
    <body>
        <h1 id="demo"></h1>
        <script>
            const xhr = new XMLHttpRequest();

            if (xhr.readyState === 0)
                console.log("0. xhr instance created, but open not called");

            xhr.onreadystatechange = function () {
                if (this.readyState === 1)
                    console.log("1. open already called, but send not called");
                if (this.readyState === 2)
                    console.log(
                        "2. send already called and return http header and status, but not return http body"
                    );
                if (this.readyState === 2) {
                    console.log(this.getAllResponseHeaders(), this.status);
                }
                if (this.readyState === 3)
                    console.log("3. receiving http body but not completed");
                if (this.readyState === 4)
                    console.log("4. fully receive http body");
                if (this.readyState === 4 && this.status === 200) {
                    myArr = JSON.parse(this.responseText);
                    document.getElementById("demo").innerHTML = myArr;
                }
            };
            xhr.open("GET", "./json_demo.txt", true);
            xhr.send();

            /*
             * json_demo.txt
             * [
             *      "Google",
             *      "Runoob",
             * 		"Taobao"
             * ]
             */
        </script>
    </body>
</html>
```

## JSONP

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>JSONP 实例</title>
    </head>

    <body>
        <div id="divCustomers"></div>
        <script type="text/javascript">
            function callbackFunction(result, methodName) {
                var html = "<ul>";
                for (var i = 0; i < result.length; i++) {
                    html += "<li>" + result[i] + "</li>";
                }
                html += "</ul>";
                document.getElementById("divCustomers").innerHTML = html;
            }
        </script>
        <script
            type="text/javascript"
            src="https://www.runoob.com/try/ajax/jsonp.php?jsoncallback=callbackFunction"
        ></script>
    </body>
</html>

<!-- 
https://www.runoob.com/try/ajax/jsonp.php?jsoncallback=callbackFunction respose result as follow

callbackFunction(["customername1", "customername2"]) -->
```

![](ajax/a01.png)
