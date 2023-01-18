---
title: Oracle Test Data Generate
tags: db
date: 2019-12-11
---

> 转载: [使用 Oracle 的存储过程批量插入数据 - liaoyu - 博客园](https://www.cnblogs.com/liaoyu/p/oracle-procedure-batch-insert.html)

最近在工作中，需要使用生成一些测试数据用来测试项目性能，我一开始是通过使用 python 生成 SQL 再执行，但性能不理想，今天想试试使用 oracle 的存储过程来实现下，效果还不错。

## 实现相关

表结构

```sql
desc TMP_UPSTATE_CASEKEY
Name                Null     Type
------------------- -------- ----------
TMP_UPSTATE_CASEKEY NOT NULL CHAR(14)
TMP_NUM_STATUS_ID   NOT NULL NUMBER(38)
UPDATED_DATE        NOT NULL DATE
```

需要生成的 SQL

```sql
insert into TMP_UPSTATE_CASEKEY values('TMP0000001', 1, sysdate);
```

存储过程实现

```sql
create or replace procedure proc_casekey_upstate
as
  casekey char(14);
begin
  for i in 1..10000000 loop
    casekey := 'TMP'||lpad(i,7,0);   -- TMP0000001
    insert into TMP_UPSTATE_CASEKEY values(casekey, 1, sysdate);
  end loop;
  commit;
end;

begin
  proc_casekey_upstate();
end;
```

测试发现生成一千万条数据用了 14 分钟左右，性能还是可以了，如果先去掉 TMP_NUM_STATUS_ID 的外键估计更快。

网友 雷厉\*风行 指出下面的方式速度更快，我测试插入一百万条记录十秒左右，当然了，这跟机器性能也有关系。

```sql
insert into TMP_UPSTATE_CASEKEY 
 select 'TMP'||LPAD(rownum,7,0),1,sysdate 
   from dual 
connect by level <= 1000000;
```

## 使用 python 生成 SQL 文件

下面贴出使用 python3 生成 SQL 的代码

```sql
from datetime import datetime

start = datetime.now();
with open('d:/casekey_upstate.sql', 'w') as f:
    for x in range(1, 10000000):
        print("insert into tmp_upstate_casekey values('TMP%07i', 1, sysdate);" %x, file=f);
end = datetime.now();
print(end-start);
```

生成的 sql 文件达 638M, 耗时 31 秒，有木有感觉使用 python 很方便呢。
