# encoding=UTF-8
'''
Deiziane Natani da Silva
2015121980

Executar o main em main.py
'''
import numpy as np
import scipy.spatial as spatial
from collections import namedtuple

# Decorate coordinate tuples to make code more readable.
# (y, x) order was chosen to match numpy's array indexing style.
Coord = namedtuple("Coord", "x y")

'''
     O mapa pode ser representado como uma lista de tamanho 30 (de 0 a 29)
     0 representa a pastilha, & um fantasma, # paredes, e - um espaço vazio onde o pacman pode se mover.
     Initial:
            # | # | # | # | # | #
            --|---|---|---|---|---
            # | - | - | - | 0 | #
            --|---|---|---|---|---
            # | - | # | - | & | #
            --|---|---|---|---|---
            # | - | - | - | - | #
            --|---|---|---|---|---
            # | # | # | # | # | #
'''

class Board:
    def __init__(self, tiles):
        self.tiles = np.array(tiles) 
    
    def get_tiles(self):
        return self.tiles

    # acha a coordenada de um número especifico
    def find_tile(self, tile_id):
        return Coord._make(
        np.concatenate(np.where(self.tiles == tile_id)))
    

    def height(self): return self.tiles.shape[0] 
    def width(self):  return self.tiles.shape[1]


    def coord_valid(self, coord):
        # print(self.height(), self.width())
        return (coord.x >= 0 and coord.y >= 0 and
                coord.x < self.height() and coord.y < self.width())

    def find_neighbors(self, coord):
        def delta_to_coord(delta):
            return Coord(coord.x + delta[0], coord.y + delta[1]) 
    
        return set(filter(self.coord_valid, map(delta_to_coord, [(0,-1), (0,1), (-1,0), (1,0)]))) # ordem: esquerda, direita, cima, baixo


    def legal_moves(self):
        l = self.find_neighbors(self.find_empty())
        return l


    