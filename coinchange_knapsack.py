# you are given a list of coins and an amount
# return the fewest number of coins to get that amount
# assume you have infinite number of coins

# optimizations
# sorting coins array, you can add else statement and break
# if coins[j] >= i

def solution(coins, amount):
    dp = [0 for x in range(amount) + 1]  # array of size amount + 1
    dp[0] = 0  # already done, actually.

    j = 0
    i = 0
    while i <= amount:
        while j < len(coins):
            if coins[j] <= i:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
            j += 1

    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]
