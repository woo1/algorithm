"""
코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.

브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.

코니는 가속도운동을 해서 초당 1씩 더 많이 간다.
브라운은 +1, -1, *2 중 하나의 운동을 반복한다.
t 초에서 위치가 p라고 가정할 때, t + 1초에서 위치는 p일 수 없습니다. 하지만 t + 2초에서는 위치가 p일 수 있습니다 (t → t – 1 → t 혹은 t → t + 1 → t).
위 사실을 토대로 방문 시간을 홀수, 짝수로 나눠서 고려해야 한다는 것을 알 수 있습니다.
그래서 짝수, 홀수로 나눠서 지금 코니 위치가 브라운이 2초 전에 갔던 곳이면 지금 잡았다고 할 수 있습니다.
"""
from collections import deque
def solve(conyPosition, brownPosition):
    time = 0
    visit = [[0]*2 for _ in range(200001)]
    q = deque()
    q.append((brownPosition, 0))

    while 1:
        conyPosition += time

        if conyPosition > 200000:
            return -1
        if visit[conyPosition][time%2]:
            return time

        for i in range(0, len(q)):
            current = q.popleft()
            currentPosition = current[0]
            newTime = (current[1]+1)%2

            newPosition = currentPosition - 1
            if newPosition >= 0 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

            newPosition = currentPosition + 1
            if newPosition < 200001 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

            newPosition = currentPosition * 2
            if newPosition < 200001 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

        time += 1

if __name__ == '__main__':
    tm = solve(11, 2)
    print(tm)