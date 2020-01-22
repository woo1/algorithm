def binarySearch(num_list):
    while num_list:
        mid = len(num_list) // 2
        if target == num_list[mid]:
            return True
        elif target < num_list[mid]:
            num_list = num_list[:mid]
        elif target > num_list[mid]:
            num_list = num_list[mid+1:]
    return False

num_list = [9, 4, 2, 5, 3, 8]
num_list.sort()

target = 12
print(binarySearch(num_list))