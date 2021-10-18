---
title: Python Requests with pkcs12
date: 2021-06-28
tag: python
---

## python requests_pkcs12

```python
from requests_pkcs12 import get, post
url = ''
asn_status_url = ''

pkcs12_filename = 'test.p12'
pkcs12_password = 'test'

headers = {
    'Content-Disposition': 'upload; filename="ShortASN.xml"',
    'Content-Type': 'text/xml',
}

with open('ShortASN.xml') as f:
    data = f.read()

response = post(url, data=data, headers=headers,
                pkcs12_filename=pkcs12_filename, pkcs12_password=pkcs12_password)

print(response.status_code)
print(response.text)

# headers = {
#     'Accept': 'application/json'
# }

# response = get(f'{asn_status_url}?min_id=13496&max_id=13496', headers=headers,
#                pkcs12_filename=pkcs12_filename, pkcs12_password=pkcs12_password)
```

## node request

```javascript
const fs = require('fs');
const path = require('path')
const request = require('request');
const express = require('express');
const app = express()

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

asn_status_url = ''

app.get("/", async (req, res) => {

    const options = {
        url: asn_status_url,
        headers: {
            'Accept': 'application/json',
        },
        agentOptions: {
            pfx: fs.readFileSync(__dirname + '/certs/test.p12'),
            passphrase: 'test'
        }
    };

    request.get(options, (error, response, body) => {
        res.render('index', {asns: JSON.parse(body)})
    });
})


app.listen(3000, () => {
    console.log('listening on 3000')
})
```

