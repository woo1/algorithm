# https://deepwelloper.tistory.com/112?category=795989
N, M = map(int, input().split())
trees_height = list(map(int, input().split()))

min_height = 0;
max_height = max(trees_height)

while max_height > min_height + 1:
    cutting_height = (max_height + min_height)//2
    sum = 0
    for trees in trees_height:
        if cutting_height < trees:
            sum += (trees - cutting_height)
    if sum >= M:
        min_height = cutting_height
    else:
        max_height = cutting_height

    if max_height == min_height + 1:
        cutting_height = min_height
        sum = 0
        for trees in trees_height:
            if cutting_height < trees:
                sum += (trees - cutting_height)

print(cutting_height)