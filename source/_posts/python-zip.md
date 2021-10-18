---
title: Python Uncompress Compressed File
tags: python
date: 2019-10-25
---

> [使用Python3解压gz、tar、tgz、zip、rar五种格式的压缩文件例子 - lykops - 博客园](https://www.cnblogs.com/lykops/p/8263112.html)

gz： 即gzip，通常只能压缩一个文件; 与tar结合起来就可以实现先打包，再压缩。

tar： linux系统下的打包工具，只打包，不压缩。

tgz：即tar.gz，先用tar打包，然后再用 gz 压缩得到的文件。

zip： 不同于gzip，虽然使用相似的算法，可以打包压缩多个文件，不过分别压缩文件，压缩率低于tar。

rar：打包压缩文件，最初用于DOS，基于window操作系统。压缩率比zip高，但速度慢，随机访问的速度也慢。

#### Example

```python
import gzip
import os
import tarfile
import zipfile
import rarfile


def get_filetype(filepath):
    extension = filepath.split('.')[-2:]
    if extension[0] == 'tar' and extension[1] == 'gz':
        return 'tgz'
    return extension[1]


def uncompress(compress_file, dest_dir):
    extension = get_filetype(compress_file)

    try:
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
    except Exception as a:
        return (False, 'Create Uncompressed Dir Failed', extension)

    if extension in ('tgz', 'tar'):
        try:
            tar = tarfile.open(compress_file)
            names = tar.getnames()
            for name in names:
                tar.extract(name, dest_dir)
            tar.close()
        except Exception as e:
            return (False, e, extension)

    elif extension == 'zip':

        try:
            extension = zipfile.ZipFile(compress_file)
            for name in extension.namelist():
                extension.extract(name, dest_dir)
            extension.close()
        except Exception as e:
            return (False, e, extension)

    elif extension == 'rar':

        try:
            rar = rarfile.RarFile(compress_file)
            os.chdir(dest_dir)
            rar.extractall()
            rar.close()
        except Exception as e:
            return (False, e, extension)

    elif extension == 'gz':
        try:
            # gz just compress one file, generally use tar package file then use gz compress
            # test.txt.gz => test.txt
            file_name = dest_dir + '/' + \
                os.path.splitext(os.path.basename(compress_file))[0]

            with gzip.open(compress_file, 'rb') as gz, open(file_name, 'wb') as f:
                f.write(gz.read())

        except Exception as e:
            return (False, e, extension)
    else:
        return (False, 'Unsupported Compressed File Type', extension)

    return (True, '', extension)


uncompress('git.txt.gz', 'gz')
```
