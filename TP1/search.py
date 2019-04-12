import heapq
import numpy as np
from queue import PriorityQueue
from collections import deque

'''
Deiziane Natani da Silva 
2015121980
'''
class Search:
    '''
    Breadth-first Search (Busca em Largura)
    Busca sem informação
    '''
    def __init__(self):
        self.path_to_solution = []
        self.states = []
        self.max_search_depth = 0
        self.nodes_expanded = 0

    def bfs (self, board):
        frontier = deque()
        explored = set()
        frontier.append(board)

        while frontier:
            puzzle = frontier.popleft()
            explored.add(tuple(puzzle.state))

            if puzzle.goal_test:
                self.path_to_solution = []
                self.path_trace(self.path_to_solution, puzzle)
                return len(
                    self.path_to_solution), self.states, self.max_search_depth, self.nodes_expanded

            self.nodes_expanded += 1

            children = puzzle.expand

            for c in children:
                if tuple(c.state) not in explored:
                    frontier.append(c)
                    explored.add(tuple(c.state))
                    self.max_search_depth = max(self.max_search_depth, c.depth)
   

    '''
    Iterative Deepening Search
    Busca sem informação

    '''


    '''
    Uniform-cost Search (Busca de custo uniforme)
    Busca sem informação

    '''

    '''
    A* Search
    Busca com informação

    '''

    '''
    Greedy Best-First Search
    Busca com informação

    '''

    '''
    Hill Climbing, permitindo movimentos laterais.
    Busca Local
    '''
    def path_trace(self, path_to_solution, child):
        print("Tracing path...")
        child.print_puzzle
        while child.parent:
            parent = child.parent
            self.states.append(child.state)
            path_to_solution.append(child)
            child = parent
            child.print_puzzle