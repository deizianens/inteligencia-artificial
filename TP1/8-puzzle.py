# encoding=UTF-8
'''
Deiziane Natani da Silva
2015121980

Código baseado em: https://github.com/rjoonas/AI-assignment-1
'''
from sys import stdout
import datetime as dt

from board import Board
from search import bfs, ids, ucs, astar, gbfs

def run_timed(algorithm, board, heuristic = None):
  # Write a dot to stdout every twenty thousand iterations.
  def anim(iterations):
    if (iterations % 20000 == 0):
      stdout.write("."); stdout.flush()

  start = dt.datetime.now()
  result = algorithm(board, anim, heuristic) if heuristic else algorithm(board, anim)
  end = dt.datetime.now()

  result["executionTime"] = end - start 
  return result

def print_result(result):

  stats = [("Execution time",     result["executionTime"]),
           ("Path cost to goal",  "{} moves".format(result["pathCost"])),
           ("Iterations",         result["iterations"]),
           ("Queue size at goal", result["queueSize"])]

  for s in stats:
    print("    * {:<20} {:<20}".format(s[0] + ":", str(s[1])))
  print("")

def main():
  # puzzle inicial
  board = Board([[1,2,3],
                 [4,8,0],
                 [7,6,5]])

  # stdout.write("  a) Uninformed breadth-first search")
  # print_result(run_timed(bfs, board))

  # stdout.write("  b) Iterative deepening depth-first search")
  # print_result(run_timed(ids, board))

  # stdout.write("  c) Uniform cost search")
  # print_result(run_timed(ucs, board))

  # stdout.write("  d I) A* search using number of misplaced tiles heuristic")
  # print_result(run_timed(astar, board, lambda b: b.count_misplaced()))

  # stdout.write("  d II) A* search using sum of manhattan distances heuristic")
  # print_result(run_timed(astar, board, lambda b: b.manhattan_distances_sum()))

  stdout.write("  e) Greedy best-first search")
  print_result(run_timed(gbfs, board, lambda b: b.manhattan_distances_sum()))

# Execute solver only when running this module
if __name__ == "__main__":
  main()