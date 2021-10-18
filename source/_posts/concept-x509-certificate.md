---
title: X.509数字证书的结构与解析
tags: concept
date: 2019-10-28
---

> [X.509 数字证书的结构与解析 - ZP1015 - CSDN 博客](https://blog.csdn.net/xy010902100449/article/details/52145009)

### 数字签名

将报文按双方约定的 HASH 算法计算得到一个固定位数的报文摘要。在数学上保证：只要改动报文中任何一位，重新计算出的报文摘要值就会与原先的值不相符。这样就保证了报文的不可更改性。

将该报文摘要值用发送者的私人密钥加密，然后连同原报文一起发送给接收者，而产生的报文即称数字签名

### 数字证书

数字证书就是互联网通讯中标志通讯各方身份信息的一系列数据，提供了一种在 Internet 上验证您身份的方式，其作用类似于司机的驾驶执照或日常生活中的身份证。它是由一个由权威机构 - CA 机构，又称为证书授权，（Certificate Authority）中心发行的，人们可以在网上用它来识别对方的身份。数字证书是一个经证书授权中心数字签名的包含公开密钥拥有者信息以及公开密钥的文件。最简单的证书包含一个公开密钥、名称以及证书授权中心的数字签名。

### 交互过程

鲍勃有两把钥匙，一把是公钥，另一把是私钥。

![](concept-x509-certificate/20160807210347532.jpg)

鲍勃把公钥送给他的朋友们-帕蒂、道格、苏珊-每人一把。

![](concept-x509-certificate/20160807210405977.jpg)

苏珊要给鲍勃写一封保密的信。她写完后用鲍勃的公钥加密，就可以达到保密的效果

![](concept-x509-certificate/20160807210420243.jpg)

鲍勃收信后，用私钥解密，就看到了信件内容。这里要强调的是，只要鲍勃的私钥不泄露，这封信就是安全的，即使落在别人手里，也无法解密。

![](concept-x509-certificate/20160807210804580.jpg)

鲍勃给苏珊回信，决定采用 “数字签名”。他写完后先用 Hash 函数，生成信件的摘要（digest）。

![](concept-x509-certificate/20160807210507751.jpg)

然后，鲍勃使用私钥，对这个摘要加密，生成”数字签名”（signature）。

![](concept-x509-certificate/20160807210529876.jpg)

鲍勃将这个签名，附在信件下面，一起发给苏珊。

![](concept-x509-certificate/20160807210545845.jpg)

苏珊收信后，取下数字签名，用鲍勃的公钥解密，得到信件的摘要。由此证明，这封信确实是鲍勃发出的。

![](concept-x509-certificate/20160807210601886.jpg)

苏珊再对信件本身使用 Hash 函数，将得到的结果，与上一步得到的摘要进行对比。如果两者一致，就证明这封信未被修改过。

![](concept-x509-certificate/20160807210619814.jpg)

复杂的情况出现了。道格想欺骗苏珊，他偷偷使用了苏珊的电脑，用自己的公钥换走了鲍勃的公钥。此时，苏珊实际拥有的是道格的公钥，但是还以为这是鲍勃的公钥。因此，道格就可以冒充鲍勃，用自己的私钥做成”数字签名”，写信给苏珊，让苏珊用假的鲍勃公钥进行解密。

![](concept-x509-certificate/20160807210640793.jpg)

后来，苏珊感觉不对劲，发现自己无法确定公钥是否真的属于鲍勃。她想到了一个办法，要求鲍勃去找”证书中心”（certificate authority，简称 CA），为公钥做认证。证书中心用自己的私钥，对鲍勃的公钥和一些相关信息一起加密，生成”数字证书”（Digital Certificate）。

![](concept-x509-certificate/20160807210656731.jpg)

鲍勃拿到数字证书以后，就可以放心了。以后再给苏珊写信，只要在签名的同时，再附上数字证书就行了。

![](concept-x509-certificate/20160807210712846.jpg)

苏珊收信后，用 CA 的公钥解开数字证书，就可以拿到鲍勃真实的公钥了，然后就能证明”数字签名”是否真的是鲍勃签的。

![](concept-x509-certificate/20160807210734721.jpg)

### X.509 数字证书

X.509 标准规定了证书可以包含什么信息，并说明了记录信息的方法（数据格式）。除了签名外，所有 X.509 证书还包含以下数据：

**版本**
识别用于该证书的 X.509 标准的版本，这可以影响证书中所能指定的信息。迄今为止，已定义的版本有三个。

**序列号**
发放证书的实体有责任为证书指定序列号，以使其区别于该实体发放的其它证书。此信息用途很多。例如，如果某一证书被撤消，其序列号将放到证书撤消清单 (CRL) 中。

**签名算法标识符**
用于识别 CA 签写证书时所用的算法。

**签发人姓名**
签写证书的实体的 X.500 名称。它通常为一个 CA。 使用该证书意味着信任签写该证书的实体（注意：有些情况下（例如根或顶层 CA 证书），签发人会签写自己的证书）。

**有效期**
每个证书均只能在一个有限的时间段内有效。该有效期以起始日期和时间及终止日期和时间表示，可以短至几秒或长至一世纪。所选有效期取决于许多因素，例如用于签写证书的私钥的使用频率及愿为证书支付的金钱等。它是在没有危及相关私钥的条件下，实体可以依赖公钥值的预计时间。

**主体名**
证书可以识别其公钥的实体名。此名称使用 X.500 标准，因此在 Internet 中应是唯一的。它是实体的特征名 (DN)，例如，
CN=Java Duke，OU=Java Software Division，O=Sun Microsystems Inc，C=US
（这些指主体的通用名、组织单位、组织和国家）。

**主体公钥信息**
这是被命名实体的公钥，同时包括指定该密钥所属公钥密码系统的算法标识符及所有相关的密钥参数。

**常见的 X.509 证书格式**

```yaml
cer/crt: 是用于存放证书，它是 2 进制形式存放的，不含私钥。

pem: 跟 crt/cer 的区别是它以 Ascii 来表示，可以用于存放证书或私钥。

pfx/p12: 用于存放个人证书/私钥，他通常包含保护密码，2 进制方式。

p10: 是证书请求。

p7r: 是 CA 对证书请求的回复，只用于导入

p7b: 以树状展示证书链(certificate chain)，同时也支持单个证书，不含私钥。
```

**证书文件/私钥文件**

在 HTTPS 通讯中最常用的是 cer/crt 和 pem。下面以 pem 格式的证书为例进行说明。下面是一个完整的 PEM 格式证书：

Certificate:

```
Data:

     Version: 1 (0x0)

Serial Number: 1 (0x1)

Signature Algorithm: md5WithRSAEncryption

Issuer: C=US, ST=Montana, L=Bozeman, O=sawtooth, OU=consulting, CN=www.sawtooth-consulting.com/emailAddress=info@yassl.com

Validity

    Not Before: Jun 30 18:52:17 2010 GMT

    Not After : Mar 26 18:52:17 2013 GMT

Subject: C=US, ST=Montana, L=Bozeman, O=yaSSL, OU=support, CN=www.yassl.com/emailAddress=info@yassl.com

Subject Public Key Info:

Public Key Algorithm: rsaEncryption

RSA Public Key: (512 bit)

    Modulus (512 bit):

        00:c6:7b:c0:68:81:2f:de:82:3f:f9:ac:c3:86:4a:66:b7:ec:d4:f1:f6:64:21:ff:f5:a2:34:42:d0:38:9f:c6:dd:3b:6e:26:65:6a:54:96:dd:d2:7b:eb:36:a2:ae:7e:2a:9e:7e:56:a5:b6:87:9f:15:c7:18:66:7e:16:77:e2:a7

    Exponent: 65537 (0x10001)

Signature Algorithm: md5WithRSAEncryption

    58:a9:98:e7:16:52:4c:40:e7:e1:47:92:19:1b:3a:8f:97:6c:7b:b7:b0:cb:20:6d:ad:b5:d3:47:58:d8:e4:f2:3e:32:e9:ef:87:77:e5:54:36:f4:8d:50:8d:07:b4:77:45:ea:9d:a4:33:36:9b:0b:e0:74:58:11:c5:01:7b:4d

-----BEGIN CERTIFICATE-----

MIICFDCCAb4CAQEwDQYJKoZIhvcNAQEEBQAwgZ4xCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdNb250YW5hMRAwDgYDVQQHEwdCb3plbWFuMREwDwYDVQQKEwhzYXd0b290aDETMBEGA1UECxMKY29uc3VsdGluZzEkMCIGA1UEAxMbd3d3LnNhd3Rvb3RoLWNvbnN1bHRpbmcuY29tMR0wGwYJKoZIhvcNAQkBFg5pbmZvQHlhc3NsLmNvbTAeFw0xMDA2MzAxODUyMTdaFw0xMzAzMjYxODUyMTdaMIGKMQswCQYDVQQGEwJVUzEQMA4GA1UECBMHTW9udGFuYTEQMA4GA1UEBxMHQm96ZW1hbjEOMAwGA1UEChMFeWFTU0wxEDAOBgNVBAsTB3N1cHBvcnQxFjAUBgNVBAMTDXd3dy55YXNzbC5jb20xHTAbBgkqhkiG9w0BCQEWDmluZm9AeWFzc2wuY29tMFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMZ7wGiBL96CP/msw4ZKZrfs1PH2ZCH/9aI0QtA4n8bdO24mZWpUlt3Se+s2oq5+Kp5+VqW2h58VxxhmfhZ34qcCAwEAATANBgkqhkiG9w0BAQQFAANBAFipmOcWUkxA5+FHkhkbOo+XbHu3sMsgba2100dY2OTyPjLp74d35VQ29I1QjQe0d0XqnaQzNpsL4HRYEcUBe00=

-----END CERTIFICATE-----

     从Certificate开始到“-----BEGIN CERTIFICATE-----”为止，中间的内容是证书的明文格式。

    从“-----BEGIN CERTIFICATE-----”开始到“-----END CERTIFICATE-----”为止是证书的明文格式经过ASN.1编码再经过Base64编码得到的。

对于私钥文件，真正的私钥是包含在字符串"-----BEGIN PRIVATE KEY-----"和字符串"-----END PRIVATE KEY-----"之间。
```

如果该私钥文件是 pkcs8 格式的，那么该私钥文件的格式为

```
PrivateKeyInfo ::= SEQUENCE {

    version Version(INTEGER),

    privateKeyAlgorithm PrivateKeyAlgorithmIdentifier (AlgorithmIdentifier),

    privateKey PrivateKey(OCTET STRING),

    attributes [] IMPLICIT Attributes OPTIONAL(SET OF Attribute)

}

    如果不是pkcs8格式的，那么"-----BEGIN PRIVATE KEY-----"和"-----END PRIVATE KEY-----"之间的内容就是私钥的Base64编码。

    在客户端或服务器在交换证书时，需要首先把Base64编码转换为ASCII编码再进行传输。
```

**公钥和私钥**

公钥和私钥是证书文件和私钥文件中最核心的内容。

在 SSL/TLS 协议中需要是用公钥算法，来进行对称密钥的交换。最常见的算法是 RSA 和 DH，而 RSA 算法和 DH 算法的公钥、私钥的数据格式是不同的。

### X.509 证书数据结构

```
Certificate ::= SEQUENCE {

        tbsCertificate       TBSCertificate, -- 证书主体

        signatureAlgorithm   AlgorithmIdentifier, -- 证书签名算法标识

        signatureValue       BIT STRING --证书签名值,是使用signatureAlgorithm部分指定的签名算法对tbsCertificate证书主题部分签名后的值.

         }

TBSCertificate ::= SEQUENCE {

        version         [] EXPLICIT Version DEFAULT v1, -- 证书版本号

        serialNumber         CertificateSerialNumber, -- 证书序列号，对同一CA所颁发的证书，序列号唯一标识证书

        signature            AlgorithmIdentifier, --证书签名算法标识

        issuer               Name,                --证书发行者名称

        validity             Validity,            --证书有效期

        subject              Name,                --证书主体名称

        subjectPublicKeyInfo SubjectPublicKeyInfo,--证书公钥

        issuerUniqueID [] IMPLICIT UniqueIdentifier OPTIONAL,

                             -- 证书发行者ID(可选)，只在证书版本2、3中才有

        subjectUniqueID [] IMPLICIT UniqueIdentifier OPTIONAL,

                             -- 证书主体ID(可选)，只在证书版本2、3中才有

        extensions      [] EXPLICIT Extensions OPTIONAL

                             -- 证书扩展段（可选），只在证书版本3中才有

        }

Version ::= INTEGER { v1(0), v2(1), v3(2) }

CertificateSerialNumber ::= INTEGER

AlgorithmIdentifier ::= SEQUENCE {

        algorithm               OBJECT IDENTIFIER,

        parameters              ANY DEFINED BY algorithm OPTIONAL }

parameters:

Dss-Parms ::= SEQUENCE { -- parameters ，DSA(DSS)算法时的 parameters,

RSA 算法没有此参数

        p             INTEGER,

        q             INTEGER,

        g             INTEGER }

signatureValue：

Dss-Sig-Value ::= SEQUENCE { -- sha1DSA 签名算法时,签名值

                   r       INTEGER,

                      s       INTEGER }

Name ::= CHOICE {

     RDNSequence }

RDNSequence ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::=

     SET OF AttributeTypeAndValue

AttributeTypeAndValue ::= SEQUENCE {

     type     AttributeType,

     value    AttributeValue }

AttributeType ::= OBJECT IDENTIFIER

AttributeValue ::= ANY DEFINED BY AttributeType

Validity ::= SEQUENCE {

        notBefore      Time,  -- 证书有效期起始时间

        notAfter       Time  -- 证书有效期终止时间

        }

Time ::= CHOICE {

        utcTime        UTCTime,

        generalTime    GeneralizedTime }

UniqueIdentifier ::= BIT STRING

SubjectPublicKeyInfo ::= SEQUENCE {

        algorithm            AlgorithmIdentifier, -- 公钥算法

        subjectPublicKey     BIT STRING            -- 公钥值

        }

subjectPublicKey:

RSAPublicKey ::= SEQUENCE { -- RSA 算法时的公钥值

         modulus            INTEGER, -- n

         publicExponent     INTEGER -- e -- }

Extensions ::= SEQUENCE SIZE (1..MAX) OF Extension

Extension ::= SEQUENCE {

        extnID      OBJECT IDENTIFIER,

        critical    BOOLEAN DEFAULT FALSE,

        extnValue   OCTET STRING }
```
