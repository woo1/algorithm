T = int(input())

rank_2017 = [1, 3, 6, 10, 15, 21]
award_2017 = [500, 300, 200, 50, 30, 10]

rank_2018 = [1, 3, 7, 15, 31]
award_2018 = [512, 256, 128, 64, 32]

awards = []
for _ in range(T):
    award = 0
    a, b = map(int, input().split())
    if a:
        for i, r in enumerate(rank_2017):
            if a <= r:
                award += award_2017[i]
                break
    if b:
        for i, r in enumerate(rank_2018):
            if b <= r:
                award += award_2018[i]
                break
    awards.append(award*10000)

for val in awards:
    print(val)