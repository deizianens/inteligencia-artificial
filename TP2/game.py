import random
import numpy as np

'''
Deiziane Natani da Silva
2015121980

Executar o main em main.py
'''

class Game():
    def __init__(self, maze, alpha, epsilon, n_episodes, gama = 0.9):
        self.maze = maze
        self.alpha = alpha
        self.epsilon = epsilon
        self.n_episodes = n_episodes
        self.gama = gama
        self.moves = ((1, 0), (-1, 0), (0, -1), (0, -1)) # up, down, left, rigth 
        self.rewards = {'-': -1, '0': 10, '&': -10, '#': -1}
        self.q_table = self.create_qtable()
        self.valid_states = self.get_valid_states()

    def create_qtable(self):
        r = {'0': [10.], '&': [-10.], '-': [0.], '#': [0.]}

        lines, cols = self.maze.height(), self.maze.width()
        return [[r[self.maze.get_tile(i,j)] * 4 for j in range(cols)]
                for i in range(lines)]


    # define a starting point for pacman    
    def initial_state(self):
        return random.choice(self.valid_states)


    def is_terminal(self, state):
        return (self.maze.get_tile(state[0],state[1]) == '0' or self.maze.get_tile(state[0],state[1]) == '&')


    # return valid places where pacman can start (only '-')
    def get_valid_states(self):
        lines, cols = self.maze.height(), self.maze.width()
        return [(i, j) for i in range(lines) for j in range(cols)
                if self.maze.get_tile(i,j) == '-']


    def get_reward(self, state):
        position = self.maze.get_tile(state[0],state[1])
        return self.rewards[position]


    # if random < epsilon then exploitation else exploration
    def e_greedy(self, state):
        if random.random() < self.epsilon:
            return random.randrange(len(self.moves))
        else:
            return max(enumerate(self.q_table[state[0]][state[1]]), key=lambda x: x[1])[0]


    def move(self, state, act):
        action = self.moves[act]
        next_state = (state[0] + action[0], state[1] + action[1])
        return state if self.maze.get_tile(next_state[0],next_state[1]) == '#' else next_state


    def update_q_table(self, state, action, next_state):
        r = self.get_reward(state)
        current_q_table = self.q_table[state[0]][state[1]][action]
        next_q_table = max(self.q_table[next_state[0]][next_state[1]])

        self.q_table[state[0]][state[1]][action] += self.alpha * (r + self.gama * next_q_table - current_q_table)


    # runs the episodes
    def play(self):
        total_episodes = 0
        episode = 0
        while True:
            print("----- Episode ", episode, "------\n")
            state = self.initial_state()
            while not self.is_terminal(state):
                if total_episodes >= self.n_episodes:
                    return self.q_table

                action = self.e_greedy(state)
                next_state = self.move(state, action)
                self.update_q_table(state, action, next_state)
                total_episodes += 1
                state = next_state

            episode += 1