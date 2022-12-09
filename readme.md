# python笔记

## 位运算

与C语言一致



## assert断言

与C语言一样

`a = 6
b =int(input("a test"))
assert b != 0
print(a / b)`



## enumerate()函数

##### enumerate(list, (start = i))

既返回索引值，又返回列表里的内容

`alist = [a,b,c,d]`

`enumerate(alist, start = 2)`

`#从第二个开始返回`



## try, expect, raise



```python
try:
    检测范围
except:
    出现异常后的处理代码
finally:
	except没截住的else
else:
    如果没有异常执行这块代码
```

raise the_type_of_error("显示报错原因")



## 列表的几种方法

#### 列表的常用操作符

等号操作符：`==`

连接操作符 `+`

重复操作符 `*`

成员关系操作符 `in、not in`

#### list.count(obj)

统计某个元素在列表中出现的次数

#### list.index(x[, start[, end]])

返回从start到end的第一个x的索引

若无，会报错

#### list.reverse()

反向列表中元素

#### list.sort(key=None, reverse=False)

 对原列表进行排序

reverse = True 降序， reverse = False 升序

key = None 可忽略，也可自定义函数



## 元组不可更改



## 字符串

##### capitalize() 将字符串的首个字符转换为大写

##### swapcase() 将字符串中大写转换为小写，小写转换为大写。

##### endswith(str, beg=0, end=len(string))  or startswith(substr, beg=0,end=len(string))

检查字符串是否以指定子字符串 str 结束(开始)

##### find(str, beg=0, end=len(string)) or refind(str, beg=0, end=len(string))

字面意思，一左一右

##### strip([chars])在字符串上执行lstrip()和rstrip()

##### strip().partition(sub) and strip().rpartition(sub)

找到子字符串sub，把字符串分为一个三元组

##### replace(old, new [, max])

 将字符串中的old替换成new，如果max指定，则替换不超过max次

##### center

```python
str.center(width[, fillchar])
```



## 字典

如何快速判断一个数据类型 `X` 是不是可变类型的呢？两种方法：

- 麻烦方法：用 `id(X)` 函数，对 X 进行某种操作，比较操作前后的 `id`，如果不一样，则 `X` 不可变，如果一样，则 `X` 可变。
- 便捷方法：用 `hash(X)`，只要不报错，证明 `X` 可被哈希，即不可变，反过来不可被哈希，即可变。

##### dict.setdefault(key, default=None)

返回指定键的值，将会添加键并将值设为默认值。



## 集合

##### set.add(elmnt) or set.update(set)

用于给集合添加元素

##### set.remove(item)

用于移除集合中的指定元素

##### set.discard(value)

不会报错

##### `set1 & set2` 

返回两个集合的交集

#####  ##### set.union(set1, set2)  or set1 | set2

返回两个集合的并集。

set.difference(set) and set1 - set2

##### set.symmetric_difference ^

异或

##### set.issubset(set1)  <=

判断set是不是set1的子集

issuperset(set)  >= 反之

##### set.isdisjoint(set) 

用于判断两个集合是不是不相交，如果是返回 True，否则返回 False。

#### 互相转化

list, set, tuple


## zip and *zip

合并及拆开



### tip:

while 可以和 else













