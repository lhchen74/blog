---
title: Python jieba
tags: python
date: 2020-10-30
---

### 分词

```python
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))     # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")     # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

```

输出:
Full Mode: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学
Default Mode: 我/ 来到/ 北京/ 清华大学
他, 来到, 了, 网易, 杭研, 大厦
小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, ，, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造

### 关键词提取

```python
import jieba.analyse
# 基于TF-IDF：jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
# 基于TextRank：jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
# topK=20前20个, allowPos()允许的词性
'''
sentence = r'中国特色社会主义是我们党领导的伟大事业，\
全面推进党的建设新的伟大工程，是这一伟大事业取得胜利的关键所在。\
党坚强有力，事业才能兴旺发达，国家才能繁荣稳定，人民才能幸福安康。\
党的十八大以来，我们党坚持党要管党、从严治党，凝心聚力、直击积弊、扶正祛邪，\
党的建设开创新局面，党风政风呈现新气象。习近平总书记围绕从严管党治党提出一系列新的重要思想\
为全面推进党的建设新的伟大工程进一步指明了方向。'.encode('UTF-8')
'''
import jieba.analyse
print(jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=()))
print(jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')))
```

### 词性标注

```python
import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s, %s' % (word, flag))
# 我, r
# 爱, v
# 北京, ns
# 天安门, ns

words = pseg.cut("我们可以将网页内容保存到笔记中，这样可以更方便自己查阅。")
for world,flag in words:
    if  flag !='w' and  flag != 'x' :   #去除标点符号等
        print('%s, %s' %(world, flag))
```
