#!/usr/bin/python3
"""Log parsing script."""
import sys

total_sz = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
iterat = 0


def print_stats():
    """Function that prints resume of stats."""
    print("File size: {}".format(total_sz))
    for l, m in sorted(codes.items()):
        if m is not 0:
            print("{}: {}".format(l, m))


try:
    for line in sys.stdin:
        line = line.split()
        if len(line) >= 2:
            temp = iterat
            if line[-2] in codes:
                codes[line[-2]] += 1
                iterat += 1
            try:
                total_sz += int(line[-1])
                if temp == iterat:
                    iterat += 1
            except:
                if temp == iterat:
                    continue

        if iterat % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()

