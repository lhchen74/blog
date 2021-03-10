---
title: ajax
tags: js
date: 2020-04-17
---

xhr

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

/*
0. xhr instance created, but open not called 
1. open already called, but send not called
2. send already called and return http header and status, but not return http body 
accept-ranges: bytes
access-control-allow-credentials: true 
cache-control: public, max-age=0
content-length: 48 
content-type: text/plain; 
charset=UTF-8 date: Fri, 17 Apr 2020 07:00:57 GMT 
etag: W/"30-170d6998891" 
last-modified: Sat, 14 Mar 2020 01:12:31 GMT 
vary: Origin 200 
3. receiving http body but not completed 
4. fully receive http body
*/
```

### jsonp

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
https://www.runoob.com/try/ajax/jsonp.php?jsoncallback=callbackFunction 返回

callbackFunction(
[
"customername1",
"customername2"
]
) -->
```

![1587179903092](ajax/a01.png)
