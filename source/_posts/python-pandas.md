---
title: Python Pandas
tags: python
date: 2020-10-30
---

### 创建对象

```python
1. 通过传递一个list对象来创建一个Series，pandas会默认创建整型索引
import pandas as pd
import numpy as np
s = pd.Series([1,3,5,np.nan])
# print(s)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# dtype: float64

2. 通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame
dates = pd.date_range('20180119',periods = 6)
# print(dates)
# DatetimeIndex(['2018-01-19', '2018-01-20', '2018-01-21', '2018-01-22',
#                '2018-01-23', '2018-01-24'],
#               dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# print(df)
#                    A         B         C         D
# 2018-01-19 -2.902452 -0.311695 -0.342849  1.616858
# 2018-01-20  0.475718 -0.323746  1.885224 -1.139170
# 2018-01-21  0.404301  0.386661  1.176591 -0.889582
# 2018-01-22 -0.415695 -0.027721  0.565688 -0.158884
# 2018-01-23 -0.361975  0.508800 -1.429186 -0.638797
# 2018-01-24  0.466634 -0.655750  0.845265 -1.381422
# numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。
# numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中

3. 通过传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame
df2 = pd.DataFrame({
    'A' : 1.,
    'B' : pd.Timestamp('20180119'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(['test','test','test2','test3']),
    'F' : 'foo'
})
# print(df2)
#     A          B    C  D      E    F
# 0  1.0 2018-01-19  1.0  3   test  foo
# 1  1.0 2018-01-19  1.0  3   test  foo
# 2  1.0 2018-01-19  1.0  3  test2  foo
# 3  1.0 2018-01-19  1.0  3  test3  foo
# print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object
```

### 查看数据

```python
import pandas as pd
import numpy as np
dates = pd.date_range('20180119',periods = 6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
1. 查看frame中头部和尾部的行
# print(df.head())
#                   A         B         C         D
# 2018-01-19  0.315776 -1.262597  0.417930  0.816487
# 2018-01-20 -1.851086 -0.081404 -0.816561 -0.275335
# 2018-01-21  2.198723 -1.162804  0.455082 -1.106705
# 2018-01-22 -1.086726 -0.974309  0.975481 -0.053164
# 2018-01-23 -1.808937 -1.477894  0.392138  0.131833
# print(df.tail(3))
#                    A         B         C         D
# 2018-01-22 -1.086726 -0.974309  0.975481 -0.053164
# 2018-01-23 -1.808937 -1.477894  0.392138  0.131833
# 2018-01-24  2.435823  0.010048  0.806189  0.559598
2. 显示索引、列和底层的numpy数据
# print(df.index)
# DatetimeIndex(['2018-01-19', '2018-01-20', '2018-01-21', '2018-01-22',
#                '2018-01-23', '2018-01-24'],
#               dtype='datetime64[ns]', freq='D')
# print(df.columns)
# Index(['A', 'B', 'C', 'D'], dtype='object')
# print(df.values)
# [[ 0.24919313  1.69670287  0.00307654 -0.22192602]
#  [-0.49304832 -1.15940945 -0.33040307  0.83062988]
#  [-0.60605614 -0.94390582  0.0920051  -0.25452046]
#  [ 0.49692782 -0.68505704 -0.06938114  0.69423629]
#  [-0.67451809 -0.49074972  1.2760681   0.06424315]
#  [ 1.11390404 -1.37691908 -0.03828506 -0.88249195]]
3. describe()函数对于数据的快速统计汇总
# print(df.describe())
#              A         B         C         D
# count  6.000000  6.000000  6.000000  6.000000
# mean   0.234599 -0.066277 -0.368595 -0.078489
# std    0.714956  1.322297  0.774115  1.201034
# min   -0.578654 -1.756372 -1.624966 -1.429098
# 25%   -0.151149 -0.930873 -0.774090 -0.965526
# 50%    0.131585  0.018819 -0.009791 -0.034075
# 75%    0.380844  0.441674  0.059116  0.319939
# max    1.504540  1.985881  0.379752  1.864379
4.  对数据的转置
# print(df.T)
#  2018-01-19  2018-01-20  2018-01-21  2018-01-22  2018-01-23  2018-01-24
# A   -0.919441    1.018841   -1.539721   -0.863824   -2.239723   -0.103792
# B   -1.830522    1.425763   -1.757576    0.848743   -0.520246    1.281699
# C    0.592624    0.960820    0.117273    0.189679    1.452047    1.237425
# D    0.195343   -1.081498    0.237329    0.237053   -0.859959   -0.031775
5. 按轴进行排序
# print(df.sort_index(axis=1,ascending=False))
#                   D         C         B         A
# 2018-01-19  0.539793  0.586982 -0.913723 -0.565786
# 2018-01-20 -0.965416  0.611870 -0.007035  0.241761
# 2018-01-21  0.200597  0.301047  0.762469  0.674582
# 2018-01-22 -0.647771  1.014385  0.953812 -0.852226
# 2018-01-23  0.317777  0.207167  0.086378  0.446269
# 2018-01-24  1.180738 -2.144122  0.214231  0.423743
6. 按值进行排序
# print(df.sort_values(by='B'))
#                    A         B         C         D
# 2018-01-19 -0.565786 -0.913723  0.586982  0.539793
# 2018-01-20  0.241761 -0.007035  0.611870 -0.965416
# 2018-01-23  0.446269  0.086378  0.207167  0.317777
# 2018-01-24  0.423743  0.214231 -2.144122  1.180738
# 2018-01-21  0.674582  0.762469  0.301047  0.200597
# 2018-01-22 -0.852226  0.953812  1.014385 -0.647771
```

