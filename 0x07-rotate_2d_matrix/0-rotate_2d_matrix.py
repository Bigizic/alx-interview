#!/usr/bin/python3
"""Rotate 2D Matrix Solution
"""


def rotate_2d_matrix(matrix):
    """Implementation
    """
    m_len = len(matrix) - 1
    sm = []
    for _ in range(len(matrix)):
        for sets in matrix:
            sm.append(sets[_])
    s = [sm[i:i+len(matrix)] for i in range(0, len(sm), len(matrix))]
    temp = []
    for i in s:
        temp.append(i[::-1])
    matrix[0:m_len + 1] = temp
