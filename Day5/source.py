from collections import deque
import re

def driver():
  stack = dict([(key, []) for key in range(1,10)])
  data, instr = parseData(stack)
  #print(partOne(data, instr)) #Uncomment to run partOne
  print(partTwo(data, instr))

def parseData(stack):
  with open("text.txt") as f:
    data = f.read().split("\n\n")
    chart = data[0].splitlines()[:-1]
    instructions = data[1].splitlines()
  for row in chart:
    for j in range(1, len(row), 4):
      pos = j // 4 + 1
      if row[j] != " ":
        stack[pos].append(row[j])
  return stack, instructions

def partOne(stack, instr):
  for line in instr:
    loc = line.rstrip().split(" ")
    for i in range(0, int(loc[1])):
      stack[int(loc[5])].insert(0, stack[int(loc[3])].pop(0))
  #return ''.join([value[len(value)-1] for (key, value) in stack.items()]) 
  finalStr = ""
  for key in stack.keys():
    finalStr += stack[key][0]
  return finalStr

def partTwo(stack, instr):
  for line in instr:
    loc = line.rstrip().split(" ")
    stack[int(loc[5])] = stack[int(loc[3])][:int(loc[1])]+stack[int(loc[5])]
    stack[int(loc[3])] = stack[int(loc[3])][int(loc[1]):]
  finalStr = ""
  for key in stack.keys():
    finalStr += stack[key][0]
  return finalStr

def main():
  driver()

main()
