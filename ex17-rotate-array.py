def rotate_90(m):
    N = len(m)
    ret = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def rotate_180(m):
    N = len(m)
    ret = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret

def rotate_270(m):
    N = len(m)
    ret = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret

m = [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
print(rotate_90(m))
print(rotate_180(m))
print(rotate_270(m))