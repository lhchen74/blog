---
title: pandoc
tags: other
date: 2018-02-28
---

> 有阳光的地方就会有阴影，所以有阴影的地方也一定会有阳光。绝望的颜色越是浓厚，在哪里也一定会存在耀眼的希望之光。- 银魂

### pandoc

**Pandoc**是由[John MacFarlane](https://baike.baidu.com/item/John%20MacFarlane)开发的[标记语言](https://baike.baidu.com/item/%E6%A0%87%E8%AE%B0%E8%AF%AD%E8%A8%80)转换工具，可实现不同标记语言间的格式转换，堪称该领域中的“[瑞士军刀](https://baike.baidu.com/item/%E7%91%9E%E5%A3%AB%E5%86%9B%E5%88%80)”。Pandoc使用[Haskell](https://baike.baidu.com/item/Haskell)语言编写，以[命令行](https://baike.baidu.com/item/%E5%91%BD%E4%BB%A4%E8%A1%8C)形式实现与用户的交互，可支持多种操作系统；Pandoc采用[GNU GPL](https://baike.baidu.com/item/GNU%20GPL)授权协议发布，属于[自由软件](https://baike.baidu.com/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6)。

### pandoc 常用命令

```ini
-f: 指定输入格式，比如docx、epub、markdown、html等
-t: 指定输出格式，比如docx、epub、md、html等
-o: 输出到file文件
--verbost: 显示详细调试信息
--log: 指定输出日志信息
 
--list-input-formats: 列出支持的输入格式
--list-output-formats: 列出支持的输出格式
--list-extensions: 列表支持Markdown扩展，后面跟一个+或者-说明是否在pandoc的Markdown中默认启用
--list-highlight-languages: 列出语法突出显示支持的语言
--list-highlight-styles: 列出支持语法高亮的样式
-v: 打印版本信息
-h: 显示语法帮助
```

`pandoc -f html -t markdown https://lhchen74.github.io/` 获取 html 内容并转换为 markdown

`pandoc test.md -o out.pdf` 未指定 -f, -t 根据文件后缀判断

`iconv -t utf-8 input.txt | pandoc | iconv -f utf-8` 可以使用 iconv 命令对输入输出编码进行编码转换

### python 调用 pandoc

```python
import os

dir = "/Users/jbn/Desktop/study/python/pandoc"
all_md_files = []
all_files_name = os.listdir(dir)
for file_name in all_files_name:
    if file_name.endswith(".md"):
        all_md_files.append(file_name)

for md_file in all_md_files:
    try:
        # 获取不包含后缀的文件名
        temp_doc_name = os.path.splitext(md_file)[0] + ".docx"
        # pandoc命令
        md_to_doc = f"pandoc {md_file} -o {temp_doc_name}"
        result = os.popen(md_to_doc).readlines()
        if len(result) == 0:
            print(md_file,"转换成功")
    except Exception as e:
        print(e)
'''
os.system(cmd) 的返回值只会有0(成功),1,2；
os.popen(cmd) 会把执行的cmd的输出作为值返回。
os.popen(cmd) 这种调用方式是通过管道的方式来实现，函数返回一个file-like的对象，里面的内容是脚本输出的内容。
'''
```