---
title: Oracle PL/SQL Mail
date: 2018-10-25
tags: db
---

### Mail Procedure

```sql
CREATE OR REPLACE PROCEDURE proc_sendmail(p_receiver VARCHAR2, -- 邮件接收人
                                          p_subject  VARCHAR2, -- 邮件标题
                                          p_message  VARCHAR2  -- 邮件正文
                                         ) IS
  --下面四个变量请根据实际邮件服务器进行赋值
  v_smtphost VARCHAR2(30) := 'xxx'; --SMTP服务器地址
  v_smtpport number(5) := 25;       --SMTP服务端口
  v_user     VARCHAR2(30) := 'xxx@xxx.com'; --登录SMTP服务器的用户名
  v_pass     VARCHAR2(20) := 'xxx'; --登录SMTP服务器的密码
  v_sender   VARCHAR2(50) := 'xxx@xxx.com'; --发送者邮箱，一般与 ps_user 对应
  v_conn     UTL_SMTP.connection; --到邮件服务器的连接
  v_msg      varchar2(4000); --邮件内容
  v_subject  varchar2(4000); --邮件主题

BEGIN
  v_conn := UTL_SMTP.open_connection(v_smtphost, v_smtpport);
  --用 ehlo() 而不是 helo() 函数
  --否则会报：ORA-29279: SMTP 永久性错误: 503 5.5.2 Send hello first.
  UTL_SMTP.ehlo(v_conn, v_smtphost);

  -- SMTP服务器登录校验
  --UTL_SMTP.command(v_conn, 'AUTH LOGIN');
  --UTL_SMTP.command(v_conn, UTL_RAW.cast_to_varchar2(UTL_ENCODE.base64_encode(UTL_RAW.cast_to_raw(v_user))));
 -- UTL_SMTP.command(v_conn, UTL_RAW.cast_to_varchar2(UTL_ENCODE.base64_encode(UTL_RAW.cast_to_raw(v_pass))));

  --设置发件人及收件人
  UTL_SMTP.mail(v_conn, '<' || v_sender || '>');
  UTL_SMTP.rcpt(v_conn, '<' || p_receiver || '>');

 l_subject := '=?utf-8?B?'|| utl_raw.cast_to_varchar2(utl_encode.base64_encode(utl_raw.cast_to_raw(convert(p_subject,'UTF8'))))||'?='; -- l_subject 可以显示中文

  -- 创建要发送的邮件内容 注意报头信息和邮件正文之间要空一行
  v_msg := 'Date:' || TO_CHAR(SYSDATE, 'yyyy mm dd hh24:mi:ss') ||
           UTL_TCP.CRLF || 'From: ' || v_sender || '' || UTL_TCP.CRLF ||
           'To: ' || p_receiver || '' || UTL_TCP.CRLF || 'Subject: ' ||
           v_subject || UTL_TCP.CRLF || UTL_TCP.CRLF -- 这前面是报头信息
           || p_message; -- 这个是邮件正文

  --打开流
  UTL_SMTP.open_data(v_conn);
  --标题和内容都都可用中文, 设置 Content-Type
  utl_smtp.write_raw_data(v_conn, utl_raw.cast_to_raw('Content-Type: text/plain; charset=utf-8' || utl_tcp.CRLF));
  UTL_SMTP.write_raw_data(v_conn, UTL_RAW.cast_to_raw(v_msg));
  --关闭流
  UTL_SMTP.close_data(v_conn);
  --关闭连接
  UTL_SMTP.quit(v_conn);
EXCEPTION
  WHEN OTHERS THEN
    DBMS_OUTPUT.put_line(DBMS_UTILITY.format_error_stack);
    DBMS_OUTPUT.put_line(DBMS_UTILITY.format_call_stack);
    UTL_SMTP.quit(v_conn);
END proc_sendmail;

```

### Test

sqlplus 连接 Oracle: `sqlplus username/password@host:port/instance`

`SQL> exec proc_sendmail(p_receiver => 'xxx@xxx.com',p_subject => '世界，你好',p_message => '你好啊，世界!');`
