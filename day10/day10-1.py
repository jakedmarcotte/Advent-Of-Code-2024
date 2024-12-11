# https://adventofcode.com/2024/day/10

import sys

file_name = sys.argv[1]

discovered = set()

def explore_trail(map, y, x, h): 
  if y < 0 or y >= len(map) or x < 0 or x >= len(map[y]):
    return 
  elif map[y][x] != h:
    return
  elif map[y][x] == 9:
    discovered.add((y, x))
    return
  return explore_trail(map, y - 1, x, h + 1), explore_trail(map, y + 1, x, h + 1), explore_trail(map, y, x - 1, h + 1), explore_trail(map, y, x + 1, h + 1)

with open(file_name, 'r', encoding='utf8') as file:
  map = []
  score = 0

  for line in file.readlines():
    row = []
    for h in line.strip():
      row.append(int(h))
    map.append(row)

  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x] == 0:
        discovered = set()
        explore_trail(map, y, x, 0)
        score += len(discovered)
  
  print(score)