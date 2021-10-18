---
title: Oracle PL/SQL Code Fragments
tag: db
date: 2021-04-30
---

### debug

```sql
procedure debug(p_str in varchar2) is
begin
  dbms_output.put_line(p_str); --client PL/SQL output
  fnd_file.put_line(fnd_file.log, p_str); --application ERP log
exception
  when others then
    dbms_output.put_line('debug = ' || sqlerrm);
end;
```

### rpad & lpad

```sql
function char_format(p_data   in varchar2,
                     p_length in number,
                     p_align  in varchar2) return varchar2 is
  v_char varchar2(999);
begin

  begin
    select decode(p_align,
                  'R', rpad(nvl(p_data, ' '), p_length, ' '),
                  'L', lpad(nvl(p_data, ' '), p_length, ' '))
      into v_char
      from dual;
  end;

  return(v_char);
end char_format;


select char_format('H855', 15, 'R')
    || char_format('00', 3, 'R')
    || char_format('AC', 3, 'R')
  from dual;

--'H855            00 AC '
```

### put_file

```sql
procedure put_file(p_str in varchar2, p_flag in varchar2 default 'Y') is
begin
  if p_flag = 'Y' then 
    fnd_file.put_line(fnd_file.output, p_str); --file
  else 
    dbms_output.put_line(p_str); --client
    fnd_file.put_line(fnd_file.log, p_str); --application
  end if;
end;
```

### for loop mock seq, pallet, carton

```sql
for i in  0..99  loop

    if mod(i, 10) = 0 then
        l_carton_seq := l_carton_seq + 1;
    end if;

    if mod(i, 50) = 0 then
        l_pallet_seq := l_pallet_seq + 1;
    end if;

    l_sn_seq := l_sn_seq + 1;

end loop;
```

### put format json

```sql
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
```

### string clean

```sql
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
```

### date string change delimiter

```sql
--select som_edi_custom_utils_pkg.date_str_change_delimiter('20201012', '-') from dual;
--select som_edi_custom_utils_pkg.date_str_change_delimiter('2020/10/12', '-') from dual;
--select som_edi_custom_utils_pkg.date_str_change_delimiter('2020-10-12', '/') from dual;
function date_str_change_delimiter(p_date_str in varchar2, p_delimiter in varchar2 default '/') return varchar2
is
  l_dest_date_format varchar2(100);
  l_dest_date_str    varchar2(100);
begin
    begin
      l_dest_date_format := 'yyyy' || p_delimiter || 'mm' || p_delimiter || 'dd';

      /**
      * to_date(date_str, date_format) don't care what delimiter in date_str.
      * such as to_date('2020/10/12', 'yyyy#mm#dd'), to_date('20201012', 'yyyy#mm#dd') is right.
      * but to_date('2020/10/12', 'yyyymmdd') occurs error as below.
      * ORA-01858: a non-numeric character was found where a numeric was expected
      */
      select to_char(to_date(p_date_str, 'yyyy#mm#dd'), l_dest_date_format)
        into l_dest_date_str
        from dual;

    exception
      when others then
        debug('date_str_change_delimiter error: ' || sqlerrm);
        raise;
    end;

    return l_dest_date_str;
end date_str_change_delimiter;
```

### number to string with decimal

```sql
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
```

### string split

```sql
type table_str is table of varchar2(4000);
--select trim(column_value) from table(som_edi_custom_utils_pkg.str_split_to_table('a, b, c')); => a b c
function str_split_to_table(p_str in varchar2, p_separator in varchar2 default ',') return table_str 		pipelined
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
```

### get table columns

```sql
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
```

### get split sub str

```sql
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

function get_sub_str(p_str in varchar2, p_separator in varchar2, p_appear_position in number) return varchar2
is
   l_return varchar2(4000);
begin
   begin
     select column_value
       into l_return
       from (select rownum as no, trim(column_value) as column_value
               from table(str_split_to_table(p_str, p_separator)))
      where no = p_appear_position;
   end;

   return l_return;
end get_sub_str;
```

### seq add

```sql
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
```

### test regexp

```sql
procedure str_regexp_test
is
  l_index number;
begin

  l_index := regexp_instr('H850 PO001', '^H\d{3}');

  if l_index = 1 then
    debug('New po line.');
  end if;

end str_regexp_test;
```

### test pivot

```sql
/*
procedure pivot_test
is
begin
  begin
    with employee(id, firstname, lastname, hobbies) as
    (
      select 1, 'a', 'b', '1' from dual union
      select 2, 'a', 'b', '2' from dual union
      select 3, 'a', 'b', '3' from dual union
      select 4, 'c', 'd', '3' from dual union
      select 5, 'e', 'f', '2' from dual
    )

    select *
      from employee
      pivot
      (
        max(id) foo,
        max(1)  bar
        for(hobbies)
          in('2' as two, '3' as three)
      );


    select
      firstname,
      lastname,
      max(case when hobbies = '2' then id end) two_foo,
      max(case when hobbies = '2' then 1  end) two_bar,
      max(case when hobbies = '3' then id end) three_foo,
      max(case when hobbies = '3' then 1  end) three_bar
    from employee
    group by
      firstname,
      lastname;



    --the pivot generates N * M new columns, where N = number of values of the IN clause and M = number of aggregations specified,
    --so having no filters and that single harmless aggregation will produce 0 * 1 = 0 new columns and will remove the ones specified in the PIVOT clause, which is just the hobbies.
    select *
      from employee
      pivot(
        max(1) -- fake  m
        for(hobbies)  -- put the undesired columns here
        in ()  -- no values here
      )
      where 1=1 -- and your filters here

  end;
end pivot_test;
*/
```

### test array

```sql
procedure array_test
is
  type var_array_type is varray(10) of varchar2(20);
  var_array var_array_type := var_array_type('Oracle', 'MySQL', 'SQLServer');

  type table_array_type is table of varchar2(20) index by binary_integer;
  table_array table_array_type;

  type table_rows_type is table of scott.emp%rowtype index by binary_integer;
  table_rows table_rows_type;
begin
  for i in 1 .. var_array.count loop
    debug(var_array(i));
  end loop;

  table_array(1) := 'MongoDB';
  table_array(2) := 'Redis';
  table_array(3) := 'Memcache';
  for i in 1 .. table_array.count loop
    debug(table_array(i));
  end loop;

  select * bulk collect into table_rows from scott.emp;
  for i in 1..3 loop
    debug(table_rows(i).empno || ': ' || table_rows(i).ename);
  end loop;

end array_test;
```
