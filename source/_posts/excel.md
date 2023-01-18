---
title: Excel Basic
tag: excel
categories: manual
date: 2021-04-25
---

## 常用技巧

### 移动和选择

| Key                     | Meaning                |
| :---------------------- | ---------------------- |
| `TAB`                   | 跳到本行下一个单元格   |
| `SHIFT TAB`             | 跳到本行上一个单元格   |
| `ENTER`                 | 跳到本列下一个单元格   |
| `SHIFT ENTER`           | 跳到本列下一个单元格   |
| `CTRL + 方向键`         | 跳到指定方向的边界     |
| `SHIFT + 方向键`        | 选择指定方向一个单元格 |
| `CTRL + SHIFT + 方向键` | 选择到指定方向边界     |

### 拖动

鼠标左键栏位边缘呈现十字箭头拖动。

-   拖动复制：CTRL+ 鼠标左键十字箭头。
-   拖动插入：SHIFT + 鼠标左键十字箭头。

### 调整栏宽行高

鼠标放至栏位分隔线处出现 `<-|->`

- 调整单个栏宽至内容宽度：`<-|-> ` 单击鼠标左键。

- 调整所有栏宽至内容宽度：选择所有栏，`<-|->` 单击鼠标左键。如果栏宽没有调整到内容的宽度，需要注意是否开启了自动换行。

  ![](excel/1662025467649.png)

-   调整所有栏宽至相同宽度：选择所有栏，`<-|->`鼠标左键拖动。

### 快速插入多个空行

-   右键插入空行，然后 F4 重复上次操作。
-   选择多行，然后右键插入。

### 重复填充

选择需要重复填充的源和待填充的行， 执行 `CTRL + D` 。

| Initial                                   | Result                                    |
| ----------------------------------------- | ----------------------------------------- |
| ![1641454418471](excel/1641454418471.png) | ![1641454453915](excel/1641454453915.png) |

### 跨行复制

按住 `CTRL`，鼠标选择要复制的行，然后 `CTRL + C` 复制。

### 单元格内换行

`ALT + ENTER`

### 批注

右键 => 插入批注 => 右键批注设置格式

### F4 相对应用变绝对引用

`A1 => $A$1`

### F9 刷新公式

### 从下拉列表中选择

鼠标右键 => 从下拉列表中选择

![](excel/1619329395586.png)

### 选择性粘贴 转置

复制数据 => 选择性粘贴 => 勾选转置

### 选择性粘贴 运算

所有英文成绩加 5

复制数据 5 => 选择性粘贴 => 选择需要运算区域 => 勾选运算 **加**

### 模拟分析

已知国语，数学，英文成绩，计算英文达到多少平均值才能达到 60

数据 => 模拟分析 => 单变量求解

![](excel/1619329611722.png)

![](excel/1619329691785.png)

### 表格对角线

1. 绘图边框

    选择绘图边框，沿着对角线绘制

    ![](excel/1619329837509.png)

2. 右键单元格格式 => 边框

    ![](excel/1619329920228.png)

### 向右补充空格到指定长度

`LEFT("AAAA"&REPT(" ", 5), 5)` => "AAAA "

## 数据分列

数据 => 分列

1. 先根据空格分列
2. 姓名根据宽度分为姓和名

![](excel/1619333908325.png)

![](excel/1619333874816.png)

案例：将 students.txt 转换为 excel 格式, 并且 `001` 保留原有的格式。

```csv
id|name|age
001|babb|28
002|julian|30
003|owen|40
```

1. 选择待分列的列(A 列)，点击数据 -> 分列，合适的文件类型中选择分隔符号。

    ![1629871207427](excel/1629871207427.png)

2. 选择分隔符号，可以勾选其他，手动填写分隔符号，这里使用 `|`。

![1629870555192](excel/1629870555192.png)

3. 设置列的数据类型，这里将 id，name 设置为文本格式，可以 Shift 点选, 需要选择所有列使用 CTRL + A.

![1629871012544](excel/1629871012544.png)

4. 文件另存为 xlsx.

![1629871285323](excel/1629871285323.png)

## 打印预览

默认 Excel 打印不会显示网格綫, 勾选打印网格綫, 会打印默认的虚綫格式

![](excel/1619330076738.png)

