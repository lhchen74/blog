---
title: ruby homework
tags: ruby
date: 2020-11-29
---

> 最远的旅行，是从自己的身体到自己的心，是从一个人的心到另一个人的心。坚强不是面对悲伤不流一滴泪，而是擦干眼泪后微笑面对以后的生活。—宫崎骏 《风之谷》

### number and text

-   Determines if a string is palindrome, such as abcba

-   Find all even number location letter in a string, such as `"abcd" => "bd"`

```ruby
def palindrome?(str)
    len = str.length
    count = (len / 2).floor()
    for i in 0..count
        if str[i] != str[len-i-1]
            return false
        end
    end
    return true
end

def palindrome?(string)
 if string == string.reverse
   return true
 else
   return false
 end
end

puts palindrome?("abcba")
puts palindrome?("abba")
puts palindrome?("abcb")

def even_letters(str)
    s = ""
    for i in 0...str.length
        if (i + 1) % 2 == 0
            s += str[i]
        end
    end
    return s
end

puts even_letters("abcd")
```

### array

input = [1, 2, 3], output = [2, 4, 6]

```ruby

output = []
input = [1, 2, 3]
input.each{ |e| output << e * 2  }
p output

output = input.map{ |e| e * 2  }
p output
```

### block

Create a method each_starts_with, which can work like this:

`each_starts_with(["abcd", "axyz", "able", "xyzab"], "ab") { |s| puts s }`

abcd

able

```ruby
def each_starts_with(arr, str)
    arr.each { |e| yield e if e.start_with?(str)   }
end

def each_starts_with(arr, str, &block)
    arr.each { |e| block.call(e) if e.start_with?(str)   }
end

each_starts_with(["abcd", "axyz", "able", "xyzab"], "ab") { |s| puts s   }
```

### hash, set, range

How to solve the problem that switch symbol and string key of hash?

### method

Use singleton method transfer [1, 2, 3] it self to [2, 4, 6]

```ruby
arr = [1, 2, 3]
def arr.*(num)
    self.map{ |e| e * 2   }
end

puts arr * 2
```

### exception

```ruby
arr = [1, 2, "abc", 3, "hello", " world", "abc", 0.3]
def sum_pair(arr)
    sum = 0
    arr.each_slice(2) do |pair|
        begin
            puts pair[0] + pair[1]
        rescue TypeError => e
            puts "Invalid sumation of #{ pair[0].class   } + #{ pair[1].class   }"
        else
            sum += 1
        ensure

        end
    end

    puts '**! Altogether there are #{ sum   } pairs processed !**'
end

sum_pair(arr)
```

### regex

```ruby
# We want to get both {{mustache_template}}, and a normal substitution { like_this }, but not a { {{ crazy_one }} }

text = "We want to get both {{mustache_template}}, and a normal substitution {like_this}, but not a { {{ crazy_one }} }"
p text.scan(/\{{1,2}([^{}]+)\}{1,2}[^}]/)  # [["mustache_template"], ["like_this"]]
```

### io

Create a directory 'Log/' whith 10 log files named log0.txt, log1.txt, ... ,etc. Each of which prints `hello\n world\n #{ file_name }`

And then read from eatch file, and append them into array

```ruby
Dir.mkdir('Log')
Dir.chdir('Log')
10.times.each do |i|
    file_name = "log#{i}.txt"
    File.open(file_name, 'w') do |f|
        f.puts 'hello'
        f.puts 'world'
        f.puts file_name
    end
end


res = Dir.glob('Log/*.txt').each_with_object([]) do |file_name, ret|
    ret.push(*File.readlines(file_name))
end

puts res
```

### class

Write a class called BankAccount, which has the following internal structure:

-   class/instaince variable

    -   exchange_rate($ and ￥)
    -   balance

-   and class methods:
    -   def usd_to_rmb(amount)
    -   def rmb_to_usd(amount)
-   and instance methods:

    -   def deposit(amount)
    -   def withdraw(amount)

-   and the ability to get balance but not directly set balance

