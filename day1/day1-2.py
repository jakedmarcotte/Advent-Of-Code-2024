# https://adventofcode.com/2024/day/1

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:

    left = []
    right = []
    total = 0

    for line in file:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)


    for l in left:
      similarity = l * right.count(l)
      total += similarity

    print(total)