# https://adventofcode.com/2024/day/3

import re
import sys

file_name = sys.argv[1]

def extract_mul_nums(s):
  return s.replace('mul(', '').replace(')', '').split(',')

with open(file_name, 'r', encoding='utf8') as file:
  words = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', file.read())
  total = 0
  do = True
  for w in words:
    if w == "do()":
      do = True
    elif w == "don't()":
      do = False
    elif do:
      (a, b) = extract_mul_nums(w)
      total += (int(a) * int(b))
  print(total)