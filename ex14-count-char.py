alphabet_list = []
word = input()

for ascii_code in range(65, 91):
    alphabet_list.append(word.count(chr(ascii_code)))

for ascii_code in range(97, 123):
    alphabet_list[ascii_code-97] += word.count(chr(ascii_code))

max_count = max(alphabet_list)
if alphabet_list.count(max_count) > 1:
    print('?')
else:
    print(chr(alphabet_list.index(max_count)+65))