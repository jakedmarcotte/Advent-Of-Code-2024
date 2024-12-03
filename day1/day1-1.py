# https://adventofcode.com/2024/day/1

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:

    left = []
    right = []
    total = 0

    for line in file:
        l, r = map(int, line.split())
        left.append(int(l))
        right.append(int(r))
    
    left.sort()
    right.sort()

    for l, r in zip(left, right):
      total += abs(r - l)

    print(total)