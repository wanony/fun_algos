# find the number of ways to climb stairs
# when you can take one or two steps at a time
# n is the number of stairs you need to clim

def solution(n):
    dp = [0 for x in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

"""
General framework for solving DP problems:
Stolen from Andrey Grehov: https://youtu.be/QlT4HG93Gaw
1. Define the objective function
    solution(n) is the number of distrinct ways to reach the n-th stair
2. Identify base cases
    solution(0) = 1 as there is 1 way to reach the 0th stair
    solution(1) = 1 as there is 1 way to reach the 1st stair
3. Write down a recurrence relation for the optimised objective function
    solution(n) = solution(n - 1) + solution(n - 2)
4. What is the order of the execution of the function?
    In this case, it is Bottom-Up, as solution(0), solution(1) is needed to solve solution(2)
5. Where do we need to look in our DP to get the answer?
    In this case, it is stored in dp[n]
"""

# we can further optimise this solution to use less memory

def solution(n):
    a = 1
    b = 1
    for i in range(2, n):
        c = a + b
        b = c
        a = b
    
    return c


# lets solve for climbing stairs at 1, 2, or 3 steps at a time

def solution(n):
    dp = [x for x in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

# this could then be optimised in the same way above


# solving for being able to climb 1 to k steps

# when identifying the base case here, we need to sum
# f(n) = f(n - 1) + f(n - 2) + ... + f(n - k)

def solution(n, k):
    dp = [0 for x in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        # create another loop to sum all of the k steps
        # this looks very similar to the coin change/knapsack problem
        # this solution is O(nk), O(n)
        for j in range(1, k):
            if i - j < 0:
                continue
            dp[i] += dp[i - j]

    return dp(n)


# if we optimise this problem

def solution(n, k):
    dp = [0 for x in range(k + 1)]
    dp[0] = 1
    # [1, 1, 2], we need to rewrite previous values with % to get the index
    for i in range(1, n):
        for j in range(1, k):
            if i - j < 0:
                continue
            dp[i % k] += dp[(i - j) % k]

    return dp[n % k]


# now we will add a problem where we cannot step on certain stairs
# lets say we cannot step on "red" stairs.
# we get an array rs, which contains the indices of the stairs that 
# are red, lets say for example [1, 3, 4]

def solution(n, k, rs):
    dp = [0 for x in range(n + 1)]
    dp[0] = 1
    for i in range(1, n):
        for j in range(1, k):
            if i in rs:
                dp[i] = 0
                continue
            if i - j < 0:
                continue
            dp[i] += dp[i - j]

    return dp[n]