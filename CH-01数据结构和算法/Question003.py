##   问题   ##
# 在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

## 解决方案 ##
# 保留有限历史记录正是 collections.deque 大显身手的时候。比如，下面的代码在多行上面做简单的文本匹配，并只返回在前N行中匹配成功的行：

from collections import deque
"""
  python中collections模块是内置的一个集合模块，提供了许多有用的集合类和方法
  >>> print(dir(collections))
  其中，**deque**: 高效增删改双向列表，类似列表的容器，实现了在两端快速添加(append)和弹出(pop)
"""

def search(lines, pattern, history=5):
  previous_lines = deque(maxlen=history)
  for li in lines:
    if pattern in li:
      yield li, previous_lines
     previous_lines.append(li)
    
if __name__ == '__main__':
  with open(r'../../cookbook/somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
      for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
