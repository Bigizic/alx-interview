#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print(isWinner(3, [4, 5, 1]))
print(isWinner(4, [11, 2, 1, 1]))
print(isWinner(1, [10000]))
