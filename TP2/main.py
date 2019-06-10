from board import Board
# import numpy as np

def main():
  # initial puzzle
  with open("pacmaze.txt", 'r') as f:
      l = f.readline() # read first line (lines x columns)
      l = l.split()
      lines = int(l[0])
      columns = int(l[1])
      aux = []
      for _ in range(lines):
        l = f.readline()
        for j in range(columns):
          aux.append(l[j])

  maze = Board(aux)
  print(maze.get_tiles())
      

# Execute solver only when running this module
if __name__ == "__main__":
  main()