如果需要其它类型网格綫使用网格綫工具

![](excel/1619330092382.png)

## 打印设定

视图 => 分页预览 调整分页符到合适的位置

![](excel/1619331077141.png)

页面布局 => 打印标题 进行页眉页脚，顶端标题行设置

![](excel/1619331270249.png)

![](excel/1619331381373.png)

![](excel/1619331458759.png)

打印预览

![](excel/1619331615197.png)

## 冻结窗格，分隔视窗

视图 => 冻结窗格

视图 => 分隔视窗

行, 列同时冻结需要选择行和列交叉処

![](excel/1619330145698.png)

## 创建组

数据 => 创建组

![](excel/1619330254865.png)

## 复制非隐藏内容

1. 开始 => 查找 => 定位

![](excel/1619330339372.png)

1. 选择可见单元格 => 定位 然后复制区域

![](excel/1619330326199.png)

## 排序

数据 => 排序 可以自订清单(自定义序列)

![](excel/1619330359331.png)

## 数据筛选

数据 => 自动筛选

自动筛选也可以根据颜色筛选和排序

![](excel/1619330504026.png)

## 格式化表格(表格样式)

-   方式一: 开始 => 格式化为表格 (表格样式)

-   方式二: 插入 => 表格

    格式化的表格可以使用汇总行

![](excel/1619330569238.png)

## 条件格式

开始 => 条件格式

![](excel/1619330670527.png)

## 合并计算

数据 => 合并计算

可以将分布在不同表格中的季度数据合并

![](excel/1619330723950.png)

## 数据透视表

数据 => 数据透视表

## 保护工作表

CTRL + 1 设定公式单元格 锁定(保护工作表后不可更改) + 隐藏(保护工作表后公式不可见)

![](excel/1619340356193.png)

取消保护工作表后可以修改单元格的锁定

![](excel/1619340615319.png)

审阅 => 允许用户编辑区域

保护工作表之后用户可以通过输入区域密码对允许编辑区域进行修改

![](excel/1619340927978.png)

审阅 => 保护工作表

![](excel/1619340736107.png)

## IF

![](excel/1619331804427.png)

## VLOOKUP

`VLOOKUP(查找值, 数据表, 列序数, [匹配条件])`

成绩:`=VLOOKUP(J3,$M$2:$N$7,2,TRUE)` TRUE 表示模糊匹配

![](excel/1619331982085.png)

姓名:`=VLOOKUP($C$3,$E$2:$K$12,2,FALSE)`
总平均:`=VLOOKUP($C$3,$E$2:$K$12,6,FALSE)`
成绩:`=VLOOKUP($C$3,$E$2:$K$12,7,FALSE)` FALSE 代表精确匹配，7 代表取第七列数据（从 1 开始）

![](excel/1619332234222.png)

## HLOOKUP

![](excel/1619332589201.png)

## IFERROR

姓名 `IF(C3="","",IFERROR(VLOOKUP($C$3,$E$2:$K$12,2,FALSE),"查无此人"))`

如果学号为空，姓名显示为空；如果学号在列表中不存在，显示`查无此人`

![](excel/1619332650461.png)

这里也可以对学号进行数据有效性验证，不在验证范围内的学号提示错误

![](excel/1619332859406.png)

![](excel/1619332898848.png)

![](excel/1619332922938.png)

## COUNTIF、COUNTIFS

COUNTIFS 可以指定多个条件

SUMIFS 需要先指定一个求和区域

![](excel/1619333348223.png)

## COUNTIF 标识重复

![](excel/1619335602916.png)

## 名称设定

![](excel/1619333521003.png)

## INDIRECT

![](excel/1619333572173.png)

### INDIRECT 实现下拉选单

![](excel/1619333630046.png)

公式 => 指定 => 根据范围指定名称

![](excel/1619333661319.png)

定位到餐点名称 数据 => 数据有效性

![](excel/1619333688847.png)

## 数值格式

