# https://adventofcode.com/2024/day/3

import re
import sys

file_name = sys.argv[1]

def extract_mul_nums(s):
  return s.replace('mul(', '').replace(')', '').split(',')

with open(file_name, 'r', encoding='utf8') as file:
  occurrences = re.findall(r'mul\(\d+,\d+\)', file.read())
  total = 0
  for o in occurrences:
    (a, b) = extract_mul_nums(o)
    # print(a, b)
    total += (int(a) * int(b))
  print(total)