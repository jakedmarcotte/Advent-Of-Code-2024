# https://adventofcode.com/2024/day/4

import re
import sys

file_name = sys.argv[1]

def check_backslash(letters, x, y):
  return (letters[x - 1][y - 1] == 'S' and letters[x + 1][y + 1] == 'M') or (letters[x - 1][y - 1] == 'M' and letters[x + 1][y + 1] == 'S')

def check_forward_slash(letters, x, y):
  return (letters[x + 1][y - 1] == 'S' and letters[x - 1][y + 1] == 'M') or (letters[x + 1][y - 1] == 'M' and letters[x - 1][y + 1] == 'S')

with open(file_name, 'r', encoding='utf8') as file:
  letters = []
  total = 0
  for line in file.readlines():
    letters.append(list(line.strip()))
  
  for x in range(1, len(letters) - 1):
    for y in range(1, len(letters) - 1):
      if letters[x][y] == 'A' and check_backslash(letters, x, y) and check_forward_slash(letters, x, y):
        total += 1

  print(total)
    