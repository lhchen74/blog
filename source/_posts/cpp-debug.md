---
title: C/C++ How do you set GDB debug flag (-g) with cmake?
tags: c
date: 2021-04-16
---

> 转载: [C/C++: How do you set GDB debug flag (-g) with cmake? – Bytefreaks.net](https://bytefreaks.net/programming-2/cc-how-do-you-set-gdb-debug-flag-g-with-cmake)

### Solution 1: Modify the CMakeLists.txt file

Add the following line to your `CMakeLists.txt` file to set the compilation mode to `Debug` (non-optimized code with debug symbols):

```cmake
set(CMAKE_BUILD_TYPE Debug)
```

Add the following line to your `CMakeLists.txt` file to set the compilation mode to `RelWithDebInfo` (optimized code with debug symbols):

```cmake
set(CMAKE_BUILD_TYPE RelWithDebInfo)
```

### Solution 2: Add a command line argument to your cmake command:

Modify as follows your `cmake` command to set the compilation mode to `Debug` (non-optimized code with debug symbols):

```cmake
cmake -DCMAKE_BUILD_TYPE=Debug <path and other arguments>
```

Modify as follows your `cmake` command to set the compilation mode to `RelWithDebInfo` (optimized code with debug symbols):

```cmake
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo <path and other arguments>
```

### Bonus material:

The difference between `Debug` and `RelwithDebInfo` modes is that `RelwithDebInfo` optimizes the code similarly to the behavior of `Release` mode. It produces fully optimized code, but also creates the symbol table and the debug metadata to give the debugger as much input as it is possible to map the execution back to the original code at any time.

Code build with `RelwithDebInfo` mode should not have it’s performance degraded in comparison to `Release` mode, as the symbol table and debug metadata that are generated do not live in the executable code section, so they should not affect the performance when the code is run without a debugger attached.
