## 问题1

### 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？


## 解决方案
### 任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

### 代码示例：

p = [3, 4]

a, b = p
print(a)
print(b)

### 如果变量个数和序列元素的个数不匹配，会产生一个异常。
p = (4, 5)
x, y, z = p
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ValueError: need more than 2 values to unpack

### 解压序列用于字典时，默认是对“key”进行操作；如果需要对key-value进行操作则需要使用items; 如果需要对 value 进行操作，则需要values（）

dict1 = {'a': 1, 'b': 2, 'c': 3}
a, b, c = dict1 # 返回keys
a, b, c = dict1.items() #返回键值对
a, b, c = dict1.values() #返回values
