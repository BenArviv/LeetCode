'''
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
        all the original letters exactly once.
'''

def isAnagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    n = len(s)
    while n != 0:
        if s[0] not in t:
            return False
        else:
            index = t.index(s[0])
            t = t[:index] + t[index + 1:]
            s = s[1:]
            n = len(s)
            
    if len(s) != len(t):
        return False
    return True

# Testing example
s = "aacc"
t = "ccac"
print(isAnagram(s, t))