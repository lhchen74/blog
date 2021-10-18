---
title: Go Question
tags: go
date: 2020-03-17
---

### go package

1>  package 可以和目录名不一致

2>  main func 必须在 main package 里

3>  gopath 可以有多个, 例如 D:\study\go;C:\Users\11435\Desktop\practice\go , go 会按照 gopath 查找 引用包

C:\Users\11435\Desktop\practice\go\src\queue\queue.go

```go
package queue

// Queue type rename
type Queue []interface{}

// Push method for Queue
func (queue *Queue) Push(value interface{}) {
	*queue = append(*queue, value)
}

// Pop method for Queue
func (queue *Queue) Pop() interface{} {
	head := (*queue)[0]
	*queue = (*queue)[1:]
	return head
}

// IsEmpty method for Queue
func (queue *Queue) IsEmpty() bool {
	return len(*queue) == 0
}

```

C:\Users\11435\Desktop\practice\go\src\queue\entry\main.go

```go
package main  // 1> package 可以和目录名不一致

import (
	"fmt"
	"queue"   // 3> go 会按照 gopath 查找 引用包
)

func main() { // 2> main func 必须在 main package 里
	q := queue.Queue{1}
	q.Push(2)
	q.Push(3)
	fmt.Println(q.Pop())
	fmt.Println(q.Pop())
	fmt.Println(q.IsEmpty())
	fmt.Println(q.Pop())
	fmt.Println(q.IsEmpty())

	q.Push("a")
	q.Push("b")
	fmt.Println(q.Pop())
}
```

