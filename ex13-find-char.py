# https://deepwelloper.tistory.com/109?category=795989
# find alphabet
alphabet_list = []
S = input()

# small alphabet characters
for ascii_code in range(97, 123):
    alphabet_list.append(S.find(chr(ascii_code)))
print(*alphabet_list)