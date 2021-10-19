# input is a 2d grip map of 1's and 0's and count the number of islands
# connected by 1's connect horizontally or vertically

# examples

# 1

# input

# 11110
# 11010
# 11000
# 00000

# output: 1

# 2

# input

# 11000
# 11000
# 00100
# 00011

# output: 3


def solution(grid: list):
    
    def do_dfs(grid, i, j):
        # check for all possible fails, ie boundary check
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        
        grid[i][j] = 0

        do_dfs(grid, i + 1, j)  # check up
        do_dfs(grid, i - 1, j)  # check down
        do_dfs(grid, i, j - 1)  # check left
        do_dfs(grid, i, j + 1)  # check right

    # set an initial count up
    count = 0

    # loop through top left to bottom right
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count += 1
                do_dfs(grid, i, j)

    return count