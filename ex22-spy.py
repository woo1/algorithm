from collections import Counter
def solution(clothes):
    cloth_list = []
    for cloth in clothes:
        cloth_list.append(cloth[1])
    answer = Counter(cloth_list)
    if len(answer) == 1:
        return list(answer.values())[0]
    else:
        ret = 1
        for v in list(answer.values()):
            ret *= (v+1)

        return ret-1

rslt = solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])
print(rslt)