| CTRL + 1 设置单元格格式                                                              |
| ------------------------------------------------------------------------------------ |
| # 一个位数的预留位置, 无意义的 0 会被省略 82.56 #.# => 82.6                          |
| ？一个位数的预留位置, 无意义的 0 会被空格代替 "90" #.? => "90. "                     |
| 0 强制显示每一个指定的位数, 90 #.00 => 90.00                                         |
| @ 单元格内的文字, 甲 @"等" => 甲等                                                   |
| _ 重复指定的符号直到填满储存格 简介 @_. => 简介...................... wps not valid? |
| , 千分位 1000000 0,,"M" => 1M                                                        |
| \_ 以后面的符号的宽度增加留白                                                        |
| 特殊语法: 正值格式;负值格式;零值格式;文本格式 0.00;(0.00);0.00;@                     |
| 0.00[红色];(0.00)[绿色];0.00[蓝色];@[黄色]                                           |

## DATEDIFF

![](excel/1619334996147.png)

## NETWORKDAYS

`NETWORKDAYS(开始日期, 终止日期, [指定假期])`
`NETWORKDAYS.INTL(开始日期, 终止日期, [周末], [指定假期])1`

![](excel/1619335027500.png)

## TODAY、NOW

![](excel/1619334523833.png)

## RANK.EQ

RANK.EQ(数值,引用区域,[排位方式])

排位方式: 1 模糊排位, 0 精确匹配(默认)

![](excel/1619334942810.png)

## LEFT、MID、RIGHT

![](excel/1619334907151.png)

## INDEX、MATCH

![](excel/1619335150024.png)

### 等第

![](excel/1619335294024.png)

### 考绩

![](excel/1619335396601.png)

## RANDBETWEEN

![](excel/1619335662528.png)

## CHOOSE

![](excel/1619335816075.png)

## RAND

![](excel/1619335909013.png)

## RANK

![](excel/1619336030807.png)

## OR、AND

![](excel/1619336177787.png)

## SUMPRODUCT

![](excel/1619336227870.png)

![](excel/1619336302138.png)

## PARETO CHART

按住 CTRL 键，选择投诉内容、投诉次数、累计百分比 => 图表 => 组合图 => 折线图使用次坐标轴

![](excel/1619336608650.png)

设置坐标轴相关属性

![](excel/1619336953756.png)

## 学生成绩表

| 学号 | 姓名   | 国文 | 数学 | 英文 | 总平均 | 成绩 |
| ---- | ------ | ---- | ---- | ---- | ------ | ---- |
| 101  | 刘明哲 | 65   | 85   | 72   | 74     | C    |
| 102  | 黄雅婷 | 78   | 30   | 66   | 58     | E    |
| 103  | 蔡宜芳 | 84   | 61   | 50   | 65     | D    |
| 104  | 陈翰松 | 100  | 60   | 59   | 73     | C    |
| 105  | 戴育如 | 98   | 74   | 80   | 84     | B    |
| 106  | 汪贞仪 | 35   | 64   | 27   | 42     | E    |
| 107  | 李承航 | 86   | 37   | 30   | 51     | E    |
| 108  | 林淑慈 | 82   | 69   | 50   | 67     | D    |
| 109  | 张淑卿 | 99   | 100  | 86   | 95     | A    |
| 110  | 吴芊菱 | 90   | 85   | 80   | 85     | B    |

## 宏

开发工具 => 录制新宏

![](excel/1619339242436.png)

宏 => 选择要执行的宏

单步执行可以进行调试

![](excel/1619339504619.png)

## VBA

### Variable、Const

```vb
Option Explicit

Sub Variable()
'    Dim Score As Integer
'    Score = 100
'    MsgBox Score
'
'    Dim Price As Double
'    Price = 9.6
'    MsgBox Price
'
'    Dim Birthday As Date
'    Birthday = #4/23/2021#
'    MsgBox Birthday

'
'    Dim Message As String
'    Message = "Hello, World!"
'    MsgBox Message
'
'    Dim Pass As Boolean
'    Pass = True
'    MsgBox Pass

'    Dim Score As Integer, Price As Double
'    MsgBox Score
'    MsgBox Price
'
'    Dim var
'    var = 10
'    MsgBox var
'    var = #4/24/2021#
'    MsgBox var

'    MsgBox Scoe  'Option Explicit variable not defined

End Sub

Sub StaticCount()
    Static Count As Integer

    Count = Count + 1

    MsgBox Count
End Sub


Sub Constant()

    Const PI As Double = 3.14

    Dim Area As Double

    Area = PI * 2 * 2

    MsgBox Area

    'vbRed 内置常量
    ActiveCell.Interior.Color = vbRed

End Sub
```

