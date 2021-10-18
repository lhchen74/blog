---
title: Oracle Erp
date: 2018-10-17
tags: erp
---

记录 oracle erp 报错处理，错误描述：在做 Transact Move Orders 时弹出错误：`累计拣货数量超过报关数量`

1. 搜索 `累计拣货数量超过报关数量`, 检查 form 的 trigger 都没有发现相关代码和描述
2. 在 plsql 中使用 `select * from all_source s where s.TEXT like '%累计拣货数量超过报关数量%';` 结果在一个 trigger 中找到相关文字，查看 trigger 代码可以看到实际原因是报关资料抄写没有抄写成功。
