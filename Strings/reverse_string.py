'''
    Reverse String:
    
    Write a function that reverses a string.
    The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.
'''

def reverseString(s: list[str]):
    j = len(s) - 1
    i = 0
    temp = 0
    while i <= j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        
        i += 1
        j -= 1
