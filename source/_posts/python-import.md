---
title: python import
tags: python
date: 2019-07-16
description: python import and from import
---

### 目录结构

import_test
├── __init__.py
├── test.py
├── test1.py
└── test2.py

### test.py

```python
import sys
print(sys.path)
print(__package__)

"""
在 import_test 目录内

python3 test.py 是将 test.py 所在的目录添加到 sys.path
['/Users/jbn/Desktop/study/python/import_test',       	  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/libdynload',
'/Users/jbn/Library/Python/3.6/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
None

python3 -m test 是将执行命令的目录添加到 sys.path 此时 __package__ 是 ''
['', 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Users/jbn/Library/Python/3.6/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']

"""

"""
退到 import_test 目录外

python3 ./import_test/test.py 是将 test.py 所在的目录添加到 sys.path
['/Users/jbn/Desktop/study/python/import_test', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/libdynload',
'/Users/jbn/Library/Python/3.6/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
None

python3 -m import_test.test 是将执行命令的目录添加到 sys.path 此时 __package__ 是 import_test 
['', 
'/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Users/jbn/Library/Python/3.6/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
import_test  
"""
```

### test2.py

```python
print(__package__)

# import test1  # 1
from . import test1 # 2

"""
import_test 目录内

python3 test2.py
1 ok
2 ok

python3 -m test2
1 ok
2 error  # ImportError: attempted relative import with no known parent package
"""

"""
import_test 目录外

python3 ./import_test/test2.py
1 ok
2 ok


python3 -m import_test.test2
1 error ModuleNotFoundError: No module named 'test1'
2 ok
__package__ == 'import_test'
"""
```

