def driver():
  print(partOne())
  print(partTwo())
  print(partOneExt())
  print(partTwoExt())

def partOne():
  total = 0
  fSet = set()
  secSet = set()
  f = open("text.txt", "r")
  lines = f.readlines()
  for line in lines:
    line = line.split(",")
    firstElf = line[0].split("-")
    secondElf = line[1].split("-")
    for i in range(int(firstElf[0]), int(firstElf[1]) + 1):
      fSet.add(i)
    for i in range(int(secondElf[0]), int(secondElf[1]) + 1):
      secSet.add(i)
    result = fSet.intersection(secSet)
    if result == fSet or result == secSet:
      total += 1
    fSet.clear()
    secSet.clear()
  return total

def partTwo():
  total = 0
  fSet = set()
  secSet = set()
  f = open("text.txt", "r")
  lines = f.readlines()
  for line in lines:
    line = line.split(",")
    firstElf = line[0].split("-")
    secondElf = line[1].split("-")
    for i in range(int(firstElf[0]), int(firstElf[1]) + 1):
      fSet.add(i)
    for i in range(int(secondElf[0]), int(secondElf[1]) + 1):
      secSet.add(i)
    result = fSet.intersection(secSet)
    if result:
      total += 1
    fSet.clear()
    secSet.clear()
  return total

def partOneExt():
  total = 0
  f = open("text.txt", "r")
  lines = f.readlines()
  for line in lines:
    line = line.split(",")
    firstElf = line[0].split("-")
    secondElf = line[1].split("-")
    if(int(firstElf[0]) >= int(secondElf[0]) and int(firstElf[1]) <= int(secondElf[1])) or (int(secondElf[0]) >= int(firstElf[0]) and int(secondElf[1]) <= int(firstElf[1])):
      total += 1
  return total  

def partTwoExt():
  total = 0
  f = open("text.txt", "r")
  lines = f.readlines()
  for line in lines:
    line = line.split(",")
    firstElf = line[0].split("-")
    secondElf = line[1].split("-")
    if ( int(firstElf[1]) >= int(secondElf[0]) and int(secondElf[1]) >= int(firstElf[0])):
      total += 1
  return total 

def main():
  driver()

main()
