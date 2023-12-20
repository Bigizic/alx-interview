#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics
"""

import sys
import json


def log_parsing():
    """Implementation
    """
    big_list = []
    total_items = 0
    status_count = {}
    for line in sys.stdin:
        data = line.strip().split()
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

                big_list.clear()
                # status_count.clear()


if __name__ == '__main__':
    log_parsing()
