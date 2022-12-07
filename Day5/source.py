def parseData():
  with open("text.txt", "r") as f:
    data = f.read()
  data = data.split("\n\n")
  chart = data[0].splitlines()[:-1] 
  instr = data[1].splitlines()
  return chart, instr

def partOne(chart, instr):
  stack = dict([(key, []) for key in range(1, 10)])
  for row in chart:
    for j in range(1, len(row), 4):
      pos = j // 4 + 1
      if row[j] != ' ':
        stack[pos].append(row[j])
  for line in instr:
    line = [int(i) for i in line.split() if i.isdigit()]
    for i in range(0, line[0]):
      stack[line[2]].insert(0, stack[line[1]].pop(0))
  final_str = ""
  for key in stack.keys():
    final_str += stack[key][0] 
  return final_str

def partTwo(chart, instr):
  stack = dict([(key, []) for key in range(1,10)])
  for row in chart:
    for j in range(1, len(row), 4):
      pos = j // 4 + 1
      if(row[j] != " "):
        stack[pos].append(row[j])
  for line in instr:
    line = [int(i) for i in line.split() if i.isdigit()]
    stack[line[2]] = stack[line[1]][:line[0]] + stack[line[2]]
    stack[line[1]] = stack[line[1]][line[0]:]
  final_str = ""
  for key in stack.keys():
    final_str += stack[key][0]
  return final_str

def main():
  chart, instr = parseData()
  print(partOne(chart, instr))
  print(partTwo(chart, instr))

main()
