## 数据结构

### 数组

python中为列表（list）

```python
# list的基本操作
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# 1 返回列表中元素 x 出现的次数
# list.count(x)
fruits.count('apple')

# 2 返回第一个值为banana的索引，未找到报错
# list.index(x[, start[, end]])，可选参数 start 和 end 是切片索引。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。
fruits.index('banana')

# 3 翻转列表
# list.reverse()
fruits.reverse()

# 4 在列表末尾添加一个元素
# list.append(x)
fruits.append('grape')

# 5 就地排序列表中的元素，默认从小到大
# list.sort(*, key=None, reverse=False)
fruits.sort()


# 6 删除列表中指定位置的元素，并返回被删除的元素。i未指定时，删除并返回最后一个元素
# list.pop([i])
fruits.pop()

# 7 扩展列表
# list.extend(iterable)

# 8 在指定位置i插入元素x
# list.insert(i, x)

# 9 从列表中删除第一个值为 x 的元素。未找到指定元素时，报错。
# list.remove(x)

# 10 返回列表的浅拷贝
# list.copy()
```

### 字符串

#### 字符串常用操作

```python
# 创建字符串
string = "abcde"

# 1 返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。 可选参数 start 与 end 会被解读为切片表示法
string.count(sub[, start[, end]])

# 2 返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。 可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。
string.find(sub[, start[, end]])

# 3 如果字符串不为空，且由字母或数字组成，则返回 True ， 否则返回 False 
string.isalnum()

# 4 如果字符串不为空，且由全由字母组成，返回 True ，否则返回 False 
string.isalpha()

# 5 如果字符串为空或字符串中的所有字符都是 ASCII ，返回 True ，否则返回 False
string.isascii()

# 6 返回原字符串的副本，其所有区分大小写的字符均转换为小写。
string.lower()

# 7 返回原字符串的副本，其中所有区分大小写的字符均转换为大写
string.upper()

# 8 返回子字符串 sub 在字符串内被找到的最大（最右）索引，这样 sub 将包含在 s[start:end] 当中。 可选参数 start 与 end 会被解读为切片表示法。 如果未找到则返回 -1。
string.rfind(sub[, start[, end]])

# 9 返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。 如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。 如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）。
string.split(sep=None, maxsplit=- 1)

# 10 如果字符串以指定的 prefix 开始则返回 True，否则返回 False。 prefix 也可以为由多个供查找的前缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。
string.startswith(prefix[, start[, end]])
```

