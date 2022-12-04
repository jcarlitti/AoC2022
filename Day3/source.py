def driver():
  print(partOne())
  print(partTwo())

def partOne():
  total = 0 
  alphaList = [chr(i) for i in range(97, 97+26)]
  alphaList.extend([chr(i) for i in range(65, 65+26)])
  f = open("text.txt", "r")
  file = f.read().splitlines()
  for line in file:
    fhalf, bhalf = line[:len(line)//2], line[len(line)//2:]
    intersection = set([value for value in list(fhalf) if value in list(bhalf)])
    total += alphaList.index(list(intersection)[0]) + 1
  return total 

def partTwo():
  total = 0
  alphaList = [chr(i) for i in range(97, 97+26)]
  alphaList.extend([chr(i) for i in range(65, 65+26)])
  f = open("text.txt", "r")
  file = f.read().splitlines()
  n = len(file)
  for i in range(0, n, 3):
    one, two, three = file[i], file[i+1], file[i+2]
    intersection = set(one).intersection(set(two), set(three))
    total += alphaList.index(intersection.pop()) + 1
  return total

def main():
  driver()

main()
