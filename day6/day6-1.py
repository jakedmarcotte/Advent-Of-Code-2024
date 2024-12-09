# https://adventofcode.com/2024/day/6

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:
  board = []
  curr_x = curr_y = 0
  dx = 0
  dy = -1
  visits = 0
  for line in file.readlines():
    board.append(list(line.strip()))
    if '^' in line:
      curr_x = line.index('^')
      curr_y = len(board) - 1

  # square grid
  max_y = max_x = len(board) - 1

  escaped = False

  while not escaped:
    current_position = board[curr_y][curr_x]
    if current_position == '.' or current_position == '^':
      board[curr_y][curr_x] = 'X'
      visits += 1
    move_x = curr_x + dx
    move_y = curr_y + dy
    # check for obstacles
    if move_x < 0 or move_x > max_x or move_y < 0 or move_y > max_y:
      escaped = True
      break
    elif board[move_y][move_x] == '#':
      # rotate
      new_x = -dy
      new_y = dx
      dx = new_x
      dy = new_y
      curr_x = curr_x + dx
      curr_y = curr_y + dy
    else: 
      curr_x = move_x
      curr_y = move_y
  
  for row in board:
    print(''.join(row))

  print(visits)
