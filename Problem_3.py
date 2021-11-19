def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    merge_sort(input_list)
    count_1 = 0
    count_2 = 0
    first = 0
    second = 0
    for index, element in enumerate(input_list):
        if index % 2 == 0:
            first += element*10**count_1
            count_1 += 1
        else:
            second += element*10**count_2
            count_2 += 1

    return [first, second]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    if len(arr) < 3:
        if arr[0] > arr[1]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    def merge(arr, left, right):
        left_index = 0
        right_index = 0
        index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                arr[index] = left[left_index]
                left_index += 1
                index += 1
            else:
                arr[index] = right[right_index]
                right_index += 1
                index += 1
        for rest in left[left_index:]:
            arr[index] = rest
            index += 1
        for rest in right[right_index:]:
            arr[index] = rest
            index += 1
        return arr
    merge(arr, left, right)

    return arr


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0],[0,0]])
