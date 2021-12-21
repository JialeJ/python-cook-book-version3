"""
url: https://www.w3cschool.cn/youshq/q71zhozt.html
"""

##  问题
### 如果一个可迭代对象的元素个数超过变量个数时，会出现”太多解压值”的异常。那么怎样才能从这个可迭代对象中解压出N个元素出来？


## 解决方案
### Python的 *星号表达式* 可以用来解决这个问题。 >>> 星号表达式返回类型一定是列表
### 比如，你在学习一门课程，在学期末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。
### 如果只有四个分数，你可能就直接去简单的手动赋值，但如果有24个呢？这时候星号表达式就派上用场了：
def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

# 星号表达式同样也能用在列表的开始或者结尾的部分


### 小练习
r1 = {"name":"Tom", "age":11, "sex":"male"}
r2 = {"name":"Bob", "age":22, "sex":"female"}
tb = [r1, r2]
for i in range(len(tb)):
	for j in tb[i].keys():
		print(tb[i].get(j), end='\t')
	print()

# bucket = key: value	
###

"""星号表达式在迭代元素为可变长元组的序列时是很有用的"""

星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
"""
>>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
>>> uname, *fields, homedir, sh = line.split(':')
>>> uname
'nobody'
>>> fields
['*', '-2', '-2', 'Unprivileged User']
"""
