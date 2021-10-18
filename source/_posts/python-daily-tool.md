---
title: Daily Tool
date: 2021-07-20
categories: manual
tags: python
---

### Read Excel to Oracle

```python
from pathlib import Path
from sqlalchemy.dialects.oracle import VARCHAR2
from sqlalchemy import create_engine
import pandas as pd

dev = 'apps:apps@DEV'
conn_string = f'oracle+cx_oracle://{dev}'


def read_excels_to_db(paths):
    for path in paths:
        tablename = path.stem
        df = pd.read_excel(path, keep_default_na=False, engine='xlrd')
        # dtype = {c: VARCHAR2(df[c].str.len().max())
        #          for c in df.columns[df.dtypes == 'object'].tolist()}
        dtype = {c: VARCHAR2(1000)
                 for c in df.columns[df.dtypes == 'object'].tolist()}

        engine = create_engine(conn_string, echo=False)
        df.to_sql(tablename, con=engine, index=False, if_exists='append',
                  dtype=dtype, chunksize=10**4)


if __name__ == '__main__':
    paths = Path('./').glob('*.xlsx')
    read_excels_to_db(paths)

```

