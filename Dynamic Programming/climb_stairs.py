'''
    Climbing Stairs:
    
    You are climbing a staircase.
    It takes n steps to reach the top.
    
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
'''
import numpy as np

def climbStairs(n: int) -> int:
    
    def rec_climbStairs(n: int) -> int:
        if n <= 0:
            new_list[n] = 0
            return 0
        elif n == 1:
            new_list[n] = 1
            return 1
        elif n == 2:
            new_list[n] = 2
            return 2
        else:
            if new_list[n] == -1:
                new_list[n] = rec_climbStairs(n - 2) + rec_climbStairs(n - 1)
            return new_list[n]
        
    new_list = np.full((n + 1), -1, dtype=int)
    rec_climbStairs(n)
    return new_list[n]

# Testing examples
n = 2
print(climbStairs(n))
