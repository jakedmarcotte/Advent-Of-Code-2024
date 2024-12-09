# https://adventofcode.com/2024/day/6

import sys
import copy


file_name = sys.argv[1]

def print_board(board):
  for row in board:
    print(''.join(row))

def check_out_of_bounds(x, y, max_x, max_y):
  return x < 0 or x > max_x or y < 0 or y > max_y

def check_turn_for_loops(board, x, y, dx, dy):
  og_x = x
  og_y = y
  next_y = dx
  next_x = -dy
  board[y + dy][x + dx] = 'O'
  origin_crosses = -1
  while True:
    # current_position = board[y][x]
    # if current_position == '.':
    #   board[y][x] = '|' if abs(dy) > 0 else '-'
    # elif current_position == '|' and current_position == '-':
    #   board[y][x] = '+'
    move_x = x + next_x
    move_y = y + next_y
    # print('crosses', origin_crosses)
    print('og', og_x, og_y)
    print('curr', x, y)
    # print('move', move_x, move_y)
    # print(x, y, move_x, move_y)
    print_board(board)
    if x == og_x and y == og_y: 
      origin_crosses += 1
    if check_out_of_bounds(move_x, move_y, max_x, max_y):
      return False
    elif origin_crosses > 0:
      print_board(board)
      return True
    elif board[move_y][move_x] in ['#', 'O']:
      # rotate
      if (board[y][x] != '^'):
        board[y][x] = '+'
      new_x = -next_y
      new_y = next_x
      next_x = new_x
      next_y = new_y
      x = x + next_x
      y = y + next_y
    else:
      # board[y][x] = 'X'
      x = x + next_x
      y = y + next_y

with open(file_name, 'r', encoding='utf8') as file:
  board = []
  curr_x = curr_y = 0
  dx = 0
  dy = -1
  loops = 0
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
    if current_position == '.':
      board[curr_y][curr_x] = '|' if abs(dy) > 0 else '-'
    elif current_position == '|' or current_position == '-':
      board[curr_y][curr_x] = '+'
    move_x = curr_x + dx
    move_y = curr_y + dy
    # check for obstacles
    if move_x < 0 or move_x > max_x or move_y < 0 or move_y > max_y:
      escaped = True
      break
    elif board[move_y][move_x] == '#':
      # rotate
      if (board[curr_y][curr_x] != '^'):
        board[curr_y][curr_x] = '+'
      new_x = -dy
      new_y = dx
      dx = new_x
      dy = new_y
      curr_x = curr_x + dx
      curr_y = curr_y + dy
    elif board[move_y + dx][move_x - dy] in ['|', '-', '+']:
      curr_x = move_x
      curr_y = move_y
      copy_board = copy.deepcopy(board)
      is_loop = check_turn_for_loops(copy_board, curr_x, curr_y, dx, -dy)
      if is_loop:
        loops += 1
        print(loops)
      # break
    else:
      curr_x = move_x
      curr_y = move_y
  # print_board(board)
  print(loops)
