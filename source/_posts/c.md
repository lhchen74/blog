---
title: C
tags: c
date: 2019-10-30
---

### scanf & printf

**printf 打印格式**

```C
#include <stdio.h>

int main(int argc, char const *argv[])
{
    printf("%9d\n", 666);     // 9 个字符宽，右对齐
    printf("%*d\n", 9, 666);  // * 表示使用 9 占位，9 可以使用变量
    printf("%09d\n", 666);    // 补 0
    printf("%-9d\n", 666);    // - 左对齐
    printf("%9.2f\n", 666.0); // .2 两位小数
    return 0;
}

//       666
//       666
// 000000666
// 666
//    666.00

```

**scanf 可以从文件读取内容, printf 内容可以输出到文件，在控制台不会提示用户输入，也不会显示用户输出**

```c
// test.c
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int num;
    scanf("%d", &num);  // scanf 第二个参数需要传入地址
    printf("%d\n", num);
}
// file.in
// 666
```

gcc test.c -o test.exe

读取 file.in 中的 666，输出到 file.out

test.exe < file.in > file.out

**scanf 和 printf 中的类型转换**

对于 printf, 任何小于 int 的类型会被转换为 int，float 会被转换为 double；

但是 scanf 不会，要输入 short, 需要使用 %hd。

### 类型转换

强制转换 `(变量类型)变量名`

```c
#include <stdio.h>

int main()
{
    // short -2^15 - 2^15 => -32768 - 32767
    // 32768 超过 short 范围发生越界
    int i = 32768;
    short s = (short)i;
    printf("%d\n", s);  // -32768
    return 0;
}
```

### 函数

c 语言传递参数和函数参数类型可以不匹配， 这是 c 语言传统上最大的漏洞, 因为参数可能来自于变量，很难保证变量的类型和参数的类型一致。

```c
#include <stdio.h>

void cheer(int i);   // 函数声明

int main(int argc, char const *argv[])
{
    cheer(2.4);  // 2
    // double f = 2.4;
    // cheer(f);
    return 0;
}

void cheer(int i)  // 函数定义
{
    printf("cheer %d\n", i);
}
```

### 控制字符

控制字符不同的 shell 下会有不同的解释

```c
#include <stdio.h>

int main(int argc, char const *argv[])
{
    printf("123\b\n456");
    // git
    // 123
    // 456

    // cmd
    // 123
    // 456


    printf("123\bA\n456");
    // git
    // 123A
    // 456

    // cmd
    // 12A
    // 456


    printf("123\t456\n12\t456");
    // 123	456
    // 12	456
    printf("123\t456\n1234\t456");
    // 123 456
    // 1234    456

    return 0;
}
```

### char

char 是一种整数，也是一种特殊的类型：字符, 用单引号表示的字符字面量 'a', '1', ' ' 都是字符, printf 和 scanf 里用 %c 来输入输出字符

```c
#include <stdio.h>

int main(int argc, char const *argv[])
{
    char c;
    char d;
    c = 1;
    d = '1';
    if (c == d) {
        printf("equal\n");
    } else {
        printf("not equal\n");
    }
    printf("c=%d\n", c);
    printf("d=%d\n", d);
    printf("d='%c'\n", d);
    // not equal
    // c=1
    // d=49
    // d='1'


    // alpha + 'a' - 'A' 大写转小写
    // alpha + 'A' - 'a' 小写转大写
    char c;
    printf("pelase input upper alpha: ");
    scanf("%c", &c);
    char lc = c + 'a' - 'A';
    printf("the alpha '%c' lower is '%c'\n", c, lc);
    // pelase input upper alpha: A
    // the alpha 'A' lower is 'a'

    return 0;
}
```

### bool

```c
#include <stdio.h>
#include <stdbool.h>

int main(int argc, char const *argv[])
{
    // 没有 bool 类型，实际仍然是整数
    bool b = 6 > 5;
    bool t = true;
    t = 2;
    // 没有特别方式输出 bool
    printf("%d\n", b);  // 1
    return 0;
}
```

### 数组

```c
int main()
{
    //统计 [0-9] 数字出现的个数
    const int number = 10;                // 1.数组大小
    int count[number];                    // 2.定义数组并初始化
    for (int i = 0; i < number; i++)      // 3.初始化数组
    {
        count[i] = 0;
    }

    int x;
    printf("please input number: ");
    scanf("%d", &x);
    while(x != -1) {
        if (x >=0 && x <= 9) {
            count[x]++;                  // 4.数组参与运算
        }
        scanf("%d", &x);
    }

    for ( i = 0; i < number; i++)        // 5.遍历输出
    {
        printf("%d appear %d times\n", i, count[i]);
    }
    return 0;
}
```

