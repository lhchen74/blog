---
title: Python Pandas Load Excel To Oracle
tags: python
date: 2020-01-20
---
### pandas.DataFrame.to_sql[¶](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html#pandas-dataframe-to-sql)

`DataFrame.to_sql(*self*, *name*, *con*, *schema=None*, *if_exists='fail'*, *index=True*, *index_label=None*, *chunksize=None*, *dtype=None*, *method=None*)`

Write records stored in a DataFrame to a SQL database.

Databases supported by SQLAlchemy [[1\]](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html#r689dfd12abe5-1) are supported. Tables can be newly created, appended to, or overwritten.

| param                                                        | mean                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **name** : string                                            | Name of SQL table.                                           |
| **name** : stringName of SQL table.**con** : sqlalchemy.engine.Engine or sqlite3.Connection | Using SQLAlchemy makes it possible to use any DB supported by that library. Legacy support is provided for sqlite3.Connection objects. |
| **schema** : string, optional                                | Specify the schema (if database flavor supports this). If None, use default schema. |
| **if_exists** : {‘fail’, ‘replace’, ‘append’}, default ‘fail’ | How to behave if the table already exists.fail: Raise a ValueError. replace: Drop the table before inserting new values. append: Insert new values to the existing table. |
| **index** : bool, default True                               | Write DataFrame index as a column. Uses index_label as the column name in the table. |
| **index_label** : string or sequence, default None           | Column label for index column(s). If None is given (default) and index is True, then the index names are used. A sequence should be given if the DataFrame uses MultiIndex. |
| **chunksize** : int, optional                                | Rows will be written in batches of this size at a time. By default, all rows will be written at once. |
| **dtype** : dict, optional                                   | Specifying the datatype for columns. The keys should be the column names and the values should be the SQLAlchemy types or strings for the sqlite3 legacy mode. |
| **method** : {None, ‘multi’, callable}, default None         | Controls the SQL insertion clause used:  None : Uses standard SQL `INSERT` clause (one per row). ‘multi’: Pass multiple values in a single `INSERT` clause. callable with signature `(pd_table, conn, keys, data_iter)`. |

### excel to oracle
```python
from sqlalchemy import create_engine
from sqlalchemy.dialects.oracle import VARCHAR2
import pandas as pd
import time

start = time.time()
df = pd.read_excel('./test.xls') # use openpyxl read excel to DataFrame

dtype = {c: VARCHAR2(df[c].str.len().max())
         for c in df.columns[df.dtypes == 'object'].tolist()} # convert object to oracle VARCHAR2

dev = 'name:password@instance'
conn_string = f'oracle+cx_oracle://{dev}'
engine = create_engine(conn_string, echo=False)
df.to_sql(name='babb_temp', con=engine, index=False, if_exists='append',
          dtype=dtype, chunksize=10**4)
# res = engine.execute("SELECT * FROM babb_temp").fetchall()

print(time.time() - start)
```

