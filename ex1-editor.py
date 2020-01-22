# Editor
"""
한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.
"""
import sys
from collections import deque

class Editor:
    def __init__(self, input_text):
        self.left_deque = deque(input_text)
        self.right_deque = deque()

    def move_cursor_left(self):
        if self.left_deque:
            print(self.left_deque, self.right_deque)
            self.right_deque.appendleft(self.left_deque.pop())
            print(self.left_deque, self.right_deque)

    def move_cursor_right(self):
        if self.right_deque:
            print(self.left_deque, self.right_deque)
            self.left_deque.appendleft(self.right_deque.popleft())
            print(self.left_deque, self.right_deque)

    def delete_left_char(self):
        if self.left_deque:
            self.left_deque.pop()

    def add_char_to_left(self, character2add):
        self.left_deque.append(character2add)

"""
- command : P x
self.left_deque
[a, b, c, d]->[a, b, c, d, x]
self.right_deque
[]
- command : L
self.left_deque
[a, b, c, d, x]->[a, b, c, d]
self.right_deque
[x]
- command : P y
self.left_deque
[a, b, c, d]->[a, b, c, d, y]
self.right_deque
[x]
"""

editor = Editor(sys.stdin.readline().strip())

N = int(sys.stdin.readline().strip())
while N:
    command = sys.stdin.readline().strip()
    cmd = command[0]
    if cmd == 'L':
        editor.move_cursor_left()
    elif cmd == 'D':
        editor.move_cursor_right()
    elif cmd == 'B':
        editor.delete_left_char()
    else:
        editor.add_char_to_left(command[2])
    N -= 1

print(''.join(editor.left_deque)+''.join(editor.right_deque))