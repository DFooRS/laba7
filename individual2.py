#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(float, input().split()))

    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    negative_mult = 1
    for i, item in enumerate(a):
        if item < 0:
            negative_mult *= item

    max_a = a[0]
    index_max_a = 0
    for i, item in enumerate(a):
        if item > max_a:
            max_a = item
            index_max_a = i
    a = a[:index_max_a]

    positive_count = 0
    for i, item in enumerate(a):
        if item > 0:
            positive_count += item

    print(negative_mult)
    print(positive_count)
