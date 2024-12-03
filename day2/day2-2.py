# https://adventofcode.com/2024/day/2

import sys

file_name = sys.argv[1]

def determine_safety(report, isIncreasing):
  # start at 1 to compare prev and next
  for i in range(1, len(report) - 1):
    before = int(report[i - 1])
    curr = int(report[i])
    next = int(report[i + 1])
    # any two consecutive numbers are the same
    if (curr == before or curr == next):
      return (False, i)
    # increases then decreases
    if (before < curr and curr > next):
      return (False, i)
    # decreases then increases
    elif (before > curr and curr < next): 
      return (False, i)
    # difference between two consecutive numbers is greater than 3
    elif (abs(curr - next) > 3 or abs(curr - before) > 3):
      return (False, i)
    # reached the end of the report
    if (i == len(report) - 2):
      return (True, i)

with open(file_name, 'r', encoding='utf8') as file:
    safeCount = 0
    results = []
    for line in file:
        ogReport = line.split()
        numOfTries = len(ogReport)
        # attempt report without removal
        (isSafe, index) = determine_safety(ogReport, True)
        if isSafe:
          results.append((ogReport, isSafe))
          safeCount += 1
          continue
        # attempt to remove each number and check if the report is safe
        for n in range(numOfTries):
          increport = ogReport.copy()
          increport.pop(n)
          # print('try', n, increport)
          (isSafe, index) = determine_safety(increport, True)
          # print(isSafe, index)
          if (isSafe):
            safeCount += 1
            break
        results.append((ogReport, isSafe))
        
    # 328 is correct
    print(safeCount)