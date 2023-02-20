#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a dataset represents a valid UTF8 encoding"""
    ref = 128
    for num in data:
        if num > ref:
            return False
    return True
