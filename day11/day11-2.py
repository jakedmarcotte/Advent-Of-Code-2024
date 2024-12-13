# https://adventofcode.com/2024/day/11

import sys
from functools import cache

file_name = sys.argv[1]

blinks = 75

@cache
def explore_stone(stone) -> list[int]:
  if stone == 0:
    return [1]
  
  stringified = str(stone)
  length = len(stringified)
  if length % 2 == 0:
    i = length // 2
    return [int(stringified[:i]), int(stringified[i:])]
  
  return [stone * 2024]
  
@cache
def count_stones(stone: int, b: int):
  if b == 0:
    return 1
  
  new_stones = explore_stone(stone)
  return sum(count_stones(num, b - 1) for num in new_stones)

with open(file_name, 'r', encoding='utf8') as file:
  stones = list(map(int, file.readline().split(' ')))
  count = 0
  
  for s in range(len(stones)):
    count += count_stones(stones[s], blinks)
    print('count:', count)
