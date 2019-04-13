from collections import namedtuple

'''
Deiziane Natani da Silva 
2015121980
'''
def goal_test(state):
    return str(state) == str(range(0, 9))

'''
    Breadth-first Search (Busca em Largura)
    Busca sem informação
'''
def bfs(start):
    SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

    position = SearchPos(start, 0, 0, None)

    # a fronteira contém posições ainda não exploradas
    frontier = [position]
    explored = set()

    while len(frontier) > 0:
        # posição atual é a primeira da fronteira
        position = frontier.pop(0)

        node = position.node

        # testa se já chegou no goal
        if goal_test(node):
            max_depth = max([pos.depth for pos in frontier])
            Success = namedtuple('Success', 'position, max_depth, nodes_expanded')
            success = Success(position, max_depth, len(explored))
            return success

        # adiciona nós ja explorados
        explored.add(node)

        # todas as posições alcançadas a partir da posição atual são adicionadas à fronteira
        for neighbor in node.successors():
            new_position = SearchPos(neighbor, position.cost + 1, position.depth + 1, position)
            frontier_check = neighbor in [pos.node for pos in frontier]

            if neighbor not in explored and not frontier_check:
                frontier.append(new_position)

    # impossível chegar no goal
    return None
   

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
    def ast(self, start):
        SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

        position = SearchPos(start, 0, 0, None)

        # a fronteira contém posições ainda não exploradas
        frontier = [position]

        explored = set()
       
        while len(frontier) > 0:
            puzzle = heapq.heappop(frontier)
            explored.add(tuple(puzzle.puzzle_state))

            if puzzle.goal_test:
                self.path_to_solution = []
                self.path_trace(self.path_to_solution, puzzle)
                return len(
                    self.path_to_solution), self.states, self.max_search_depth, self.nodes_expanded

            self.nodes_expanded += 1

            children = puzzle.expand

            for c in children:
                if tuple(c.puzzle_state) not in explored:
                    heapq.heappush(frontier, c)
                    explored.add(tuple(c.puzzle_state))
                    self.max_search_depth = max(self.max_search_depth, c.depth)

    '''
    Greedy Best-First Search
    Busca com informação
    '''

    '''
    Hill Climbing, permitindo movimentos laterais.
    Busca Local
    '''
   
