N = int(input())
times_list = list(map(int, input().split()))

times_list.sort()
# print(times_list)

sum = 0
cnt = 0
for t in times_list:
    cnt += t
    sum += cnt
print(sum)