T = int(input())

# https://deepwelloper.tistory.com/74?category=795989

l = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        l[i] = l[i-1] + l[i-2] + l[i-3]
    print(l[n])