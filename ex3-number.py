import sys
from collections import deque

# get numbers between 2 numbers

a, b = map(int, sys.stdin.readline().strip().split())
if a>b:
    tmp = a
    a = b
    b = tmp

deque = deque()
for i in range(a+1, b):
    deque.append(i)

print(len(deque))
print(*deque)