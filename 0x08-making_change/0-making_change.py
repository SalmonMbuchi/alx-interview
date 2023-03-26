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
    if max(coins) > total or sum(coins) > total:
        return -1
    reversed = sorted(coins, reverse=True)
    count = 1
    first = reversed[0]
    for num in reversed:
        if num == first:
            continue
        while (first < total):
            first = first + num
            count += 1
    return count
