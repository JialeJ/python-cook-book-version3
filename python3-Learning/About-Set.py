# 集合（set）是一个无序的不重复元素序列。因此在每次运行的时候集合的运行结果的内容都是相同的，但元素的排列顺序却不是固定的
## 无序：无法用数字下标索引；
## 不重复： 可用于序列元素去重。

"""
函数	功能
len()	        计算序列的长度，即返回序列中包含多少个元素。
max()	        找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，
              不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。
min()	        找出序列中的最小元素。
list()	      将序列转换为列表。
str()	        将序列转换为字符串。
sum()	        计算元素和。
sorted()	    对元素进行排序，默认为正。
reversed()	  反向序列中的元素。
enumerate()	  将序列组合为一个索引序列，多用在 for 循环中。
 部分序列不能应用其中的部分函数，比如字典中不能直接使用list，详细的函数介绍请参阅相应数据类型的函数介绍。
 """

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)  # 这里演示的是去重功能
{'orange', 'banana', 'apple', 'pear'}
>>> print('organe' in basket)
False
>>> print('crabgrass' in basket)
False
>>> print('orange' in basket)
True
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> print(a)
{'r', 'b', 'c', 'a', 'd'}
>>> print(b)
{'c', 'a', 'z', 'l', 'm'}
>>> print(a-b)
{'b', 'd', 'r'}
>>> a.difference(b)
{'b', 'd', 'r'}
>>> print(a|b)
{'r', 'b', 'c', 'a', 'd', 'z', 'l', 'm'}
>>> a.intersection(b)
{'c', 'a'}
>>> a.union(b)
{'r', 'b', 'c', 'a', 'd', 'z', 'l', 'm'}
>>> a & b
{'c', 'a'}
>>> print(a^b)
{'z', 'l', 'r', 'd', 'b', 'm'}
>>> c = {x for x in a if x not in 'abc'}
>>> c
{'d', 'r'}
>>> thisset = set(("Google", "W3Cschool", "Taobao")) 
thisset.add('Baidu')
>>> print(thisset)
{'W3Cschool', 'Baidu', 'Taobao', 'Google'}
>>> thisset.update({1,3})
>>> thisset
{1, 3, 'Google', 'W3Cschool', 'Baidu', 'Taobao'}
>>> thisset.update((1,3),[2,4])
>>> thisset
{1, 2, 3, 4, 'Google', 'W3Cschool', 'Baidu', 'Taobao'}
>>> thisset.remove("Taobao")
>>> thisset
{1, 2, 3, 4, 'Google', 'W3Cschool', 'Baidu'}
>>> thisset.discard(1)
>>> thisset
{2, 3, 4, 'Google', 'W3Cschool', 'Baidu'}
>>> thisset.discard(1)
>>> thisset
{2, 3, 4, 'Google', 'W3Cschool', 'Baidu'}
>>> thisset.pop()
2
>>> thisset.pop(3)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    thisset.pop(3)
TypeError: pop() takes no arguments (1 given)
>>> thisset.clear()
>>> thisset
set()
>>> thisset == None
False
>>> a
{'r', 'b', 'c', 'a', 'd'}
>>> b
{'c', 'a', 'z', 'l', 'm'}
>>> c
{'d', 'r'}
>>> d = c.copy()
>>> d
{'d', 'r'}
>>> a.difference((b,c))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.difference((b,c))
TypeError: unhashable type: 'set'
>>> a.difference(b,c )
{'b'}
>>> a[1]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a[1]
TypeError: 'set' object is not subscriptable
>>> a['1']
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a['1']
TypeError: 'set' object is not subscriptable
  
"""
a.add(x)	        为集合添加元素
a.clear()	      移除集合中的所有元素
b = a.copy()	      拷贝一个集合
a.difference(b)	返回多个集合的差集 s1 - s2
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
a.discard(x)  	      删除集合中指定的元素
a.intersection(b)	    返回集合的交集 s1 & s2
intersection_update()	返回集合的交集。
a.isdisjoint(b)	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	  判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
a.pop()	        随机移除元素
a.remove(x)	    移除指定元素
symmetric_difference()	        返回两个集合中不重复的元素集合。
symmetric_difference_update()	  移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
a.union(b)	      返回两个集合的并集 s1 | s2
a.update(x)	    给集合添加元素
"""
