---
title: calulate cost time
tags: other
date: 2019-10-29
---

> 我们之所以觉得悬崖上的花朵美丽，那是因为我们会在悬崖停下脚步，而不是像那些毫不畏惧的花朵般，能向天空踏出一步。- 死神

### Python

```python
import time

n = 1
start = time.time()
while n < 100000000:
    n = n + 1
end = time.time()
print((end - start) * 1000)
```

### PHP

```php
<?php

$n = 1;
$start = time();
while ($n < 100000000) {
    $n = $n + 1;
}
$end = time()
echo ($end - $start) * 1000;
```

### Node.js

```js
let n = 1;
const start = Date.now();
while (n < 100000000) {
    n = n + 1;
}
const end = Date.now();
console.log(end - start);
```

### C\#

csc Test.cs => ./Test.exe

```c#
using System;

namespace Application
{
   class Test
   {
      static void Main(string[] args)
      {
         DateTime start = System.DateTime.Now;

         int n = 1;
         while (n < 100000000) {
            n = n + 1;
         }

         DateTime end = System.DateTime.Now;
         TimeSpan ts = end.Subtract(start);

         Console.WriteLine("{0}ms", ts.TotalMilliseconds);
      }
   }
}
```

### Java

javac Test.java => java Test

```java
import java.time.Instant;
import java.time.Duration;

class Test{
    public static void main(String[] args) {
        Instant start = Instant.now();
        // long n = 1;
        // 如果没有超出 int 范围，不要使用 long, 否则会很慢
        int n = 1;
        while (n < 100000000) {
            n = n + 1;
        }

        Instant end = Instant.now();
        System.out.println(Duration.between(start, end).toMillis());
    }
}
```

### C

gcc test.c -o testc.exe -> ./testc.exe

```c
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    time_t c_start, c_end;

    c_start = clock();
    int n = 1;
    while (n < 100000000)
    {
        n = n + 1;
    }
    c_end = clock();

    printf("%f", difftime(c_end, c_start));
}
```

### C++

g++ test.cpp -o testcpp.exe -> ./testcpp.exe

```c++
#include <time.h>
#include <iostream>

using namespace std;

int main()
{

    time_t c_start, c_end;

    c_start = clock();
    int n = 1;
    while (n < 100000000)
    {
        n = n + 1;
    }
    c_end = clock();

    cout << difftime(c_end, c_start) << endl;
}
```

### Go

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	for n := 1; n < 100000000; {
		n = n + 1
	}

	elapsed := time.Since(start)
	fmt.Println(elapsed)
}
```

### PL/SQL

PL/SQL Developer -> Execute

```sql
declare 
  l_start   date;
  l_count   number;
  l_elapsed number;
begin
   l_count := 1;
   l_start := sysdate;
  
   while l_count < 100000000
   loop
      l_count := l_count + 1;
   end loop;
   
   l_elapsed := (sysdate - l_start) * 24 * 60 * 60;
   
   dbms_output.put_line(l_elapsed || 's');
end;
```