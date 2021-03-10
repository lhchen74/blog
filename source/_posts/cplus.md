---
title: c++ basic
tags: c
date: 2019-10-30
---

### 引用 c 库

c++ 引用 c 库，使用 cxx，不用加 .h

```c++
#include <cmath>
#include <cstdio>

int main(int argc, char const *argv[])
{
    double a = 1.2;
    a = sin(a);
    printf("%f\n", a);
}
```

### 命名空间

```c++
#include <cstdio>

namespace first
{
int a;
void f();
} // namespace first

namespace second
{
double a;
double f();
} // namespace second

int main()
{
    first::a = 66;
    second::a = 66.0;
    printf("%d\n", first::a);
    printf("%.2f\n", second::a);

    return 0;
}
```

### 全局作用域限定

`::` 全局作用域限定符，用于访问全局作用域中的变量

```c++
#include <iostream>
using namespace std;

double b = 11;
int main()
{
    double b = 66;
    cout << "local b: " << b << endl;
    cout << "global b: " << ::b << endl;

    return 0;
}
```

### 引用变量

引用就是变量的别名，不会占用额外的内存

```c++
#include <iostream>

using namespace std;

// 在 c++ 中交换变量的值可以不使用指针传递，可以使用变量引用传递
void swap(int &x, int &y)
{
    int t = x;
    x = y;
    y = t;
}

void change(int &x, const int &y)
{
    // y 是引用变量，不会占用额外的内存
    // const 表明该变量不能修改，所以函数内部 y 的操作不会影响到外部变量
}

int main(int argc, char const *argv[])
{
    int x = 10;
    int &y = x;    // y 就是 x 的别名
    y = 12;        // y = 12 也就是 x 内存块的值为 12
    cout << "x: " << x << endl; // x: 12

    int a = 11;
    int b = 22;
    swap(a, b);
    cout << a << ":" << b << endl;  // 22:11
    return 0;
}
```

### 异常捕获

```c++
int a = 90;
try
{
    if (a > 100)
    {
        throw 100;
    }
    throw "hello";
}
catch (int result)
{
    cout << result << endl;
}
catch (char const *s)
{
    cout << s << endl;
}
catch (...)
{
    cout << "other error" << endl;
}

// hello
```

### 操作符重载

```c++
#include <iostream>

using namespace std;

struct Vector2
{
    int x;
    int y;
};

Vector2 operator+(Vector2 v1, Vector2 v2)
{
    return Vector2{v1.x + v2.x, v1.y + v2.y};
}

// &operator ???
ostream &operator<<(ostream &o, Vector2 v)
{
    o << "(" << v.x << "," << v.y << ")" << endl;
    return o;
}

int main(int argc, char const *argv[])
{
    Vector2 v1 = {1, 2};
    Vector2 v2 = {3, 4};
    Vector2 v = v1 + v2;
    cout << v.x << ":" << v.y << endl;
    cout << v << endl;
}

// 4:6
// (4,6)
```

### 函数重载

### 函数参数默认值

### 模板 template

```c++
#include <iostream>
#include <cstring>

using namespace std;

template <class T>
class Array {
    int size;
    T *data;
public:
    Array(int s) {
        size = s;
        data = new T[s];
    }

    ~Array() {
        delete []data;
    }

    T &operator [] (int i) {
        if (i < 0 || i >= size) {
            // cerr << endl << "Index out of range" << endl;
            // exit(EXIT_FAILURE);
            throw "Index out of range";
        }
        else
        {
            return data[i];
        }
    }
};

int main(int argc, char const *argv[])
{
    Array<int> arr(5);
    arr[0] = 1;
    arr[1] = 2;
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    try
    {
       arr[5] = 5;
    }
    catch(char const* res)
    {
        cerr << res << '\n';
    }

    // 1 2 1767332922 2003788910 1029636211
    // Index out of range

    return 0;
}
```

### 动态分配内存 new

