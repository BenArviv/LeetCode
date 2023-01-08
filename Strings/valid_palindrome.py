'''
    A phrase is a palindorme if, after converting all uppercase letters and removing all non-alphanumeric characters,
        it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.
    
    Given a string s, return true if s is a palindrome, or false otherwise.
'''

def isPalindrome(s: str) -> bool:
    n = len(s)
    i = 0
    while i < n:
        if not s[i].isalnum():
            s = s[:i] + s[i + 1:]
        else:
            i += 1
        n = len(s)
    
    s = s.casefold()
    i, j = 0, n - 1
    while i < j:
        if not s[i] == s[j]:
            return False
        i += 1
        j -= 1
        
    return True

# Testing example
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))