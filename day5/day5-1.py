# https://adventofcode.com/2024/day/5

import math
import sys

file_name = sys.argv[1]

class Rule:
  value: int
  before: list[int]
  after: list[int]

  def __init__(self, value: int):
    self.value = value
    self.before = []
    self.after = []

class Ruleset:
  rules: dict[Rule]

  def __init__(self):
    self.rules = {}
  
  def get_or_create_rule(self, value: int) -> Rule: 
    if not value in self.rules:
      self.rules[value] = Rule(value)
    return self.rules[value]
  
  def add_rule(self, before: int, after: int):
    rule_before = self.get_or_create_rule(before)
    rule_after = self.get_or_create_rule(after)
    
    rule_before.after.append(after)
    rule_after.before.append(before)

with open(file_name, 'r', encoding='utf8') as file:
  rules = Ruleset() 
  pages = []
  valid_pages = []
  
  for line in file.readlines():
    if ('|' in line):
      (b, a) = line.strip().split('|')
      rules.add_rule(int(b), int(a))
    elif (',' in line):
      pages.append(list(map(int, line.strip().split(','))))
    
  for page in pages:
    is_valid = True
    for i in range(0, len(page) - 1):
      rule = rules.get_or_create_rule(page[i])
      is_valid = set(set(page[i+1:])).issubset(rule.after) and set(set(page[:i])).issubset(rule.before)
      if not is_valid:
        is_valid = False
        break
    if is_valid:
      valid_pages.append(page)

  result = 0
  for valid in valid_pages:
    result += valid[math.floor(len(valid)/2)]

  print(result)