### 选择

```python
import pandas as pd
import numpy as np
dates = pd.date_range('20180119',periods = 6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
1. 获取
1.1 选择一个单独的列，这将会返回一个Series，等同于df.A
# print(df['A'])
# 2018-01-19   -0.453672
# 2018-01-20    0.014933
# 2018-01-21    0.519788
# 2018-01-22    0.259396
# 2018-01-23    1.510170
# 2018-01-24    0.765011
# Freq: D, Name: A, dtype: float64
1.2 通过[]进行选择，这将会对行进行切片
# print(df[0:2])
#                    A         B         C         D
# 2018-01-19  1.244513 -0.186764 -0.215445 -0.678315
# 2018-01-20 -0.390595 -0.089850  1.693733  1.326059
# print(df['20180119':'20180121'])
#                    A         B         C         D
# 2018-01-19  1.244513 -0.186764 -0.215445 -0.678315
# 2018-01-20 -0.390595 -0.089850  1.693733  1.326059

2. 通过标签选择
2.1 使用标签来获取某一行
# print(df.loc[dates[0]])
# A   -0.267135
# B   -1.417678
# C   -0.418960
# D   -0.481945
# Name: 2018-01-19 00:00:00, dtype: float64
2.2 通过标签来在多个轴上进行选择
# print(df.loc[:, ['A','B']])
#                   A         B
# 2018-01-19 -0.267135 -1.417678
# 2018-01-20  0.646314  0.840619
# 2018-01-21  0.715013  1.101890
# 2018-01-22 -2.059424  1.981140
# 2018-01-23  0.085624  0.081103
# 2018-01-24  0.554221 -1.941612
2.3 标签切片
# print(df.loc['20180119':'20180121',['A','B']])
#                   A         B
# 2018-01-19 -0.267135 -1.417678
# 2018-01-20  0.646314  0.840619
# 2018-01-21  0.715013  1.101890
2.4 对返回的对象进行维度缩减
# print(df.loc['20180119',['A','B']])
# A   -0.267135
# B   -1.417678
2.5 获取一个标量
# print(df.loc[dates[0],'A'])
# -0.267135186243
2.6 快速访问一个标量（与上一个方法等价）
# print(df.at[dates[0],'A'])
# -0.267135186243

3. 通过位置选择
3.1 通过传递数值进行位置选择（选择的是行）
# print(df.iloc[3])
# A    0.014979
# B    1.848822
# C   -0.195405
# D   -0.698225
# Name: 2018-01-22 00:00:00, dtype: float64
3.2 通过数值进行切片，与numpy/python中的情况类似
# print(df.iloc[3:5,0:2])
#                  A         B
# 2018-01-22  0.014979  1.848822
# 2018-01-23 -0.474405 -1.333422
3.3 通过指定一个位置的列表，与numpy/python中的情况类似
# print(df.iloc[[1,2,4],[0,2]])
#                   A         C
# 2018-01-20  0.225366 -0.127717
# 2018-01-21  2.062152  0.064430
# 2018-01-23 -0.474405  0.423630
3.4 对行进行切片
# print(df.iloc[1:3,:])
#                    A         B         C         D
# 2018-01-20  0.225366 -2.010948 -0.127717 -0.352816
# 2018-01-21  2.062152  1.307013  0.064430  0.866045
3.5 对列进行切片
# print(df.iloc[:,1:3])
#                    B         C
# 2018-01-19 -0.099002 -0.903149
# 2018-01-20 -2.010948 -0.127717
# 2018-01-21  1.307013  0.064430
# 2018-01-22  1.848822 -0.195405
# 2018-01-23 -1.333422  0.423630
# 2018-01-24  2.056474 -1.5990
3.6 获取特定的值
# print(df.iloc[1,1])
# 2.01094849818
# print(df.iat[1,1])
# 2.01094849818

4. 布尔索引
4.1 使用一个单独列的值来选择数据
# print(df[df.A > 0])
#                    A         B         C         D
# 2018-01-19  0.967563  0.826202 -0.659629 -1.255783
# 2018-01-21  1.222864  1.007020 -0.403161  1.219606
# 2018-01-23  0.344947  0.138564 -1.451801  1.862504
# 2018-01-24  0.142064  0.804119 -1.562833 -0.101581
4.2 使用where操作来选择数据
# print(df[df > 0])
#                    A         B   C         D
# 2018-01-19  0.967563  0.826202 NaN       NaN
# 2018-01-20       NaN       NaN NaN       NaN
# 2018-01-21  1.222864  1.007020 NaN  1.219606
# 2018-01-22       NaN       NaN NaN       NaN
# 2018-01-23  0.344947  0.138564 NaN  1.862504
# 2018-01-24  0.142064  0.804119 NaN       NaN
# df2 = df.copy()
# df2['E'] = ['one','two','three','one','two','four']
# print(df2)
#                   A         B         C         D      E
# 2018-01-19 -1.888155 -0.327337  0.927265 -1.782017    one
# 2018-01-20  0.075757  1.071116  0.299332 -0.194304    two
# 2018-01-21 -0.762645  1.139858  0.395793  1.439923  three
# 2018-01-22 -0.885407  0.361705  2.067125 -0.279005    one
# 2018-01-23 -0.255210  0.675473  1.148087 -0.144612    two
# 2018-01-24 -0.774092  1.433175  1.243407 -2.192897   four
# print(df2[df2['E'].isin(['two','four'])])
#                    A         B         C         D     E
# 2018-01-20  0.075757  1.071116  0.299332 -0.194304   two
# 2018-01-23 -0.255210  0.675473  1.148087 -0.144612   two
# 2018-01-24 -0.774092  1.433175  1.243407 -2.192897  four

4. 设置
4.1 设置一个新的列
nl = pd.Series([1,2,3,4,5,6],index = pd.date_range('20180119',periods=6))
df['F'] = nl
4.2 通过标签设置新的值
df.at[dates[0],'A'] = 0
4.3 通过位置设置新的值
df.iat[0,1] = 0
4.4 通过一个numpy数组设置一组新值
df.loc[:,'D'] = np.array([5] * len(df))
# print(df)
#                    A         B         C  D  F
# 2018-01-19  0.000000  0.000000 -0.263677  5  1
# 2018-01-20 -0.230378  0.037756 -0.590645  5  2
# 2018-01-21 -0.664824  0.840482  0.194120  5  3
# 2018-01-22  0.919228 -1.004659  0.817310  5  4
# 2018-01-23  0.013167  0.298806  1.107084  5  5
# 2018-01-24  0.072986 -0.094253  0.263455  5  6
4.5 通过where操作来设置新的值
df2 = df.copy()
df2[df2 > 0] = -df2
# print(df2)
#                    A         B         C  D  F
# 2018-01-19  0.000000  0.000000 -1.387060 -5 -1
# 2018-01-20 -0.205605 -0.393647 -0.372126 -5 -2
# 2018-01-21 -1.347434 -1.480279 -0.314913 -5 -3
# 2018-01-22 -0.642557 -0.762170 -0.703247 -5 -4
# 2018-01-23 -0.634930 -1.000218 -0.523227 -5 -5
# 2018-01-24 -0.340961 -1.349274 -0.521104 -5 -6
```

