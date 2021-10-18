---
title: Discovering Python 3’s pathlib
tag: python
date: 2021-03-13
---

> 转载: [Discovering Python 3’s pathlib – Dante's Python musings](https://danteandpython.wordpress.com/2016/04/30/discovering-python-3s-pathlib/)

The pathlib is one of the new features in Python 3 I loved immediatly when I recognized it’s advantages. The pathlib a sort of a swiss knife tool and more than capable to replace os.path because it gives object orientated programming a reason. Especially for configuration purposes the pathlib is handy:

```python
>>> from pathlib import Path
>>> root = Path('../myproject')
>>> config_dir = root / Path('config')
>>> str(config_dir)
'../myproject/config'
```

The slash as an operator avoids brackets to join paths and makes the code very simplistic. But here doesn’t the advantage:

```python
>>> path1 = Path('/home/dante')
>>> path2 = Path('/home/dante/project/src')
>>> path2.relative_to(path1)
PosixPath('project/src')
```

Of course fundamental operations like file IO and file name attributes are available:

```python
>>> config_files = config_dir.glob('*.conf))
>>> config_files
[PosixPath('root/config/network.conf'), PosixPath('root/config/project.conf')]
>>> config_files[0].unlink() # delete root/config/network.conf
>>> config_files = config_dir.glob('*.conf))
[PosixPath('root/config/project.conf')]
>>> config_files[0].stem
'project'
>>> config_files[0].suffix
'.conf'
>>> config_files[0].parent
PosixPath('root/config/)
>>> list(config_files[0].parents)
[PosixPath('root/config'), PosixPath('root'), PosixPath('.')]
```

Every Path object linked to a file is able to open this file:

```python
>>> config_file = config_dir / Path('project.conf')
>>> with config_file.open('r') as f:
...    print(f.read)
ip=127.0.0.1
>>>
```

But reading a file can be even shorter:

```python
>>> config_file = config_dir / Path('project.conf')
>>> print(config_file.read_text())
ip=127.0.0.1
>>>
```

Python 3’s pathlib is able to supersede os.path with ease. The OOP approach makes working with this library fun.
