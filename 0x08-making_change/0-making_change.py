#!/usr/bin/python3


def makeChange(coins, total):
    """Determines  the fewest number of coins needed to meet a given amount
    total
    Parameters:
        - @param {coins}: List
        - @param {total}: int
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for _ in range(1, total + 1):
        for coin in coins:
            if _ - coin >= 0:
                dp[_] = min(dp[_], dp[_ - coin] + 1)
    if dp[total] == float('inf'):
        return -1
    return dp[total]
