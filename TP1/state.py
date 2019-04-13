from board import Board

class State:
    '''
        Define os estados que o jogo se encontra
    '''
    def __init__(self, initial_state=[]):
        self.current = Board(initial_state)

    def __eq__(self, other): 
        return self.current == other.current

    def __str__(self):
        return str(self.current)

    def __hash__(self):
        return hash(str(self))

    def move_up(self):
        move_up = self.current.move_up()
        if move_up is not None:
            return State(move_up)
        else:
            return self

    def move_down(self):
        move_down = self.current.move_down()
        if move_down is not None:
            return State(move_down)
        else:
            return self

    def move_left(self):
        move_left = self.current.move_left()
        if move_left is not None:
            return State(move_left)
        else:
            return self

    def move_right(self):
        move_right = self.current.move_right()
        if move_right is not None:
            return State(move_right)
        else:
            return self

    def successors(self):
        succ = []

        move_up = self.current.move_up()
        if move_up != None:
            succ.append(State(move_up))


        move_down = self.current.move_down()
        if move_down != None:
            succ.append(State(move_down))


        move_left = self.current.move_left()
        if move_left != None:
            succ.append(State(move_left))


        move_right = self.current.move_right()
        if move_right != None:
            succ.append(State(move_right))

        return succ