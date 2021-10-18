---
title: FTP XML Config
tag: [edi, miscellaneous, xml]
date: 2021/10/15
---

在数据传输过程中经常需要使用 FTP 传输文件，其基础操作是类似的，不同的部分可以使用配置文件。如下是关于 FTP 推送文件的基础配置。

```xml
<Config>
    <Targets>
        <Target ID="CustomerCode" Description="">
            <FTP Site="" UserName="" Password="">
                <File Type="ASN" Template="FR*.xml.gpg" SourceFolder="D:\HUB_EDI\Test\FilePool\CustomerCode\ASN" UploadFolder="/ASN" BackupFolder="D:\HUB_EDI\Test\FilePool\CustomerCode\ASN\bak\" MailAppender="MailBusiness" />
                <File Type="ASN_DIRECT" Template="FR*.xml.gpg" SourceFolder="D:\HUB_EDI\Test\FilePool\CustomerCode\ASN_DIRECT" UploadFolder="/ASN" BackupFolder="D:\HUB_EDI\Test\FilePool\CustomerCode\ASN_DIRECT\bak\" MailAppender="MailBusiness" />
            </FTP>
        </Target>     
        <Target ID="CustomerCode2" Description="">
            <FTP Site="" UserName="" Password="">
                <File Type="DN" Template="DN*.csv" SourceFolder="D:\HUB_EDI\Test\FilePool\CustomerCode2\OUT\" UploadFolder="/In" BackupFolder="D:\HUB_EDI\Test\FilePool\CustomerCode2\OUT\bak\" MailAppender="MailBusiness" />
                <File Type="ASN" Template="ASN*.xls" SourceFolder="D:\HUB_EDI\Test\FilePool\CustomerCode2\OUT\" UploadFolder="/In" BackupFolder="D:\HUB_EDI\Test\FilePool\CustomerCode2\OUT\bak\" MailAppender="MailBusiness" />
            </FTP>
        </Target>
    </Targets>
    <Log FileName="D:\HUB_EDI\Test\LogFiles\FtpFilePusher_%s.log" />
    <Notification>
        <SMTP Server="172.31.7.240" UserName="" Password="" />
        <Sender Value="edi_it@team.com" />

        <Appender Name="MailBusiness">
            <Level Value="success" />
            <Receiver Value="busines@team.com" />
        </Appender>
        
        <MailSpec>
            <Alarm Type="EXCEPTION" Subject="[FTP File Pusher][%s][EXCEPTION] Exception of Upload File" Receiver="edi_it@team.com" />
            <Alarm Type="ERROR" Subject="[FTP File Pusher][%s][%s][ERROR] Upload File Failed:%s" Receiver="edi_it@sercomm.com" />
            <Alarm Type="SUCCESS" Subject="[FTP File Pusher][%s][%s][SUCCESS] Upload File:%s Successfully" Receiver="edi_it@sercomm.com" />
        </MailSpec>
    </Notification>
</Config>
```

:::info

`Targets` 设定不同客户的讯息。

::::

:::info

`FTP` 设定 FTP 的连接讯息。

::::

:::info

`File` 设定不同的文件类型。 

::::

- `Template`指定要发送的文件形式，例如 FR-20211015-SI123.xml.gpg

- `MailAppender` 指定邮件需要通知的人员。详细讯息在 Notification 的 Appender 中配置。

:::info

`Notification` 配置邮件发送的相关讯息。

:::

- `SMTP` 邮件服务器配置。 

- `MailSpec` 指定程式 EXCEPTION, ERROR 时需要通知人员。