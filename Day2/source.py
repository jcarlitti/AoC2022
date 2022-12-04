def func():
  print(partOne())
  print(partTwo())

def partOne():
  total = 0
  finalScore = {"AX": 4, "AY": 8, "AZ":3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ":6}
  f = open("text.txt", "r")
  games = f.readlines()
  for l in games:
    l = l.replace(" ", "")
    total += finalScore[l[0]+l[1]]
  return total     

def partTwo():
  total = 0
  finalScore = {"AX": 4, "AY": 8, "AZ":3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ":6}
  f = open("text.txt", "r")
  games = f.readlines()
  for l in games:
    l = l.replace(" ", "")
    oppSelect = l[0]
    mySelect = l[1]  
    if(mySelect == "X"):
      if(oppSelect == "A"):
        mySelect = "Z"
      elif(oppSelect == "C"):
        mySelect = "Y"
    elif(mySelect == "Y"):
      if(oppSelect == "A"):
        mySelect = "X"
      elif(oppSelect == "C"):
        mySelect = "Z"
    else:
      if(oppSelect == "A"):
        mySelect = "Y"
      elif(oppSelect == "C"):
        mySelect = "X"
    total += finalScore[oppSelect + mySelect]
  return total

def main():
  func()

main()
