---
title: Python Fire
tags: python
date: 2019-06-06
---

Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

- Python Fire is a simple way to create a CLI in Python.
- Python Fire is a helpful tool for developing and debugging Python code.
- Python Fire helps with exploring existing code or turning other people's code into a CLI.
- Python Fire makes transitioning between Bash and Python easier.
- Python Fire makes using a Python REPL easier by setting up the REPL with the modules and variables you'll need already imported and created.

### Hello World

fire.Fire() 文件名后直接接变量名，会返回文件变量的值

```python
import fire
english = 'Hello World'
spanish = 'Hola Mundo'
fire.Fire()

$ python example.py english
Hello World
$ python example.py spanish
Hola Mundo
```

fire.Fire() 文件名后直接接函数名，函数参数，会调用文件函数返回函数返回值

```python
import fire

def hello(name):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  fire.Fire()

$ python example.py hello World
Hello World!
```

fire.Fire(fn) 使用 fire.Fire(fn) 调用函数，执行命令行只需要传递参数即可

```python
import fire

def hello(name):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  fire.Fire(hello)

$ python example.py World
Hello World!
```

### Exposing Multiple Commands

fire.Fire()

```python
import fire

def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

if __name__ == '__main__':
  fire.Fire()

$ python example.py add 10 20
30
$ python example.py multiply 10 20
200
```

fire.Fire(dict)

```python
import fire

def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

if __name__ == '__main__':
  fire.Fire({
      'add': add,
      'multiply': multiply,
  })

$ python example.py add 10 20
30
$ python example.py multiply 10 20
200
```

fire.Fire(object)

```python
import fire

class Calculator(object):

  def add(self, x, y):
    return x + y

  def multiply(self, x, y):
    return x * y

if __name__ == '__main__':
  calculator = Calculator()
  fire.Fire(calculator)

$ python example.py add 10 20
30
$ python example.py multiply 10 20
200
```

fire.Fire(class)

```python
import fire

class Calculator(object):

  def add(self, x, y):
    return x + y

  def multiply(self, x, y):
    return x * y

if __name__ == '__main__':
  fire.Fire(Calculator)

$ python example.py add 10 20
30
$ python example.py multiply 10 20
200
```

fire.Fire(class) 也可以通过参数构建类

```python
import fire

class BrokenCalculator(object):

  def __init__(self, offset=1):
      self._offset = offset

  def add(self, x, y):
    return x + y + self._offset

  def multiply(self, x, y):
    return x * y + self._offset

if __name__ == '__main__':
  fire.Fire(BrokenCalculator)

$ python example.py add 10 20
31
$ python example.py multiply 10 20
201

$ python example.py add 10 20 --offset=0
30
$ python example.py multiply 10 20 --offset=0
200
```

### Grouping Commands

```python
class IngestionStage(object):

  def run(self):
    return 'Ingesting! Nom nom nom...'

class DigestionStage(object):

  def run(self, volume=1):
    return ' '.join(['Burp!'] * volume)

  def status(self):
    return 'Satiated.'

class Pipeline(object):

  def __init__(self):
    self.ingestion = IngestionStage()
    self.digestion = DigestionStage()

  def run(self):
    self.ingestion.run()
    self.digestion.run()

if __name__ == '__main__':
  fire.Fire(Pipeline)

$ python example.py run
Ingesting! Nom nom nom...
Burp!
$ python example.py ingestion run
Ingesting! Nom nom nom...
$ python example.py digestion run
Burp!
$ python example.py digestion status
Satiated.
```

### Accessing Properties

```python
import fire

airports = []
airports.append(["ABI", "Abilene, TX - Abilene Regional (ABI)"])
airports.append(["BQN", "Aguadilla, PR - Rafael Hernandez (BQN)"])

class Airport(object):
    def __init__(self,code):
        self.code = code
        self.name = dict(airports).get(self.code)
        self.city = self.name.split(',')[0] if self.name else None

if __name__ == '__main__':
    fire.Fire(Airport)

$ python example.py --code=ABI code
ABI
$ python example.py --code=ABI name
Abilene, TX - Abilene Regional (ABI)
$ python example.py --code=ABI city
Abilene
```

### Chaining Function Calls

```python
 python example.py --code=ABI city upper
 ABILENE
```

### Calling Functions

simple

```python
import fire

class Building(object):

  def __init__(self, name, stories=1):
    self.name = name
    self.stories = stories

  def climb_stairs(self, stairs_per_story=10):
    for story in range(self.stories):
      for stair in range(1, stairs_per_story):
        yield stair
        yield 'Phew!'
    yield 'Done!'

if __name__ == '__main__':
  fire.Fire(Building)


$ python example.py --name="Sherrerd Hall" --stories=3 climb_stairs 10
$ python example.py --name="Sherrerd Hall" climb_stairs --stairs_per_story=10
$ python example.py --name="Sherrerd Hall" climb_stairs --stairs-per-story 10
$ python example.py climb-stairs --stairs-per-story 10 --name="Sherrerd Hall"
```

with `*varargs` and `**kwargs`

```python
import fire

def order_by_length(*items):
  # 先根据字符长度排序，再根据首字母排序
  sorted_items = sorted(items, key=lambda item: (len(str(item)), str(item)))
  return ' '.join(sorted_items)

if __name__ == '__main__':
  fire.Fire(order_by_length)

$ python example.py dog cat elephant
cat dog elephant

$ python example.py dog cat elephant - upper
CAT DOG ELEPHANT

$ python example.py dog cat elephant upper
cat dog upper elephant

$ python example.py dog cat elephant X upper -- --separator=X
CAT DOG ELEPHANT
```

### Argument Parsing

```python
import fire
fire.Fire(lambda obj: type(obj).__name__)

$ python example.py 10
int
$ python example.py 10.0
float
$ python example.py hello
str
$ python example.py '(1,2)'
tuple
$ python example.py [1,2]
list
$ python example.py True
bool
$ python example.py {name: David}
dict
```

### Flags

| Using a CLI                                                                                       | Command                    | Notes                                                         |
| ------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------- |
| [Help](https://github.com/google/python-fire/blob/master/docs/using-cli.md#help-flag)             | `command -- --help`        | Show help and usage information for the command.              |
| [REPL](https://github.com/google/python-fire/blob/master/docs/using-cli.md#interactive-flag)      | `command -- --interactive` | Enter interactive mode.                                       |
| [Separator](https://github.com/google/python-fire/blob/master/docs/using-cli.md#separator-flag)   | `command -- --separator=X` | This sets the separator to `X`. The default separator is `-`. |
| [Completion](https://github.com/google/python-fire/blob/master/docs/using-cli.md#completion-flag) | `command -- --completion`  | Generate a completion script for the CLI.                     |
| [Trace](https://github.com/google/python-fire/blob/master/docs/using-cli.md#trace-flag)           | `command -- --trace`       | Gets a Fire trace for the command.                            |
| [Verbose](https://github.com/google/python-fire/blob/master/docs/using-cli.md#verbose-flag)       | `command -- --verbose`     | Include private members in the output.                        |

```python
python example.py -- --help
Type:        type
String form: <class '__main__.Airport'>
File:        g:\python\firetest\example.py.py
Line:        8

Usage:       example.py CODE
             example.py --code CODE
```
