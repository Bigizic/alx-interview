#!/usr/bin/python3
"""function that validates if a given data set is UTF-8 encodable
"""


def validUTF8(data):
    """@param (data): <list>
    Return: True if data is valid UTF-8 encodable otherwise false
    """
    count = 0
    for item in data:
        if count == 0:
            if (item >> 7) == 0b0:
                continue
            elif (item >> 5) == 0b110:
                count = 1
            elif (item >> 4) == 0b1110:
                count = 2
            elif (item >> 3) == 0b11110:
                count = 3
            """else:
                return False"""
        else:
            if (item >> 6) != 0b10:
                return False
            count -= 1

    return count == 0