### 缺失值处理

```python
'''在pandas中，使用np.nan来代替缺失值，这些值将默认不会包含在计算中'''
import pandas as pd
import numpy as np
dates = pd.date_range('20180119',periods = 6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
1. reindex()方法可以对指定轴上的索引进行改变/增加/删除操作，这将返回原始数据的一个拷贝
df1 = df.reindex(index = dates[0:4],columns = list(df.columns)+['E'])
# print(df1)
#                    A         B         C         D   E
# 2018-01-19  1.642620 -0.395311 -1.600835 -0.859785 NaN
# 2018-01-20  0.507611  0.272737  0.752700 -0.945402 NaN
# 2018-01-21  1.388164  2.008823  0.141275  0.000459 NaN
# 2018-01-22 -0.149260  0.475242 -0.103702  0.931095 NaN
df1.loc[dates[0]:dates[1],'E'] = 1
# print(df1)
#                    A         B         C         D    E
# 2018-01-19  1.642620 -0.395311 -1.600835 -0.859785  1.0
# 2018-01-20  0.507611  0.272737  0.752700 -0.945402  1.0
# 2018-01-21  1.388164  2.008823  0.141275  0.000459  NaN
# 2018-01-22 -0.149260  0.475242 -0.103702  0.931095  NaN
2. 去掉包含缺失值的行
# print(df1.dropna(how='any'))
#                    A         B         C         D    E
# 2018-01-19 -0.482124  2.026149 -0.946748  1.085659  1.0
# 2018-01-20 -0.341300  0.004407  0.808773  0.002304  1.0
3. 对缺失值进行填充
# print(df1.fillna(value=5))
#                    A         B         C         D    E
# 2018-01-19 -0.482124  2.026149 -0.946748  1.085659  1.0
# 2018-01-20 -0.341300  0.004407  0.808773  0.002304  1.0
# 2018-01-21  0.872226 -2.001683  1.528639 -1.464248  5.0
# 2018-01-22  1.730996 -0.843465  0.711038  1.324974  5.0
4. 对数据进行布尔填充
# print(pd.isnull(df1))
#                 A      B      C      D      E
# 2018-01-19  False  False  False  False  False
# 2018-01-20  False  False  False  False  False
# 2018-01-21  False  False  False  False   True
# 2018-01-22  False  False  False  False   True
```

