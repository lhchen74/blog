---
title: C# Action 和 Func 的使用
tags: csharp
date: 2019-11-2
---

> 转载：[C# action 和 func 的使用-程序员徐坤-博客园](https://www.cnblogs.com/xuxiaoshuan/p/6844511.html)

以前我都是通过定义一个 delegate 来写委托的，但是最近看一些外国人写的源码都是用 action 和 func 方式来写，当时感觉对这很陌生所以看起源码也觉得陌生，所以我就花费时间来学习下这两种方式，然后发现确实代码简洁了不少。这两种方式我们也可以去实践的过程去慢慢运用。

### delegate

先说一下委托：

模拟一下场景：小明最近学习情绪高涨，以前买的书已经满足不了欲望，打算去买本（一个程序员的自我修养）。可是呢以前总是跑书厂买，nm，太远了扛不住，就去跑去附近书店去买，小明去给钱就弄了一本书回来，这个过程就是委托。开始分析

1：小明要买一本程序员自的我修养的书籍（xx 书就不买）硬性要求（定义委托性质）

```c#
private delegate void BuyBook();
```

2：附近书店（委托的方法）

```c#
public static void Book()
{
    Console.WriteLine("我是提供书籍的");
}
```

3：小明和书店建立关系（给委托绑定方法）

```c#
BuyBook buybook = new BuyBook(Book);
```

4：小明给钱拿书（触发）

```c#
buybook();
```

上面的内容是为了能理解委托的用法下面呢我开始讲解 Action 和 Func

### Action

1：小明很是苦恼，我就是买一本书籍，每次都让我定义下，烦死了，有没有一种方法不去定义委托呢，那么有吗，还真有，就是我们今天讲的 Action

```c#
Action BookAction = new Action(Book);
```

这样是不是就简单了很多

2：小明现在又不满意了，我把一个程序员的自我修养看完了，现在呢想买本其他书，那怎么办，我是不是要重新再次定义委托。其实不需要你只需要把参数传过来就可以了。下面我们看`Action<T>`的用法

```c#

public static void Book(string BookName)
{
    Console.WriteLine("我是买书的是:{0}",BookName);
}

static void Main(string[] args)
{
    Action<string> BookAction = new Action<string>(Book);
    BookAction("百年孤独");
}
```

3：现在小明又改变主意了，我不仅要自己选择书籍，我还要在一个牛逼的书籍厂家买，有没有这种方式呢，那么告诉你有 `Action<in T1,in T2>`

```c#
public static void Book(string BookName, string ChangJia)
{
    Console.WriteLine("我是买书的是:{0}来自{1}",BookName,ChangJia);
}

static void Main(string[] args)
{
    Action<string,string> BookAction = new Action<string,string>(Book);
    BookAction("百年孤独", "北京大书店");
}
```

### Func

小明又发生疑问了，每次我自己都去书店去拿书，有没有一种方法直接送到我家里呢，那么 Func 专门提供了这样的服务

Func 解释, 封装一个不定具有参数（也许没有）, 但却返回 TResult 参数指定的类型值的方法。

1：我们先看一个没有参数只有返回值的方法

```c#
static void Main(string[] args)
{
    Func<string> RetBook = new Func<string>(FuncBook);
    Console.WriteLine(RetBook);
}

public static string FuncBook()
{
    return "送书来了";
}
```

2：有参数有返回值的方法

```c#
static void Main(string[] args)
{
    Func<string,string> RetBook = new Func<string,string>(FuncBook);
    Console.WriteLine(RetBook("Think in c#"));
}

public static string FuncBook(string BookName)
{
    return BookName;
}
```

3：Func 一个很重要的用处就是传递值，下面我举一个简单的代码来说明

```c#
private static Func<string> funcValue = delegate
{
    return "我是即将传递的值";
};

// DisplayVaue是处理传来的值，比如缓存的处理，或者统一添加数据库等
private static void DisplayValue(Func<string> func)
{
    string RetFunc = func();
    Console.WriteLine("我在测试一下传过来值：{0}", RetFunc);
}
static void Main(string[] args)
{
    DisplayValue(funcValue);
}
```

### summary

1：Action 用于没有返回值的方法（参数可以根据自己情况进行传递）

2：Func 恰恰相反用于有返回值的方法（同样参数根据自己情况）

3：记住无返回就用 Action，有返回就用 Func
