from collections import Counter
from collections import namedtuple
from collections import deque
# a = 'aaaabbbbccccc'
# my_Counter = Counter(a)
# print(my_Counter)
# print(list(my_Counter.elements()))

# point = namedtuple('point','x,y')
# pt = point(1,-4)
# print(pt.x)

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.extend([4,5,6])
print(d)