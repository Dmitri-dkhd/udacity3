import math
def sqrt(number): 
    """ Calculate the floored square root of a number Args: number(int): Number to find the floored squared root Returns: int: Floored Square Root """ 
    if number <2:
        return number
    high=number
    low=0
    

    while low <high:
        middle=low+(high-low)//2
        if middle**2 <=number and (middle+1)**2>number:
            return middle
        elif middle**2<number:
            low=middle
        else:
            high=middle
        
    
        
    
print ("Pass" if (3 == sqrt(9)) else "Fail") 
print ("Pass" if (0 == sqrt(0)) else "Fail") 
print ("Pass" if (4 == sqrt(16)) else "Fail") 
print ("Pass" if (1 == sqrt(1)) else "Fail") 
print ("Pass" if (20 == sqrt(400)) else "Fail")