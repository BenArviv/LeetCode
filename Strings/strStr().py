'''
    Implement strStr():
    
    Given two strings needle and haystack, return the index of the first occurence of needle in haystack, 
        or -1 if needle is not part of haystack.
'''

def strStr(haystack: str, needle: str) -> int:
    index = -1
    temp_index = 0
    flag = False
    i = j = 0
    n1, n2 = len(haystack), len(needle)
    while i < n1:
        if haystack[i] == needle[j]:
            if flag == False:
                flag = True
                temp_index = i
            if flag == True:
                if j == n2 - 1: # Last character in needle
                    index = temp_index
                    break
                j += 1
                i += 1
        else:
            if flag == False:
                i += 1
            else:
                j = 0
                i = temp_index + 1
                flag = False
        
    return index

# Testing example
n = "leeto"
h = "leetcode"
print(strStr(h, n))