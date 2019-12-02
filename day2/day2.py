import csv

if __name__ == "__main__":

  memory = []
  with open("input.txt") as csvfile:
     memory = [list(map(int,rec)) for rec in csv.reader(csvfile, delimiter=',')][0]
  print(memory)

  program_counter = 0
  while memory[program_counter] != 99:
    if memory[program_counter] == 1:
      memory[memory[program_counter+3]] = memory[memory[program_counter+1]] + memory[memory[program_counter+2]]

    elif memory[program_counter] == 2:
      memory[memory[program_counter+3]] = memory[memory[program_counter+1]] * memory[memory[program_counter+2]]
    
    program_counter+=4

  print(memory)
  print(memory[0])