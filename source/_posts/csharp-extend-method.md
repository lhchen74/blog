---
title: C# Extend Method
tags: csharp
date: 2019-10-30
---

> 转载:[C#扩展方法的理解 - suger - 博客园](https://www.cnblogs.com/suger/archive/2012/05/13/2498248.html)

扩展方法使您能够向现有类型"添加"方法，而无需创建新的派生类型、重新编译或以其他方式修改原始类型。也就是你可以对 String,Int,DataRow,DataTable 等这些类型的基础上增加一个或多个方法，使用时不需要去修改或编译类型本身的代码。

先做个例子吧，以 String 为例，需要在字符串类型中加一个从字符串转为数值的功能。

以往我们可能是这样做的，会专门写一个方法做过转换

```c#
public static int StrToInt(string s)
{
    int id;
    int.TryParse(s, out id); //这里当转换失败时返回的id为0
    return id;
}
```

调用就使用

```c#
string s = "abc";
int i = StrToInt(s);
```

**若是 String 类型有一个名为 ToInt()（从字符串转为数值）的方法**，就可以这样调用了

```c#
string s = "abc";
int i = s.ToInt();
```

这样看起来是不是更好，下面来看看具体怎么实现吧

**第一步**

先创建一个解决方案，一个应用程序(test)及一个类库(Common)

**第二步**

在类库中新建一个名为 EString.cs 类

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Common
{
    public static class EString
    {
        /// <summary>
        /// 将字符串转换为Int
        /// </summary>
        /// <param name="t"></param>
        /// <returns>当转换失败时返回 0</returns>
        public static int ToInt(this string t)
        {
            int id;
            int.TryParse(t, out id);//这里当转换失败时返回的id为0
            return id;
        }
    }
}
```

看了上面的代码了吧，扩展方法规定类必须是一个静态类，EString 是一个静态类，里面包含的所有方法都必须是静态方法。

msdn 是这样规定扩展方法的："扩展方法被定义为静态方法，但它们是通过实例方法语法进行调用的。它们的第一个参数指定该方法作用于哪个类型，并且该参数以`this` 修饰符为前缀。"

**EString 里有一个 ToInt 的静态方法，他接收一个自身参数 this，类型为 string，this string 必须在方法参数的第一个位置。**

这句话什么意思，即你需要对 string 扩展一个 ToInt 方法，**this 是 string 实例化后的对象**，这可能说的不太清楚，我的表述能力能弱，不要见怪呀。。。通俗的说就是，扩展方法跟静态类的名称无关，只需要在一个静态类里面定义一个静态方法，第一个参数必须 this string 开头。

如果需要你要对 DateTime 类型扩展方法名为 IsRange（判断是否在此时间范围内），代码如下：

```c#
/// <summary>
/// 此时间是否在此范围内 -1:小于开始时间 0:在开始与结束时间范围内 1:已超出结束时间
/// </summary>
/// <param name="t"></param>
/// <param name="startTime"></param>
/// <param name="endTime"></param>
/// <returns></returns>
public static int IsRange(this DateTime t, DateTime startTime, DateTime endTime)
{
    if ((startTime - t).TotalSeconds > 0)
    {
        return -1;
    }

    if ((endTime - t).TotalSeconds < 0)
    {
        return 1;
    }

    return 0;
}
```

这里的扩展方法是用 this DateTime 打头，那么就可以这样调用

```c#
time.IsRange(t1,t2); //判断时间time是否在t1到t2的范围内
```

webtest 在使用扩展方法前需要先引用命名空间

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using Common; //这里引用扩展方法所在的命名空间

namespace test
{
    public class Test :
    {
        /// <summary>
        /// 没有用扩展方法
        /// </summary>
        private void use1()
        {
            string s = "abc";
            int i = StrToInt(s);
            Response.Write("没有用扩展方法:" + i);
        }

        /// <summary>
        /// 使用扩展方法
        /// </summary>
        private void use2()
        {
            string s = "2012";
            int i = s.ToInt();
            Response.Write("使用扩展方法:" + i);
        }

        public static int StrToInt(string s)
        {
            int id;
            int.TryParse(s, out id);//这里当转换失败时返回的id为0
            return id;
        }
    }
}
```
