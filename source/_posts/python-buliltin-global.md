---
title: Python内置全局变量
tags: python
date: 2019-10-29
---

> 转载: [第三十九节，python 内置全局变量 - 林贵秀 - 博客园](https://www.cnblogs.com/adc8868/p/5811566.html)

### vars()

以字典方式返回内置全局变量

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
print(vars())
#输出
# {'__builtins__': <module 'builtins' (built-in)>, '__spec__': None, '__package__': None, '__doc__': None, '__name__': '__main__', '__cached__': None, '__file__': 'H:/py/index.py', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000AC32C66A58>}
```

### \_\_doc\_\_

获取文件的注释

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
这里是文件的注释
"""
print(__doc__)  #__doc__    ：获取文件的注释
#输出
# 这里是文件的注释
```

### \_\_file\_\_

获取当前文件的路径

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
print(__file__)  #__file__ ：获取当前文件的路径
#输出
# H:/py/index.py
```

会经常用到 `__file__`，一般配合 os 模块的 os.path.dirname()，os.path.basename() ，os.path.join() 模块函数来使用

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
a = __file__    # __file__全局变量获取当前文件路径
print(a)

b = os.path.dirname(a) #获取文件当前目录：注意：os.path.dirname()叠加一次向上找一次 如下
print(b)

b2 = os.path.dirname(b) #获取文件当前目录的上级目录，注意：os.path.dirname()叠加一次向上找一次
print(b2)

c = os.path.basename(a) #获取文件名称
print(c)
#输出
# H:/py/lib/ska/mk.py
# H:/py/lib/ska
# H:/py/lib
# mk.py
```

用 `__file__` 获取模块路径，添加到解释器模块路径里

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import os
a = __file__    # __file__全局变量获取当前文件路径
print(a)
b = os.path.dirname(a) #获取文件当前目录
print(b)
c = "lib" #自定义文件目录名称
d = os.path.join(b,c) #将获取文件当前目录，与自定义文件目录名称，拼接成完整的路径
print(d)
print("\n")

sys.path.append(d) #将拼接好的路径，添加到解释器模块路径中

for i in sys.path:  #
    print(i)
#输出
# H:/py/index.py
# H:/py
# H:/py\lib
#
#
# H:\py
# C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\pip-8.1.2-py3.5.egg
# H:\py
# C:\Users\admin\AppData\Local\Programs\Python\Python35\python35.zip
# C:\Users\admin\AppData\Local\Programs\Python\Python35\DLLs
# C:\Users\admin\AppData\Local\Programs\Python\Python35\lib
# C:\Users\admin\AppData\Local\Programs\Python\Python35
# C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages
# H:/py\lib
```

### \_\_package\_\_

获取导入文件的路径，多层目录以点分割，注意：对当前文件返回 None

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
print(__package__)  #注意：对当前文件返回None
from lib.ska import mk  #导入mk模块文件
print(mk.__package__) #__package__ ：获取导入文件的路径，多层目录以点分割，注意：对当前文件返回None
# 输出
# None
# lib.ska
# lib.ska
```

### \_\_cached\_\_

获取导入文件的缓存路径

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
from lib.ska import mk  #导入mk模块文件
print(mk.__cached__) #__cached__ ：获取导入文件的缓存路径
#输出
# H:\py\lib\ska\__pycache__\mk.cpython-35.pyc
```

### \_\_name\_\_

获取导入文件的路径加文件名称，路径以点分割，注意:获取当前文件返回`__main__`

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
print(__name__) #注意:获取当前文件返回__main__
from lib.ska import mk  #导入mk模块文件
print(mk.__name__)  #获取导入文件的路径加文件名称，路径以点分割
#输出
# __main__
# lib.ska.mk
```

`__name__` 全局变量写在入口文件里，只有执行入口文件时的返回值才是 `__main__` ，如果入口文件被导入到别的文件里，此时入口文件的 `__main__` 返回值就不在是 `__main__` ，而是如果文件的路径加入口文件名称，所以我们可以用`__name__` 全局变量来防止别人盗链入口文件

```python
#!/usr/bin/env python
# -*- coding:utf8 -*-
if __name__ == "__main__": #__name__  全局变量写在入口文件里，只有执行入口文件时的返回值才是__main__  ，如果入口文件被导入到别的文件里，此时入口文件的__name__返回值就不在是__main__，而是如果文件的路径加入口文件名称，所以我们可以用__name__全局变量来防止别人盗链入口文件
    print("执行")
#这样只有执行index文件时才执行判断里的，index被导入到到别的文件，就不会执行判断里的
```

### \_\_builtins\_\_

内置函数在这里面
