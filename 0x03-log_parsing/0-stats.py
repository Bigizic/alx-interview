#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics
"""

import sys

output = sys.stdin


def log_parsing():
    """implementation
    """
    big_list = []
    total_items = 0
    status_count = {}

    try:
        for line in output:
            data = line.strip().split()
            log_helper(data, big_list, total_items, status_count)

    except KeyboardInterrupt:
        return


def log_helper(data, big_list, total_items, status_count):
    """Helper function for log_parsing
    """
    status_code = int(data[-2])
    file_size = int(data[-1])

    if isinstance(status_code, int) and isinstance(file_size, int):
        my_dict = {'status_code': status_code, 'file_size': file_size}
        big_list.append(my_dict)
        # print(f'{status_code}: {file_size}')

        if len(big_list) == 10:
            for items in big_list:
                total_items += items.get('file_size')
                code = items.get('status_code')
                status_count[code] = status_count.get(code, 0) + 1
            print(f'File size: {total_items}')

            """for items in big_list:
            print('{}: {}'.format(items.get('status_code'),
            items.get('file_size')))"""

            for key_code, val_count in sorted(status_count.items()):
                print(f'{key_code}: {val_count}')
            print(big_list)
            big_list.clear()
            # status_code.clear()


if __name__ == '__main__':
    log_parsing()
