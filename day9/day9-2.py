# https://adventofcode.com/2024/day/9

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:
  file_block = list(str())
  id = step = fragments = 0

  for digit in file.read():
    is_id = step % 2 == 0
    block = ''
    for i in range(int(digit)):
      if is_id:
        block = str(id)
      else:
        block = '.'
        fragments += 1
      file_block.append(block)
    if is_id:
      id += 1
    step += 1

  print(''.join(file_block))
  # print(file_block)

  space = 0
  curr_id = id - 1
  id_len = 0
  for pos in range(len(file_block) - 1, 0, -1):
    
    print('curr', curr_id, file_block[pos])
    if file_block[pos] != str(curr_id):
      if id_len > 0:
        for i in range(len(file_block)):
          print('space', space, i)
          if id_len <= space:
            print('id_len', id_len, i)
            for c in range(i - id_len, i):
              # print('whoa')
              print('c', c, file_block[c], curr_id)
              file_block[c] = str(curr_id)
              # file_block[pos] = '.'
            for p in range(pos + 1, pos + id_len + 1):
              file_block[p] = '.'
              curr_id -= 1
              id_len = 0
            break
          elif file_block[i] == '.':
            space += 1
          else:
            space = 0
      # curr_id -= 1
      # id_len = 0
    elif file_block[pos] == str(curr_id):
      id_len += 1
    elif file_block[pos] == '.':
      space = 0

    # continue
    
    print(''.join(file_block))
    # print(file_block)
    
  checksum = 0
  for idx, file in enumerate(file_block):
    if '.' in file:
      break
    checksum += idx * int(file)
  print(checksum)
