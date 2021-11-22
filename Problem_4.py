

def sort_012(input_list):
    end_index = len(input_list)-1
    start_index = 0
    count = 0

    while count < len(input_list):
        if count > end_index:
            break
        if input_list[count] == 1:
            count += 1

        elif input_list[count] == 2:
            temp = input_list[end_index]
            input_list[end_index] = 2
            input_list[count] = temp
            end_index -= 1
        else:
            temp = input_list[start_index]
            input_list[start_index] = 0
            input_list[count] = temp
            start_index += 1
            count += 1
    return input_list


def test_function(test_case):
    sort_012(test_case)

    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0,
             2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case) #[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]


test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

test_case = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2] #[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function(test_case)

test_case = []
test_function(test_case) #[]

test_case = [0]
test_function(test_case) #[0]

