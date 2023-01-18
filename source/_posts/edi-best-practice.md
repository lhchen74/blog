---
title: EDI Experience
tag: edi
date: 2021/05/06
---

### Data Status

表中的数据状态不要使用 `E, S` 这种简码，尽量使用 `Error, Success` 全称, 见名知意，可以在 Package Spec 顶部定义状态相关的全局变量。

```sql
g_pending    varchar2(100) := 'Pending';
g_running    varchar2(100) := 'Running';
g_reject     varchar2(100) := 'Reject';
g_error      varchar2(100) := 'Error';
g_success    varchar2(100) := 'Success';
```

### Trigger

Trigger 中如果包含外部 Package 中的代码，保证 Package 的最简化，或者将 Trigger 需要调用的功能移动到单独的 Package。因为 Package 中包含过多其它逻辑代码，对其修改过程造成的错误会影响 Trigger 的正常执行。

### Cursor

避免在 Cursor 中使用函数，因为函数错误在 Cursor 中没有办法检查。

### Group By

SQL 语句中存在 Group By 时，添加 Select 字段时需要确认 Group By 中同步添加，因为 Group By 中没有添加 Select 字段编译不会报错，但是执行会报错。

### Rollback

程式写入出错时应该尽量使用 rollback, 不要在出错后删除错误数据，这样不仅会增加加额外的操作，而且删除会导致误删等情況。

```sql
if l_err_msg is not null then
  rollback;

  debug(l_err_msg);

  update som_edi_extreme_source
     set transfer_flag = 'F',
         transfer_date = sysdate,
         ret_msg = l_err_msg
   where seq_id = r_import_list.seq_id;
else
  update som_edi_extreme_source
     set transfer_flag = 'Y',
         transfer_date = sysdate,
         ref_id = l_header_seq,
         ref_line_id = l_line_seq
   where seq_id = r_import_list.seq_id;
end if;
```

### String Concat

多个字符串连接可以考虑将连接符(||)放在每个字段最前面，这样每次字段调整不用刻意调整 || 的位置。

```sql
cursor cur_hst(p_edi_id in number) is
    select som_edi_pkg.char_format('H', 1, 'R')
        || som_edi_pkg.char_format('ST', 3, 'R')
        || som_edi_pkg.char_format(seh.ship_to, 61, 'R')
        || som_edi_pkg.char_format('92', 3, 'R')
        || som_edi_pkg.char_format(seh.ship_to_location, 81, 'R')
        || som_edi_pkg.char_format(seh.ship_to_line1, 56, 'R')
        || som_edi_pkg.char_format(seh.ship_to_line2, 56, 'R')
        || som_edi_pkg.char_format(seh.ship_to_city, 31, 'R')
        || som_edi_pkg.char_format(seh.ship_to_state, 3, 'R')
        || som_edi_pkg.char_format(seh.ship_to_zip_code, 16, 'R')
        || som_edi_pkg.char_format(seh.ship_to_country, 4, 'R')
        data
     from som_edi_temp_h seh
    where seh.edi_id = p_edi_id;
```

### Concurrent Request

首先更新表的 request_id 为当前 conc_request_id, 然后以此 conc_request_id 为参数查询表中数据

```sql
procedure process_856_batch(errbuf          out varchar2,
                            retcode         out varchar2,
                            p_delivery_id   in  varchar2)
is
  l_sub_retcode number;
  l_request_id number := fnd_global.conc_request_id;

  cursor cur_asn(p_request_id in number) is
    --Step two
    select seh.delivery_id
      from som_edi_856_header seh
     where seh.send_asn_parent_request_id = p_request_id
       and seh.asn_status = 'R';

  l_req_id_fee                number;
  l_req_option                boolean;

begin

  --Step one
  update som_edi_856_header seh
      set seh.asn_status = 'R',
          seh.send_asn_parent_request_id = l_request_id
    where nvl(seh.asn_status, 'N') = 'R'
      and get_order_type(seh.delivery_id) = 'A01'
      and seh.send_asn_parent_request_id is null
      and seh.delivery_id = nvl(p_delivery_id, seh.delivery_id);

  commit;

  for r_asn in cur_asn(l_request_id) loop

      l_req_option:=fnd_request.add_delivery_option(TYPE=>'T',
                                                    p_argument1 =>FND_PROFILE.VALUE('SOM_EDI_FTP_IP'),
                                                    p_argument2 =>FND_PROFILE.VALUE('SOM_EDI_FTP_ACCOUNT'),
                                                    p_argument3 =>FND_PROFILE.VALUE('SOM_EDI_FTP_PASSWORD'),
                                                    p_argument4 =>FND_PROFILE.VALUE('SOM_EDI_DIRECT_856'),
                                                    nls_language=>'');


      l_req_id_fee:= fnd_request.submit_request(application  => 'YSC',
                                                program      => 'SOMP4028_S',
                                                description  => null,
                                                start_time   => null,
                                                sub_request  => false,
                                                argument1    => r_asn.delivery_id);

      if l_req_id_fee = 0 then
        retcode := '2';
        debug('Failed to submit request for delivery_id: '|| r_asn.delivery_id);

        update som_edi_856_header seh
            set seh.asn_status = null,
                seh.send_asn_parent_request_id = null
          where seh.delivery_id = r_asn.delivery_id;
        commit;

      else
        debug('Submitted request id: '|| l_req_id_fee
              ||' for delivery_id: '|| r_asn.delivery_id);
      end if;
  end loop;
end process_856_batch;
```

