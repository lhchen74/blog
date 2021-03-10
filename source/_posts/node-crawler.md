---
title: node sample crawler
tags: node
date: 2019-07-15
---

王者荣耀【原创内容大赛皮肤设计比赛】获奖作品

```js
const https = require('https')
const iconv = require('iconv-lite')
const fs = require('fs')
const uuidv4 = require('uuid/v4')

const url =
  'https://pvp.qq.com/webplat/info/news_version3/15592/29030/35315/35316/m15241/201903/800890.shtml'

const fileDir = 'skin'

function get_images(url) {
  https.get(url, res => {
    let data = []
    let len = 0

    res.on('data', chunk => {
      data.push(chunk)
      len += chunk.length
    })

    res.on('end', () => {
      let html
      html = Buffer.concat(data, len)
      html = iconv.decode(html, 'gb2312')
      // fs.writeFile('skin.html', html, 'utf-8', err => {
      //     if (!err) {
      //         console.log(err)
      //     }
      // })
      // console.log(html)

      // html = '<img src="//ossweb-img.qq.com/upload/webplat/info/yxzj/20190329/877551344946132.jpg" alt="" />'
      let matches = html.matchAll(
        /<img src="(\/\/ossweb-img.qq.com\/[\s\S]*?)" alt="" \/>/gi
      )
      for (match of matches) {
        let imgUrl = `https:${match[1]}`
        https.get(imgUrl, function(res) {
          let imgData = ''

          // 一定要设置 response 的编码为binary否则会下载下来的图片打不开
          res.setEncoding('binary')

          res.on('data', function(chunk) {
            imgData += chunk
          })

          res.on('end', function() {
            let imgName = `${uuidv4()}.jpg`
            let filePath = fileDir + '/' + imgName
            fs.writeFile(filePath, imgData, 'binary', function(err) {
              if (err) {
                console.log('down fail')
              }
              console.log('down success')
            })
          })
        })
      }
    })
  })
}

get_images(url)
```

### headless crawler

picCrawler.js

```js
const puppeteer = require('puppeteer')
const { picDir } = require('./config/default')
const saveImg = require('./helper/saveImg')
const url = 'https:/image.baidu.com'

;(async () => {
  const browser = await puppeteer.launch({ headless: false })
  const page = await browser.newPage()
  await page.goto(url)
  console.log(`go to ${url}`)

  await page.setViewport({
    width: 1080,
    height: 1080
  })
  console.log('reset viewport')

  await page.focus('#kw')
  await page.keyboard.sendCharacter('艺术')
  await page.click('.s_search')
  // await page.keyboard.press('Enter')
  console.log('go to search list page')

  page.on('load', async () => {
    console.log('page loading done, start fecth...')

    // const srcs = await page.evaluate(() => {
    //     const images = document.querySelectorAll('img.main_img')
    //     return Array.prototype.map.call(images, img => img.src)
    // })

    const srcs = await page.$$eval('img.main_img', imgs => {
      return Array.prototype.map.call(imgs, img => img.src)
    })

    console.log(`get ${srcs.length} images, start download...`)

    srcs.forEach(async src => {
      await page.waitFor(200) // sleep
      await saveImg(src, picDir)
    })

    await browser.close()
  })
})()
```

config/default.js

```js
const path = require('path')

module.exports = {
  picDir: path.resolve(__dirname, '../pic')
}
```

helper/saveImg.js

```js
const http = require('http')
const https = require('https')
const path = require('path')
const fs = require('fs')
const { promisify } = require('util')
const writeFile = promisify(fs.writeFile)

module.exports = async (src, dir) => {
  if (/\.(jpeg|jpg|png|gif)/.test(src)) {
    await urlToImg(src, dir)
  } else {
    await base64ToImg(src, dir)
  }
}

// url => image
// promisify make Call back => Promise
const urlToImg = promisify((url, dir, callback) => {
  const mod = /^https:/.test(url) ? https : http
  const ext = path.extname(url)
  const file = path.join(dir, `${Date.now()}${ext}`)
  mod.get(url, res => {
    res.pipe(fs.createWriteStream(file)).on('finish', () => {
      callback()
      console.log(file)
    })
  })
})

// base64 => image

const base64ToImg = async function(base64Str, dir) {
  // data:image/jpeg;base64,content

  const matches = base64Str.match(/data:image\/(.+?);base64,(.+)$/)
  try {
    const ext = matches[1].replace('jpeg', 'jpg')
    const file = path.join(dir, `${Date.now()}.${ext}`)
    const content = matches[2]
    await writeFile(file, content, 'base64')
    console.log(file)
  } catch {
    console.log('Illegal Base64!!!')
  }
}
```

### headless crawler2

爬取云中君皮肤设计大赛所有皮肤，因为数据是通过 Ajax 请求获得的，无法直接从页面获取，所以使用 puppetter 加载页面，点解 Load More 按钮直到所有的图片加载完成之后，抓取页面的 Image Url，然后写入文件。

```js
const puppeteer = require('puppeteer');
const https = require('https');
const fs = require('fs');
const { v4 } = require('uuid');

const isElementVisible = async (page, selector) => {
    let visible = true;
    await page
        .waitForSelector(selector, { visible: true, timeout: 2000 })
        .catch(() => {
            visible = false;
        });
    return visible;
};

(async () => {
    const chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    const browser = await puppeteer.launch({ executablePath: chromePath, headless: false });
    const page = await browser.newPage();
    await page.goto('https://pvp.qq.com/hdy/p1/all_works.html');


    selectorForLoadMoreButton = "a.btn-load.js-load-more"
    let loadMoreVisible = await isElementVisible(page, selectorForLoadMoreButton);
    while (loadMoreVisible) {
        await page
            .click(selectorForLoadMoreButton)
            .catch(err => console.log("click load more button err: ", err));
        loadMoreVisible = await isElementVisible(page, selectorForLoadMoreButton);
    }

    // $ selector one, $$ selector all, $$eval selector all and execute callback func
    const ulHandle = await page.$('ul#rankingList')  
    const imageUrls = await ulHandle.$$eval("li>img.image", nodes => nodes.map(node => node["src"]))

    await browser.close()

    console.log("total images count: ", imageUrls.length)

    for (imageUrl of imageUrls) {
        try {
            const imageData = await getImageData(imageUrl)
            await writeToFile('./yunzhongjun', imageData)
        } catch (error) {
            console.log(error)
        }
    }
})();

function getImageData (imageUrl) {
    console.log(imageUrl)
    return new Promise((resolve, reject) =>
        https.get(imageUrl, res => {
            let imgData = ''
            res.setEncoding('binary')

            res.on('data', (chunk) => {
                imgData += chunk
            })

            res.on('end', () => {
                resolve(imgData)
            })

            res.on('error', err => {
                reject(err)
            })
        })
    )
}

function writeToFile (fileDir, imageData) {
    return new Promise((resolve, reject) => {
        let imageName = `${v4()}.jpg`
        let filePath = fileDir + '/' + imageName
        fs.writeFile(filePath, imageData, 'binary', err => {
            if (err) reject(err)
            resolve()
        })
    })
}
```

