---
title: Python Call C
tags: python
date: 2019-04-30
---

> 将`.c`后缀的文件编译为动态库文件(`.so`结尾)

```c
gcc c_dll.c -shared -o c_dll.so
```

> 在 python 文件中导入头文件

```python
from ctypes import *
```

> 在 python 中引入 c 动态库,并用变量接收动态库的引用

```python
result = cdll.LodaLibrary("./c_dll.so")
```

> 调用动态库方法

```python
result.my_add(num)
```

> source code

c_dll.c

```python
#include<stdio.h>

void my_add(int num){

    long int result = 0;

    for (long int i=1; i<=num; i++){
        result += i;
    }
    printf("从1到%d累加的计算结果为%d\n",num,result);
}
```

c_add.py

```python
import time
from ctypes import *
def main():
    num = int(input("请输入整数值:"))
    result = 0
    start_time = time.time()

    result = cdll.LoadLibrary("./c_dll.so")
    result.my_add(num)

    end_time = time.time()

    print("总共用时%s"%(end_time-start_time))

if __name__ == "__main__":
    main()
# 10000000    总共用时0.03500175476074219
```

python_add.py

```python
import time

def main():
    num = int(input("请输入整数值:"))
    result = 0
    start_time = time.time()

    for i in range(num+1):
        result += i
    end_time = time.time()

    print("从1到%d累加的计算结果为%d"%(num,result))
    print("总共用时%s"%(end_time-start_time))

if __name__ == "__main__":
    main()
# 10000000    总共用时0.7695105075836182
```

> 作者：木子昭
> 链接：<https://www.jianshu.com/p/edb8698d1374>
> 來源：简书
> 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
