# https://adventofcode.com/2024/day/2

import sys

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf8') as file:
    safeCount = 0
    for line in file:
        report = line.split()
        isIncreasing = True
        for i in range(len(report) - 1):
          curr = int(report[i])
          next = int(report[i + 1])
          if (curr == next):
            break
          if (i == 0):
            isIncreasing = True if curr < next else False
          if (isIncreasing and curr > next):
            break
          elif (not isIncreasing and curr < next): 
            break
          elif (abs(curr - next) > 3):
            break
          if (i == len(report) - 2):
            safeCount += 1
        
    print(safeCount)