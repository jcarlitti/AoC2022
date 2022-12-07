def partOne():
  counter = 4
  with open("text.txt", "r") as f:
    data = f.read()
  for i in range(0, len(data)):
    if len(set(data[i:i+4])) == 4:
      break
    counter += 1
  return counter

def partTwo():
  counter = 14
  with open("text.txt", "r") as f:
    data = f.read()
  for i in range(0, len(data)):
    if len(set(data[i:i+14])) == 14:
      break
    counter += 1
  return counter

def main():
  print(partOne())
  print(partTwo())

main()
