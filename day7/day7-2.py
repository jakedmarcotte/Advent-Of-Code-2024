# https://adventofcode.com/2024/day/7

import sys

file_name = sys.argv[1]

def to_ternary(n):
  if n == 0:
    return "0"

  result = ""
  while n > 0:
    result = str(n % 3) + result
    n //= 3

  return result

with open(file_name, 'r', encoding='utf8') as file:
  calibrations = []
  
  for line in file.readlines():
    (total, sequence) = line.strip().split(':')
    sequence = sequence.strip()
    num_of_operators = sequence.count(' ')
    
    for i in range(3**num_of_operators):
      seq = sequence
      op_str = to_ternary(i).zfill(num_of_operators)
      nums = list(map(int, seq.split(' ')))
      val = nums[0]
      for (num, op) in zip(nums[1:], op_str):
        # 0 represents a + operator
        if op == '0':
          val += num
        elif op == '1':
          val *= num
        else:
          val = int(str(val) + str(num))
      if val == int(total):
        calibrations.append(val)
        break
    
  print(calibrations, sum(calibrations))
