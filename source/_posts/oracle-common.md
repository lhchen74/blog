---
title: oracle common
date: 2018-08-08
tags: db
---

### group then fetch max

```sql
--method1
select *
  from som_edi_temp_d setd
 where seq_id = (select max(setd2.seq_id)
                   from som_edi_temp_d setd2
                  where setd.po_line = setd2.po_line
                    and setd2.cust_po_number = '4512229779')

--method2
select a.*
  from som_edi_temp_d a,
       (select sd.po_line, max(sd.seq_id) seq_id
          from som_edi_temp_d sd
         where sd.cust_po_number = '4512229779'
         group by sd.po_line) b
 where a.po_line = b.po_line
   and a.seq_id = b.seq_id

--method3
--num 也会查询出来
select *
  from (select sd.*,
               row_number() over(partition by po_line order by seq_id desc) as num
          from som_edi_temp_d sd
         where sd.cust_po_number = '4512229779') t
 where t.num = 1
```

### dbms_output, fnd_file

| code                                   | meaning                                                          |
| -------------------------------------- | ---------------------------------------------------------------- |
| dbms_output.put('')                    | Output content to buffer                                         |
| dbms_output.put_line('')               | Output content to console and newline                            |
| fnd_file.put(fnd_file.output, '')      | Writes text to a file, without appending any new line characters |
| fnd_file.new_line(fnd_file.output, 1)  | Writes line terminators to a file (new line character)           |
| fnd_file.put_line(fnd_file.output, '') | Writes text to a file followed by a new line character           |


### debug log and raise exception

select get_mes_snvalue_data(1001, 'HW_VER') from dual;

```sql
function get_mes_snvalue_data(p_body_id in varchar2, p_qualified_code in varchar2) return varchar2
is
  l_return varchar2(100);
begin
  begin
    select sn.itemvalue into l_return
      from ssc_t_edi_snvalue sn
      where sn.body_id = p_body_id
        and sn.item = p_qualified_code;
  exception
      when others then
          som_edi_pkg.debug('get_mes_snvalue_data error, ssc_t_edi_snvalue.body_id: ' || p_body_id
          || ', ' || 'ssc_t_edi_snvalue.item: ' || p_qualified_code || sqlcode || sqlerrm);
          raise;
  end;
  return l_return;
end get_mes_snvalue_data;
```

### common util 

