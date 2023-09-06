#!/usr/bin/python3
for phabet in range(97, 123):
    alpha = chr(phabet)
    if phabet != 113 and phabet != 101:
        print("{}".format(alpha), end='')
