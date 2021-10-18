---
title: Python HTML2PDF
tags: python
date: 2020-11-01
---

> I can't be a savior. If I save one's life, i am required to save others. Once I fail to save everyone, the world will call me hypocritical. - Strive to live in this world

### 下载 html 并转换为 pdf

```python
import os
import shutil

import pdfkit
from bs4 import BeautifulSoup
import requests
from PyPDF2 import PdfFileReader, PdfFileWriter

# 全局变量
base_url = 'http://python3-cookbook.readthedocs.io/zh_CN/latest/'
book_name = ''
chapter_info = []


def get_one_page(url):
    return requests.get(url).content


def parse_title_and_url(html):
cover: /img/post-cover/36.jpg
    """
    解析全部章节的标题和url
    :param html: 需要解析的网页内容
    :return None
    """
    # BeautifulSoup 需要先通过 requests 获取内容
    html = get_one_page(html)
    soup = BeautifulSoup(html, 'html.parser')

    # 获取书名
    book_name = soup.find('div', class_='wy-side-nav-search').a.text.strip()
    print(book_name)
    menu = soup.find_all('div', class_='section')
    chapters = menu[0].div.ul.find_all('li', class_='toctree-l1')
    for chapter in chapters:
        info = {}
        # 获取一级标题和url
        # 标题中含有'/'和'*'会保存失败
        info['title'] = chapter.a.text.replace('/', '').replace('*', '')
cover: /img/post-cover/36.jpg
        info['url'] = base_url + chapter.a.get('href')
        info['child_chapters'] = []

        # 获取二级标题和url
        if chapter.ul is not None:
            child_chapters = chapter.ul.find_all('li')
            for child in child_chapters:
                url = child.a.get('href')
                # 如果在url中存在'#'，则此url为页面内链接，不会跳转到其他页面
                # 所以不需要保存
                if '#' not in url:
                    info['child_chapters'].append({
                        'title': child.a.text.replace('/', '').replace('*', ''),
cover: /img/post-cover/36.jpg
                        'url': base_url + child.a.get('href'),
                    })

        chapter_info.append(info)


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


def get_content(url):
    """
    解析URL，获取需要的html内容
    :param url: 目标网址
    :return: html
    """
    # print(url)
    html = get_one_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', attrs={'itemprop': 'articleBody'})
    html = html_template.format(content=content)
    return html


def save_pdf(html, filename):
    """
    把所有html文件保存到pdf文件
    :param html:  html内容
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }

    # 配置 wkhtmltopdf.exe 位置
    path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wk)

    pdfkit.from_string(html, filename, configuration=config,options=options)


def parse_html_to_pdf():
    """
    解析URL，获取html，保存成pdf文件
    :return: None
    """
    try:
        for chapter in chapter_info:
            ctitle = chapter['title']
cover: /img/post-cover/36.jpg
            url = chapter['url']
            # 文件夹不存在则创建（多级目录）
            dir_name = os.path.join(os.path.dirname(__file__), 'gen', ctitle)
cover: /img/post-cover/36.jpg
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            html = get_content(url)

            pdf_path = os.path.join(dir_name, ctitle + '.pdf')
cover: /img/post-cover/36.jpg
            save_pdf(html, pdf_path)

            children = chapter['child_chapters']
            if children:
                for child in children:
                    html = get_content(child['url'])
                    pdf_path = os.path.join(dir_name, child['title'] + '.pdf')
cover: /img/post-cover/36.jpg
                    save_pdf(html, pdf_path)

    except Exception as e:
        print(e)



def merge_pdf(infnList, outfn):
    """
    合并pdf
    :param infnList: 要合并的PDF文件路径列表
    :param outfn: 保存的PDF文件名
    :return: None
    """
    pagenum = 0
    pdf_output = PdfFileWriter()

    for pdf in infnList:
        # 先合并一级目录的内容
        first_level_title = pdf['title']
cover: /img/post-cover/36.jpg
        dir_name = os.path.join(os.path.dirname(__file__), 'gen', first_level_title)
cover: /img/post-cover/36.jpg
        padf_path = os.path.join(dir_name, first_level_title + '.pdf')
cover: /img/post-cover/36.jpg

        pdf_input = PdfFileReader(open(padf_path, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))

        # 添加书签
        parent_bookmark = pdf_output.addBookmark(
            first_level_title, pagenum=pagenum)
cover: /img/post-cover/36.jpg

        # 页数增加
        pagenum += page_count

        # 存在子章节
        if pdf['child_chapters']:
            for child in pdf['child_chapters']:
                second_level_title = child['title']
cover: /img/post-cover/36.jpg
                padf_path = os.path.join(dir_name, second_level_title + '.pdf')
cover: /img/post-cover/36.jpg

                pdf_input = PdfFileReader(open(padf_path, 'rb'))
                # 获取 pdf 共用多少页
                page_count = pdf_input.getNumPages()
                for i in range(page_count):
                    pdf_output.addPage(pdf_input.getPage(i))

                # 添加书签
                pdf_output.addBookmark(
                    second_level_title, pagenum=pagenum, parent=parent_bookmark)
cover: /img/post-cover/36.jpg
                # 增加页数
                pagenum += page_count

    # 合并
    pdf_output.write(open(outfn, 'wb'))
    # 删除所有章节文件
    # shutil.rmtree(os.path.join(os.path.dirname(__file__), 'gen'))

if __name__ == '__main__':
    parse_title_and_url(base_url)
cover: /img/post-cover/36.jpg
    # print(chapter_info.__len__())
    # parse_html_to_pdf()
    merge_pdf(chapter_info, 'python-cookbook.pdf')
```
