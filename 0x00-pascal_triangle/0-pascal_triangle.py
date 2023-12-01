#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """A function  that returns a list of lists of integers
    representing the Pascal’s triangle of n
    Assume n will be always an integer

    Returns an empty list if n <= 0
    """
    result = []

    if n <= 0:
        return result

    for r in range(n):
        temp = []
        for c in range(r + 1):
            if c == 0 or c == r:
                temp.append(1)
            else:
                temp.append(result[r-1][c-1] + result[r-1][c])
        result.append(temp)

    return result