### 相关操作

```python
import pandas as pd
import numpy as np
dates = pd.date_range('20180119',periods = 6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
1. 统计（相关操作通常情况下不包括缺失值）
1.1 执行描述性统计
print(df.mean())
# A    0.720938
# B   -0.653084
# C   -0.748462
# D   -0.581817
# dtype: float64
1.2 在其他轴上进行相同的操作
print(df.mean(1))
# 2018-01-19    0.431505
# 2018-01-20    0.384786
# 2018-01-21   -0.040841
# 2018-01-22    0.264810
# 2018-01-23    0.180190
# 2018-01-24   -0.924237
# Freq: D, dtype: float64
1.3 对于拥有不同维度，需要对齐的对象进行操作；Pandas会自动的沿着指定的维度进行广播
s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
# print(s)
# 2018-01-19    NaN
# 2018-01-20    NaN
# 2018-01-21    1.0
# 2018-01-22    3.0
# 2018-01-23    5.0
# 2018-01-24    NaN
# Freq: D, dtype: float64
# print(df.sub(s,axis='index'))
#                    A         B         C         D
# 2018-01-19       NaN       NaN       NaN       NaN
# 2018-01-20       NaN       NaN       NaN       NaN
# 2018-01-21 -2.368813 -1.484338 -0.528546 -1.707081
# 2018-01-22 -4.079782 -2.097843 -3.377571 -1.564515
# 2018-01-23 -4.887766 -5.817630 -5.109856 -5.165325
# 2018-01-24       NaN       NaN       NaN       NaN
2. Apply
2.1 对数据在列上应用函数
print(df.apply(np.cumsum))
# cumsum 计算累加值
# 比如一个列表是这样[1,2,3,4,5]
# 返回是这样[1,3,6,10,15]
#                    A         B         C         D
# 2018-01-19  0.795920  0.014270 -0.622258 -0.348737
# 2018-01-20  0.105926  0.236074 -2.368370 -0.287449
# 2018-01-21 -1.931999  1.868371 -2.526263 -0.013665
# 2018-01-22 -0.036079  0.976260 -2.906968  0.583806
# 2018-01-23  0.296386  1.971066 -4.294293  1.715660
# 2018-01-24 -2.085994  3.238730 -6.224375  1.005203
# print(df.apply(lambda x: x.max()-x.min()))
# A    2.138003
# B    4.037926
# C    1.753592
# D    2.419793
# dtype: float64
2.2 对数据在行上应用函数
print(df.apply(lambda x: x.max()-x.min(),axis=1))
# 2018-01-19    2.374446
# 2018-01-20    1.545403
# 2018-01-21    1.709167
# 2018-01-22    2.893604
# 2018-01-23    1.162231
# 2018-01-24    3.495989
# Freq: D, dtype: float64
3. 直方图
s = pd.Series(np.random.randint(0,7,size=10))
# print(s)
# 0    5
# 1    2
# 2    6
# 3    6
# 4    3
# 5    6
# 6    2
# 7    6
# 8    3
# 9    1
# dtype: int32
print(s.value_counts())
# 4    4
# 1    2
# 6    1
# 5    1
# 2    1
# 0    1
# dtype: int64
4. 字符串方法
Series对象在其str属性中配备了一组字符串处理方法，可以很容易的应用到数组中的每个元素
s = pd.Series(['A','B',np.nan,'JAVA'])
print(s.str.lower())
# 0       a
# 1       b
# 2     NaN
# 3    java
# dtype: object
```

