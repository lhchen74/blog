---
title: Clear explanation of Rust’s module system
tags: rust
date: 2020-09-07
---

> [Clear explanation of Rust’s module system](http://www.sheshbabu.com/posts/rust-module-system/)

Rust’s module system is surprisingly confusing and causes a lot of frustration for beginners.

In this post, I’ll explain the module system using practical examples so you get a clear understanding of how it works and can immediately start applying this in your projects.

Since Rust’s module system is quite unique, I request the reader to read this post with an open mind and resist comparing it with how modules work in other languages.

Let’s use this file structure to simulate a real world project:

```shell
my_project
├── Cargo.toml
└─┬ src
  ├── main.rs
  ├── config.rs
  ├─┬ routes
  │ ├── health_route.rs
  │ └── user_route.rs
  └─┬ models
    └── user_model.rs
```

These are the different ways we should be able to consume our modules:

![img](rust-modules/rust-module-system-1.png)

These 3 examples should be sufficient to explain how Rust’s module system works.

## Example 1

Let’s start with the first example - importing `config.rs` in `main.rs`.

```rust
// main.rs
fn main() {
  println!("main");
}
// config.rs
fn print_config() {
  println!("config");
}
```

The first mistake that everyone makes is just because we have files like `config.rs`, `health_route.rs` etc, we think that these files are `modules` and we can import them from other files.

Here’s what we see (file system tree) and what the compiler sees (module tree):

![img](rust-modules/rust-module-system-2.png)

Surprisingly, the compiler only sees the `crate` module which is our `main.rs` file. This is because we need to explicitly build the module tree in Rust - there’s no implicit mapping between file system tree to module tree.

> We need to explicitly build the module tree in Rust, there’s no implicit mapping to file system

To add a file to the module tree, we need to declare that file as a submodule using the `mod` keyword. The next thing that confuses people is that you would assume we declare a file as module in the same file. But we need to declare this in a different file! Since we only have `main.rs` in the module tree, let’s declare `config.rs` as a submodule in `main.rs`.

> The mod keyword declares a submodule

The `mod` keyword has this syntax:

```rust
mod my_module;
```

Here, the compiler looks for `my_module.rs` or `my_module/mod.rs` in the same directory.

```shell
my_project
├── Cargo.toml
└─┬ src
  ├── main.rs
  └── my_module.rs

or

my_project
├── Cargo.toml
└─┬ src
  ├── main.rs
  └─┬ my_module
    └── mod.rs
```

Since `main.rs` and `config.rs` are in the same directory, let’s declare the config module as follows:

```diff
// main.rs
+ mod config;

fn main() {
+ config::print_config();
  println!("main");
}
// config.rs
fn print_config() {
  println!("config");
}
```

We’re accessing the `print_config` function using the `::` syntax.

Here’s how the module tree looks like:

![img](rust-modules/rust-module-system-3.png)

We’ve successfully declared the `config` module! But this is not sufficient to be able to call the `print_config` function inside `config.rs`. Almost everything in Rust is private by default, we need to make the function public using the `pub` keyword:

> The pub keyword makes things public

```rust
// main.rs
mod config;

fn main() {
  config::print_config();
  println!("main");
}
// config.rs
- fn print_config() {
+ pub fn print_config() {
  println!("config");
}
```

Now, this works. We’ve successfully called a function defined in a different file!

## Example 2

Let’s try calling the `print_health_route` function defined in `routes/health_route.rs` from `main.rs`.

```rust
// main.rs
mod config;

fn main() {
  config::print_config();
  println!("main");
}
// routes/health_route.rs
fn print_health_route() {
  println!("health_route");
}
```

As we discussed earlier, we can use the `mod` keyword only for `my_module.rs` or `my_module/mod.rs` in the same directory.

So in order to call functions inside `routes/health_route.rs` from `main.rs`, we need to do the following things:

- Create a file named `routes/mod.rs` and declare the `routes` submodule in `main.rs`
- Declare the `health_route` submodule in `routes/mod.rs` and make it public
- Make the functions inside `health_route.rs` public

```diff
my_project
├── Cargo.toml
└─┬ src
  ├── main.rs
  ├── config.rs
  ├─┬ routes
+ │ ├── mod.rs
  │ ├── health_route.rs
  │ └── user_route.rs
  └─┬ models
    └── user_model.rs
// main.rs
mod config;
+ mod routes;

fn main() {
+ routes::health_route::print_health_route();
  config::print_config();
  println!("main");
}
// routes/mod.rs
+ pub mod health_route;
// routes/health_route.rs
- fn print_health_route() {
+ pub fn print_health_route() {
  println!("health_route");
}
```

Here’s how the module tree looks like:

![img](rust-modules/rust-module-system-4.png)

We can now call a function defined in a file inside a folder.

## Example 3

Let’s try calling from `main.rs => routes/user_route.rs => models/user_model.rs`

```rust
// main.rs
mod config;
mod routes;

fn main() {
  routes::health_route::print_health_route();
  config::print_config();
  println!("main");
}
// routes/user_route.rs
fn print_user_route() {
  println!("user_route");
}
// models/user_model.rs
fn print_user_model() {
  println!("user_model");
}
```

We want to call the function `print_user_model` from `print_user_route` from `main`.

Let’s make the same changes as before - declaring submodules, making functions public and adding the `mod.rs` file.

```diff
my_project
├── Cargo.toml
└─┬ src
  ├── main.rs
  ├── config.rs
  ├─┬ routes
  │ ├── mod.rs
  │ ├── health_route.rs
  │ └── user_route.rs
  └─┬ models
+   ├── mod.rs
    └── user_model.rs
// main.rs
mod config;
mod routes;
+ mod models;

fn main() {
  routes::health_route::print_health_route();
+ routes::user_route::print_user_route();
  config::print_config();
  println!("main");
}
// routes/mod.rs
pub mod health_route;
+ pub mod user_route;
// routes/user_route.rs
- fn print_user_route() {
+ pub fn print_user_route() {
  println!("user_route");
}
// models/mod.rs
+ pub mod user_model;
// models/user_model.rs
- fn print_user_model() {
+ pub fn print_user_model() {
  println!("user_model");
}
```

Here’s how the module tree looks like:

![img](rust-modules/rust-module-system-5.png)

Wait, we haven’t actually called `print_user_model` from `print_user_route`! So far, we’ve only called the functions defined in other modules from `main.rs`, how do we do that from other files?

If we look at our module tree, the `print_user_model` function sits in the `crate::models::user_model` path. So in order to use a module in files that are not `main.rs`, we should think in terms of the path necessary to reach that module in the module tree.

```diff
// routes/user_route.rs
pub fn print_user_route() {
+ crate::models::user_model::print_user_model();
  println!("user_route");
}
```

We’ve successfully called a function defined in a file from a file that’s not `main.rs`.

## super

The fully qualified name gets too lengthy if our file organization is multiple directories deep. Let’s say for whatever reason, we want to call `print_health_route` from `print_user_route`. These are under the paths `crate::routes::health_route` and `crate::routes::user_route` respectively.

We can call it by using the fully qualified name `crate::routes::health_route::print_health_route()` but we can also use a relative path `super::health_route::print_health_route();`. Notice that we’ve used `super` to refer to the parent scope.

> The super keyword in module path refers to the parent scope

```rust
pub fn print_user_route() {
  crate::routes::health_route::print_health_route();
  // can also be called using
  super::health_route::print_health_route();

  println!("user_route");
}
```

## use

It would be tedious to use the fully qualified name or even the relative name in the above examples. In order to shorten the names, we can use the `use` keyword to bind the path to a new name or alias.

> The use keyword is used to shorten the module path

```rust
pub fn print_user_route() {
  crate::models::user_model::print_user_model();
  println!("user_route");
}
```

The above code can be refactored as:

```rust
use crate::models::user_model::print_user_model;

pub fn print_user_route() {
  print_user_model();
  println!("user_route");
}
```

Instead of using the name `print_user_model`, we can also alias it to something else:

```rust
use crate::models::user_model::print_user_model as log_user_model;

pub fn print_user_route() {
  log_user_model();
  println!("user_route");
}
```

## External modules

Dependencies added to `Cargo.toml` are available globally to all modules inside the project. We don’t need to explicitly import or declare anything to use a dependency.

> External dependencies are globally available to all modules inside a project

For example, let’s say we added the [rand](https://crates.io/crates/rand) crate to our project. We can use it in our code directly as:

```rust
pub fn print_health_route() {
  let random_number: u8 = rand::random();
  println!("{}", random_number);
  println!("health_route");
}
```

We can also use `use` to shorten the path:

```rust
use rand::random;

pub fn print_health_route() {
  let random_number: u8 = random();
  println!("{}", random_number);
  println!("health_route");
}
```

## Summary

- The module system is explicit - there’s no 1:1 mapping with file system
- We declare a file as module in its parent, not in itself
- The `mod` keyword is used to declare submodules
- We need to explicitly declare functions, structs etc as public so they can be consumed in other modules
- The `pub` keyword makes things public
- The `use` keyword is used to shorten the module path
- We don’t need to explicitly declare 3rd party modules
