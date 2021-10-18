---
title: Programming Language Interaction
tags: other
date: 2020-01-20
---

## python call go

1. go 文件添加导入 `import "C"`
2. go 文件在需要导出的函数上添加注释 `//export run`
3. 执行构建 `go build -buildmode=c-shared -o test.so test.go`
4. python文件 使用 CDLL 导入 so `CDLL('./utils/test.so').run`

utils/test.go

```go
package main

import "C"

//export run
func run(n int) {
	for n > 0 {
		n = n - 1
	}
}

func main() {

}
```

test.py

```python
import time
from ctypes import CDLL

run = CDLL('./utils/test.so').run

target = 1000000000

start = time.time()
run(target)
end = time.time()
print(end - start)
```



 