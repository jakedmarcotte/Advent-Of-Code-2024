# https://adventofcode.com/2024/day/9

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:
  file_block = []
  id = step = fragments = 0

  for digit in file.read():
    is_id = step % 2 == 0
    
    for i in range(int(digit)):
      if is_id:
        file_block.append(str(id))
      else:
        file_block.append('.')
        fragments += 1
    if is_id:
      id += 1
    step += 1

  for pos in range(len(file_block) - 1, fragments, -1):
    if file_block.index('.') >= pos:
      break
    m = file_block[pos]
    if not m == '.':
      file_block[file_block.index('.')] = m
      file_block[pos] = '.'
    
  checksum = 0
  for idx, file in enumerate(file_block):
    if file == '.':
      break
    checksum += idx * int(file)
  print(checksum)
