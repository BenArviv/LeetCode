'''
    String to Integer (atoi):
    
    Implement the myAtoi(String s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s
        atoi function).
        
    The algorithm for myAtoi(string s) is as follows:

    *   Read in and ignore any leading whitespace.
    *   Check if the next character (if not already at the end of the string) is '-' or '+'. 
            Read this character in if it is either. 
            This determines if the final result is negative or positive respectively. 
            Assume the result is positive if neither is present.
    *   Read in next the characters until the next non-digit character or the end of the input is reached. 
            The rest of the string is ignored.
    *   Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
            If no digits were read, then the integer is 0. 
            Change the sign as necessary (from step 2).
    *   If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that 
            it remains in the range. 
            Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1
            should be clamped to 231 - 1.
    *   Return the integer as the final result.
    
        Note:
        Only the space character ' ' is considered a whitespace character.
        Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''
from enum import Enum

def myAtoi(s: str) -> int:
    class State(Enum):
            BEFORE = 0
            DIGIT = 1
            AFTER = 2
            
    state = [State.BEFORE, State.DIGIT, State.AFTER]
    i = len(s) - 1
    j = 0
    num = 0
    sign_count = 0
    positive = True
    cur_state = State.BEFORE
    while i >= 0:
        if not s[i].isdigit():
            if cur_state == State.DIGIT:
                cur_state = State.AFTER
            if cur_state == State.AFTER:
                if s[i] == ' ':
                    i -= 1
                    continue
                elif s[i] == '-' and sign_count == 0:
                    sign_count = 1
                    positive = False
                elif s[i] == '+' and sign_count == 0:
                    sign_count = 1
                    positive = True
                else:
                    num = 0
                    j = 0
                    sign_count = 0
                    positive = True
                    cur_state = State.BEFORE
        else:
            if cur_state == State.BEFORE:
                cur_state = State.DIGIT
            elif cur_state == State.AFTER:
                num = 0
                j = 0
                sign_count = 0
                positive = True
                cur_state = State.DIGIT
            if cur_state == State.DIGIT:
                num += (10 ** j) * int(s[i])
                j += 1
                positive = True
        i -= 1
    
    if not positive:
        num *= -1
    
    if num < - 2 ** 31:
        num = - 2 ** 31
    elif num > 2 ** 31 - 1:
        num = 2 ** 31 - 1
    
    return num

# Testing example
s = "words and 987"
print(myAtoi(s))
            