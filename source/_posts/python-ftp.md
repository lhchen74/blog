---
title: python ftp sftp
tags: python
date: 2019-02-28
---

### ftp 上传下载文件

```python
from ftplib import FTP
import time
import os
import shutil

port = 21

def ftpconnect(host, port, username, password):
    ftp = FTP()
    ftp.set_debuglevel(2)           # 打开调试级别2，显示详细信息
    ftp.connect(host, port)         # 连接
    ftp.login(username, password)   # 登录，如果匿名登录则用空串代替即可
    return ftp


def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024                  # 设置缓冲块大小
    fp = open(localpath, 'wb')      # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)           # 关闭调试
    fp.close()                      # 关闭文件


def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == '__main__':
   ftp = ftpconnect(host, port, username, password)
   print(ftp)
```

### paramiko 上传下载 SFTP 文件

```python
import paramiko
import os

hostname = 'xxx'
username = 'xxx'
password = 'xxx'
port = 22  # int
upload_local_dir = 'xxx'
download_local_dir = 'xxx'
remote_dir = 'inbox/' # 注意目录，需要手动添加 /
SFTP_DOWNLOAD_FLAG = False # 用来判断文件是否下载成功


def sftp_callback(transfered, total):
    global SFTP_DOWNLOAD_FLAG
    if transfered == total:
        SFTP_DOWNLOAD_FLAG = True

def sftpconnect(host, port, username, password):
    try:
        sf = paramiko.Transport((host, port))
        sf.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(sf)
        return sftp
    except Exception as e:
        print('connect exception: ', e)


def sftp_upload(host, port, username, password, local, remote):
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        if os.path.isdir(local):
            for f in os.listdir(local):
                sftp.put(os.path.join(local, f), os.path.join(remote+f))
        else:
            sftp.put(local, remote)
    except Exception as e:
        print('upload exception: ', e)
    finally:
        if sf is not None:
            sf.close()


def sftp_download(host, port, username, password, local, remote):
    global SFTP_DOWNLOAD_FLAG
    sf = paramiko.Transport((host, port))
    sf.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    try:
        # 远程目录不要用 os.path.isdir(local) 判断是否是文件夹，除非已经确定
        # 因为 inbox/ 的上层目录可能没有权限访问，判断目录总是会返回 False
        for f in sftp.listdir(remote):
            sftpAttributes = sftp.lstat(os.path.join(remote+f))
            fileSize = sftpAttributes.st_size
            if fileSize:  # 只有文件不为空，才会调用 sftp_callback 函数
                sftp.get(os.path.join(remote+f), os.path.join(local, f), sftp_callback)
            else:         # 空文件无法用 sftp_callback 判断是否下载成功，所以不下载
                continue

            if SFTP_DOWNLOAD_FLAG:  # 下载成功，移除远程目录文件
                SFTP_DOWNLOAD_FLAG = False
                sftp.remove(os.path.join(remote+f))
            else:                   # 如果上传存在问题，移除本地已经上传的文件
                os.remove(os.path.join(local, f))

    except Exception as e:
        print('download exception: ', e)
    finally:
        if sf is not None:
            sf.close()


if __name__ == '__main__':
    # 测试连接
    sftp = sftpconnect(host, port, username, password)
    print(sftp)
```
