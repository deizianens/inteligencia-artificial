import sys
import numpy as np
import random
from board import Board
from game import Game

direction = ('U', 'D', 'R', 'L')  # UP, DOWN, RIGHT, LEFT

'''
The q.txt file should show the value of ALL the state-action pairs in the world (for states
non-terminal). Each action-state pair must be printed on a line in the following format:

line, column, action, value
'''
def create_q_txt(maze, q):
    with open('q.txt', 'w') as f:
        for i, line in enumerate(maze):
            for j, element in enumerate(line):
                if element == '-':
                    for action, q_value in zip(direction, q[i][j]):
                        f.write('%d,%d,%s,%f\n' % (i, j, action, q_value))


'''
The pi.txt file must have the action dictated by its policy for each non-terminal state of the
world. The content of the file is the world itself, replacing non-terminal states with a
character corresponds to the action dictated by the policy (terminal states and walls are maintained).
'''
def create_pi_txt(maze, q):
    with open('pi.txt', 'w') as f:
        for i, line in enumerate(maze):
            for j, element in enumerate(line):
                if element == '-':
                    f.write(direction[np.argmax(q[i][j])])
                else:
                    f.write(element)
            f.write('\n')


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
  maze = Board(aux, lines, columns)         # create maze read by file
  print(maze.get_tiles())
  gama = 0.9                # discount rate
  game = Game(maze, alpha, epsilon, n_episodes, gama)
  q_learning = game.play()

  create_q_txt(maze, q_learning)
  create_pi_txt(maze, q_learning)


# Execute solver only when running this module
if __name__ == "__main__":
  if(len(sys.argv) == 5):
    file_ = sys.argv[1]           # maze file
    alpha = float(sys.argv[2])      # learning rate
    epsilon = float(sys.argv[3])    # exploration factor
    n_episodes = int(sys.argv[4]) # number of episodes
  else:
    print("Parâmetros indefinidos!")
    sys.exit()

  main(file_, alpha, epsilon, n_episodes)