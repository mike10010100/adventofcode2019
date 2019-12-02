import math

if __name__ == "__main__":
  input = open("input.txt",'r')

  sum = 0

  for line in input:
    mass = int(line)
    fuel = math.floor(mass/3)-2
    sum += fuel
  
  print(sum)