#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [
    [1],    # Box 0 has a key to Box 1
    [],     # Box 1 has no keys
    [2],    # Box 2 has a key to Box 3
    [],     # Box 3 has no keys
    [0]     # Box 4 has a key to Box 0
]
print(canUnlockAll(boxes))

print(canUnlockAll([]))

print(canUnlockAll([[], []]))

print(canUnlockAll([[1], []]))

print(canUnlockAll([[], [1]]))

print(canUnlockAll([[1], [3, 4], [1], [4], [5], [], [], [], []]))

print(canUnlockAll([[1], [3, 4], [1], [4], [5], [], []]))

print(canUnlockAll([[1], [3, 4], [1], [4], [5], [], [], []]))

print(canUnlockAll([[], [3, 4], [1], [4], [5], [], []]))

print(canUnlockAll([[], [3, 4], [1], [4], [5]]))

print(canUnlockAll([[1], [0], [1], [4], [5]]))

print(canUnlockAll([[0], [0], [0], [0]]))
