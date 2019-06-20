# encoding=UTF-8
'''
Deiziane Natani da Silva
2015121980

Executar o main em main.py
'''
import numpy as np

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
    def __init__(self, tiles, l, c):
        t = np.array(tiles)
        self.tiles =  np.reshape(t, (l,c))
    
    def get_tiles(self):
        return self.tiles

    def height(self): return self.tiles.shape[0] 
    def width(self):  return self.tiles.shape[1]

    def get_tile(self, i, j):
        return self.tiles[i][j]

        