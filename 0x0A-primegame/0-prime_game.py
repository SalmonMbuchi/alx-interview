#!/usr/bin/python3
"""Prime Game"""

def generate_primes(n):
    """Generates all prime numbers up to `n`"""
    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return primes

def can_win(primes, n):
    """Determine which player can win"""
    dp = [False] * (n + 1)
    for i in range(2, n + 1):
        if i in primes:
            dp[i] = True
        else:
            for prime in primes:
                if prime > i:
                    break
                if not dp[i - prime]:
                    dp[i] = True
                    break
    return dp[n]

def isWinner(x, nums):
    """Determine the winner"""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = generate_primes(n)
        if can_win(primes, n):
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
