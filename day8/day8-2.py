# https://adventofcode.com/2024/day/8

import sys
from collections import defaultdict

file_name = sys.argv[1]

def out_of_bounds(y, x, grid_size):
  return y < 0 or y >= grid_size or x < 0 or x >= grid_size

with open(file_name, 'r', encoding='utf8') as file:
  waves = []
  antinodes = set()

  for line in file.readlines():
    waves.append(list(line.strip()))

  freq = defaultdict(list)
  grid_size = len(waves)
  for y in range(grid_size):
    for x in range(grid_size):
      node = waves[y][x]
      if node != '.':
        freq[node].append((y, x))
  
  for f in freq:
    freqs = freq[f].copy()
    for i in range(len(freqs)):
      (y, x) = freqs[i]
      if len(freqs) > 2:
        antinodes.add((y, x))
      for (cy, cx) in freqs[:i] + freqs[i+1:]:
        dy = cy - y
        dx = cx - x
        new_y = y + dy * -1
        new_x = x + dx * -1

        while not out_of_bounds(new_y, new_x, grid_size):
          antinodes.add((new_y, new_x))

          if waves[new_y][new_x] == '.':
            waves[new_y][new_x] = '#'
          new_y = new_y + dy * -1
          new_x = new_x + dx * -1
            
  for wave in waves:
    print(''.join(wave))
  print(len(antinodes))
