#!/usr/bin/python3
"""Rotate 2D Matrix Solution
"""


def rotate_2d_matrix(matrix):
    """function attempts to rotate a n by n nested list to 90 deg

    for each set in matrix the index of each sets are taken for each rows
    and appends the integers in sm, then creates a nested list of each
    element in sm to align it in a n by n nested list cuz sm contains each
    element in matrix in a long list and not nested

    e.g of sm: [1, 4, 7, 2, 5, 8, 3, 6, 9]

    e.g of s: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    e.g of temp: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix[0 to 2 + 1] = temp
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
