"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""
from collections import deque

def bfs(graph, start):
    for i in graph:
        graph[i].sort()

    explored, queue = set(), deque([start])
    explored.add(start)
    track_list = [start]
    # 연결된 걸 추가해도 popleft를 하니까 추가된 건 나중에, 이미 상단에서 연결된 건 먼저 파악한다.
    while queue:
        v = queue.popleft()
        if v in graph:
            for w in graph[v]:
                if w not in explored:
                    explored.add(w)
                    track_list.append(w)
                    queue.append(w)
    return track_list


def dfs(graph, start):
    # 큐를 사용하기 때문에 pop하면 제일 오른쪽에 있는 게 나온다. 그래서 내림차순을 해서 낮은 숫자가 뒤로 가게 해야 한다.
    # 연결된 걸 계속 오른쪽에 추가하니까 그걸 먼저 pop하고, 해당 노드의 자식 노드 파악이 다 끝나면 넘어간다.
    for i in graph:
        graph[i].sort(reverse=True) # 내림차순 정렬

    # print(graph)
    track_list, explored, stack = list(), set(), deque([start])
    while stack:
        v = stack.pop()

        if v in explored:
            continue

        explored.add(v)
        track_list.append(v)

        if v in graph:
            for w in graph[v]:
                if w not in explored:
                    stack.append(w)
    return track_list

n, m, v = map(int, input().split())
graph = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

print(*dfs(graph, v))
print(*bfs(graph, v))