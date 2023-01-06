'''
    First Unique Character in a String:
    
    Given a string s, find the first non-repeating character in it and return its index.
    If it does not exist, return -1
'''

def firstUniqueChar(s: str) -> int:
    index = -1
    string = str(s)
    i = 0
    n = len(string)
    while n != 0:
        temp = string[0]
        string = string[1:n]
        if temp in string: # There is another occurence of the character
            while temp in string:
                temp_ind = string.index(temp)
                string = string[:temp_ind] + string[temp_ind + 1:] # Removing that character
        else:
            index = s.find(temp)
            break
        n = len(string)
    return index

# Testing examples
s = "aadadaad"
print(firstUniqueChar(s))