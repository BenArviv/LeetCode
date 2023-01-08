'''
    Longest Common Prefix:
    
    Write a function to find the longest common prefix string amongst an array of strings.
    If there are no common prefix, return an empty string "".
'''

def longestCommonPrefix(strs: list[str]) -> str:
    min_n = len(strs[0])
    len_pref = 0
    flag = True
    for string in strs:
        if len(string) < min_n:
            min_n = len(string)
    
    for i in range(min_n):
        cur_ch = strs[0][i]
        for string in strs:
            if string[i] != cur_ch:
                flag = False
        if flag == True:
            len_pref += 1
        else:
            break
    
    return strs[0][:len_pref]