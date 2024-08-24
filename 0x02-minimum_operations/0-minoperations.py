#!/usr/bin/python3
"""Minimum operations coding challenge"""


def minOperations(n):
    """Method that calculates the fewest number of operations
    needed to result in exactly n H characters"""
    ops = 0
    cur = 2
    while n > 1:
        while n % cur == 0:
            ops += cur
            n /= cur
        cur += 1
    return ops
