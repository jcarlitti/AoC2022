def func():
  f = open("text.txt", "r")
  f.readline()
  total = 0
  elfNum = 1
  elfDict = {}
  for i in f:
    if(i != '\n'):
      total += int(i)
    else:
      elfNum += 1
      total = 0
      continue
    elfDict[str(elfNum)] = total
  print(elfDict[getMax(elfDict)])
  print(topThree(elfDict))

def getMax(dict):
  return max(dict, key = lambda k: dict[k])

def topThree(dict):
  total = 0
  for i in sorted(dict, key=dict.get, reverse=True)[:3]:
    total += int(dict[i])
  return total

def main():
  func()

main()