```sql
create or replace package body som_edi_custom_utils_pkg is

 /**
  * put_json_line('name', 'babb')
  *     "name": "babb",
  */
  procedure put_json_line(p_field in varchar2, p_value in varchar2, p_tab_num in number default 1) is
  begin
    for k in 1..p_tab_num loop
      dbms_output.put(chr(9));  --char(9) tab
    end loop;
    
    dbms_output.put_line('"' || p_field || '"' ||  ': ' || '"' || p_value || '"' || ',');
  exception
    when others then
      raise;
  end put_json_line;
  
  --Remove all CR/LF, trim the left and right spaces, tabs
  function str_clean(p_str in varchar2) return varchar2 
  is
    l_return varchar2(1000);
    l_tab_space varchar2(10) := chr(9) || ' ';
  begin
    /** 
     * Standard ASCII Characters
     * Decimal    Description
     * 9    	    Horizontal tab (HT)
     * 10         Line feed (LF)
     * 13         Carriage return (CR)
     */
    begin 
      --translate(p_str, 'a' || chr(10) || chr(13), 'a'): a translate to a, chr(10) & chr(13) replace to empty
      --ltrim(str, l_tab_space): trim left tab and space behavior like translate, such as 'chr(9) chr(9) a' will trim to 'a'
      --if use trim twice select trim(trim(chr(9) from chr(9) || ' ' || chr(9) ||  'a')) from dual; will got 'chr(9) a'  	
      select rtrim(ltrim(translate(p_str, 'a' || chr(10) || chr(13), 'a'), l_tab_space), l_tab_space) 
        into l_return
        from dual;
    end;
  
    return l_return;

  end str_clean;
  
  
  --select trim(column_value) from table(som_edi_custom_utils_pkg.str_split_to_table('a, b, c')); => a b c
  function str_split_to_table(p_str in varchar2, p_separator in varchar2 default ',') return table_str pipelined
  is
    l_src    varchar2(4000);
    l_index  pls_integer;
    l_start  pls_integer;
  begin   
    begin
      l_src := p_str;
      l_start := 1;
        
      loop
          l_index := instr(l_src, p_separator, l_start);
          if nvl(l_index, 0) = 0 then
              pipe row (substr(l_src, l_start)); 
              exit;
          else
              pipe row (substr(l_src, l_start, l_index - l_start));     
              l_start := l_index + length(p_separator);
          end if;
      end loop;
      
    exception
      when others then
         debug(dbms_utility.format_error_backtrace||sqlerrm);
         debug('String: "' || l_src ||'", l_start: ' || l_start || ', l_index: '|| l_index);
    end;
        
    return;
       
  end str_split_to_table;
  
  procedure str_regexp_test
  is
    l_index number;
  begin
    
    l_index := regexp_instr('H850 PO001', '^H\d{3}');
    
    if l_index = 1 then
      debug('New po line.');
    end if;
    
  end str_regexp_test;
  
  
  --11.256 => 11.26  11 => 11.00  11.2 => 11.20
  function num_to_str_with_decimal(p_number in number, p_decimal in number default 2) return varchar2
  is
     l_str           varchar2(100);
     l_dot_index     number;
     l_zero_count    number;
  begin
     begin 
       --11.256 => 11.26  11 => 11  11.2 => 11.2
       l_str := to_char(round(p_number, p_decimal));
       
       if p_decimal = 0 then
         return l_str;
       end if;
       
       l_dot_index := instr(l_str, '.');
       
       if l_dot_index = 0 then
         l_str := l_str || '.';
         l_zero_count := p_decimal;
       else
         l_zero_count := p_decimal - (length(l_str) - l_dot_index);
       end if;
       
       for i in 1..l_zero_count loop
         l_str := l_str || '0';
       end loop;
       
     end;
     
     --other way: keep two decimals
     --select trim(to_char(11.256, '99999990.00')) from dual;
     
     return l_str;
  end num_to_str_with_decimal;
  
  --select som_edi_custom_utils_pkg.get_table_columns('som_edi_temp_h') from dual;
  --select som_edi_custom_utils_pkg.get_table_columns('som_edi_temp_h', '|', 'SSIS_ID|EDI_DATE') from dual;
  function get_table_columns(p_table_name      in varchar2, 
                             p_delimiter       in varchar2 default ',', 
                             p_exclude_columns in varchar2 default null) return varchar2 
  is
    l_count   number;
    l_columns varchar2(1000);
  begin
    begin
      
      select count(*)
        into l_count
        from dba_tables
       where owner in ('YSC', 'APPS')
         and table_name = upper(p_table_name);
      
      if l_count = 0 then 
        return 'ERROR: Table not exists in YSC or APPS.';
      end if;
   
      select listagg(t.column_name, p_delimiter) within group(order by t.segment_column_id)
        into l_columns
        from all_tab_cols t
       where t.table_name = upper(p_table_name)
         and (t.column_name not in (
               select trim(column_value) 
                 from table(str_split_to_table(p_exclude_columns, p_delimiter))
               ) or p_exclude_columns is null
         );
         
    end;
    
    return l_columns;
  end get_table_columns;
  
  
  --After manual mock data, update db seq avoid conflict with erp generate data
  --select som_edi_custom_utils_pkg.seq_add('seq_name', 2) from dual;
  function seq_add(p_seq_name in varchar2, p_count in number) return number
  is
    l_last_seq number;
  begin  
    
    begin
      for i in 1 .. p_count loop
        --ORA-01722: invalid number 
        --object_name can't use bind variable
        --execute immediate 'select :1.nextval from dual' into l_last_seq using p_seq_name;
        execute immediate 'select ' || p_seq_name || '.nextval from dual' into l_last_seq;
      end loop;
    end;
    
    return l_last_seq;

  end seq_add;
  
  procedure mail_template is 
    
     x_ret_code        varchar2(1);
     x_ret_msg         varchar2(4000);
    
     l_table_start     varchar2(10)  := '<table>';
     l_table_end       varchar2(10)  := '</table>';
     l_tr_start        varchar2(5)   := '<tr>';
     l_tr_end          varchar2(5)   := '</tr>';
     l_th_start        varchar2(5)   := '<th>';
     l_th_end          varchar2(5)   := '</th>';
     l_td_start        varchar2(5)   := '<td>';
     l_td_end          varchar2(5)   := '</td>';
     
     l_internal_style  varchar2(1000); 
        
     l_subject         varchar2(2000);      
     l_sender          varchar2(1000);
     l_receiver        varchar2(4000);
     l_cc              varchar2(8000);
     l_bcc             varchar2(8000);
       
     l_body            varchar2(32767);
     l_subject_keyword        varchar2(32767);
               
     cursor c_rcpt is
       select dl.rcpt_cat,
              dl.email_address
         from sfn_distribution_list_h dh,
              sfn_distribution_list_l dl
        where dh.list_name = 'SOM_EDI_INBOUND'
          and dh.header_id = dl.header_id 
          and nvl(dh.status, 'N') = 'Y'
          and nvl(dl.status, 'N') = 'Y'
          and (nvl(dl.rcpt_name, 'N') like 'EXTREME%' or nvl(dl.rcpt_name,'N') like 'IT%');
    
    cursor data_list is 
      select '1' column_one, '2' column_two from dual
      union
      select 'a' column_one, 'b' column_two from dual;
                   
  begin     
     begin
       --use internal style sheet rather than inline style
       l_internal_style := '
         <style>
             table {
                 width: 100%; 
                 border-collapse: collapse; 
                 text-align: center;
             }
             
             th {
                border:1px solid #cad9ea; 
                background-color:#cce8eb;
             }
             
             td {
                border: 1px solid #cad9ea;
             }
          </style>';
       
       l_body := '<html><head>' || l_internal_style || '</head><body>';
       
       --table start
       l_body := l_body || l_table_start;  
         l_body := l_body || 
         l_tr_start ||
           l_th_start||'Column One'||l_th_end||
           l_th_start||'Column Two'||l_th_end||
         l_tr_end;
          
         for r_d in data_list loop 
           
           if l_subject_keyword is not null then 
              l_subject_keyword := l_subject_keyword || ',';
           end if;
           l_subject_keyword := l_subject_keyword || r_d.column_one;
           
           l_body := l_body || 
           l_tr_start ||
             l_td_start||r_d.column_one||l_td_end||
             l_td_start||r_d.column_two||l_td_end||
           l_tr_end;

         end loop;
       
       l_body := l_body || l_table_end;
       --table end
       
       l_body := l_body || '</body></html>';
         

       for r_rcpt in c_rcpt loop
         if r_rcpt.rcpt_cat = 'TO' then
           l_receiver := l_receiver || r_rcpt.email_address || ',';
         elsif r_rcpt.rcpt_cat = 'CC' then
           l_cc := l_cc || r_rcpt.email_address || ',';
         elsif r_rcpt.rcpt_cat = 'BCC' then
           l_bcc := l_bcc || r_rcpt.email_address || ',';
         end if;
       end loop;    
       
       
       l_subject := '[NOTIFY] Test OK [ ' || l_subject_keyword || ']';  
       l_sender := 'Babb_Chen <Babb_Chen@sdc.sercomm.com>';
       --Just for test
       l_receiver := 'Babb_Chen <Babb_Chen@sdc.sercomm.com>'; 
       l_cc := 'Babb_Chen <Babb_Chen@sdc.sercomm.com>'; 
       l_bcc := 'Babb_Chen <Babb_Chen@sdc.sercomm.com>'; 
       --
       
       sfn_mail.send_email(
               p_directory   => null,     
               p_priority    => 1,       
               p_sender      => l_sender,
               p_recipient   => l_receiver,
               p_cc          => l_cc,
               p_bcc         => l_bcc,
               p_subject     => l_subject,
               p_body        => l_body,    
               p_attachment1 => null,      
               p_attachment2 => null,     
               p_attachment3 => null,      
               p_attachment4 => null,      
               p_mime_type   => 'text/html; charset=utf-8',
               x_ret_code    => x_ret_code,
               x_ret_msg     => x_ret_msg);     
     end; 
  end  mail_template;
  

  procedure debug(p_str in varchar2) is
  begin
    dbms_output.put_line(p_str); --client PL/SQL output
    fnd_file.put_line(fnd_file.log, p_str); --application ERP log
  exception
    when others then
      dbms_output.put_line('debug = ' || sqlerrm);
  end;
  
end som_edi_custom_utils_pkg;
```