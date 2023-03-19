#!/usr/bin/python3
"""
Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    copy = []
    i = -1

    for row in range(len(matrix)):
        last_row = len(matrix) - 1
        i += 1
        for col in range(len(matrix)):
            a_row = []
            while (last_row >= 0):
                a_row.append(matrix[last_row][i])
                last_row -= 1
            copy.append(a_row)
            break
    matrix[:] = copy

    # Optimal/Alternative solution

    # n = len(matrix[0])

    # for i in range(n - 1, -1, -1):
    #    for j in range(0, n):
    #        matrix[j].append(matrix[i].pop(0))
