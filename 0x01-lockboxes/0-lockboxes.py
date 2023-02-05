#!/usr/bin/python3
"""Determine if all boxes can be opened"""


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