### FTP

FTP Push & FTP Pull 同时对文件操作导致最终 Pull 下来的文件不完整。

Push 时如果文件未 Push 完成，加上 .temp 的后缀，当文件 Push 完成时再还原为原来的文件名，Pull 文件时忽略 .temp 的文件。

### Schedule Overlap

每个 schedule 处理文件时为当前文件加上处理时间戳，然后处理此指定时间戳的文件，其它 schedule 程式处理时忽略已经有时间戳的文件。

### for update avoid update at the same time

```sql
begin
  --for update 当前 session 可以执行更新，其它 session 更新必须等到当前 session for update 的 commit 或者 rollback
  --在 PL/SQL 不能使用 select 1 from som_edi_asn_header for update; select 必须有 insert 语句; 否则会出现 Error: PLS-00428: an INTO clause is expected in this SELECT statement；
  --for update 查询也不能有聚合函数, select distinct 1 into l_fake_column from som_edi_asn_header for update; 会出现 Error: PL/SQL: ORA-01786: FOR UPDATE of this query expression is not allowed；
  --所以使用 execute 执行 SQL 语句。
  execute immediate 'select 1 from som_edi_asn_header for update'; -- Lock

  update som_edi_asn_header seh
      set seh.file_counter =
          (select nvl(max(sh.file_counter), 0) + 1
            from som_edi_asn_header sh
            where sh.transfer_flag = 'Y'
              and sh.creation_date >= trunc(sysdate)
              and sh.creation_date < trunc(sysdate) + interval '1' day)
    where seh.header_id = p_header_id;

  commit; --Release Lock
end;

begin
  select
      'ASN'
      || '_' || count(*)
      || '_' || to_char(sh.creation_date, 'yyyymmdd')
      || '_' || sh.file_counter
      || '.txt'
    into l_asn_filename
    from som_edi_asn_header sh,
          som_edi_asn_line   sl
    where sh.header_id = sl.header_id
      and sh.header_id = p_header_id
    group by sh.creation_date, sh.file_counter;
exception
  when others then
    debug('get ans_filename error, header_id: ' || p_header_id);
    retcode := '2';
end;
```

```sql
execute immediate 'select 1 from som_edi_asn_header for update'; --Lock

--已经有相同时间产生的文件，将当前资料增加 1s，这样依据时间（yyyymmddhhmiss）命名文件不会重复。
update som_edi_asn_header sh
    set sh.creation_date = sh.creation_date + interval '1' second
  where sh.header_id = p_header_id
    and sh.creation_date in
        (select creation_date from som_edi_asn_header);

commit; --Release Lock

begin
    select
        'ASN'
        || '_' || to_char(sh.creation_date, 'yyyymmddhhmiss')
        || '.csv'
    into l_asn_filename
    from som_edi_asn_header sh
    where sh.header_id = p_header_id;
exception
  when others then
    debug('get asn_filename error, header_id: ' || p_header_id);
    retcode := '2';
end;
```

### FTP UploadFolder use Absolute Path

在连接到 FTP 之后，可能会执行多个类型文件传输，当上传 SN 时用 `objFTP.cwd(sectionUpload.get("UploadFolder"))` 进入 FTP Folder `TEST/Outbound/SN` 上传成功后，FTP 没有断开连接还是在 `TEST/Outbound/SN` 这个目录，当再上传 RFID 时，`objFTP.cwd(sectionUpload.get("UploadFolder"))` 目录会变成 `TEST/Outbound/SN/TEST/Outbound/RFID` 会出现找不到此目录错误，可以使用绝对路径`/TEST/Outbound/SN`, `/TEST/Outbound/RFID`，每次都是从根目录开始进入 FTP Folder。

```python
for sectionFTP in sectionTarget.iter('FTP'):
  objFTP = FTP(sectionFTP.get("SITE"))
  objFTP.login(sectionFTP.get("ID"), sectionFTP.get("PASSWORD"))
  for sectionUpload in sectionFTP.iter('FILE'):
    objFTP.cwd(sectionUpload.get("UploadFolder"))
```

```xml
<TARGET ID="ASN" Description="SN and RFID files">
  <FTP SITE="site" ID="username" PASSWORD="password">
      <FILE TYPE="SN" TEMPLATE="VZ*.txt" SourceFolder="D:\HUB_EDI\TEST\FilePool\SN\" UploadFolder="TEST/Outbound/SN" BackupFolder="D:\HUB_EDI\TEST\FilePoolSN\bak\" MailAppender="MailASN" />
      <FILE TYPE="RFID" TEMPLATE="SERC*.csv" SourceFolder="D:\HUB_EDI\TEST\FilePool\RFID\" UploadFolder="TEST/Outbound/RFID" BackupFolder="D:\HUB_EDI\TEST\FilePoolRFID\bak\" MailAppender="MailASN" />
  </FTP>
</TARGET>
```