### 求素数

素数：除了 1 以外只能被自己整除的数，2 是第一个素数

```c
#include <stdio.h>
#include <math.h>

// int isPrime(int x);

int isPrime(int x, int knownPrimes[], int numberOfKnownPrimes);

int main(int argc, char const *argv[])
{
    // 找前10个素数
    /*
    const int number = 10;
    int prime[number];

    for (int i = 0; i < number; i++)
    {
        prime[i] = 2;
    }

    int i = 3;      // 从 3 开始找，1 不是素数，2 是第一个素数
    int count = 1;  // prime[0] 已经初始化为 2，第一个素数，从 1 开始向右填充数组
    while (count < number)
    {
        if (isPrime(i, prime, count)) {
            prime[count++] = i;
            // prime[count] = i;
            // count = count + 1;
        }
        i++;
    }
    */


    // inprovement 4：质数的倍数不是质数
    const int maxNumber = 10;
    int isPrime[maxNumber];
    // 全部初始化为 1
    for (int i = 0; i < maxNumber; i++)
    {
        isPrime[i] = 1;
    }

    // 质数的倍数不是质数
    for (int x = 2; x < maxNumber; x++)
    {
        if (isPrime[x]) {
            for (int i = 2; i * x < maxNumber; i++)
            {
                // 不是质数赋值为 0
                isPrime[i * x] = 0;
            }
        }
    }

    for (int i = 2; i < maxNumber; i++)
    {
       if (isPrime[i]) {
           printf("%d\t", i);
       }
    }
    printf("\n");

}

// basic
// int isPrime(int x)
// {
//     int ret = 1;
//     if (x == 1) ret = 0;   // c 函数一般使用单一出口，不要在这里 return ret;
//     for (int i = 2; i < x; i++)
//     {
//         if (x % i == 0) {
//             ret = 0;
//             break;
//         }
//     }
//     return ret;
// }


// inprovement 1：除了 2 以外所有的偶数都不是素数
// int isPrime(int x)
// {
//     int ret = 1;
//     if (x == 1 || (x % 2 == 0 && x != 2))
//         ret = 0;
//     for (int i = 3; i < x; i+=2)
//     {
//         if (x % i == 0) {
//             ret = 0;
//             break;
//         }
//     }
//     return ret;
// }


// inprovement 2: 判断N是否是素数，只需要判断到根号N就可以了
//首先，约数是成对出现的。比如24,你找到个约数3,那么一定有个约数8,因为24/3=8。然后，这对约数必须一个在根号n之前，一个在根号n之后。因为都在根号n之前的话，乘积一定小于n（根号nX根号n=n），同样，都在根号n之后的话，乘积一定大于n。所以，如果你在根号n之前都找不到约数的话，那么根号n之后就不会有了。
// int isPrime(int x)
// {
//     int ret = 1;
//     if (x == 1 || (x % 2 == 0 && x != 2))
//         ret = 0;
//     for (int i = 3; i < sqrt(x); i+=2)
//     {
//         if (x % i == 0) {
//             ret = 0;
//             break;
//         }
//     }
//     return ret;
// }



// inprovement 3: 如果一个数不能被小于它的任意素整除，那么这个数也是素数
int isPrime(int x, int knownPrimes[], int numberOfKnownPrimes)
{
    int ret = 1;
    for (int i = 0; i < numberOfKnownPrimes; i++)
    {
        if (x % knownPrimes[i] == 0){
            ret = 0;
        }
    }
    return ret;
}
```

### 动态分配内存

**Stack （栈内存）**：主要是用来存储 **function calls （函数调用）** 和 **local variables** 的空间，其本质就是一个 **Stack（栈）。**最底层的便是 _main()_ 函数，每调用一个函数时就会执行 _push_ 操作，每当函数 _return_ 时便执行 _pop_ 操作。什么时候 _main()_ 也被 _pop_ 了，整个程序也就结束了。如果这个 stack 变得太高以至于超出了最大内存地址，就会出现所谓的 **stackoverflow**。

**Heap（堆内存）**：堆是程序共有的空间，主要是用来存储由 malloc() 等申请的内存位置，使用完成后需要手动释放。如果 malloc() 返回 null 的话就往往表示这一块空间已经用完了。

**Static (静态内存，全局区)**：这里的变量的生命周期与整个程序相同，即在进程创建是被申明，在程序退出时被销毁。**global variables（全局作用域变量）**， **file scope variables（文件作用域变量）**和被 **static 关键字修饰的变量**会存在这里。

