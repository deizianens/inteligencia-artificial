import sys
import numpy as np
from search import Search

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


    def move_up(self, i):
        if i - self.column_size >= 0:
            puzzle_new, parent = self.swap(i, i - 3)
            return Board(puzzle_new, parent, state='Up')

    def move_down(self, i):
        if i + self.column_size <= len(self.puzzle_state) - 1:
            puzzle_new, parent = self.swap(i, i + 3)
            return Board(puzzle_new, parent, state='Down')

    def move_left(self, i):
        if i % self.column_size > 0:
            puzzle_new, parent = self.swap(i, i - 1)
            return Board(puzzle_new, parent, state='Left')

    def move_right(self, i):
        if i % self.column_size < self.column_size - 1:
            puzzle_new, parent = self.swap(i, i + 1)
            return Board(puzzle_new, parent, state='Right')

    def swap(self, index_one, index_two):
        puzzle_new = self.puzzle_state.copy()
        puzzle_new[index_one], puzzle_new[index_two] = puzzle_new[index_two], puzzle_new[index_one]
        return puzzle_new, self


def main():
    puzzle_state = sys.argv[2].split(",")
    puzzle_state = list(map(int, puzzle_state)) # transforma tudo em int
    pb = Board(puzzle_state)

    search_depth, states, max_depth, nodes_expanded = Search().bfs(pb)


if __name__ == '__main__':
    main()