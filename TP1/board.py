# encoding=UTF-8
'''
Deiziane Natani da Silva
2015121980

Código baseado em: https://github.com/rjoonas/AI-assignment-1
'''
import numpy as np
import scipy.spatial as spatial
from collections import namedtuple
from hashlib import sha1

# Decorate coordinate tuples to make code more readable.
# (y, x) order was chosen to match numpy's array indexing style.
Coord = namedtuple("Coord", "y x")

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
        # Stores tiles in numpy array with type int8 (byte, -128 to 127).
        self.tiles = np.array(tiles, dtype=np.int8) 
        self.moves = moves
        # Enforce immutability to avoid bugs.
        self.tiles.flags.writeable = False 
    

    # acha a coordenada de um número especifico
    def find_tile(self, tile_id):
        return Coord._make(
        np.concatenate(np.where(self.tiles == tile_id)))


    def count_misplaced(self):
        return np.count_nonzero(self.tiles != goal_tiles())


    def find_empty(self): return self.find_tile(0)
    def is_goal(self): return self.count_misplaced() == 0 
    

    def height(self): return self.tiles.shape[0] 
    def width(self):  return self.tiles.shape[1]


    def coord_valid(self, coord):
        return (coord.y >= 0 and coord.x >= 0 and
                coord.y < self.height() and coord.x < self.width())


    # move uma peça de posição
    def move_empty_to(self, coord):
        old_empty = self.find_empty()
        swapped_tiles = np.copy(self.tiles)
        
        swapped_tiles[old_empty.y][old_empty.x] = self.tiles[coord.y][coord.x]
        swapped_tiles[coord.y][coord.x] = 0

        return Board(swapped_tiles, self.moves + 1)


    def find_neighbors(self, coord):
        def delta_to_coord(delta):
            return Coord(coord.y + delta[0], coord.x + delta[1]) 
        
        return set(filter(self.coord_valid, map(delta_to_coord, [(0,1), (1,0), (0,-1), (-1,0)])))


    def legal_moves(self):
        return self.find_neighbors(self.find_empty())


    # lista de movimentos que podem ser feitos
    def children(self):
        return map(self.move_empty_to, self.legal_moves())


    # SHA1 hashcode for comparing tiles, doesn't check move count.
    # Not called __hash__ as this does not ensure deep equality.
    def tilehash(self):
        return sha1(self.tiles).hexdigest()


    # Distância de manhattan para o goal 
    def manhattan_to_goal(self, tile_id):
        return spatial.distance.cityblock(goal_coord(tile_id), self.find_tile(tile_id))  


    # Soma das distâncias de Manhattan para todas as posições
    def manhattan_distances_sum(self):
        return sum(map(lambda tile_id: self.manhattan_to_goal(tile_id), np.nditer(self.tiles)))

