---
title: language typed
tags: other
---

### 基础概念

#### Program Errors

`trapped errors` 出错后导致程序终止执行，如除 0，Java 中数组越界访问
`untrapped errors` 出错后继续执行，但可能出现任意行为，如 C 里的缓冲区溢出、Jump 到错误地址

#### Forbidden Behaviours

`forbidden behaviors` 语言设计时，可以定义一组 forbidden behaviors. 它必须包括所有 untrapped errors, 可能包含 trapped errors.

#### Well behaved、ill behaved

`well behaved` 如果程序执行不可能出现 forbidden behaviors, 则为 well behaved.
`ill behaved` 如果程序执行可能出现 forbidden behaviors, 则为 ill behaved.

### 强、弱类型

`strongly typed` 如果一种语言的所有程序都是 well behaved 即不可能出现 forbidden behaviors ，则该语言为 strongly typed
`weakly typed` 否则为 weakly typed，比如C语言的缓冲区溢出，属于 untrapped errors，即属于 forbidden behaviors 故C是弱类型

### 动态、静态类型

`statically` 如果在编译时拒绝 ill behaved 程序，则是statically typed;
`dynamiclly` 如果在运行时拒绝 ill behaved 程序, 则是dynamiclly typed