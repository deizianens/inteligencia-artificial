# encoding=UTF-8
'''
Deiziane Natani da Silva
2015121980

Executar o main em 8-puzzle.py
'''
import numpy as np
import scipy.spatial as spatial
from collections import namedtuple
from hashlib import sha1

# Decorate coordinate tuples to make code more readable.
# (y, x) order was chosen to match numpy's array indexing style.
Coord = namedtuple("Coord", "x y")

# An immutable sliding puzzle board with (y, x) coordinate system.
# Its state consists of a numpy array of tiles and a moves count.

'''
     O 8-puzzle pode ser representado como uma lista de tamanho 9 (de 0 a 8)
     0 representa o espaço vazio, onde é permitido que as peças se movam
     Goal:
            1 | 2 | 3
            --|---|---
            4 | 5 | 6
            --|---|---
            7 | 8 | 0
'''
def goal_tiles():
    g = np.arange(1, 10)
    g[8] = 0
    g = np.reshape(g, (3,3))
    return g

# verifica o local exato que um numero deve ficar
def goal_coord(tile_id):
 return np.where(goal_tiles() == tile_id)


class Board:
    def __init__(self, tiles, moves = 0):
        self.tiles = np.array(tiles, dtype=np.int8) 
        self.moves = moves
        # Enforce immutability to avoid bugs.
        self.tiles.flags.writeable = False 
    
    def get_tiles(self):
        return self.tiles

    # acha a coordenada de um número especifico
    def find_tile(self, tile_id):
        return Coord._make(
        np.concatenate(np.where(self.tiles == tile_id)))


    # quantidade de numeros fora do lugar
    def count_misplaced(self):
        # print(np.count_nonzero(self.tiles != goal_tiles()))
        return np.count_nonzero(self.tiles != goal_tiles())


    def find_empty(self): return self.find_tile(0)
    def is_goal(self): 
        if self.count_misplaced() == 0:
            print(self.get_tiles())
        return self.count_misplaced() == 0 
    

    def height(self): return self.tiles.shape[0] 
    def width(self):  return self.tiles.shape[1]


    def coord_valid(self, coord):
        # print(self.height(), self.width())
        return (coord.x >= 0 and coord.y >= 0 and
                coord.x < self.height() and coord.y < self.width())


    # move uma peça de posição
    def move_empty_to(self, coord):
        old_empty = self.find_empty()
        swapped_tiles = np.copy(self.tiles)
        
        swapped_tiles[old_empty.x][old_empty.y] = self.tiles[coord.x][coord.y]
        swapped_tiles[coord.x][coord.y] = 0
        
        aux = Board(swapped_tiles, self.moves + 1)
        # print(aux.get_tiles())
        return aux


    def find_neighbors(self, coord):
        def delta_to_coord(delta):
            return Coord(coord.x + delta[0], coord.y + delta[1]) 
    
        return set(filter(self.coord_valid, map(delta_to_coord, [(0,-1), (0,1), (-1,0), (1,0)]))) # ordem: esquerda, direita, cima, baixo


    def legal_moves(self):
        l = self.find_neighbors(self.find_empty())
        return l


    # lista de movimentos que podem ser feitos
    def children(self):
        c = map(self.move_empty_to, self.legal_moves())
        # print("\n")
        return c


    # SHA1 hashcode for comparing tiles, doesn't check move count.
    # Not called __hash__ as this does not ensure deep equality.
    def tilehash(self):
        return sha1(self.tiles).hexdigest()


    # Distância de manhattan para o goal 
    def manhattan_to_goal(self, tile_id):
        return spatial.distance.cityblock(goal_coord(tile_id), self.find_tile(tile_id))  


    ''' Soma das distâncias de Manhattan para todas as posições
        -  É a soma das distâncias entre as peças e suas
        respectivas posições
    '''
    def manhattan_distances_sum(self):
        # print(sum(map(lambda tile_id: self.manhattan_to_goal(tile_id), np.nditer(self.tiles))))
        return sum(map(lambda tile_id: self.manhattan_to_goal(tile_id), np.nditer(self.tiles)))