### Select Case

```vb
Sub SelectCase()

    Dim Score As Integer

    Score = 100

    Select Case Score
        Case Is >= 90
            MsgBox "good"
        Case Is >= 70
            MsgBox "normal"
        Case Else
            MsgBox "bad"
    End Select
End Sub
```

### Loop

```vb
Sub ForLoop()

    Dim Num As Integer
    Dim Total As Integer

    For Num = 1 To 100 Step 2
        If Num > 50 Then
            Exit For
        End If

        Total = Total + Num

        Next Num

    MsgBox Total
End Sub


Sub DoWhile()

    Dim Num As Integer
    Dim Total As Integer

    Do While Num <= 100
        Total = Total + Num
        Num = Num + 1
    Loop

    MsgBox Total
End Sub


Sub DoUntil()

    Dim Num As Integer
    Dim Total As Integer

    Do Until Num > 100
        Total = Total + Num
        Num = Num + 1
    Loop

    MsgBox Total
End Sub
```

### Array

```vb
Sub ArrayTest()
    Dim MyArray(1 To 3) As Integer
'    Dim MyArray(3) As Integer  3 代表最大下标，最小默认为 0, Option Base 1 可以指定最小下标为 1

    MyArray(1) = 1
    MyArray(2) = 2
    MyArray(3) = 3

    Dim Index As Integer

'    For Index = 1 To 3
'        MsgBox MyArray(Index)
'        Next Index


    For Index = LBound(MyArray) To UBound(MyArray)
        MsgBox MyArray(Index)
        Next Index
End Sub


Sub DoubleDimensionArrayTest()
    Dim MyArray(1 To 2, 1 To 3) As Integer

    MyArray(1, 1) = 11
    MyArray(1, 2) = 12
    MyArray(1, 3) = 13

    MyArray(2, 1) = 21
    MyArray(2, 2) = 22
    MyArray(2, 3) = 23

    Dim Row As Integer, Col As Integer

    For Row = LBound(MyArray, 1) To UBound(MyArray, 1)
        For Col = LBound(MyArray, 2) To UBound(MyArray, 2)
            MsgBox MyArray(Row, Col)
            Next Col
        Next Row
End Sub


Sub DynamicArrayTest()

    Dim MyArray() As Integer

    ReDim MyArray(1 To 3)
    MyArray(1) = 1
    MyArray(2) = 2
    MyArray(3) = 3


    Dim Index As Integer
    For Index = LBound(MyArray) To UBound(MyArray)
        MsgBox MyArray(Index)
        Next Index

    ReDim MyArray(1 To 2, 1 To 3) As Integer
    MyArray(1, 1) = 11
    MyArray(1, 2) = 12
    MyArray(1, 3) = 13

    MyArray(2, 1) = 21
    MyArray(2, 2) = 22
    MyArray(2, 3) = 23

    Dim Row As Integer, Col As Integer

    For Row = LBound(MyArray, 1) To UBound(MyArray, 1)
        For Col = LBound(MyArray, 2) To UBound(MyArray, 2)
            MsgBox MyArray(Row, Col)
            Next Col
        Next Row

End Sub
```

### Object Hirerarchy

```vb
Sub ObjectHierarchy()
'    Application.Workbooks("Excel.xlsm").WorkSheets("VBA").Range("A6").Value = 6
    Range("A6").Value = 66
'    Range("A6").Clear
    MsgBox Worksheets("VBA").Name
'    Worksheets.Add
End Sub
```

### Cell Reference

