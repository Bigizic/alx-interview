#!/usr/bin/python3
"""Minimum Operations
@param (n): <int>

Return: <int> fewest number of operation need to result in exactly n of H
"""

"""def mudo(n, d=2):
    if n % d == 0:
        return d
    else:
        return mudo(n, d + 1)"""


def mudo(n):
    """ Implementation """
    my_list = []
    result = []
    for i in range(n):
        my_list.append(i)
    my_list.pop(0)
    my_list.pop(0)
    for x in my_list:
        if n % x == 0:
            result.append(x)

    return result


def minOperations(n):
    """ implementation """
    cut = mudo(n)
    if len(cut) > 1:
        return len(cut) + cut[1]
    else:
        return cut[0] * 2


"""def minOperations(n):
    if n <= 1:
        return 0
    charH = ['H']
    c = copyAll(charH)
    my_list = ['C']
    M = mudo(n)

    for _ in range(M - 1):
        paste(charH)
        my_list.append('P')

    my_list.append('C')
    c = copyAll(charH)
    return my_list



    if n % len(charH) == 0:
        i = n / len(charH)
        for _ in range(i):
            c = copyAll(charH)
            paste(c, charH)

    if len(charH) == n:
        return count
    else:
        count = operations(n, charH)"""


def copyAll(charH):
    return len(charH)


def paste(charH, c):
    if c:
        for _ in range(c):
            charH.append(charH[0])

    charH.append(charH[0])


def pasteAll(c, charH):
    for _ in range(c):
        charH.append(charH[0])


def operations(n, charH, count=0):
    for _ in range(n):
        c = copyAll(charH)
        count += 1
        paste(c, charH)

    return operations(n, charH, count)
