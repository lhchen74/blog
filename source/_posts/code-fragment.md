---
title: Code Fragment
tags: other
date: 2020-05-28
---


## 百钱百鸡

中国古代数学家张丘建在他的《算经》中提出了一个著名的“百钱百鸡问题”:
一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱，现在要用百钱买百鸡，请问公鸡、母鸡、小鸡各多少只？

```go
package main

import "fmt"

fun one() {
    count := 0
	for cock := 0; cock <= 20; cock++ {
		for hen := 0; hen <= 33; hen++ {
			for chick := 0; chick <= 100; chick++ {
				count++
				if chick%3 == 0 && cock+hen+chick == 100 && cock*5+hen*3+chick/3 == 100 {
					fmt.Printf("公鸡：%d, 母鸡：%d, 小鸡：%d\n", cock, hen, chick)
				}
			}
		}
	}
	//72114
	fmt.Println(count)
}

func two() {
    count := 0
	for cock := 0; cock <= 20; cock++ {
		for hen := 0; hen <= 33; hen++ {
			for chick := 0; chick <= 100; chick += 3 {
				count++
				if cock+hen+chick == 100 && cock*5+hen*3+chick/3 == 100 {
					fmt.Printf("公鸡：%d, 母鸡：%d, 小鸡：%d\n", cock, hen, chick)
				}
			}
		}
	}
	//24276
	fmt.Println(count)
}

func three() {
    count := 0
	for cock := 0; cock <= 20; cock++ {
		for hen := 0; hen <= 33; hen++ {
			count++
			chick := 100 - cock - hen
			if chick%3 == 0 && 5*cock+3*hen+chick/3 == 100 {
				fmt.Printf("公鸡：%d, 母鸡：%d, 小鸡：%d\n", cock, hen, chick)
			}
		}
	}
	//714
	fmt.Println(count)
}

func main() {
	one()
    two()
    three()
}
```

## BinarySearch

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	size := 1_000_000
	list := make([]int, size)

	for i := 0; i < size; i++ {
		list = append(list, i+1)  // The first 1_000_000 elements in the list is 0
		// list[i] = i + 1
	}

	rand.Seed(time.Now().UnixNano())

	for i := 0; i < 20; i++ {
		v := rand.Intn(size-1) + 1
		fmt.Printf("Find %d begin\n", v)
		idx := binarySearch(list, v)
		fmt.Printf("Find %d index is [%d]\n", v, idx)
		fmt.Println("=============================")
	}
}

func binarySearch(list []int, target int) int {
	low := 0
	high := len(list) - 1
	step := 0

	for {
		step += 1
		if low <= high {
			mid := (low + high) / 2
			guess := list[mid]

			if guess == target {
				fmt.Printf("Find %d times\n", step)
				return mid
			}

			if guess > target {
				high = mid - 1
			}

			if guess < target {
				low = mid + 1
			}
		}
	}
}
```


## 统计字符串中每个字符出现的次数

```c
#include<stdio.h>
int main()
{
	char str[] = "hellowrold";

	unsigned char all[256] = { 0 };
	char* tmep = str;
	while (*tmep)
	{
		all[*tmep]++;
		tmep++;
	}
	for (int i = 0; i < 256; i++)
	{
		if (all[i] != 0)
			printf("字符%c出现的次数：%d\n", i, all[i]);
	}
}
```