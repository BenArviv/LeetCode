'''
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1],
        the return 0.
'''

def reverse(x: int) -> int:
    min = - (2 ** 31)
    max = 2 ** 31 - 1
    neg = 1
    y = 0
    i = -1
    if x < 0:
        neg = -1
        x *= -1
    
    temp = x
    while temp != 0:
        temp //= 10
        i += 1
        
    while x != 0:
        rem = x % 10
        x //= 10
        y += (10 ** i) * rem
        i -= 1
        if y < min or y > max:
            return 0
        
    y *= neg
    return y

# Testing examples
x = -123
print(reverse(x))
