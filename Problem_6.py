def get_min_max(ints):
    if not ints:
        return None
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_int=ints[0]
    max_int=ints[0]
    for number in ints:
        if number < min_int:
            min_int=number
        if number > max_int:
            max_int=number
    return (min_int,max_int)
        


import random

l = [i for i in range(0, 20)]  # a list containing 0 - 9
random.shuffle(l)
print(l)
print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")
random.shuffle(l)
print(l)
print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")
random.shuffle(l)
print(l)

print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")

if not get_min_max([]): #None
    
    print('Pass')
else:
    print('Fail')

if not get_min_max(None): #None
    print('Pass')
else:
    print('Fail')

print ("Pass" if (0, 0) == get_min_max([0]) else "Fail")