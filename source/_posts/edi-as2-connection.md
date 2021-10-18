---
title: EDI AS2 Connection
date: 2021-10-14
tags: edi
---

在与客人进行 AS2 Connectivity Setup 时，EDI 讯息无法发送到客人，Cleo 工具产生 Connection timed out exception。

检查相关设定并沒有发现有什么问题。

| **General Information** |              |       |      |             |      |
| ----------------------- | ------------ | ----- | ---- | ----------- | ---- |
| **Company Name**        | Dew          |       |      |             |      |
| **Address**             | xxx          |       |      |             |      |
| **City**                | xxx          | State | xxx  | Postal Code | xxx  |
| **Contact Email**       | dew@list.com |       |      |             |      |


| **AS2 Information**        |                                                              |
| -------------------------- | ------------------------------------------------------------ |
| **Transportation Methods** | HTTPS                                                        |
| **Encryption Algorithm**   | Triple DES                                                   |
| **Requested MDN**          | Synchronous                                                  |
| **Hashing Algorithm**      | SHA2                                                         |
|                            |                                                              |
| **Test Information**       |                                                              |
| **AS2 ID**                 | DEW_AS2_T                                                    |
| **IP Addresses**           | **Send to Dew**:  ip1, ip2 ...<br />**Receive from Dew**: ip3, ip4... |
| **Sending/Receiver Port**  | 9093                                                         |
| **HTTPS URL**              | https://dew-test.com:9093/as2/main                           |
| **Certificate**            |                                                              |



使用 ping, tracert 等工具测试连接 `dew-test.com` 发现无法连接成功，可能是客人有 block 我们，所以我们请客人将我们 Sever 的 IP 添加到他们防火墙的允许名单内。

但是客人反馈他们不会阻挡外部的连接，ping, tracert 失败是因为他们没有开放相关功能，所以可能是我们自己内部防火墙有阻挡 Out Port。

最后我们自己在内部 Sever 上通过 Telnet 测试 `telnet dew-test.com 9093` 连接失败，但是在外部网络中可以连接成功。经 OA 确认，Server 上没有开放 9093 Port, 开放之后，测试连接成功。

TIP: 网络上有很方便的测试网络连通的工具，如下：

> [Online Ping, Traceroute, DNS lookup, WHOIS, Port check, Reverse lookup, Proxy checker, Bandwidth meter, Network calculator, Network mask calculator, Country by IP, Unit converter](https://ping.eu/)

> [Ping, mtr, dig and TCP port check from multiple locations](http://ping.pe/)