#### 字典树

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.tree
        for w in word:
            tree = tree.setdefault(w, {})
        # 是否是一个完整的单词
        tree["is_word"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.tree
        for w in word:
            if w not in tree: return False
            tree = tree[w]
        return tree.get('is_word', False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.tree
        for ch in prefix:
            if ch not in tree: return False
            tree = tree[ch]
        return True


```

### 链表

```python
# 链表节点的常用定义
class ListNode:
    def __init__(self, val=0, next=None):
        # 节点的值
        self.val = val
        # 指向下一个节点
        self.next = next
```

### 哈希表

python中为字典（dict）

```python
# 1 创建空字典
d = {}

# 2 返回字典 d 中使用的所有键的列表。
list(d)

# 3 返回字典 d 中的项数。
len(d)

# 4 返回 d 中以 key 为键的项。 如果映射中不存在 key 则会报错
d[key]

# 5 如果 key 存在于字典中则返回 key 的值，否则返回 default。 如果 default 未给出则默认为 None，因而此方法绝不会报错
d.get(key[, default])

# 6 将 d[key] 设为 value
d[key] = value

# 7 将 d[key] 从 d 中移除。 如果映射中不存在 key 则会引发 KeyError。
del d[key]

# 8 如果 d 中存在键 key 则返回 True，否则返回 False。
key in d

# 9 返回以字典的键为元素的迭代器。 这是 iter(d.keys()) 的快捷方式。
iter(d)

# 10 返回由字典值组成的一个新视图
d.values()

# 11 返回由字典项 ((键, 值) 对) 组成的一个新视图。 参见 视图对象文档。
d.items()

# 12 如果 key 存在于字典中则将其移除并返回其值，否则返回 default。 如果 default 未给出且 key 不存在于字典中，则会引发 KeyError。
d.pop(key[, default])

# 13 如果字典存在键 key ，返回它的值。如果不存在，插入值为 default 的键 key ，并返回 default 。 default 默认为 None。
d.setdefault(key[, default])
# 等价于
def setdefault(d, key, default=None):
    if d.get(key):
        return d.get(key)
    d[key] = default
    return default
```

### 队列

```python
### 使用标准库collections.deque(双端队列）实现
from collections import deque

# 队列初始化
# deque([iterable[, maxlen]])
queue = deque()

# 添加 x 到右端
queue.append(x)

# 添加 x 到左端
queue.appendleft(x)

# 移去并且返回deque 最右侧的那一个元素，如果没有元素的话，将报错
queue.pop()

# 移去并且返回deque 最左侧的那一个元素，如果没有元素的话，将报错
queue.popleft()

# 向右循环移动 n 步。 如果 n 是负数，就向左循环。
# 如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。
queue.rotate(n=1)
```

### 栈

```python
### 1 使用list实现栈
stack = [3, 4, 5]
# 把元素添加到栈的顶端
stack.append(6)
# 从堆栈顶部取出元素
stack.pop()


### 2 使用标准库collections.deque(双端队列）实现
from collections import deque
stack = deque()
# 把元素x添加到栈的顶端
stack.append(x)
# 从堆栈顶部取出元素
stack.pop()
```

### 树(二叉查找树、二叉树)

```python
# 二叉树节点的常用定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # 节点的值
        self.val = val
        # 指向左节点
        self.left = left
        # 指向右节点
        self.right = right
```

### 堆（优先队列、二叉堆）

python中默认为最小堆

可以将堆中每个数字乘以-1，来实现最大堆

获取最大值时，将根节点的值再次乘以-1

```python
import heapq

heap = []
# 将 item 的值加入 heap 中，保持堆的不变性。
heapq.heappush(heap, item)

# 弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。
heapq.heappop(heap)

# 将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用 heappush() 再调用 heappop() 运行起来更有效率。
heapq.heappushpop(heap, item)

# 将list x 转换成堆，原地，线性时间内。
heapq.heapify(x)

# 弹出并返回 heap 中最小的一项，同时推入新的 item。 堆的大小不变。 如果堆为空则引发 IndexError。
heapq.heapreplace(heap, item)

# 从 iterable 所定义的数据集中返回前 n 个最大元素组成的列表。 如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。 等价于: sorted(iterable, key=key, reverse=True)[:n]
heapq.nlargest(n, iterable, key=None)

# 从 iterable 所定义的数据集中返回前 n 个最小元素组成的列表
heapq.nsmallest(n, iterable, key=None)
```

### 图





## 算法

### 排序及查找

```python
# 列表有一个内置的list.sort(key=None, reverse=False方法可以直接修改列表，并返回（None），如果不需要原列表，list.sort()效率更高
# sorted(iterable,key=None, reverse=False)内置函数，它会从一个可迭代对象构建一个新的排序列表
# 默认从小到大排序，reverse=True时从大到小排序

a = [9, 2, 4, 8, 0, 5, 3, 6, 1, 7]
# 1 list.sort() 方法只是为列表定义的
a.sort()
# 2 sorted()函数可以接受任何可迭代对象
sorted(a)

# 3 key可以自定义
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# 根据年龄排序
sorted(student_tuples, key=lambda student: student[2])

# 4 对象排序
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    
    def __lt__(self, other):
        # 当在两个对象之间进行比较时，会调用对象的 __lt__()方法。 因此，通过定义 __lt__() 方法可以很容易地为类添加一个标准排序:
        return self.age < other.age
  students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane': 'A', 'dave': 'C'}
a = sorted(students, key=lambda x: newgrades[x])  
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age) 

# 5 使用Operator 模块的函数
from operator import itemgetter, attrgetter
# 等价于 sorted(student_tuples, key=lambda student: student[2])
sorted(student_tuples, key=itemgetter(2))
# 等价于 sorted(student_objects, key=lambda student: student.age) 
sorted(student_objects, key=attrgetter('age'))
# 6 Operator 模块功能允许多级排序。 例如，按先 grade 排序，然后按 age 排序：
sorted(student_tuples, key=itemgetter(1,2))
sorted(student_objects, key=attrgetter('grade', 'age'))

# 7 键函数不需要直接依赖于被排序的对象。键函数还可以访问外部资源。例如，如果学生成绩存储在字典中，则可以使用它们对单独的学生姓名列表进行排序：
students = ['dave', 'john', 'jane']
newgrades = {'john': 'F', 'jane': 'A', 'dave': 'C'}
sorted(students, key=lambda x: newgrades[x])
```

### 枚举（遍历、排列、组合）



### 滑窗



### 双指针

### 前缀和

### 迭代

### 递归

### 回溯

### 分治（归并、二分）

### 搜索（深搜、广搜）

### 贪心

### 模拟

## 进制与位运算

### 位运算

### 进制转换

### 进位计算

