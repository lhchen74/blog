---
title: 字典、哈希与Map
tags: java
date: 2021-03-13
---

> 转载：[【必须学好】字典、哈希与 Map_niu0147 的专栏-CSDN 博客](https://blog.csdn.net/niu0147/article/details/51682132)

在实际问题中，按照给定的值进行数据查询是经常遇到的，比如，在电话号码簿中查询某个人的电话号码；在图书馆中按照 ISBN 编号查找某本书的位置；在地图中按照坐标查找某个地点的地名等等。为此，人们创造了一种能够根据记录的关键码(也就是用以标识数据在记录中的存放位置的数据项)方便的检索到对应的记录信息的数据结构，这就是字典(Dictionary)。

### 字典的定义

我们都使用过字典，如英汉字典、成语字典，图书的检索目录、电话簿等也可以看作广义上的字典。在计算机科学中，把字典也当成一种数据结构。

我们把字典定义为“键-值对”(Key-Value Pair)的集合。根据不同的问题，我们为名字和值赋予不同的含义，比如，在英汉字典中，英文单词是名字，此单词的中文解释条目是值；在电话簿中，人名是名字，此人名对应的电话号码是值。

字典最基本的操作包括：find(查找)、add(插入)、remove(删除)，分别用来从字典中检索数据、插入数据和删除数据。在实际存储中，我们将“键-值对”存储于记录中，通过键(也就是“键-值对”中的名字)来标识该“键-值对”。“键-值对”的存放位置和其键之间的对应关系用一个二元组表示：(键,值的位置)。

从字典中查找“键-值对”的最简单方法就是使用数组存储，然后在查找的时候遍历此数组，当遍历到和被查找的“键-值对”的名字相同项的时候，这个“键-值对”就被找到了。这种最朴实的方式肯定是不能满足实际要求的，因此人们发明了一种检索效率非常高的组织字典数据的方法，即哈希表结构。

### 哈希表与哈希方法

哈希方法在“键-值对”的存储位置与它的键之间建立一个确定的对应函数关系 hash()，使得每一个键与结构中的一个唯一的存储位置相对应：

存储位置=hash(键)

在搜索时，首先对键进行 hash 运算，把求得的值当做“键-值对”的存储位置，在结构中按照此位置取“键-值对”进行比较，若键相等，则表示搜索成功。在存储“键-值对”的时候，依照相同的 hash 函数计算存储位置，并按此位置存放，这种方法就叫做哈希方法，也叫做散列方法。在哈希方法中使用的转换函数 hash 被称作哈希函数(或者散列函数)。按照此中算法构造出来的表叫做哈希表(或者散列表)。

哈希函数建立了从“键-值对”到哈希表地址集合的一个映射，有了哈希函数，我们就可以根据键来确定“键-值对”在哈希表中的位置的地址。使用这种方法由于不必进行多次键的比较，所以其搜索速度非常快，很多系统都使用这种方法进行数据的组织和检索。

举一个例子，有一组“键值对”：<5,"tom">、<8,"Jane">、<12,"Bit">、<17,"Lily">、<20,"sunny">，我们按照如下哈希函数对键进行计算:hash(x)=x%17+3，得出如下结果：hash(5)=8、hash(8)=11、hash(12)=15、hash(17)=3、hash(20)=6。我们把<5,"tom">、<8,"Jane">、<12,"Bit">、<17,"Lily">、<20,"sunny">分别放到地址为 8、11、15、3、6 的位置上。当要检索 17 对应的值的时候，只要首先计算 17 的哈希值为 3，然后到地址为 3 的地方去取数据就可以找到 17 对应的数据是"Lily"了，可见检索速度是非常快的。

### 冲突与冲突的解决

通常键的取值范围比哈希表地址集合大很多，因此有可能经过同一哈希函数的计算，把不同的键映射到了同一个地址上面，这就叫冲突。比如，有一组“键-值对”，其键分别为 12361、7251、3309、30976，采用的哈希函数是：

```java
public static int hash(int key)
{
    return key % 73 + 13420;
}
```

则将会得到 hash(12361)=hash(7251)=hash(3309)=hash(30976)=13444，即不同的键通过哈希函数对应到了同一个地址，我们称这种哈希计算结果相同的不同键为同义词。

如果“键-值对”在加入哈希表的时候产生了冲突，就必须找另外一个地方来存放它，冲突太多会降低数据插入和搜索的效率，因此希望能找到一个不容易产生冲突的函数，即构造一个地址分布比较均匀的哈希函数。常用的哈希函数包括：直接定址法、数字分析法、除留余数法、乘留余数法、平方取中法、折叠法等。应该根据实际工作中关键码的特点选用适当的方法。

虽然采用合适的哈希方法能够降低冲突的概率，但是冲突仍然是不可避免的，处理冲突的最常用方法就是“桶”算法：假设哈希表有 m 个地址，就将其改为 m 个“桶”，其桶号与哈希地址一一对应，每个桶都用来存放互为同义词的键，也就是如果两个不同的键用哈希函数计算得到了同一个哈希地址，就将它们放到同一个桶中，检索的时候在桶内进行顺序检索。

### Java 中的 Map 接口

字典数据结构如此重要，以至于实际开发中经常需要使用它们。JDK 中提供了相关的类供我们使用，从而避免了自己开发字典类的麻烦。

在以前版本的 JDK 中，最常使用的字典类就是 Dictionary 抽象类及其实现类 Hashtable，不过在新版本的 JDK 中不推荐读者使用 Dictionary 抽象类而是使用 Map 接口，并且由于 Dictionary 的实现类 Hashtable 也实现了 Map 接口，所以我们没有理由不使用 Map 接口。

Map 接口有很多实现类，比如 HashMap、TreeMap、Hashtable、SortedMap 等，在第三方开源包中也有提供了更多功能的实现类，比如 Apache-Commons 项目中的 LRUMap。最常用的就是 HashMap 和 Hashtable，它们最大的区别就是 Hashtable 是线程安全的，而 HashMap 则不是线程安全的，在使用的时候必须进行同步。由于 JDK 中的工具类 java.util.Collections 提供了一个 synchronizedMap 方法，可以将非线程安全的 Map 接口变量采用装饰者模式改造成线程安全的，因此使用 HashMap 的场合更多一些，后边的论述也将以 HashMap 为主。

### HashMap

HashMap 是 Map 接口的实现类中最常用的一个，熟练的掌握这个类的使用将会提高解决问题的速度。

HashMap 的主要方法

```yaml
int size(): 得到 Map 中“键-值对”的数量

boolean isEmpty(): Map 是否是空的，也就是是否不含有任何“键-值对”

boolean containsKey(Object key): Map 中是否含有以 key 为键的“键-值对”

boolean containsValue(Object value): Map 中是否含有以 value 为值的“键-值对”

Object get(Object key): 从 Map 中得到以 key 为键的值，如果 Map 中不含有以 key 为键的“键-值对”则返回 null

Object put(Object key, Object value): 向 Map 中存储以 key 为键、value 为值的“键-值对”

Object remove(Object key):从 Map 中移除以 key 为键的“键-值对”

void putAll(Map t): 将另一个 Map 中的所有“键-值对”导入到此 Map 中

void clear(): 清除所有“键-值对”

Set keySet(): 得到所有的键

Collection values(): 得到所有的值

Set entrySet(): 得到所有的“键-值对”，Set 中的类型是 Map.Entry
```

### 应用举例

#### 工号查询

Tom 的工号是 1155669，Jim 的工号是 1155689，Jane 的工号是 1255669，Kevin 的工号是 1165669，Bit 的工号是 1155660，Gavin 的工号是 1155639。请编写一个程序，输入工号后显示此工号对应的人名。

```java
public class Map01 {
    public static void main(String[] args) {
        NameSearcher ns = new NameSearcher();
        System.out.println(ns.searchByNum("1155669"));
    }
}

class NameSearcher {
    private Map map;

    public NameSearcher() {
        super();
        map = new HashMap();
        map.put("1155669", "Tom");
        map.put("1155689", "Jim");
        map.put("1255669", "Jane");
        map.put("1165669", "Kevin");
        map.put("1155660", "Bit");
        map.put("1155639", "Gavin");
    }

    public String searchByNum(String num) {
        return (String) map.get(num);
    }
}

// Tom
```

#### 枚举工号

Tom 的工号是 1155669，Jim 的工号是 1155689，Jane 的工号是 1255669，Kevin 的工号是 1165669，Bit 的工号是 1155660，Gavin 的工号是 1155639。请编写一个程序，显示所有工号。

Map 的 keySet 方法返回的是所有的键，如果要显示所有人名，只要使用 values 方法即可。注意 values 方法的返回值是 Collection 接口，与 keySet 方法的 Set 类型不同，原因很简单，因为值不像键一样，值是存在重复的情况的。

```java
Map map = new HashMap();
map.put("1155669", "Tom");
map.put("1155689", "Jim");
map.put("1255669", "Jane");
map.put("1165669", "Kevin");
map.put("1155660", "Bit");
map.put("1155639", "Gavin");

Set keySet = map.keySet();
Iterator iterator = keySet.iterator();

while(iterator.hasNext())
{
    String key = (String) iterator.next();
    System.out.println(key);
}


// 1155689
// 1155660
// 1155639
// 1165669
// 1155669
// 1255669
```

#### 枚举工号名字

Tom 的工号是 1155669，Jim 的工号是 1155689，Jane 的工号是 1255669，Kevin 的工号是 1165669，Bit 的工号是 1155660，Gavin 的工号是 1155639。请编写一个程序，显示所有工号-名字“键-值对”。

```java
Map map = new HashMap();
map.put("1155669", "Tom");
map.put("1155689", "Jim");
map.put("1255669", "Jane");
map.put("1165669", "Kevin");
map.put("1155660", "Bit");
map.put("1155639", "Gavin");

Set entrySet = map.entrySet();
Iterator iterator = entrySet.iterator();

while (iterator.hasNext())
{

    Map.Entry keyValue = (Map.Entry) iterator.next();
    Object key = keyValue.getKey();
    Object value = keyValue.getValue();
    System.out.println("工号:" + key + ";姓名:" + value);

}

// 工号:1155689;姓名:Jim
// 工号:1155660;姓名:Bit
// 工号:1155639;姓名:Gavin
// 工号:1165669;姓名:Kevin
// 工号:1155669;姓名:Tom
// 工号:1255669;姓名:Jane
```

#### 嵌套哈希

某公司分为多个部门，各部门的名称不同，而且公司不设立统一的工号，而是每个部门内部自己指定工号，各个部门之间的工号有可能相同。请编写一个程序，用户输入部门名称和工号，检索出对应人的人名。

```java
public class Map04

{

    public static void main(String[] args)

    {

        PersonSearch04 ps = new PersonSearch04();

        ps.add("开发一部", "001", "Tom");

        ps.add("开发一部", "002", "Jane");

        ps.add("开发一部", "003", "Popo");

        ps.add("开发二部", "002", "Ruby");

        ps.add("开发二部", "003", "Jay");

        ps.add("开发二部", "005", "Cheris");

        System.out.println(ps.get("开发二部", "002"));

    }

}

class PersonSearch04

{

    private Map departMap;
    public PersonSearch04()

    {
        super();
        departMap = new HashMap();
    }

    public void add(String departName, String number, String personName)

    {

        // 首先取得部门人员的哈希表
        Map personMap = (Map) departMap.get(departName);
        // 由于当 key 不存在的时候 get 方法会返回 null，因此我们只要判断 get 方法
        // 是否为空就可以知道“键-值对”是否存在，不用调用 containsKey 方法
        // 去判断，这样少了一步计算 hashCode 的过程，能提高一定的效率

        if (personMap == null)
        {

            // 如果不存在部门人员哈希表,则新建一个部门人员哈希表,
            // 并以部门名称为 key,部门人员哈希表为 value 加入部门哈希表
            personMap = new HashMap();
            departMap.put(departName, personMap);

        }

        // 将人按照 number 为 key,人名为 value 加入部门人员哈希表
        personMap.put(number, personName);

    }

    public String get(String departName, String number)
    {

        // 首先取得部门人员的哈希表
        Map personMap = (Map) departMap.get(departName);
        if (personMap == null)
        {
            return null;
        }

        // 从部门人员哈希表中按照工号取出编码
        return (String) personMap.get(number);

    }

}

// Ruby
```

由于部门名称、工号、姓名没有一个能做为主键，所以可以以部门内的人员做为一个 Map，并将这个 Map 做为 Value 放入另一个 Map 中，也就是“Map 中的 Map”，这就解决了数据检索的问题。这个实现算法有点烦琐，并且有点难以理解，并且如果存在嵌套三层甚至更多层的情况就更难理解，这里采用另一种“复合主键”来实现另一种算法。

#### 复合主键

```java
public class Map05
{
    public static void main(String[] args)
    {
        PersonSearch05 ps = new PersonSearch05();
        ps.add("开发一部", "001", "Tom");
        ps.add("开发一部", "002", "Jane");
        ps.add("开发一部", "003", "Popo");
        ps.add("开发二部", "002", "Ruby");
        ps.add("开发二部", "003", "Jay");
        ps.add("开发二部", "005", "Cheris");
        System.out.println(ps.get("开发二部", "002"));
    }

}

class PersonSearch05
{
    private Map map;
    public PersonSearch05()
    {
        super();
        map = new HashMap();
    }

    public void add(String departName, String number, String personName)
    {
        map.put(departName + number, personName);
    }

    public String get(String departName, String number)
    {

        return (String) map.get(departName + number);
    }

}
```

部门名称不相同，所以部门名称加工号就可以做为键，这样就可以简化操作，算法实现起来也清晰多了。这种“复合主键”在实际应用中非常广泛，需要注意的是一定要保证这个“复合主键”不会重复，否则就会导致数据混乱。案例系统中的 SQLTranslator 中就是使用数据库类型加 SQL 语句做为“复合主键”的。

### Map 与 HashCode

开发过程中一般都是使用 String、Integer 等类型做主键的，这些类型都有已经有实现好的哈希函数算法，我们无需为其实现哈希函数算法，但是也会碰到以自定义类型做主键的情况。

#### 以自定义类型做主键

某公司工号的编号方式为“部门编号+出生年月日”，如果重复则在后边再加顺序号。比如编号为“dev002”的部门的出生年月日为“1979 年 10 月 8 日”的员工的工号为“dev00219791008”，如果已经存在此工号，则工号为“dev002197910081”。系统中有一个工号信息类 NumberInfo：

```java
class NumberInfo {
    private String departNum;
    private Date birthDay;
    private int seqNumber;

    public NumberInfo(String departNum, Date birthDay, int seqNumber) {
        super();
        this.departNum = departNum;
        this.birthDay = birthDay;
        this.seqNumber = seqNumber;
    }

    public NumberInfo(String departNum, Date birthDay) {
        super();
        this.departNum = departNum;
        this.birthDay = birthDay;
        this.seqNumber = -1;
    }

    public Date getBirthDay() {
        return birthDay;
    }

    public String getDepartNum() {
        return departNum;
    }

    public int getSeqNumber() {
        return seqNumber;
    }
}

// 接着实现一个检索程序以 NumberInfo 类型做为主键：
public class Map06 {
    public static void main(String[] args) {
        NumberInfo num1 = new NumberInfo("dev001", new Date(1979, 1, 1));
        NumberInfo num2 = new NumberInfo("dev001", new Date(1979, 1, 1), 1);
        NumberInfo num3 = new NumberInfo("dev002", new Date(1980, 6, 1));
        Map map = new HashMap();
        map.put(num1, "Tom");
        map.put(num2, "Peter");
        map.put(num3, "Bill");
        NumberInfo numToFind = new NumberInfo("dev001", new Date(1979, 1, 1));
        System.out.println(map.get(numToFind));
    }
}

// null
```

运行结果：null

有点出乎我们的意料，因为 numToFind 和我们想要查找的 num1 的 3 个域值都相等，为什么根据 numToFind 为键却查不到以 num1 为键的值呢？

由于 NumberInfo 直接从 Object 继承，而且没有重写 Object 类的方法，所有的行为都是和 Object 一致的，hashCode 方法也继承自 Object，而 Object 中的 hashCode 方法返回的 hashCode 对应于当前的地址，也就是说对于不同的对象，即使它们的内容完全相同，用 hashCode() 返回的值也会不同，这上违背了我们的意图。因为在使用 Map 时，希望利用相同内容的对象索引得到相同的目标对象，这就需要 hashCode()在此时能够返回相同的值。我们期望 numToFind 与 num1 是相等的。所以要重写 hashCode 方法和 equals 方法，保证对象内容相同的 NumberInfo 类实例有相同的 hashCode。重写如下：

```java
public boolean equals(Object obj)
{
    if (!(obj instanceof NumberInfo))
    {
        return false;
    }

    NumberInfo info = (NumberInfo) obj;
    return info.getDepartNum().equals(getDepartNum())
    && info.getBirthDay().equals(getBirthDay())
    && info.getSeqNumber() == getSeqNumber();
}

public int hashCode()
{
    String s = getDepartNum() + getBirthDay() + getSeqNumber();
    return s.hashCode();
}

// Tom
```

运行结果：Tom

根据前边所讲的哈希表的原理，不难得出如下结论：

做为键的对象其 hashCode 和 equals 方法必须满足下面的条件：如果两个对象相等，那么它们的 hashCode 必须相等。

如果要使用自定义类做为键的话，一定要覆盖 hashCode 和 equals 方法，不能只覆盖一个而不覆盖另一个。计算 hashCode 最好的方式就是找出此类的“组合主键”(比如上例中的 getDepartNum() + getBirthDay() + getSeqNumber())，然后直接返回这个“组合主键”，除非自己有十足的把握，否则不要自己实现哈希算法，因为那样很容易造成频繁的冲突。
由于使用自定义类做为键有很多问题需要处理，而且处理不当很很容易造成性能问题甚至数据混乱，所以在实际开发中尽量避免用自定义类做键。
