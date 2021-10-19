
# find the number of ways to get to position
# x, y
# in a matrix of MxN, eg 3 x 5:
"""
[[0], [0], [0], [0, [0]]
 [0], [0], [0], [0, [0]]
 [0], [0], [0], [0, [0]]]

Starting from [0][0], find your way to [M][N],
and return the number of all possible paths
"""

"""
Lets use the same Framework

1. Define the objective function
    f(m, n) -> int number_of_paths
2. Identify base cases
    f(1, 1) -> 1
    f(2, 2) -> 2
3. Write down a recurrence relation for the optimised objective function
    tip, think about this as if it is already solved
    f(m, n) = f(i - 1, j) + f(i, j - 1)
        this problem could be futher complicated by having
        [i][j] that cannot be travelled
        or
        coins in each [i][j] of value, and you need to return
        the max profit route
        max(f[i-1][j]), f[i][j-1]) + d[i][j]
4. What is the order of the execution of the function?
5. Where do we need to look in our DP to get the answer?
"""

def unique_paths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    for i in range(0, m - 1):
        for j in range(0, n - 1):
            if i > 0 and j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
            elif j > 0:
                dp[i][j] = dp[i][j - 1]

    return dp[m -1][n - 1]


# in this case grid is a m x n matrix with 1s filled in where
# there are blockages

def unique_paths_with_blockages(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            # add additional check for blockage
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0 and j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
            elif j > 0:
                dp[i][j] = dp[i][j - 1]

    return dp[m -1][n - 1]


# maximum profit in a grid
# where each i,j of the grid has a coin value that is 
# added to the total for the path
# we want to get the max profit path


def unique_path_max_profit(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]

    return dp[m-1][n-1]


