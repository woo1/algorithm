"""
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1≤M≤100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수들의 범위는 int 로 한다.
"""

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
Qs = list(map(int, input().split()))

hashtable = {}

for num in nums:
    index = num%10
    if index in hashtable:
        hashtable[index].append(num)
    else:
        hashtable[index] = [num]

# print(hashtable)
"""
{4: [4], 1: [1], 5: [5, 15], 3: [3]}
"""
for q in Qs:
    index = q%10
    found = 0
    if index in hashtable:
        for h in hashtable[index]:
            if h == q:
                found = 1
                break
    print(found)

"""
5
4 1 5 15 3
5
1 3 5 6 8
"""