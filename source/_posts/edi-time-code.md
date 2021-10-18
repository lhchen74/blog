---
title: EDI Time with Zone
date: 2021-10-13
tags: edi
---

跨区域跨国贸易中，因为有时区的差异，在发送 EDI 时关于时间的讯息一般会包含时区的讯息，例如 `DTM*002*20200331*121010*20` 这里的 `20` 就是 timezone，在转入订单等情况下需要将 EDI 中的时间转换为本地时间。

首先需要定义 EDI Time Code 所对应的 UTC offset.

```sql
create table SOM_EDI_TIME_CODE
(
  code        VARCHAR2(2),
  meaning     VARCHAR2(100),
  utc_offset  NUMBER
) 
```

| CODE | MEANING                       | UTC_OFFSET |
| ---- | ----------------------------- | ---------- |
| 01   | Equivalent to ISO P01         | 1          |
| 02   | Equivalent to ISO P02         | 2          |
| 03   | Equivalent to ISO P03         | 3          |
| 04   | Equivalent to ISO P04         | 4          |
| 05   | Equivalent to ISO P05         | 5          |
| 06   | Equivalent to ISO P06         | 6          |
| 07   | Equivalent to ISO P07         | 7          |
| 08   | Equivalent to ISO P08         | 8          |
| 09   | Equivalent to ISO P09         | 9          |
| 10   | Equivalent to ISO P10         | 10         |
| 11   | Equivalent to ISO P11         | 11         |
| 12   | Equivalent to ISO P12         | 12         |
| 13   | Equivalent to ISO M12         | -12        |
| 14   | Equivalent to ISO M11         | -11        |
| 15   | Equivalent to ISO M10         | -10        |
| 16   | Equivalent to ISO M09         | -9         |
| 17   | Equivalent to ISO M08         | -8         |
| 18   | Equivalent to ISO M07         | -7         |
| 19   | Equivalent to ISO M06         | -6         |
| 20   | Equivalent to ISO M05         | -5         |
| 21   | Equivalent to ISO M04         | -4         |
| 22   | Equivalent to ISO M03         | -3         |
| 23   | Equivalent to ISO M02         | -2         |
| 24   | Equivalent to ISO M01         | -1         |
| AD   | Alaska Daylight Time          | -8         |
| AS   | Alaska Standard Time          | -9         |
| AT   | Alaska Time                   | -9         |
| CD   | Central Daylight Time         | -5         |
| CS   | Central Standard Time         | -6         |
| CT   | Central Time                  | -6         |
| ED   | Eastern Daylight Time         | -4         |
| ES   | Eastern Standard Time         | -5         |
| ET   | Eastern Time                  | -5         |
| GM   | Greenwich Mean Time           | 0          |
| HD   | Hawaii-Aleutian Daylight Time | -9         |
| HS   | Hawaii-Aleutian Standard Time | -10        |
| MD   | Mountain Daylight Time        | -6         |
| MS   | Mountain Standard Time        | -7         |
| MT   | Mountain Time                 | -7         |
| ND   | Newfoundland Daylight Time    | -2.5       |
| NS   | Newfoundland Standard Time    | -3.5       |
| NT   | Newfoundland Time             | -3.5       |
| PD   | Pacific Daylight Time         | -7         |
| PS   | Pacific Standard Time         | -8         |
| PT   | Pacific Time                  | -8         |
| TD   | Atlantic Daylight Time        | -3         |
| TS   | Atlantic Standard Time        | -4         |
| TT   | Atlantic Time                 | -4         |
| UT   | Universal Time Coordinate     | 0          |

定义计算函数，传入日期和 EDI Time Code, 输出对应的 Local 时间(这里是 China Local Time UTC+8)

```sql
function get_local_time(p_datetime in date, p_time_code in varchar2) return date
   is
     l_return date;
     l_local_offset  number := 8;
     l_one_day_hours number := 24;
   begin
     begin
       select p_datetime + (l_local_offset - tc.utc_offset) / l_one_day_hours
         into l_return
         from som_edi_time_code tc
        where tc.code = p_time_code;
     exception
       when others then
         raise;
     end;
     
     return l_return;
 end get_local_time;
```



以 `DTM*002*20200331*121010*20` 为例  get_local_time 输出 `4/1/2020 1:10:10 AM`

```sql
select get_local_time(
        to_date('20200331 121010', 'yyyymmdd hh24miss'), 
        20)
  from dual;
```

