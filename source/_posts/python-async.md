---
title: python async
tags: python
date: 2019/07/15
---

### 异步 IO

当代码需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理。

异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复"读取消息-处理消息"这一过程：

```python
loop = get_event_loop()

while True:
	event = loop.get_event()
	process_event(event)
```

消息模型其实早在应用在桌面应用程序中了。一个GUI程序的主线程就负责不停地读取消息并处理消息。所有的键盘、鼠标等消息都被发送到GUI程序的消息队列中，然后由GUI程序的主线程处理。

### async

**async/await**: two new Python keywords that are used to define coroutines

**asyncio**: the Python package that provides a foundation and API for running and managing coroutines

```python
import asyncio

@asyncio.coroutine
def hello():
    print("hello world")
    r = yield from asyncio.sleep(1)
    print("hello world again")

# python3
async def hello2():
    print("hello python")
    r = await asyncio.sleep(1)
    print("hello python again")

loop = asyncio.get_event_loop()
tasks = [hello(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# hello python
# hello world
# hello python again
# hello again
```

