"""
트라이(trie) 자료구조는 접두사/접미사와 관련된 문자열 검색을 할 때 매우 빠르고 유용하게 쓸 수 있습니다.
trie를 만드는 중에 _end를 만날 경우 False를 반환해주면 됩니다.
"""
_end = '_end_'
def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        print(current_dict, 'init', word)
        for letter in word:
            if _end in current_dict:
                return False
            current_dict = current_dict.setdefault(letter, {})
            print(current_dict, word)
        current_dict[_end] = _end
        print(current_dict, word, 'finish')
    return True

print(make_trie(['119', '9764532', '119215151']))

"""
{} init 119
{} 119
{} 119
{} 119
{'_end_': '_end_'} 119 finish
{'1': {'1': {'9': {'_end_': '_end_'}}}} init 9764532
{} 9764532
{} 9764532
{} 9764532
{} 9764532
{} 9764532
{} 9764532
{} 9764532
{'_end_': '_end_'} 9764532 finish
{'1': {'1': {'9': {'_end_': '_end_'}}}, '9': {'7': {'6': {'4': {'5': {'3': {'2': {'_end_': '_end_'}}}}}}}} init 119215151
{'1': {'9': {'_end_': '_end_'}}} 119215151
{'9': {'_end_': '_end_'}} 119215151
{'_end_': '_end_'} 119215151
False
"""