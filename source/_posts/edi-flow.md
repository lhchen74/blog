---
title: EDI Flow
date: 2021/05/06
tags: edi
categories: manual
---

## EDI Direct

![EDI X12](edi-flow/1620288317885.png)

-   PO and PO response 订单及订单回复

    -   PO 订单
    -   PO Response

-   PO Change and Response 订单变更及订单
    -   CRD Pull In 交期提前
    -   CRD Push Out 需求日推迟
    -   QTY Descrease 数量减少
    -   Cancellation 订单取消
    -   Price Change 价格变动
    -   Item with Partial Delivery 部分交货
        -   CRD Push Out 需求日推迟
        -   QTY Decrease 数量减少
        -   Cancellation for balance QTY 取消订单剩余数量

## VMI

![VMI](edi-flow/1620985465578.png)

## HUB

![Hub](edi-flow/1620987870672.png)
