# encoding=UTF-8
'''
Deiziane Natani da Silva
2015121980

Código baseado no código de Joonas Rouhiainen: https://github.com/rjoonas/AI-assignment-1
'''
import itertools
from collections import deque
from Queue import PriorityQueue
from sys import stdout

def result(iterations, queue, solvedBoard = None):
  return {
    "solved":     solvedBoard != None,
    "iterations": iterations,
    "queueSize":  len(queue),
    "pathCost":   solvedBoard.moves if solvedBoard else None 
  }

'''
    Breadth-first Search (Busca em Largura)
    Busca sem informação

    Fácil de implementar, porém usa mais memória
    Fronteira usa uma queue fifo, e a estrutura de dados usada é uma dequeue
'''
def bfs(root_node, animate_progress):
  iterations = 0 
  visited = set()
  queue = deque([root_node])

  while len(queue) > 0:
    iterations = iterations + 1
    animate_progress(iterations)

    node = queue.popleft() # pega o nó da fronteira
    visited.add(node.tilehash()) # marca nó corrente como visitado

    if node.is_goal():
      return result(iterations, queue, node)

    queue.extend(
      filter(
        lambda legalMove: legalMove.tilehash() not in visited,
        node.children()))

  # Não encontrou uma solução
  return result(iterations, queue)


'''
    Iterative Deepening Search
    Busca sem informação

    Usa menos memória que o bfs, porém demora mais.
    Fronteira usa uma queue lifo, e a estrutura de dados usada é uma lista

'''
def ids(root_node, animate_progress):
  iterations = 0 

  # Profundidade de 0 a infinito, começando do 0 para verificar se estado inicial é otimo
  for depth in itertools.count(): 
    queue = [root_node]
    
    # Guarda nós já visitados para o caso de encontrá-los novamente
    visited = {} 

    while len(queue) > 0:
      iterations = iterations + 1
      animate_progress(iterations)
      
      node = queue.pop() # pega nó da maior profundidade
      visited[node.tilehash()] = node.moves # marca nó corrente como visitado

      if node.is_goal():
        return result(iterations, queue, node)
     
      if node.moves < depth:
        queue.extend(
          filter(
            lambda child:
              child.tilehash() not in visited or
              visited[child.tilehash()] > child.moves,
            node.children()))

  # Não encontrou uma solução
  return result(iterations, queue) 


'''
    Uniform-cost Search (Busca de custo uniforme)
    Busca sem informação
'''

'''
    A* Search
    Busca com informação
    
    Mais rápida que bfs e ids.
    Fronteira usa uma priority queue ordenada pela função de estimação de custo.
'''
def astar(root_node, animate_progress, heuristic):
  iterations = 0 
  visited = set()
  queue = PriorityQueue()
  queue.put((0, root_node))

  # Custo estimado = custo acumulado + custo estimado pela heuristica
  def estimate_cost(node): return node.moves + heuristic(node)
  def queue_entry(node): return (estimate_cost(node), node)

  def unvisited_children(node):
    return filter(
      lambda child: child.tilehash() not in visited,
      node.children())

  while not queue.empty():
    iterations = iterations + 1
    animate_progress(iterations)

    node = queue.get()[1] # pega nó de maior prioridade
    visited.add(node.tilehash()) # marca nó como visitado

    if node.is_goal():
      return result(iterations, queue.queue, node) # checa se atingiu goal

    for entry in map(queue_entry, unvisited_children(node)):
      queue.put(entry)

  # Não encontrou uma solução
  return result(iterations, queue)

'''
    Greedy Best-First Search
    Busca com informação
'''

'''
    Hill Climbing, permitindo movimentos laterais.
    Busca Local
'''