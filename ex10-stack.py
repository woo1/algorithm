import sys
import collections

stack = collections.deque()

n = int(sys.stdin.readline().strip())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd[:2] == 'pu': # push
        num = int(cmd.split(' ')[1])
        stack.append(num)
    if cmd[:2] == 'po': # pop
        if not stack:
            print(-1)
            continue
        print(stack.pop())
    if cmd[0] == 's': # size
        print(len(stack))
    if cmd[0] == 'e': # empty -> 1(Empty), 0(Not empty)
        if stack:
            print(0)
            continue
        print(1)
    if cmd[0] == 't': # top
        if not stack:
            print(-1)
            continue
        print(stack[-1])