### 合并

```python
import pandas as pd
import numpy as np
1. Concat
df = pd.DataFrame(np.random.randn(10,4))
# print(df)
#           0         1         2         3
# 0  0.350526 -0.677201 -0.588620 -1.748650
# 1 -2.035935  0.393700 -0.011889  0.147334
# 2 -1.299210  0.176314 -0.705539 -0.008890
# 3  1.106802 -0.514109  0.478564  1.089387
# 4  0.663188  1.149408  0.053992 -0.499767
# 5 -0.821530  1.780245 -0.504094  0.268785
# 6  0.413706 -0.370817 -0.435808  0.928407
# 7 -0.170325  0.894643 -0.290098  0.123416
# 8  0.396641  0.482592  0.342057 -1.162410
# 9 -0.196543  0.326026  0.883571  0.296892
# pieces = [df[:3],df[3:7],df[7:]]
# print(pieces)
# print(pd.concat(pieces))
2. merge类似于SQL类型的join合并
left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
right = pd.DataFrame({'key':['foo','foo'],'lval':[4,5]})
# print(left)
#    key  lval
# 0  foo     1
# 1  foo     2
# print(right)
#    key  lval
# 0  foo     4
# 1  foo     5
result = pd.merge(left,right,on='key')
# print(result)
#    key  lval_x  lval_y
# 0  foo       1       4
# 1  foo       1       5
# 2  foo       2       4
# 3  foo       2       5
3. Append 将一行连接到一个DataFrame
df = pd.DataFrame(np.random.randn(6,4),columns=['A','B','C','D'])
# print(df)
#           A         B         C         D
# 0 -0.434823 -0.674820 -1.035094  0.926023
# 1  0.281293  1.075782  0.601072 -0.840849
# 2 -0.921222 -0.013399 -0.920835 -1.104292
# 3  0.544048 -0.055161 -2.655735  0.713720
# 4 -0.260426 -0.377402 -0.633011  1.394622
# 5 -0.158969  1.372356  0.202284  1.848250
s = df.iloc[3]
# print(s)
# A    0.544048
# B   -0.055161
# C   -2.655735
# D    0.713720
# Name: 3, dtype: float64
result = df.append(s,ignore_index=True)
# print(result)
#           A         B         C         D
# 0 -0.434823 -0.674820 -1.035094  0.926023
# 1  0.281293  1.075782  0.601072 -0.840849
# 2 -0.921222 -0.013399 -0.920835 -1.104292
# 3  0.544048 -0.055161 -2.655735  0.713720
# 4 -0.260426 -0.377402 -0.633011  1.394622
# 5 -0.158969  1.372356  0.202284  1.848250
# 6  0.544048 -0.055161 -2.655735  0.713720
```

