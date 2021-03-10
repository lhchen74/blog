---
title: Rust Question
tags: rust
date: 2020-08-13
---

### What is the syntax: `instance.method::<SomeThing>()`?

This construct is called turbofish(tuna fish 金枪鱼). If you search for this statement, you will discover its definition and its usage.

path::<...>, method::<...> Specifies parameters to generic type, function, or method in an expression; often referred to as turbofish (e.g., "42".parse::<i32>())

You can use it in any kind of situation where the compiler is not able to deduce([dɪˈduːs]
vt. 推论，推断；演绎出) the type parameter, e.g.

```rust
fn main () {
    let a = (0..255).sum();
    let b = (0..255).sum::<u32>();
    let c: u32 = (0..255).sum();
}
```

a does not work because it cannot deduce the variable type.
b does work because we specify the type parameter directly with the turbofish syntax.
c does work because we specify the type of c directly.

### the size for values of type `[u8]` cannot be known at compilation time?

```rust
// @ the size for values of type `[u8]` cannot be known at compilation time, the trait `std::marker::Sized` is not implemented for `[u8]`
// const CHARSET: [u8] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ\
//                 abcdefghijklmnopqrstuvwxyz\
//                 0123456789)(*&^%$#@!~";
const CHARSET: &[u8] = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ\
                abcdefghijklmnopqrstuvwxyz\
                0123456789)(*&^%$#@!~";
```

### How to open file with open and write mode ?

```rust
// File::open open file only read mode, so write content will PermissionDenied
// let mut f = std::fs::File::open("foo.txt")
//     .ok()
//     .expect("Couldn’t open foo.txt");
// let buf = b"hello";
// f.write(buf).expect("Couldn’t write to foo.txt"); // thread 'main' panicked at 'Couldn’t write to foo.txt: Os { code: 5, kind: PermissionDenied, message: "拒绝访问。" }'

let mut f = std::fs::OpenOptions::new()
    .read(true)
    .write(true)
    .open("foo.txt")
    .ok()
    .expect("Couldn’t open foo.txt");

let buf = b"hello";
f.write(buf).expect("Couldn’t write to foo.txt");
```

### what mean of ref & ref mut below?

```rust
let mut x = 5;

match x {
    ref mut mr => println!("mut ref {}", mr),
}
```

When doing pattern matching or destructuring via the let binding, the ref keyword can be used to take references to the fields of a struct/tuple. The example below shows a few instances where this can be useful:

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // A `ref` borrow on the left side of an assignment is equivalent to
    // an `&` borrow on the right side.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 equals ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` is also valid when destructuring a struct.
    let _copy_of_x = {
        // `ref_to_x` is a reference to the `x` field of `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Return a copy of the `x` field of `point`.
        *ref_to_x
    };

    // A mutable copy of `point`
    let mut mutable_point = point;

    {
        // `ref` can be paired with `mut` to take mutable references.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Mutate the `y` field of `mutable_point` via a mutable reference.
        *mut_ref_to_y = 1;
    }

    println!("point is ({}, {})", point.x, point.y);
    println!("mutable_point is ({}, {})", mutable_point.x, mutable_point.y);

    // A mutable tuple that includes a pointer
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // Destructure `mutable_tuple` to change the value of `last`.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple is {:?}", mutable_tuple);
}
```

### What is the difference between immutable and const variables in Rust?

const, in Rust, is short for constant and is related to compile-time evaluation. It shows up:

-   when declaring constants: const FOO: usize = 3;
-   when declaring compile-time evaluable functions: const fn foo() -> &'static str

These kinds of values can be used as generic parameters: [u8; FOO]. For now this is limited to array size, but there is talk, plans, and hope to extend it further in the future.

By contrast, a let binding is about a run-time computed value.

Note that despite mut being used because the concept of mutability is well-known, Rust actually lies here. &T and &mut T are about aliasing, not mutability:

-   &T: shared reference
-   &mut T: unique reference

Most notably, some types feature interior mutability and can be mutated via &T (shared references): Cell, RefCell, Mutex, etc.

### Stack & Heap

-   栈 stack

栈 stack 是一种 后进先出 容器。就像我们的存储罐子，后面放进去的只能先拿出来（后面放进去的会放在上面）。

栈 stack 上存储的元素大小必须是已知的，也就是说如果一个变量或数据要放到栈上，那么它的大小在编译是就必须是明确的。

例如，对于一个数据类型为 i32 的变量，它的大小是可预知的，只占用 4 个字节。

Rust 语言中所有的标量类型都可以存储到栈上，因为它们的大小都是固定的。

而对于字符串这种复合类型，它们在运行时才会赋值，那么在编译时的大小就是未知的。那么它们就不能存储在栈上，而只能存储在 堆 上。

-   堆 heap

堆 heap 用于存储那些在编译时大小未知的数据，也就是那些只有在运行时才能确定大小的数据。

我们一般在堆 heap 上存储那些动态类型的数据。简而言之，我们一般在堆上存储那些可能在程序的整个生命周期中发生变化的数据。

堆 是不受系统管理的，由用户自己管理，因此，使用不当，内存溢出的可能性就大大增加了。
