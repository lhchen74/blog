---
title: Frontend CheatSheet
tags: cheatsheet
date: 2020-02-27
---

> 转载: [前端 Cheat Sheet 分享 | cheatsheet-frontend](http://zhengyaing.com/#)

## CSS BoxModel

![](cheatsheet-frontend/boxmodel.png)

## CSS FlexBox

![](cheatsheet-frontend/flexbox.png)

## CSS Grid

![](cheatsheet-frontend/grid.png)

## CSS Selector

![](cheatsheet-frontend/cssselector.png)

## CSS Transform

![](cheatsheet-frontend/transform.png)

## Sass

![](cheatsheet-frontend/sass.png)

## HTTP

![](cheatsheet-frontend/http.png)

## Head

![](cheatsheet-frontend/head.png)

## Console

![](cheatsheet-frontend/console.png)

## Regex

![](cheatsheet-frontend/regex.png)

## Git

![](cheatsheet-frontend/git.png)

**本地操作**

`git add --patch -- file_name` 分段提交

`git commit --amend --no-edit` 修复提交不更改上次提交的 message

`git commit -a -m commit_message` 等价于 `git add + git commit`

`git checkout --patch branch_name file_name` 取出指定分支文件和当前工作区做交互式比对

**分支操作**

- `git checkout -b branch_name` 根据当前分支创建新的分支并切换到新的分支，等价于 `git branch branch_name + git checkout branch_name`
- `git merge --abort` 取消 merge

**远程操作**

- `git push origin --delete branch_name` 删除远程分支
- `git push -u origin/branch_name` push 并绑定远程分支

## Markdown

![](cheatsheet-frontend/markdown.png)