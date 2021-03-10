---
title: python data clean
tags: python
date: 2019-07-15
description: python 简单数据清理
---

### 数据源 train.csv

```csv
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
7,0,1,"McCarthy, Mr. Timothy J",male,54,0,0,17463,51.8625,E46,S
8,0,3,"Palsson, Master. Gosta Leonard",male,2,3,1,349909,21.075,,S
9,1,3,"Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",female,27,0,2,347742,11.1333,,S
10,1,2,"Nasser, Mrs. Nicholas (Adele Achem)",female,14,1,0,237736,30.0708,,C
11,1,3,"Sandstrom, Miss. Marguerite Rut",female,4,1,1,PP 9549,16.7,G6,S
12,1,1,"Bonnell, Miss. Elizabeth",female,58,0,0,113783,26.55,C103,S
13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,S
14,0,3,"Andersson, Mr. Anders Johan",male,39,1,5,347082,31.275,,S
15,0,3,"Vestrom, Miss. Hulda Amanda Adolfina",female,14,0,0,350406,7.8542,,S
16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S
17,0,3,"Rice, Master. Eugene",male,2,4,1,382652,29.125,,Q
18,1,2,"Williams, Mr. Charles Eugene",male,,0,0,244373,13,,S
19,0,3,"Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",female,31,1,0,345763,18,,S
20,1,3,"Masselmani, Mrs. Fatima",female,,0,0,2649,7.225,,C
```

### 数据查看

```python
import pandas as pd
import numpy as np

file = 'train.csv'
df = pd.DataFrame(pd.read_csv(file))

# 1).查看数据的维度
print(df.shape)

# 2).查看数据的基本信息(查看数据集的整体的数据类型，比如有的int,有的是float,有的时候还有datetime64等等)
print(df.info())

# 2）查看整个数据的整体的分布
print(df.describe())

# 3).查看数据集的空值，或者说是缺失值
print(df.isnull().sum())

# 4).查看唯一值
print(df['Pclass'].unique()) # 相当于group by出所有值

# 5).查看数据集的前3行,后3行
print(df.head(3))
print(df.tail(3))
```

### 数据提取

```python

# 6).按照索引的值进行提取:
print(df.loc[630]) #提取索引值为630的那一行

# 7).按照索引的位置进行提取
print(df3.loc[2]) #取第三行的数据

# 8).取部分行和列
print(df.iloc[2:5,:5]) #取第二,三四行和前5列

# 9).按照条件提取
# 取仓位为小于2的，并且性别为女性的数据
print(df[(df['Pclass'] <= 2) & (df['Sex'] == 'female')])
```

### 数据清洗

```python
# 10).处理空值,用dropna删除空值
df.dropna(how='any')  #发现Age中的空值会全部删掉
df.fillna(value=0)
df['Age'].fillna(df['Age'].mean()) #用数据集里面的年龄均值来填充空值

# 11).对字符的处理，比如大小写的转换
df['Name'].map(str.upper)

# 12).对字符串的快速映射转换
df['Pclass'] = df['Pclass'].map({'1':'一等舱','2':'二等舱','3':'三等舱'})

# 13).对数据集中的数据格式的改变
# print(df.dtypes)
df['Fare'].astype('int')

# 14).更改列的名字
df.rename(columns={'Survied':'是否获救'})

# 15).去掉重复值
df['Embarked'].drop_duplicate() # 想知道登船的类别，去掉所有重复的数据

# 16).数据的代替,替换
df['Sex'] = df['Sex'].replace('male','男')
```

### 数据排序

```python
# 17).按照年龄进行降序排列
print(df.sort_values(by=['Age'],ascending=False).head(2))

# 18).按照index来排序
print(df.sort_index(axis=0).head(3))
print(df.sort_index(axis=1).head(3))
```

### 保存文件

```python
df.to_csv('clean.csv')
```
