---
title: EDI Expercience
tag: edi
date: 2021/05/06
---

### 数据状态

表中的数据状态不要使用`E, S`这种简码，尽量使用 `Error, Success`全称, 见名知意，可以在 Package Spec 顶部定义状态相关的全局变量。

```sql
g_pending    varchar2(100) := 'Pending';
g_running    varchar2(100) := 'Running';
g_reject     varchar2(100) := 'Reject';
g_error      varchar2(100) := 'Error';
g_success    varchar2(100) := 'Success';
```

### Trigger

trigger 中如果包含外部 package 中的代码，保证 package 的最简化，或者将 trigger 需要调用的功能移动到单独的 package。因为 package 中包含过多其它逻辑代码，对其修改过程造成的错误会影响 trigger 的正常执行。 

### 字符串连接

多个字符串连接可以考虑将连接符(||)放在每个字段最前面，这样每次字段调整不用刻意调整 || 的位置。

```	sql
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

FTP push & FTP pull 同时对文件操作导致最终 pull 下来的文件不完整。

push 时如果文件未 push 完成，加上 .temp 的后缀，当文件 push 完成时再还原为原来的文件名，pull 文件时忽略 .temp 的文件

### Schedule Overlap

每个 schedule 处理文件时为当前文件加上处理时间戳，然后处理此指定时间戳的文件，其它 schedule 程式处理时户料已经有时间戳的文件。
