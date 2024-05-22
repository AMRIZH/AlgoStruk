# problem 70 : climbing stairs
def climbStairs(n: int) -> int: # 1 <= n <= 45
    if n <= 2:  # base case
        return n 
    dp = [0] * (n+1) # create a list of n+1 elements
    dp[1] = 1 # base case
    dp[2] = 2 # base case
    for i in range(3, n+1): # iterate from 3 to n+1
        dp[i] = dp[i-1] + dp[i-2] # calculate the number of ways to reach the ith step
    return dp[n] # return the number of ways to reach the nth step
  
# improved code
def climbStairss(n: int) -> int:
    dp = [None] * (n + 1) # create a list of n+1 elements
    def helper(n): # helper function
        if n <= 2: # base case
            return n 
        
        if dp[n] is None: # if the value of dp[n] is not calculated
            dp[n] = helper(n - 1) + helper(n - 2) # calculate the number of ways to reach the nth step
        return dp[n] # return the number of ways to reach the nth step
    
    return helper(n) # return the number of ways to reach the nth step

"""Explanation:

    We start by handling the base cases: if n is 1 or 2, we return n because there is only one way to climb 1 step and two ways to climb 2 steps.
    We create a list dp of size n+1 to store the number of distinct ways to reach each step.
    We initialize dp[1] and dp[2] to 1 and 2, respectively, as there is one way to reach the first step and two ways to reach the second step.
    We use a loop to iterate from the third step to the nth step, and for each step i, we calculate dp[i] using the recurrence relation dp[i] = dp[i-1] + dp[i-2].
    Finally, we return dp[n], which represents the number of distinct ways to reach the nth step.

Time complexity: O(n)  
Space complexity: O(n)
"""
# test the function
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
print(climbStairs(4))  # Output: 5
print(climbStairs(5))  # Output: 8

"""
here's a list of results for climbStairs(n) from n=1 to n=10:
n = 1: 1 way
n = 2: 2 ways
n = 3: 3 ways
n = 4: 5 ways
n = 5: 8 ways
n = 6: 13 ways
n = 7: 21 ways
n = 8: 34 ways
n = 9: 55 ways
n = 10: 89 ways
"""