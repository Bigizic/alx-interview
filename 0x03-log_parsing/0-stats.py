#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics
"""

import sys


def log_dict(data, ctrlC=None):
    """parse the striped and splited list for the status_code and file_size
    @param (data): <list>

    Return: void
    """
    big_list = []
    total_items = 0
    status_count = {}

    status_code = int(data[-2])
    file_size = int(data[-1])

    if isinstance(status_code, int) and isinstance(file_size, int):
        my_dict = {'status_code': status_code, 'file_size': file_size}
        big_list.append(my_dict)
        print(f'{status_code}: {file_size}')

        if len(big_list) == 10:
            for items in big_list:
                total_items += items.get('file_size')
                code = items.get('status_code')
                status_count[code] = status_count.get(code, 0) + 1
            print(f'File size: {total_items}')

            for key_code, val_count in sorted(status_count.items()):
                print(f'{key_code}: {val_count}')
            big_list.clear()
            # status_code.clear()
        if ctrlC:
            sys.exit(1)


def log_parsing():
    """Implementation
    """
    for line in sys.stdin:
        try:
            data = line.strip().split()
            log_dict(data)

            """for items in big_list:
            print('{}: {}'.format(items.get('status_code'),
            items.get('file_size')))"""
        except KeyboardInterrupt:
            data = line.strip().split()
            log_dict(data, True)


if __name__ == '__main__':
    log_parsing()
