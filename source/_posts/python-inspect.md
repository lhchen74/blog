---
title: Python Inspect
tags: python
date: 2020-10-31
---

### 测试

```python
import inspect


def a(a, b=0, *c, d, e=1, **f):
    pass


aa = inspect.signature(a)
print("inspect.signature(fn)是: %s" % aa)
print("inspect.signature(fn)的类型是: %s" % (type(aa)))
print("\n")

bb = aa.parameters
print("signature.paramerters属性是: %s" % bb)
print("signature.paramerters属性的类型是: %s" % type(bb))
print("\n")


for cc, dd in bb.items():
    print("mappingproxy.items()返回的两个值分别是：%s和%s" % (cc, dd))
    print("mappingproxy.items()返回的两个值的类型分别是：%s和%s" % (type(cc), type(dd)))
    print("\n")
    ee = dd.kind
    print("Parameter.kind属性是: %s" % ee)
    print("Parameter.kind属性的类型是: %s" % type(ee))
    print("\n")
    gg = dd.default
    print("Parameter.default的值是: %s" % gg)
    print("Parameter.default的属性是: %s" % type(gg))
    print("\n")

ff = inspect.Parameter.KEYWORD_ONLY
print("inspect.Parameter.KEYWORD_ONLY的值是: %s" % ff)
print("inspect.Parameter.KEYWORD_ONLY的类型是: %s" % type(ff))
```

### 输出

inspect.signature(fn)是: (a, b=0, \*c, d, e=1, \*\*f)
inspect.signature(fn)的类型是: <class 'inspect.Signature'>

signature.paramerters 属性是: OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b=0">), ('c', <Parameter "*c">), ('d', <Parameter "d">), ('e', <Parameter "e=1">), ('f', <Parameter "**f">)])
signature.paramerters 属性的类型是: <class 'mappingproxy'>

mappingproxy.items()返回的两个值分别是：a 和 a
mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>

Parameter.kind 属性是: POSITIONAL_OR_KEYWORD
Parameter.kind 属性的类型是: <enum '\_ParameterKind'>

Parameter.default 的值是: <class 'inspect.\_empty'>
Parameter.default 的属性是: <class 'type'>

mappingproxy.items()返回的两个值分别是：b 和 b=0
mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>

Parameter.kind 属性是: POSITIONAL_OR_KEYWORD
Parameter.kind 属性的类型是: <enum '\_ParameterKind'>

Parameter.default 的值是: 0
Parameter.default 的属性是: <class 'int'>

mappingproxy.items()返回的两个值分别是：c 和\*c
mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>

Parameter.kind 属性是: VAR_POSITIONAL
Parameter.kind 属性的类型是: <enum '\_ParameterKind'>

Parameter.default 的值是: <class 'inspect.\_empty'>
Parameter.default 的属性是: <class 'type'>

mappingproxy.items()返回的两个值分别是：d 和 d
mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>

Parameter.kind 属性是: KEYWORD_ONLY
Parameter.kind 属性的类型是: <enum '\_ParameterKind'>

Parameter.default 的值是: <class 'inspect.\_empty'>
Parameter.default 的属性是: <class 'type'>

mappingproxy.items()返回的两个值分别是：e 和 e=1
mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>

Parameter.kind 属性是: KEYWORD_ONLY
Parameter.kind 属性的类型是: <enum '\_ParameterKind'>

Parameter.default 的值是: 1
Parameter.default 的属性是: <class 'int'>

mappingproxy.items()返回的两个值分别是：f 和\*\*f
mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>

Parameter.kind 属性是: VAR_KEYWORD
Parameter.kind 属性的类型是: <enum '\_ParameterKind'>

Parameter.default 的值是: <class 'inspect.\_empty'>
Parameter.default 的属性是: <class 'type'>

inspect.Parameter.KEYWORD_ONLY 的值是: KEYWORD_ONLY
inspect.Parameter.KEYWORD_ONLY 的类型是: <enum '\_ParameterKind'>

### 总结

1. inspect.signature（fn)将返回一个 inspect.Signature 类型的对象，值为 fn 这个函数的所有参数

2. inspect.Signature 对象的 paramerters 属性是一个 mappingproxy（映射）类型的对象，值为一个有序字典（Orderdict)。这个字典里的 key 是即为参数名，str 类型，这个字典里的 value 是一个 inspect.Parameter 类型的对象

3. inspect.Parameter 对象的 kind 属性是一个\_ParameterKind 枚举类型的对象，值为这个参数的类型（可变参数，关键词参数，etc）

-   a: POSITIONAL_OR_KEYWORD
-   b: POSITIONAL_OR_KEYWORD
-   c: VAR_POSITIONAL
-   d: KEYWORD_ONLY 在可变参数(包裹位置)后面的只能是仅限关键字参数和可变参数(包裹关键字)
-   e: KEYWORD_ONLY
-   f: VAR_KEYWORD

4. inspect.Parameter 对象的 default 属性：如果这个参数有默认值，即返回这个默认值，如果没有，返回一个 inspect.\_empty 类。
