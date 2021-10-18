---
title: Python XMLの要素・属性・内容を削除する(ElementTree)
tags: python
date: 2021-03-12
---

> 转载：[【Python】XMLの要素・属性・内容を削除する(ElementTree) | 鎖プログラム](https://pg-chain.com/python-xml-remove)

### サンプルXML

#### sports.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<sports>
  <sport order="001">
    <name>サッカー</name>
    <orgin>イングランド</orgin>
  </sport>
  <sport order="002">
    <name>野球</name>
    <orgin>アメリカ</orgin>
  </sport>
</sports>
```

このサンプルXMLを削除していきます。

### XMLを解析する

```python
import xml.etree.ElementTree as ET

# XMLを解析
tree = ET.parse('C:\pg\sports.xml')

# XMLを取得
root = tree.getroot()
```

まずはXMLを解析します。XMLファイルをparse で解析し、getroot でXMLのルートを取得します。

### XMLの要素を削除する remove

```python
# 要素を削除する
for sport in root.findall('sport'):
    for orgin in sport.findall('orgin'):
        sport.remove(orgin) 

# XMLファイルに保存
tree.write('C:\pg\sports.xml')
```

#### 削除（remove）後のXML

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<sports>
  <sport order="001">
    <name>サッカー</name>
  </sport>
  <sport order="002">
    <name>野球</name>
  </sport>
</sports>
```

XMLの要素を削除するには、remove を使います。

remove は「親要素.remove(削除する子要素)」と指定します。要素「sport」をfindall で取り出し、その要素の中の要素「orgin」をさらにfindall で取り出しました。

ここでは要素「orgin」を削除しました。

### XMLの属性を削除する pop

```python
# 属性を削除する 
for sport in root.iter('sport'):
    sport.attrib.pop("order", None)

# XMLファイルに保存
tree.write('C:\pg\sports.xml')
```

#### 削除（pop）後のXML

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<sports>
  <sport>
    <name>サッカー</name>
  </sport>
  <sport>
    <name>野球</name>
  </sport>
</sports>
```

XMLの属性を削除するには、pop を使います。

ここでは要素「sport」にある属性「order」を削除しました。

### XMLのデータ（テキスト、コンテンツ）を削除（クリア）する

```python
# 内容の削除
for name in root.iter('name'):
    name.text = ''

# XMLファイルに保存
tree.write('C:\pg\sports.xml')
```

#### 削除後のXML

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<sports>
  <sport>
    </name>
  </sport>
  <sport>
    </name>
  </sport>
</sports>
```

XMLの要素・属性ではなく、データ（テキスト）自体をを削除するには、text  を使います。

ここでは要素「name」にあるテキストを削除（クリア）しました。

### XMLの要素・属性・テキストを一括で削除する

```python
# 要素・属性・テキストをすべて削除する
root.clear()

# XMLファイルに保存
tree.write('C:\pg\sports.xml')
```

#### 削除後のXML

```
<?xml version="1.0"?>
<sports/>
```

XMLの要素・属性・テキストをすべて削除するには、clear  を使います。

これでPythonのXMLの削除するパターンとして、要素の削除・属性の削除・内容の削除の３パターンの削除を実行することができました。

参考ページ：https://docs.python.jp/3/library/xml.etree.elementtree.html

以上、PythonでXMLの要素・属性・内容を削除する方法でした。