# BOJ 15686
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
home, chichken, v = [], [], []
ans = 1e9

def solve(idx, cnt):
    global ans
    if idx > len(chichken):
        return -1
    if cnt == m:
        s = 0
        for hx, hy in home:
            d = 1e9 #1000000000.0
            for j in v:
                cx, cy = chichken[j]
                d = min(d, abs(hx-cx)+abs(hy-cy))
            s += d
        ans = min(ans, s)
        return ans
    v.append(idx)
    solve(idx+1, cnt+1)
    v.pop()
    solve(idx+1, cnt)

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            home.append((i+1, j+1))
        elif a[i][j] == 2:
            chichken.append((i+1, j+1))
solve(0, 0)
print(ans)