### 分组

对于”group by”操作，我们通常是指以下一个或多个操作步骤：

-   （Splitting）按照一些规则将数据分为不同的组；

-   （Applying）对于每组数据分别执行一个函数；

-   （Combining）将结果组合到一个数据结构中。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
    'B':['one','one','two','three','two','two','one','three'],
    'C':np.random.randn(8),
    'D':np.random.randn(8)
})
print(df)
#      A      B         C         D
# 0  foo    one  0.144765 -0.508662
# 1  bar    one  2.772947 -0.538177
# 2  foo    two  0.139437  1.895434
# 3  bar  three  0.444667  1.374189
# 4  foo    two  0.859788 -0.241428
# 5  bar    two  0.086100  0.178261
# 6  foo    one -0.794602  0.677456
# 7  foo  three -0.989794 -0.524439
1. 分组并对每个分组执行sum函数
result = df.groupby('A').sum()
# print(result)
#             C         D
# A
# bar  3.303714  1.014273
# foo -0.640407  1.298361
2. 通过多个列进行分组形成一个层次索引，然后执行函数
result = df.groupby(['A','B']).sum()
# print(result)
#                   C         D
# A   B
# bar one    2.772947 -0.538177
#     three  0.444667  1.374189
#     two    0.086100  0.178261
# foo one   -0.649838  0.168794
#     three -0.989794 -0.524439
#     two    0.999225  1.654005
```

### Reshaping

```python
import pandas as pd
import numpy as np
1. Stack
tuples = list(zip(*[[
    'bar','bar','baz','baz',
    'foo','foo','qux','qux'],
    ['one','two','one','two',
    'one','two','one','two']]))
# print(tuples)
# [('bar', 'one'), ('bar', 'two'), ('baz', 'one'), ('baz', 'two'),
#  ('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')]
index = pd.MultiIndex.from_tuples(tuples,names=['first','second'])
# print(index)
# MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
#            labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
#            names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8,2),index=index,columns=list('AB'))
df2 = df[:4]
# print(df2)
#                      A         B
# first second
# bar   one    -0.583892  0.112302
#       two     0.423727 -0.485348
# baz   one     0.811787 -0.218276
#       two     1.684989  0.090760
stacked = df2.stack()
# print(stacked)
# first  second
# bar    one     A   -0.049549
#                B    0.207460
#        two     A    1.185503
#                B   -1.448374
# baz    one     A   -2.666536
#                B   -0.531970
#        two     A    0.384126
#                B    0.306118
# print(stacked.unstack())
#                      A         B
# first second
# bar   one    -1.049974  0.636667
#       two     2.058770 -0.228693
# baz   one    -1.354676  1.577898
#       two    -0.286151  0.434033
print(stacked.unstack(1))
# second        one       two
# first
# bar   A -0.236040 -1.909281
#       B -0.114495 -1.118122
# baz   A  0.407393 -0.836405
#       B -0.033035 -0.696890
print(stacked.unstack(0))
# first          bar       baz
# second
# one    A -0.236040  0.407393
#        B -0.114495 -0.033035
# two    A -1.909281 -0.836405
#        B -1.118122 -0.696890
```

### 时间序列

Pandas 在对频率转换进行重新采样时拥有简单、强大且高效的功能（如将按秒采样的数据转换为按 1 分钟为单位进行采样的数据

```python
import pandas as pd
import numpy as np

