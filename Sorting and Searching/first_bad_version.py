'''
    First Bad Version:
    
    You are a product manager and currently leading a team to develop a new product.
    Unfortunately, the latest version of your product fails the quality check.
    Since each version is developed based on the previous versions, all the versions after a bad version are also bad.
    
    Suppose you have n version [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
    
    You are given an API bool isBadVersion(version) which returns whether a version is bad.
    Implement a function to find the first bad version.
    You should minimize the number of calls to the API
'''

def isBadVersion(version: int) -> bool:
    if version >= bad:
        return True
    else:
        return False

def firstBadVersion(n: int) -> int:
    if n == 0:
        return 0
    
    start = 1
    end = n
    k = (start + end) // 2
    last_bad = 1
    flag = False
    while True:
        if isBadVersion(k): # First bad one must be at the left half of k
            last_bad = k
            end = k
            k = (start + end) // 2
            flag = True
        else: # First bad one must be at the right half of k
            start = k + 1
            k = (start + end) // 2
        if flag == True and start == end:
            break
    
    return last_bad

n = 5
bad = 4
print(firstBadVersion(n))
