# https://adventofcode.com/2024/day/11

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:
  blinks = 20
  stones = list(map(int, file.readline().split(' ')))

  for b in range(blinks):
    s = 0
    while s < len(stones):
      stone = stones[s]
      length = len(str(stone))
      if stone == 0:
        stones[s] = 1
        s += 1
      elif length % 2 == 0:
        stones.insert(s, int(str(stone)[length // 2:]))
        stones.insert(s, int(str(stone)[:length // 2]))
        stones.pop(s + 2)
        s += 2
      else:
        stones[s] = stone * 2024
        s += 1

    print('Blink ' + str(b + 1) + ' stones:', len(stones))
    print('count 1: ', stones.count(1))