```ruby
class BankAccount
    @@exchange_rate = 6  # class variable

    attr_reader :balance # define instance method access instance variable
    # def balance
    #     @balance
    # end

    def initialize(amount = 0)
        @balance = amount # instance variable, can not direct access outer class
    end

    # def self.usd_to_rmb(amount)
    #     amount * @@exchange_rate
    # end

    # def self.rmb_to_usd(amount)
    #     amount / @@exchange_rate
    # end

    class << self
        def usd_to_rmb(amount)
            (amount * @@exchange_rate).round(2)
        end

        def rmb_to_usd(amount)
            (amount / @@exchange_rate).round(2)
        end
    end

    def deposit(amount)
        @balance += amount
    end

    def withdraw(amount)
        @balance -= amount
        raise 'Overdraw Alert' if @balance < 0
    end
end

account = BankAccount.new(100)
puts account.balance   # 100
account.ddeposit100)
account.withdraw(50)
puts account.balance # 150

puts BankAccount.usd_to_rmb(100) # 600
puts BankAccount.rmb_to_usd(100) # 16
```

### class extend

Based on BankAccount, write two subclasses CitiBankAccount and ChaseBankAccount:

-   transfer(to_account, amount)

-   withdraw
    -   citi bank: $3 service fee
    -   chase bank: $2 service fee

```ruby
class CitiBankAccount < BankAccount
    def transfer(to_account, amount)
        @balance -= amount
        to_account.deposit(amount)
    end

    def withdraw(amount)
        super
        @balance -= 3
    end
end

class ChaseBankAccount < BankAccount
    def transfer(to_account, amount)
        @balance -= amount
        to_account.ddepositamount)
    end

    def withdraw(amount)
        super
        @balance -= 2
    end
end
```

### module

Write a module called Lib, which provides functionality for charging annual fee

-   buckets = [0, 1000, 10_000, 50_000, 100_000], 0 ~ 1000, annual fee is 10, 1000 ~ 10_000 annual fee is 5, 10_1000 ~ 50_000 annual fee is 3, 50_000 ~ annual fee is 0
-   annual_fee

```ruby
module Lib
    BUCKETS = [0, 1000, 10_000, 50_000, 100_000]

    def annual_fee
        case balance
        when BUCKETS[0]...BUCKETS[1]
            10
        when BUCKETS[1]...BUCKETS[2]
            5
        when BUCKETS[2]...BUCKETS[3]
            3
        else
            0
        end
    end
end


class BankAccount
    include Lib
end

b = BankAccount.new(10_000)
puts b.annual_fee  # 3
```

### comparable adn enumerable

Modify the BankAccount class to make it comparable based on the account banlance
Create Bank has instance variable accounts and make it enumerable based on the accounts

Modify BankAccount

```diff
class BankAccount
    + include Enumerable

    @@exchange_rate = 6

    attr_reader :balance

    def initialize(amount = 0)
        @balance = amount
    end

    class << self
        def usd_to_rmb(amount)
            (amount * @@exchange_rate).round(2)
        end

        def rmb_to_usd(amount)
            (amount / @@exchange_rate).round(2)
        end
    end

    def deposit(amount)
        @balance += amount
    end

    def withdraw(amount)
        @balance -= amount
        raise 'Overdraw Alert' if @balance < 0
    end

    + def <=> (other)
    +    balance <=> other.balance
    + end
end

b1 = BankAccount.new(10_000)
b2 = BankAccount.new(20_000)
puts b2 > b1 # true
```

And Bank

```ruby
class Bank
    include Enumerable

    attr_reader :accounts

    def initialize(accounts)
        @accounts = accounts
    end

    def add(account)
        accounts.push(account)
    end

    def each
        accounts.each do |account|
            yield account
        end
    end
end

b1 = BankAccount.new(10_000)
b2 = BankAccount.new(20_000)
bank = Bank.new([b1, b2])
bank.each{ |e| puts e.balance}

# 10000
# 20000
```

### thread

Using 50 threads to create 200 accounts, and deposit each with a random amounts of money and store them into one file: 'balance.txt'. Each line of balance.txt is account information for each account. e.g.

Time.now.to_s 100

Time.now.to_s 32

```ruby
bank = Bank.new([])
File.open('balance.txt', 'a') do |f|
    threads = []
    50.times do |i|
        threads[i] = Thread.new do
            4.times do |j|
                account = BankAccount.new()
                account.deposit(rand(100))
                bank.add(account)
                f.puts "#{i} #{Time.now.to_s} #{account.balance}"
                f.flush
            end
        end
    end
    # threads.each{ |t| t.join   }
    threads.each(&:join)
end
bank.each { |e| puts e}
```
