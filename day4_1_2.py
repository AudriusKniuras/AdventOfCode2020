import sys
import re

f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]
input.append('')

f.close()


data = []
passport = {}

for line in input:
  if line != "":
    info = line.split()
    for single_info in info:
      key, value = single_info.split(':')
      passport[key] = value
  else:
    if all(keys in passport.keys() for keys in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
      data.append(passport)
    passport = {}

print(f'part1: {len(data)}')

p2_value = 0
## PART 2
m = ""
for d in data:
  m = re.match(r"[0-9]{4}\b", d['byr'])
  if m:
    m = int(m.group(0))
    if not (m >= 1920 and m <= 2002):
      continue
  m = re.match(r"[0-9]{4}\b", d['iyr'])
  if m:
    m = int(m.group(0))
    if not (m >= 2010 and m <= 2020):
      continue
  m = re.match(r"[0-9]{4}\b", d['eyr'])
  if m:
    m = int(m.group(0))
    if not (m >= 2020 and m <= 2030):
      continue
  m1 = re.match(r"[0-9]{3}cm\b", d['hgt'])
  m2 = re.match(r"[0-9]{2}in\b", d['hgt'])
  if m1 or m2:
    if m1:
      cm = int(m1.group(0).split("cm")[0])
      if not (cm >= 150 and cm <= 193):
        continue
    if m2:
      inch = int(m2.group(0).split("in")[0])
      if not (inch >= 59 and inch <= 76):
        continue
  else:
    continue
  m = re.match(r"#[0-9a-f]{6}\b", d['hcl'])
  if not m:
    continue
  if not any(x in d['ecl'] for x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
    continue
  m = re.match(r"[0-9]{9}\b", d['pid'])
  if not m:
    continue
  p2_value += 1

print(f'part2: {p2_value}')
  
  
  # else:
  #   print(d['byr'])