new 动态分配内存, delete 使用完成后释放内存

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    double d = 3.14;
    double *dp;
    dp = &d;
    *dp = 4.14;
    cout << "*dp=" << *dp << " d=" << d << endl;
    // *dp=4.14 d=4.14

    dp = new double;
    *dp = 5.14;
    cout << "*dp=" << *dp << " d=" << d << endl;
    delete dp;
    // *dp=5.14 d=4.14

    dp = new double[5];
    dp[0] = 6.14;
    dp[1] = 6.15;
    cout << "d[0]=" << dp[0] << " dp[1]=" << dp[1] << endl;
    delete [] dp;
    // d[0]=6.14 dp[1]=6.1

    int n = 5;
    dp = new double[n];
    for (int i = 0; i < n; i++)
    {
        dp[i] = i;
    }

    double *p = dp;
    for (int i = 0; i < n; i++)
    {
        cout << *(p+i) << " ";
    }
    cout << endl;
    // 0 1 2 3 4

    for (double *p = dp, *q = dp + n; p < q; p++)
    {
        cout << *p << " ";
    }
    cout << endl;
    delete [] dp;
    // 0 1 2 3 4


    char *s;
    s = new char[100];
    strcpy(s, "hello");
    cout << s << endl;
    delete [] s;
    // hello
}
```

### 字符串 string

```c++
#include <iostream>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    string s = "hello";
    for(string::const_iterator ci = s.begin(); ci != s.end(); ci++)
        cout << *ci << " ";
    cout << endl;
    s = s + " world";
    for (int i = 0; i < s.size(); i++)
    {
        cout << s[i] << " ";
    }
    cout << endl;

    // h e l l o
	// h e l l o   w o r l d

    return 0;
}
```

### struct

c++ struct 中可以有方法，所有的成员默认都是公开的，class 中所有的成员默认都是私有的。

```c++
#include <iostream>
#include <cstring>
using namespace std;

struct Date
{
    int d, m, y;
    Date() {
        d = 10;
        m = 10;
        y = 2019;
        cout << "default constructor" << endl;
    }
    Date(int dd, int mm, int yy)
    {
        d = dd;
        m = mm;
        y = yy;
        cout << "constructor" << endl;
    }
    void print()
    {
        cout << y << "-" << m << "-" << d << endl;
    }
    // Date &add(int dd)
    // {
    //     d += dd;
    //     return *this;
    // }
    Date &operator+=(int dd)
    {
        d += dd;
        return *this; // this 是指向调用这个函数的类型对象的指针， *this 就是指向调用这个函数的对象
    }
};

int main(int argc, char const *argv[])
{
    Date day(10, 10, 2019);
    Date day2;
    // day.add(5);
    day += 5;
    day.print();
    day2.print();

    // constructor
    // default constructor
    // 2019-10-15
    // 2019-10-10
    return 0;
}
```

### class

```c++
#include <iostream>
#include <cstring>

using namespace std;

class Employee
{
    string name;

public:
    Employee(string n);
    virtual void print();
};

class Manager : public Employee
{
    int level;

public:
    Manager(string n, int l = 2);
    void print();
};

Employee::Employee(string n) : name(n)
{
   // name(n) 相当于 name = n
}

void Employee::print()
{
    cout << name << endl;
}

// 覆盖父类的虚函数
void Manager::print()
{
    cout << level << " ";
    Employee::print();
}

Manager::Manager(string n, int l) : Employee(n), level(l)
{
    // 在这里需要调用父类构造函数, 初始化 name, 不能直接使用 name(n)
}

// 抽象类，包含纯虚函数的类，不能直接 new 使用
// 需要子类继承，重写纯虚函数
class Animal
{
private:
    string name;
public:
    Animal(string n): name(n)
    {
    };
    string getName() { return name; };
    virtual string speak() = 0;   // 纯虚函数
};

int main(int argc, char const *argv[])
{
    Employee *ep[100];
    int num = 0;
    string name;
    int level;
    char cmd;
    cout << "please input cmd: ";
    while (cin >> cmd)
    {
        if (cmd == 'M' || cmd == 'm')
        {
            cout << "please input name and level: ";
            cin >> name >> level;
            ep[num] = new Manager(name, level); num++;
        }
        else if(cmd == 'E' || cmd == 'e')
        {
            cout << "please input name: ";
            cin >> name;
            ep[num] = new Employee(name); num++;
        }
        else {
            break;
        }
        cout << "please input cmd: ";
    }

    for (int i = 0; i < num; i++)
    {
        ep[i]->print();
    }

    // please input cmd: e
    // please input name: babb
    // please input cmd: m
    // please input name and level: owen 1
    // please input cmd: q
    // babb
    // 1 owen
    return 0;
}
```
