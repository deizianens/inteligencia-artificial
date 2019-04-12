import sys
import time
import resource
import numpy as np
from search import Search
from state import State

class Board:
    '''
     O 8-puzzle pode ser representado como uma lista de tamanho 9 (de 0 a 8)
     0 representa o espaço vazio, onde é permitido que as peças se movam
     Goal:
            0 | 1 | 2
            --|---|---
            3 | 4 | 5
            --|---|---
            6 | 7 | 8
    '''
    def __init__(self, initial_values=[]):
        self.value = np.array(initial_values)


    def __eq__(self, other): 
        return self.value == other.value


    # caso em que a posição vazia não está na primeira linha (posso mover a posição vazia p/ cima)
    def move_up(self):
        pos = self.value.index(0)
        if pos in (0, 1, 2):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-3] = new_val[pos-3], new_val[pos]
            return new_val


    # caso em que a posição vazia não está na ultima linha (posso mover a posição vazia p/ baixo)
    def move_down(self):
        pos = self.value.index(0)
        if pos in (6, 7, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+3] = new_val[pos+3], new_val[pos]
            return new_val


     # caso em que a posição vazia não está na coluna da esquerda (posso mover a posição vazia p/ esquerda)
    def move_left(self):
        pos = self.value.index(0)
        if pos in (0, 3, 6):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-1] = new_val[pos-1], new_val[pos]
            return new_val


    # caso em que a posição vazia não está na coluna da direita (posso mover a posição vazia p/ direita)
    def move_right(self):
        pos = self.value.index(0)
        if pos in (2, 5, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+1] = new_val[pos+1], new_val[pos]
            return new_val


def trace_path(last_pos):
    pos = last_pos.prev
    next_pos = last_pos

    path = []

    while pos != None:
        if pos.node.up() == next_pos.node:
            path.append("Up")
        elif pos.node.down() == next_pos.node:
            path.append("Down")
        elif pos.node.left() == next_pos.node:
            path.append("Left")
        elif pos.node.right() == next_pos.node:
            path.append("Right")

        pos = pos.prev
        next_pos = next_pos.prev

    return path[::-1]


def main():
    puzzle_state = sys.argv[2].split(",")
    puzzle_state = list(map(int, puzzle_state)) # transforma tudo em int
    pb = Board(puzzle_state)

    start_time = time.time()

    search_depth, states, max_depth, nodes_expanded = Search().bfs(pb)

    config = [1,2,3,0,4,5,6,7,8]

    game = State(config)

    result = search.bfs(game)
    final_pos = result.position
    max_depth = result.max_depth
    nodes_expanded = result.nodes_expanded

    print ("path_to_goal:", trace_path(final_pos))
    print ("cost_of_path:", final_pos.cost)
    print ("nodes_expanded:", nodes_expanded)
    print ("search_depth:", final_pos.depth)
    print ("max_search_depth:", max_depth)
    print ("running_time:", time.time() - start_time)
    print ("max_ram_usage", resource.getrusage(1)[2])


if __name__ == '__main__':
    main()