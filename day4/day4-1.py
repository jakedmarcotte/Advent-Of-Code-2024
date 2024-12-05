# https://adventofcode.com/2024/day/4

import re
import sys

file_name = sys.argv[1]

letter_dict = ['X', 'M', 'A', 'S']

def check(letters, x, y, l, dx, dy):
  max_i = len(letters) - 1
  if letters[x][y] == letter_dict[letter_dict.index('S')] == letter_dict[l]:
    return 1
  elif 0 <= x + dx <= max_i and 0 <= y + dy <= max_i and letters[x + dx][y + dy] == letter_dict[l + 1]:
    return check(letters, x + dx, y + dy, l + 1, dx, dy)
  else:
    return 0

with open(file_name, 'r', encoding='utf8') as file:
  letters = []
  total = 0
  for line in file.readlines():
    letters.append(list(line.strip()))
  
  for x in range(len(letters)):
    for y in range(len(letters)):
      if letters[x][y] == 'X':
        total += (check(letters, x, y, letter_dict.index('X'), -1, -1)
        + check(letters, x, y, letter_dict.index('X'), -1, 0)
        + check(letters, x, y, letter_dict.index('X'), -1, 1)
        + check(letters, x, y, letter_dict.index('X'), 0, -1)
        + check(letters, x, y, letter_dict.index('X'), 0, 1)
        + check(letters, x, y, letter_dict.index('X'), 1, -1)
        + check(letters, x, y, letter_dict.index('X'), 1, 0)
        + check(letters, x, y, letter_dict.index('X'), 1, 1))

  print(total)
    