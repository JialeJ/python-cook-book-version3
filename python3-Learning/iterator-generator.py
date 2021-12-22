"""
https://www.w3cschool.cn/python3/python3-iterator-generator.html
"""

"""
迭代器iterator

迭代是 Python 最强大的功能之一，是访问集合元素的一种方式。。
迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：
"""

list1 = [1,2,3,4]
it = iter(list1)
print(next(it))   # 输出迭代器的下一个元素
for i in it:
    print(i, end='\t')
