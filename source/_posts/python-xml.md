---
title: python xml parsing
tags: python
date: 2019-07-15
---

### ElementTree vs SAX and DOM

`SAX (simple API for XML)` It functions as a stream parser, with an event-driven API.

`DOM (Document Object Model)` It reads the XML into memory and converts it to objects that can be accessed with Python.

`ElementTree`

* ElementTree is much easier to use, because it represents an XML tree (basically) as a structure of lists, and attributes are represented as dictionaries. 
* ElementTree needs much less memory for XML trees than DOM (and thus is faster), and the parsing overhead via(凭借) `iterparse` is comparable to SAX. Additionally, `iterparse` returns partial structures, and you can keep memory usage constant during parsing by discarding the structures as soon as you process them.
* ElementTree, as in Python 2.5, has only a small feature set compared to full-blown XML libraries, but it's enough for many applications. If you need a validating parser or complete XPath support, lxml is the way to go. For a long time, it used to be quite unstable, but I haven't had any problems with it since 2.1.
* ElementTree deviates(脱离) from DOM, where nodes have access to their parent and siblings. Handling actual documents rather than data stores is also a bit cumbersome(笨重的，难处理的）, because text nodes aren't treated as actual nodes. In the XML snippet

### SAX

movies.xml

```xml
<collection shelf="New Arrivals">
   <movie title="Enemy Behind">
      <type>War, Thriller</type>
      <format>DVD</format>
      <year>2003</year>
      <rating>PG</rating>
      <stars>10</stars>
      <description>Talk about a US-Japan war</description>
   </movie>
   <movie title="Transformers">
      <type>Anime, Science Fiction</type>
      <format>DVD</format>
      <year>1989</year>
      <rating>R</rating>
      <stars>8</stars>
      <description>A schientific fiction</description>
   </movie>
   <movie title="Trigun">
      <type>Anime, Action</type>
      <format>DVD</format>
      <episodes>4</episodes>
      <rating>PG</rating>
      <stars>10</stars>
      <description>Vash the Stampede!</description>
   </movie>
   <movie title="Ishtar">
      <type>Comedy</type>
      <format>VHS</format>
      <rating>PG</rating>
      <stars>2</stars>
      <description>Viewable boredom</description>
   </movie>
</collection>
```

saxparser.py

```python
import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""
        
    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":

    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")

```

### DOM

domparser.py

```python
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement

if collection.hasAttribute("shelf"):
    print("root element : {}".format(collection.getAttribute("shelf")))

movies = collection.getElementsByTagName("movie")

for movie in movies:
    print("***movie***")
    if movie.hasAttribute("title"):
        print("title:{}".format(movie.getAttribute("title")))
    type = movie.getElementsByTagName('type')[0]
    print('type:{}'.format(type.childNodes[0].data))
    format = movie.getElementsByTagName('format')[0]
    print ("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print ("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print ("Description: %s" % description.childNodes[0].data)
```

### ElementTree

etreeparser.py

```python
import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
tag = root.tag
attrib = root.attrib
print("root:{0},shelf:{1}".format(tag, attrib.get('shelf')))

for child in root:
    print(child.tag, child.attrib)
    title = child.get('title')
    format = child.find('format').text
    rating = child.find('rating').text
    stars = child.find('stars').text
    description = child.find('description').text
    print('***movie***')
    print("title:{}".format(title))
    print("type:{}".format(format))
    
# root:collection,shelf:New Arrivals
# movie {'title': 'Enemy Behind'}
# ***movie***
# title:Enemy Behind
# type:DVD
# movie {'title': 'Transformers'}
# ***movie***
# title:Transformers
# type:DVD
# movie {'title': 'Trigun'}
# ***movie***
# title:Trigun
# type:DVD
# movie {'title': 'Ishtar'}
# ***movie***
# title:Ishtar
# type:VHS

```

