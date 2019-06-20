import sys
import numpy as np
import random
from board import Board
from game import Game
    
def main(file_, alpha, epsilon, n_episodes):
  # initial puzzle
  with open(file_, 'r') as f:
      l = f.readline() # read first line (lines x columns)
      l = l.split()
      lines = int(l[0])
      columns = int(l[1])
      aux = []
      for _ in range(lines):
        l = f.readline()
        for j in range(columns):
          aux.append(l[j])

  f.close()
  maze = Board(aux)         # create maze read by file
  gama = 0.9                # discount rate
  q_learning = Game(maze, alpha, epsilon, n_episodes, gama)


# Execute solver only when running this module
if __name__ == "__main__":
  try:
    file_ = sys.argv[1]       # maze file
    alpha = sys.argv[2]       # learning rate
    epsilon = sys.argv[3]     # exploration factor
    n_episodes = sys.argv[4]  # number of episodes
  except:
    print("Parâmetros indefinidos!")
    sys.exit()

  main(file_, alpha, epsilon, n_episodes)