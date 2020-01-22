import sys

N = int(sys.stdin.readline().strip())
timetable = []
for _ in range(N):
    time = tuple(map(int, sys.stdin.readline().strip().split()))
    timetable.append(time)

# 빨리 끝나는 회의 순으로 정렬
# print(timetable)
timetable.sort(key=lambda time: time[0])
# print(timetable)
timetable.sort(key=lambda time: time[1])
# print(timetable)

end = timetable[0][1]
cnt = 1
for i in range(1, N):
    if timetable[i][0] < end:continue
    else:
        end = timetable[i][1]
        cnt += 1
print(cnt)