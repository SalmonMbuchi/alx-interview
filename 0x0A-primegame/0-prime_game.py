#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Determines the winner"""

    players = ('Maria', 'Ben')
    winner = []
    nums_len = len(nums) if nums else 0
    if nums_len == 0:
        return None
    for i in range(x):
        z = nums[i] if i < nums_len else 0
        z_nums = list(range(1, z + 1, 1))
        prime = 2
        turns = 0
        while True:
            remove_ocurred = False
            prime_multiples = list(range(prime, z + 1, prime))
            for multiple in prime_multiples:
                if multiple in z_nums:
                    z_nums.remove(multiple)
                    remove_ocurred = True
            turns += 1
            if remove_ocurred:
                for val in z_nums:
                    if val > prime:
                        prime = val
                        break
            else:
                break
        winner.append(players[turns % 2])
    maria_wins = winner.count(players[0])
    ben_wins = winner.count(players[1])
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'

