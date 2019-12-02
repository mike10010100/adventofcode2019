import csv

if __name__ == "__main__":

  for noun in range(0,100):
    for verb in range(0,100):
      memory = []
      with open("input.txt") as csvfile:
        memory = [list(map(int,rec)) for rec in csv.reader(csvfile, delimiter=',')][0]
      memory[1] = noun
      memory[2] = verb

      program_counter = 0
      while memory[program_counter] != 99:
        if memory[program_counter] == 1:
          memory[memory[program_counter+3]] = memory[memory[program_counter+1]] + memory[memory[program_counter+2]]

        elif memory[program_counter] == 2:
          memory[memory[program_counter+3]] = memory[memory[program_counter+1]] * memory[memory[program_counter+2]]
        
        program_counter+=4

      if memory[0] == 19690720:
        print(100*noun+verb)