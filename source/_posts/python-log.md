---
title: Python Logging
tags: python
date: 2019-02-28
---

> Remember, no matter what anyone says or tells you to do, look to yourself! What's inside you is stronger than you spell. - Ella Enchanted

### 日志级别大小关系

`CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET`

### 输出 log 到控制台

```python
import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s')
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')

# 2018-09-17 14:46:43,070 - other.py[line:6] - WARNING
# 2018-09-17 14:46:43,070 - other.py[line:7] - ERROR
# 2018-09-17 14:46:43,071 - other.py[line:8] - CRITICAL
```

### 输出 log 到文件

```python
import logging
logging.basicConfig(level=logging.WARNING,
                    filename='log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')

# log.txt
# 2018-09-17 14:45:22,340 - other.py[line:20] - WARNING: this is loggging a warning message
# 2018-09-17 14:45:22,341 - other.py[line:21] - ERROR: this is an loggging error message
# 2018-09-17 14:45:22,341 - other.py[line:22] - CRITICAL: this is a loggging critical message
```

### 输出 log 到控制台并写入文件

```python
import logging
# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)    # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = 'logger.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)       # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)     # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
```

### 日志格式

logging.basicConfig 函数中，可以指定日志的输出格式 format，这个参数可以输出很多有用的信息

| option         | meaning                            |
| -------------- | ---------------------------------- |
| %(levelname)s  | 打印日志级别名称                   |
| %(pathname)s   | 打印当前执行程序的路径 sys.argv[0] |
| %(filename)s   | 打印当前执行程序名                 |
| %(funcName)s   | 打印日志的当前函数                 |
| %(lineno)d     | 打印日志的当前行号                 |
| %(asctime)s    | 打印日志的时间                     |
| %(thread)d     | 打印线程 ID                        |
| %(threadName)s | 打印线程名称                       |
| %(process)d    | 打印进程 ID                        |
| %(message)s    | 打印日志信息                       |

常用格式,这个格式可以输出日志的打印时间，是哪个模块输出的，输出的日志级别是什么，以及输入的日志内容。

`format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'`

### 日志回滚

日志回滚的意思为：比如日志文件是 chat.log，当 chat.log 达到指定的大小之后，RotatingFileHandler 自动把文件改名为 chat.log.1。不过，如果 chat.log.1 已经存在，会先把 chat.log.1 重命名为 chat.log.2。最后重新创建 chat.log，继续输出日志信息。这样保证 chat.log 里面是最新的日志

```python
import os
import xml.etree.ElementTree
import logging
from logging.handlers import RotatingFileHandler

dir_path = os.path.dirname(os.path.realpath(__file__))
config = xml.etree.ElementTree.parse(dir_path+'\cfgFtpFilePusher.xml').getroot()

curDate = datetime.date.today()
logFile=config.find('./LOG').attrib['FILE'] % curDate
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(funcName)s(%(lineno)d)] %(message)s')
logHandler = RotatingFileHandler(logFile, maxBytes=2*1024*1024, backupCount=2, encoding=None, delay=0)
logHandler.setFormatter(log_formatter)
logHandler.setLevel(logging.INFO)
logger = logging.getLogger('root')
logger.setLevel(logging.INFO)
logger.addHandler(logHandler)
```