```vb
Sub CellRefTest()
    Range("A1").Value = 1

    Range("A1, A2, A3").Value = 2

    Range("A1:A3").Value = 3

    Range("A1:A3, C1:C3").Value = 4

    Range("test").Value = 5 ' 引用单元格名称

    Range("10:10").Value = 6

    Range("D:D").Value = 7

    Range("11:11, 13:13").Value = 8

    Range("E:E, G:G").Value = 9

    Rows("14:16").Value = 10

    Columns("H:J").Value = 11
End Sub


Sub CellRefTest2()
    Cells(1, 1).Value = 1

    Range(Cells(1, 1), Cells(2, 2)).Value = 2

    ' 引用区域中的单元格
    Range("A3:B4").Cells(2, 2).Value = 3

    Range("A3").Offset(2, 2).Value = 4

    Range("C5").Offset(-2, -2).Value = 5


End Sub


Sub CellRefTest3()
    Range("A1").Select
    Range("A1:B2").Select

    Range("A1").Activate
    Range("A1:B2").Activate

    Range("A1:B2").Select
    Range("B2").Activate

    Selection.Value = 1
    ActiveCell.Value = 2
End Sub


Sub CellRefTest4()
    Rnge("A1").End(xlDown).Select 'CTRL + 向下方向键
    Range("A2").End(xlUp).Select

    Range("A1").End(xlToRight).Select
    Range("B1").End(xlToLeft).Select

    Range("A1").End(xlToRight).End(xlDown).Select
End Sub
```

### Function

```vb
Function Concat(rng As Range, Optional sep As String = "") As String
    Dim cell As Range

    For Each cell In rng
        Concat = Comcat & cell.Value & sep
    Next cell

    Concat = Left(Comcat, Len(Comcat) - Len(sep))

End Function
```

### Hide Column

```vb
Sub HideColumn()
  Dim sheet As Worksheet

  For Each sheet In ActiveWorkbook.Sheets
     sheet.Columns("A:F").EntireColumn.Hidden = True
     sheet.Columns("O:T").EntireColumn.Hidden = True
  Next

End Sub
```

### Combine Sheet

```vb
Sub Combine()
    Dim beginRow As Integer
    Dim sheet As Worksheet
    Dim rowCount As Integer
    Dim combineSheetName As String

    combineSheetName = "Combined"

    On Error Resume Next
    Sheets(1).Select
    Worksheets.Add ' Add a sheet in first place
    Sheets(1).Name = combineSheetName

    ' Copy header
    Sheets(2).Activate
    Range("A1").EntireRow.Select
    Selection.Copy Destination:=Sheets(1).Range("A1")

    For Each sheet In ActiveWorkbook.Sheets
        If sheet.Name <> "Combined" Then

            Application.GoTo Sheets(sheet.Name).[A1]
            Selection.CurrentRegion.Select
            Selection.Offset(1, 0).Resize(Selection.Rows.Count - 2).Select ' Don't copy header and last line
            rowCount = Selection.Rows.Count 'Actual copy rowCount

            If beginRow = 0 Then
               Selection.Copy Destination:=Sheets("Combined").Cells(2, 1)
               beginRow = beginRow + 1 + rowCount ' 1 represent header count
            Else
               Selection.Copy Destination:=Sheets("Combined").Cells(beginRow, 1)
               beginRow = beginRow + rowCount
            End If

        End If
    Next

    ActiveWorkbook.Sheets(combineSheetName).Activate
    Range("A1").EntireRow.Select
    Selection.CurrentRegion.Select
End Sub
```

### Debug

1. 在需要天使程式关注点左侧打上断点
2. 点击运行
3. 点击 Debug 选择调试方式。

![](excel/1626945989638.png)

![](excel/1626946187211.png)

## 其它

### CSV

以 `,` 分隔的 `.csv` 文件可以通过 excel 直接打开；以 `tab` 分隔的 csv 将文件名重命名为`.xls/.xlsx` 可以通过 wps excel（office 未知） 直接打开。

以 `,` 分隔的 `.csv` 虽然可以直接使用 excel 开启，不过对一些特殊的符号需要进行简单的处理，例如 `="007", =007, 007` 在 excel 中的显示分别是 `007, =007, 7`

| reason                    |            csv            |             xlsx             |
| :------------------------ | :-----------------------: | :--------------------------: |
| 显示逗号                  |     "Taipei, Taiwan"      |        Taipei, Taiwan        |
| 显示双引号                |         "12'30"""         |            12’30"            |
| 显示数字或字符串前面的 00 |          ="007"           |     ="007" （显示 007）      |
| 使用 excel 公式           | =SUM(B2:B5)/"=SUM(B2:B5)" |   =SUM (B2:B5) （显示和）    |
| 双引号前后有空格          | `A, "B,C",D` `A,"B,C" ,D` | ![](excel/1575011576909.png) |
