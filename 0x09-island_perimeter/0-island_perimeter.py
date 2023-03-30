#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Finds the perimeter of an island"""
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # count all sides initially

                # subtract if adjacent top is land
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2

                # subtract if adjacent left is land
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
