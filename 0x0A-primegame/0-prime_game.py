#!/usr/bin/python3
"""Prime game solution
"""


def isEvenOrOdd(n: int) -> str:
    """Checks if a number is even or odd
    """
    if n % 2 == 0:
        return 'even'
    return 'odd'


def checkPrime(n: int) -> bool:
    """Checks if a number is a prime Number
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primeNumbers(n: int) -> list:
    """Returns a list of prime numbers starting from 2 to n
    Parameters:
        - @param {int} n: number to work on
    """
    if not isinstance(n, int) or n < 2:
        return []

    prime_list = [2]
    for i in range(3, n + 1, 2):
        if checkPrime(i):
            prime_list.append(i)

    return prime_list


def isWinner(x, nums):
    """Implementation
    """
    if x < 1 or not nums:
        return None
    myDict = []
    for i in nums:
        myDict.append(primeNumbers(i))
    p_index = 0
    Dict = {'Maria': [], 'Ben': []}
    Maria = []
    Ben = []
    for _ in range(x):
        for i in myDict[_]:
            if len(myDict[_]) == 1 and i is None:
                Ben.append('Winner')
        if isEvenOrOdd(len(myDict[_])) == 'odd' and i is not None:
            Maria.append('Winner')
        if isEvenOrOdd(len(myDict[_])) == 'even' and i is not None:
            Ben.append('Winner')
            """curr_p = Dict['Maria'] if p_index == 0 else Dict['Ben']
            if last_number == i and i != None:
                curr_p.append('Winner')
            if last_number == i and i == None:
                curr_p = Dict['Ben']
                curr_p.append('Winner')
            curr_p.append(i)
            p_index = (p_index + 1) % 2"""
    if Maria.count('Winner') == Ben.count('Winner'):
        return None
    return 'Maria' if Maria.count('Winner') > Ben.count('Winner') else 'Ben'