所有的 **local variable** 按照 _stack_ 的形式被存储在 **stack memory** 中。这个 _stack_ 由一个 **stack pointer** 来管理，它所指向的内存地址按照 **function call** 的运行情况来增加或减少。比如 _函数 A_ 调用了 _函数 B_，_函数 B_ 就会被 _push_ 到 _函数 A_ 之上，原本的 **stack pointer** 也会从 _函数 A_ 移动到 _函数 B_。_pop 函数 B_ 时 **stack pointer** 的操作也是同理，那么理论上包含在 _函数 B_ 中的变量已经被释放，为什么大多数情况还是能在 _函数 A_ 中得到这个值呢？**因为 C 语言在设计之初就是以性能为优先，所以 _pop_ 时只会移动 stack pointer 而不会花费额外的资源去覆盖掉之前的内存。如果在使用那个 _pointer_ 之前并没有再调用其他的函数，那么这个 _pointer_ 所对应的地址就不会被覆盖掉。**

使用 pointer 之前并没有再调用其他的函数

```c
#include <stdio.h>
#include <stdlib.h>

int *getAnswer()
{
    int a = 42;
    int *p = &a;
    return p; // 在有些编译器中不允许直接返回局部变量的地址，即 return &a; 所以在这里返回 p
}

int main()
{
    int *answerToLife = getAnswer();
    printf("%d\n", *answerToLife); // 42，在这里没有调用其他函数，pointer 所指向的地址没有被覆盖。
    return 0;
}
```

使用 pointer 之前调用了其他的函数

```c
#include <stdio.h>
#include <stdlib.h>

int *getAnswer()
{
    int a = 42;
    int *p = &a;
    return p;
}

void overwriteMemoryWithGarbageData()
{
    int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
}

int main()
{
    int *answerToLife = getAnswer();
    overwriteMemoryWithGarbageData();  // 调用了其他函数覆盖
    printf("%d\n", *answerToLife);     // 8
    return 0;
}
```

使用 malloc 动态分配内存

```c
#include <stdio.h>
#include <stdlib.h>

int *getAnswer()
{
   int *ret = malloc(sizeof(int));
   *ret = 42;
   return ret;
}

void overwriteMemoryWithGarbageData()
{
   int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
}

int main()
{
   int *answerToLife = getAnswer();
   overwriteMemoryWithGarbageData();
   printf("%d\n", *answerToLife);  // 42
   free(answerToLife);
   return 0;
}
```

### sizeof

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int a[5];
    printf("sizeof(a):%d\n",sizeof(a));
    printf("sizeof(a[5]):%d\n",sizeof(a[5]));
    // 因为 sizeof 是关键字，而不是函数（函数求值是在运行的时候，而关键字 sizeof 求值是在编译的时候），
    // 因此，虽然并不存在 a[5] 这个元素，但是这里也并没有真正访问 a[5]，而是仅仅根据数组元素的类型来确定其值。
    // 所以这里使用 a[5] 并不会出错，sizeof(a[5]) 的结果为 4。

    // sizeof(a):20
    // sizeof(a[5]):4
    return 0;
}

```

### Question

无法修改字符串指针变量的值

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getMemory(char *p)             // 2. p = str -> NULL
{
    p = (char *)malloc(100);        // 3. p -> new memory
}
void test(void)
{
    char *str = NULL;               // 1. str -> NUll
    getMemory(str);
    strcpy(str, "hello world");     // 4. str -> NULL  strcpy(NULL, "hello world") 错误
    printf("%s\n", str);
    free(str);
}

int main()
{
    test();
    return 0;
}
```

使用双重指针

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getMemory(char **p)                    // 2. p = &str -> 0061FF1C
{
    *p = (char *)malloc(100);               // 3. *p 即 str
}
void test(void)
{
    char *str = NULL;                       // 1. str -> NULL
    getMemory(&str);
    strcpy(str, "hello world");
    printf("%s\n", str);
    free(str);
}

int main()
{
    test();

    // 0061FF1C
	// hello world
    return 0;
}
```

### \x20

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int b[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    int i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            // "%-2d"，其中"-"表示左对齐，如果不写"-"则默认表示右对齐；
            // "2"表示这个元素输出时占两个空格的空间，所以连同后面的 \x20 则每个元素输出时都占三个空格的空间。
            // \x20 即十进制 32，ascii 中表示 space
            printf("%-2d\x20", b[i][j]);
        }
        printf("\n");
    }
    // 1  2  3  4
    // 5  6  7  8
    // 9  10 11 12
    return 0;
}

```

![](c\ascii.png)
