---
title: python cx_Oracle
tags: python
---

### 读取压缩 excel 数据到 oracle

1. 使用 7z 解压缩 zip 文件
2. 获取所有 excel 文件
3. 读取 excel 数据到列表
4. 使用 cx_Oracle 写入将列表数据写入 oracle

```python
import xlrd
import rarfile
import os
import cx_Oracle

dev1 = 'username/password@instance'
conn_str = dev1


# avoid encode error
os.environ['nls_lang'] = 'AMERICAN_AMERICA.AL32UTF8'


basedir =  r'C:\Users\11435\Desktop\SN_XLSX'

def unpack_rar(filedir):
    for filename in os.listdir(filedir):
        if filename.endswith('.rar'):
            rar_path = os.path.join(filedir, filename)
            unpack_dir = rar_path.split('.')[0]
            if not os.path.exists(unpack_dir):
                os.mkdir(unpack_dir)
            # x exclude file, -o output dir
            cmd = f'7z.exe x {rar_path} -o{unpack_dir}'
            result = os.popen(cmd).read()
            if 'Everything is Ok' in result:
                print(f'unpack {filename} success')

def get_xls_files(filedir):
    files_list = []
    for filename in os.listdir(filedir):
        filepath = os.path.join(filedir, filename)
        if os.path.isdir(filepath):
            for filename in os.listdir(filepath):
                if filename.endswith(('.xls', 'xlsx')):
                    files_list.append(os.path.join(filepath, filename))
    return files_list

def parse_data(filename):
    data = xlrd.open_workbook(filename)
    tables = data.sheets()   # get all sheets
    list_values = []
    for table in tables:
        nrows = table.nrows  # rows
        ncols = table.ncols  # cols
        start = 1            # start col, except titile
        end = nrows          # end col

        for x in range(start, end):
            values = []
            row = table.row_values(x)
            for i in range(0, ncols):
                values.append(str(row[i])) # database all fields use varchar2
            values.append(filename.split('\\')[-2]) # use dir as sheetname
            list_values.append(values)
    return list_values



def import_db(data_rows):

    con = cx_Oracle.connect(conn_str)

    # Create Oracle DB Cursor
    cursor = cx_Oracle.Cursor(con)

    # Insert data to table
    # print(con.version)

    # for row in data_rows:
    #     # get seq
    #     seq = cursor.execute('select som_edi_seq_id_s.nextval from dual')
    #     # seq.fetchone() is a tuple
    #     row.insert(0, seq.fetchone()[0])


    cursor.prepare(
        """
        INSERT INTO sms_ascp_daily_back_temp(ID, PLAN_VER, SHEET_NAME)
        VALUES (:1,	:2,	:3)
        """)

    cursor.executemany(None, data_rows)
    con.commit()


import time

if __name__ == '__main__':

    unpack_rar(basedir)

    start = time.time()

    for filename in get_xls_files(basedir):
        start_per_time = time.time()
        data_rows = parse_data(filename)
        import_db(data_rows)
        print(f"{filename} - rows: {len(data_rows)} - cost: {time.time() - start_per_time}")

    print('all cost time: {}'.format(time.time() - start))
```

### 字典快速插入数据库

> https://www.biaodianfu.com/python-insert-dict-into-db.html

该方法不支持层级嵌套的字典，也不支持数据 Value 中存在 null 和 True 和 False 的情况。

```python
def insert_data(data_table, data_dict):
    placeholders = ', '.join(['%s'] * len(data_dict))
    columns = ', '.join(data_dict.keys())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (data_table, columns, placeholders)
    print(sql)
    datas =  tuple(data_dict.values())
    cur.execute(sql, datas)
    conn.commit()
# insert_data('test', {'a': 1, 'b':2})
# INSERT INTO test ( a, b ) VALUES ( %s, %s )
```

### xlrd 数据类型的判断

| Sample           | Type symbol     | Type number | Python value                                                 | Converted value   |
| ---------------- | --------------- | ----------- | ------------------------------------------------------------ | ----------------- |
|                  | XL_CELL_EMPTY   | 0           | empty string ''                                              | None              |
| abc              | XL_CELL_TEXT    | 1           | a Unicode string                                             |                   |
| 123              | XL_CELL_TEXT    | 1           | a Unicode string                                             |                   |
| 123.0            | XL_CELL_TEXT    | 1           | a Unicode string                                             |                   |
| 123              | XL_CELL_NUMBER  | 2           | float                                                        | int               |
| 123.45           | XL_CELL_NUMBER  | 2           | float                                                        |                   |
| 2019/10/25       | XL_CELL_DATE    | 3           | float                                                        | datetime.datetime |
| 18:45:05         | XL_CELL_DATE    | 3           | float                                                        | datetime.datetime |
| 2019/10/25 19:37 | XL_CELL_DATE    | 3           | float                                                        | datetime.datetime |
| TRUE             | XL_CELL_BOOLEAN | 4           | int; 1 means TRUE, 0 means FALSE                             | bool              |
| #REF!            | XL_CELL_ERROR   | 5           | int representing internal Excel codes; for a text representation, refer to the supplied dictionary error_text_from_code | str               |

```python
import xlrd
from pprint import pprint


def read_sheet(sheet):
    """Read a worksheet's content into a 2-dimensional list

    :sheet: xlrd.sheet.Sheet instance
    :returns: list

    """
    sheet_values = []
    for row_num in range(sheet.nrows):
        row = sheet.row(row_num)
        row_values = []
        for cell in row:
            if cell.ctype == 0:     # XL_CELL_EMPTY
                row_values.append(None)
            elif cell.ctype == 2:   # XL_CELL_NUMBER
                # Trim the trailing ".0" by converting the number to int.
                if cell.value == int(cell.value):
                    row_values.append(int(cell.value))
                else:
                    row_values.append(cell.value)
            elif cell.ctype == 3:   # XL_CELL_DATE
                # Convert an Excel date/time number into a datetime.datetime object.
                # datemode=0: 1900-based on Windows
                # if excel only time show, row will show day 1899/12/31
                # such as 18:45:05 => datetime.datetime(1899, 12, 31, 18, 45, 5)
                row_values.append(
                    xlrd.xldate.xldate_as_datetime(cell.value, datemode=0))
            elif cell.ctype == 4:   # XL_CELL_BOOLEAN
                row_values.append(bool(cell.value))
            elif cell.ctype == 5:   # XL_CELL_ERROR
                row_values.append(xlrd.biffh.error_text_from_code[cell.value])
            else:
                row_values.append(cell.value)
        sheet_values.append(row_values)
    return sheet_values


if __name__ == "__main__":
    data = xlrd.open_workbook('test_excel.xlsx')
    tables = data.sheets()  # get all sheets
    for table in tables:
        data = read_sheet(table)
        pprint(data)
```



> cx-oracle: https://cx-oracle.readthedocs.io/en/latest/