rng = pd.date_range('1/1/2018',periods=120,freq='S')
ts = pd.Series(np.random.randint(0,500,len(rng)),index=rng)
res = ts.resample('1Min').sum()
# print(res)
# 2018-01-01 00:00:00    14373
# 2018-01-01 00:01:00    14489
# Freq: T, dtype: int32
```

### Categorical

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"id":[1,2,3,4,5,6],
"raw_grade":['a','b','b','a','a','e']})
# print(df)
#    id raw_grade
# 0   1         a
# 1   2         b
# 2   3         b
# 3   4         a
# 4   5         a
# 5   6         e
1. 将原始的grade转换为Categorical数据类型
df['grade'] = df["raw_grade"].astype('category')
# print(df['grade'])
# 0    a
# 1    b
# 2    b
# 3    a
# 4    a
# 5    e
# Name: grade, dtype: category
# Categories (3, object): [a, b, e]
2. 将Categorical类型数据重命名为更有意义的名称
df['grade'].cat.categories = ['very good','good','very bad']
# print(df['grade'])
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5     very bad
# Name: grade, dtype: category
# Categories (3, object): [very good, good, very bad]
3. 对类别进行重新排序，增加缺失的类别
df['grade'] = df['grade'].cat.set_categories(['very bad','bad','medium','good','very good'])
# print(df['grade'])
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5     very bad
# Name: grade, dtype: category
# Categories (5, object): [very bad, bad, medium, good, very good]
4. 排序是按照Categorical的顺序进行的而不是按照字典顺序进行
res = df.sort_values(by = 'grade')
# print(res)
#    id raw_grade      grade
# 5   6         e   very bad
# 1   2         b       good
# 2   3         b       good
# 0   1         a  very good
# 3   4         a  very good
# 4   5         a  very good
5. 对Categorical列进行排序时存在空的类别
res = df.groupby('grade').size()
# print(res)
# grade
# very bad     1
# bad          0
# medium       0
# good         2
# very good    3
# dtype: int64
```

### 画图

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

df = pd.DataFrame(np.random.randn(1000,4),index=ts.index,
                  columns=['A','B','C','D'])
df = df.cumsum()
plt.figure();df.plot();plt.legend(loc='best');plt.show()
```

![figure](python-pandas/figure.png)

### 导入和保存数据

```python
import pandas as pd
import numpy as np
dates = pd.date_range('20180119',periods = 6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
1. 写入csv文件
df.to_csv('foo.csv')
2. 从csv文件中读取
rdf = pd.read_csv('foo.csv')
# print(rdf.head())
#    Unnamed: 0         A         B         C         D
# 0  2018-01-19 -0.493852  1.111875 -1.274353  1.253351
# 1  2018-01-20 -0.955214 -0.874248  0.497260  1.422481
# 2  2018-01-21  0.990284  0.236732 -0.216565 -0.391593
# 3  2018-01-22 -1.669639  0.388650  0.729114  0.553893
# 4  2018-01-23  0.108748 -1.347310 -1.346028 -1.075332
# pip install tables==3.3.0
1. 写入HDF5存储
df.to_hdf('foo.h5','df')
2. 从HDF5存储中读取
rdf = pd.read_hdf('foo.h5','df')
# print(rdf.head())
#                    A         B         C         D
# 2018-01-19 -0.012467  0.795258  0.317056  2.658598
# 2018-01-20  0.199918 -0.404888  0.882677  1.460073
# 2018-01-21 -1.454304 -0.261921 -0.247211  0.874749
# 2018-01-22 -0.620360 -0.835549 -0.307428  2.102838
# 2018-01-23 -1.901853 -0.237466 -0.241624  0.899364
# pip install openpyxl
1. 写入excel文件
df.to_excel('foo.xlsx',sheet_name='Sheet1')
2. 从excel文件中读取
rdf = pd.read_excel('foo.xlsx','Sheet1',index_col=None,na_values=['NA'])
# print(rdf.head())
#                   A         B         C         D
# 2018-01-19 -0.721516  1.137682 -0.302877 -0.494486
# 2018-01-20  0.365947  1.494965  0.241657 -0.300226
# 2018-01-21  0.522483  1.195972 -0.403275 -0.882628
# 2018-01-22 -0.556909  0.877889 -0.218577  1.026033
# 2018-01-23  0.459684 -0.896963  1.271079 -2.797635
```

> 引用: https://www.cnblogs.com/chaosimple/p/4153083.html
