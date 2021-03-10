---
title: python and java calculate memory
tags:
  - python
  - java
---

## python 和 java 计算程序占用内存

1. python/java 调用 cmd 命令
2. 使用正则切分 cmd 命令返回结果
3. 对结果进行监控，处理

### cmd 命令

```bat
tasklist/?

显示 tasklist 命令的相关帮助

tasklist /fi "imagename eq python.exe"

映像名称                       PID 会话名              会话#       内存使用
========================= ======== ================ =========== ============
python.exe                    1688 Console                    1     74,972 K
python.exe                    5312 Console                    1     24,556 K


tasklist /fi "imagename eq python.exe" | findstr python.exe

python.exe                    1688 Console                    1     74,972 K
python.exe                    5312 Console                    1     24,556 K
```

### python 方式

```python
import os, re
import time
import string

# 统计某一个进程名所占用的内存，同一个进程名，可能有多个进程
def countProcessMemoey(processName):
    # python.exe                    1688 Console                    1     74,972 K
    pattern = re.compile(r'([^\s]+)\s+(\d+)\s.*\s([^\s]+\sK)')
    cmd = 'tasklist /fi "imagename eq ' + processName + '"' + ' | findstr.exe ' + processName
    result = os.popen(cmd).read()
    resultList = result.split("\n")

    total = 0
    for srcLine in resultList:
        srcLine = "".join(srcLine.split('\n'))
        if len(srcLine) == 0:
            break
        m = pattern.search(srcLine)
        if m == None:
            continue

        # 由于是查看python进程所占内存，因此通过pid将本程序过滤掉
        if str(os.getpid()) == m.group(2):
            continue
        ori_mem = m.group(3).replace(',','')
        ori_mem = ori_mem.replace(' K','')
        ori_mem = ori_mem.replace(r'\sK','')
        memEach = int(ori_mem) * 1.0 / 1024
        total += memEach
        print('ProcessName:'+ m.group(1) + '\tPID:' + m.group(2) + '\tmemory size:%.2f'% memEach, 'M')
    print('total: ', total, 'M', sep='')
    print("*" * 58)

if __name__ == '__main__':
    # 进程名
    ProcessName = 'python.exe'
    while True:
        countProcessMemoey(ProcessName)
        time.sleep(5)


# ProcessName:python.exe  PID:8344        memory size:27.96 M
# ProcessName:python.exe  PID:7748        memory size:21.27 M
# total: 49.2265625M
# **********************************************************
```

### java 方式

```java
package com.jbn;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class RuntimeTest {
    public static void main(String[] args) {
        Runtime runtime = Runtime.getRuntime();
        InputStream in = null;
        Reader reader = null;
        Process process = null;
        int i;
        try {
            // imagename eq Code.exe 不能使用单引号，需要使用双引号
            String cmd = "tasklist /fi \"imagename eq Code.exe\"";
            process = runtime.exec(cmd);
            in = process.getInputStream();  // 获取调用 cmd 的输出
            reader = new InputStreamReader(in, "gbk");  // 使用字符流，window 控制台输出是 gbk 编码
            StringBuffer stringBuffer = new StringBuffer();
            char[] buffer = new char[1024]; // 字符缓冲
            while ((i = reader.read(buffer)) != -1) {
                stringBuffer.append(buffer, 0, i);
            }
            String result = stringBuffer.toString();
            String[] strs = result.split("\n");
            double sum = 0;
            for (int j = 0; j < strs.length; j++) {
                if (j < 3) {
                    continue;
                }
                // 正则模块
                Pattern pattern = Pattern.compile("([^\\s]+)\\s+(\\d+)\\s.*\\s([^\\s]+\\sK)");
                Matcher matcher = pattern.matcher(strs[j]);
                if (matcher.find()) {
                    String processName = matcher.group(1);
                    String pid = matcher.group(2);
                    String memory = matcher.group(3);
                    System.out.println("process: " + processName +
                                       "  PID: " + pid + "  memory: " + memory);
                    sum += Integer.parseInt(memory.replace(",", "").split(" ")[0]) / 1024;
                }

            }
            System.out.println("total: " + sum + " M");
            process.waitFor();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (in != null) {
                try {
                    in.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```
