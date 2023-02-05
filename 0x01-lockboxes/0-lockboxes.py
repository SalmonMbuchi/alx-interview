#!/usr/bin/python3
""""You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    x = len(boxes)
    aList = [0]
    for i in my list:
        for j in boxes[i]:
            if j not in aList:
                if j < x:
                    aList.append(j)
    if len(aList) == x:
        return True
    return False
