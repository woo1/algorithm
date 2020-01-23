from collections import Counter
def solution(participiant, completion):
    answer = Counter(participiant) - Counter(completion)
    return list(answer.keys())[0]

"""
participant = ['mislav', 'stanko', 'mislav', 'ana'] completion = ['stanko', 'ana', 'mislav']
# Counter({'mislav': 2, 'stanko': 1, 'ana': 1}) 
# Counter({'stanko': 1, 'ana': 1, 'mislav': 1})
"""

ans = solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])
print(ans)