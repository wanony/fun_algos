
# find the minimum cost to get to the i-th stair
# where each stair has a cost to step on
# where p is an array of prices for each step by index

def solution(n, k, p):
    dp = [9999 for x in range(n + 1)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k):
            if i - j < 0:
                continue
            dp[i] = dp[i] + p[i]
            if dp[i - j] + p[i] > dp[i]:
                dp[i] = dp[i - j] + p[i]

    return dp[n]


# return the cheapest PATH rather than the price
# in this case we need to return an array of int
# that has the indices of the stairs to take

def solution(n, k, p):
    dp = [9999 for x in range(n + 1)]
    path = [0 for x in range(n + 1)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k):
            if i - j < 0:
                continue
            if dp[i] == 9999:
                dp[i] = dp[i] + p[i]
            if dp[i - j] + p[i] < dp[i]:
                dp[i] = dp[i - j] + p[i]
                path[i] = i - j

    return [x for x in path if x != 0]