#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the `total`
    """
    if total <= 0:
        return 0
    reversed = sorted(coins, reverse=True)
    count = 0
    for num in reversed:
        if total / num > 0:
            count = count + (total // num)
            total = total % num

    if total != 0 or count == 0:
        return -1
    return count
