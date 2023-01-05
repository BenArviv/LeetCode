'''
    Plus One:
    
    You are given a large integer represented by an integer array digits, where each digits[i] is the i-th 
        digit of the integer.
    The digits are ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.
    
    Increment the large number by one and return the resulting array of digits.
'''

def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)
    if digits[n - 1] != 9:
        digits[n - 1] += 1
        return digits
    else:
        i = n - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i < 0:
            i = 0
        else:
            digits[i] += 1
    
    if digits[0] == 10 or digits[0] == 0:
        digits[0] = 0
        digits.insert(0, 1)
    
    return digits

# Example testing
big_number = [9]

print(plusOne(big_number))