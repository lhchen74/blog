---
title: ruby attr_accessor
tags: ruby
date: 2019-10-29
---

> 转载: [ruby 疑难点之—— attr_accessor attr_reader attr_writer - 弋痕夕的残影 - 博客园](https://www.cnblogs.com/licongyu/p/5522030.html)

### 普通的实例变量

普通的实例变量，我们没法在 class 外面直接访问

```ruby
#普通的实例变量，只能在 class 内部访问
class C1
    def initialize(name)
        @name = name
    end
end

t1 = C1.new( {'a' => 1, 'b' => 2})
puts t1.name                             #报错： undefined method `name' for #<Context::C1:0x0000000142cd30 @name={:a=>1, :b=>2}>
```

如果要想在 class 外访问实例变量，我们可以自己实现实例方法来访问

```ruby
#普通的实例变量，只能在 class 内部访问
class C1
    def initialize(name)
        @name = name
    end

    def name
        @name
    end

    def name=(arg)
        @name=arg
    end
end

t1 = C1.new( {'a' => 1, 'b' => 2})
puts t1.name()                               #正确：调用 t1.name 方法
puts t1.name=( {'c' => 3, 'd' => 4} )        #正确：调用 t1.name= 方法
puts t1.name()                               #正确：{"c"=>3, "d"=>4}
```

其实这里的 name 和 name= 方法只是故意取名和实例变量有很像，用其它名称也一样

```ruby
#普通的实例变量，只能在 class 内部访问
class C1
    def initialize(name)
        @name = name
    end

    def fun1()
        @name
    end

    def fun2(arg)
        @name = arg
    end
end

t1 = C1.new( {'a' => 1, 'b' => 2})
puts t1.fun1()                               #正确：调用 t1.name 方法
puts t1.fun2( {'c' => 3, 'd' => 4} )         #正确：调用 t1.name= 方法
puts t1.fun1()                               #正确：{"c"=>3, "d"=>4}
```

### attr_reader :arg

attr_reader 限制实例变量 arg 在 class 外部只可读，其相当于在 class 中同时定义了一个 **arg** 方法

```ruby
#添加一个可 read 属性，在 class 外部只可 read 该实例变量（等同于通过 instance.arg 方法），而不可对该变量赋值（相当于调用 instance.arg= 方法不存在）
#attr_reader 的限定有点类似 C 中 int const * p的作用，限定的是变量，而非变量指向的对象
class C2
    attr_reader :name
    def initialize(name)
        @name =  {'a' => 1, 'b' => 2}
    end
end

t2 = C2.new( {'a' => 1, 'b' => 2})
puts t2.name                                      # 正确： {"a"=>1, "b"=>2}
puts (t2.name).delete('a')                        # 正确： attr_reader 保护的是变量 name ，但是变量 name 指向的对象内容是可变的
puts t2.name                                      # 正确： {"b"=>2}
puts t2.name = {'c' => 3}                         # 报错： undefined method `name=' for #<Context::C2:0x000000021cdf48 @name={"b"=>2}>

#为了说明隐式定义了 t2.name() 方法，下面通过方法调用的形式来访问
t2 = C2.new( {'a' => 1, 'b' => 2})
puts t2.name()                                    # 正确： {"a"=>1, "b"=>2}
```

### attr_writer :arg

attr_reader 限制实例变量 arg 在 class 外部只可写，其相当于在 class 中同时定义了一个 **arg=** 方法

```ruby
#添加一个可 write 属性，在 class 外部只可 write 该实例变量
class C3
    attr_writer :name
    def initialize(name)
        @name = name
    end

t3 = C3.new( {'a' => 1, 'b' => 2})
puts t3.name                           # 报错：undefined method `name' for #<Context::C3:0x0000000140afc8 @name={:a=>1, :b=>2}>
puts t3.name = {'c' => 3}              # 正确：{"c"=>3}
puts (t3.name).delete(:c)              # 报错：（没有定义方法 name，所以不能用这种方式企图获取到 name 变量指向的对象）： undefined method `name' for #<Context::C3:0x000000021e9c70 @name={"c"=>3}>
```

### attr_accessor :arg

attr_reader 限制实例变量 arg 在 class 外部只可读，其相当于在 class 中同时定义了一个 **arg 和 arg=** 方法

```ruby
class C4
    attr_accessor :name
    def initialize(name)
        @name = name
    end
end

t4 = C4.new({'a' => 1, 'b' => 2})
puts t4.name                                        #正确：相当于调用 t4.name() 方法
puts t4.name={'c' => 3, 'd' => 4}                   #正确：相当于调用 t4.name=() 方法
puts t4.name                                        #正确：{"c"=>3, "d"=>4}
#为了说明隐式定义了 t4.name() 和 t4.name=() 方法，下面通过方法调用的形式来访问
puts t4.name=( {'e' => 5, 'f' => 6} )
puts t4.name()                                      #正确：{"e"=>5, "f"=>6}
```
