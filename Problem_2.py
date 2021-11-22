def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1
    mid = len(input_list)//2
    if input_list[mid] == number:
        return mid
    """if input_list[mid] < input_list[0] than the subarray right of mid is sorted,
        else the left array is sorted"""
    if input_list[mid] < input_list[0]:
        arr = input_list[mid+1:]
        if len(arr) < 1:
            return -1
        if arr[0] <= number <= arr[-1]:
            ans = binary_search(arr, number)
            if ans != -1:
                ans += mid+1
            
            return ans
        else:
            
            return rotated_array_search(input_list[:mid], number)
    else:
        arr = input_list[:mid]
        if len(arr) < 1:
            return -1
        if arr[0] <= number <= arr[-1]:
            ans = binary_search(arr, number)
            
            return ans
        else:
            
            ans = rotated_array_search(input_list[mid+1:], number)
            if ans != -1:
                ans += mid+1
            
            return ans


def binary_search(arr, number):
    if len(arr) == 1:
        return 0
    low = 0
    high = len(arr)-1
    while low <= high:
        
        mid = (high+low)//2
        
        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            low = mid+1
        else:
            high = mid-1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[], None])
test_function([[0], 4])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 5])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4],7])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8,  2, 3, 4], 10])
test_function([list(range(10**6)), 998])
