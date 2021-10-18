---
title: R
tags: r
date: 2021-05-08
---

### Q&A

1. Restore default R dataset after edits.

    rm 删除已经修改过的 R 数据集，再重新使用时就是没有更改的默认数据集。

    ```R
    rm(mtcars)
    mtcars
    ```

2. Could not find function "view".

    R is case-sensitive, need use View. `View(mtcars)`

3. Chinese print show <U+4E50><U+6ECB>.

    设置 R 语言环境

    ```R
    sessionInfo()
    Sys.getlocale()
    Sys.setlocale(category = "LC_ALL",local="us")
    Sys.setlocale(category = "LC_ALL",local="chinese")
    ```
