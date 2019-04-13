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
        self.value = initial_values


    def __eq__(self, other): 
        return self.value == other.value
    
    def __hash__(self):
        return hash(str(self))


    # caso em que a posição vazia não está na primeira linha (posso mover a posição vazia p/ cima)
    def move_up(self):
        pos = self.value.index(0)
        # print(self.value)
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




