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

def result(iterations, queue, type, solvedBoard = None):
  if type == 1: 
    return {
      "solved":     solvedBoard != None,
      "iterations": iterations,
      "queueSize":  len(queue),
      "pathCost":   solvedBoard.moves if solvedBoard else None 
    }
  else: # qsize() pra priority queue
    return {
      "solved":     solvedBoard != None,
      "iterations": iterations,
      "queueSize": 0,
      "pathCost":   solvedBoard.moves if solvedBoard else None 
    }

'''
    Breadth-first Search (Busca em Largura)
    Busca sem informação

    - O nó raiz é expandido, em seguida todos os nós sucessores são
    expandidos, então todos próximos nós sucessores são expandidos, e
    assim em diante

    Fácil de implementar, porém usa mais memória
    Fronteira usa uma queue fifo, e a estrutura de dados usada é uma deque
'''
def bfs(root_node, animate_progress):
  iterations = 0 

  visited = set()
  queue = deque([root_node])

  while len(queue) > 0:  # verifica se a fronteira não está vazia
    iterations = iterations + 1
    animate_progress(iterations)

    node = queue.popleft() # pega o nó da fronteira
    visited.add(node.tilehash()) # marca nó corrente como visitado

    if node.is_goal():
      return result(iterations, queue, 1, node)

    queue.extend(
      filter(
        lambda legalMove: legalMove.tilehash() not in visited,
        node.children())) # adiciono nós a fronteira

  # Não encontrou uma solução
  return result(iterations, queue, 1)


'''
    Iterative Deepening Search
    Busca sem informação

    - Consiste em uma busca em profundidade onde o
    limite de profundidade é incrementado gradualmente.

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
        return result(iterations, queue, 1, node)
     
      if node.moves < depth:
        queue.extend(
          filter(
            lambda child:
              child.tilehash() not in visited or
              visited[child.tilehash()] > child.moves,
            node.children()))

  # Não encontrou uma solução
  return result(iterations, 1, queue) 


'''
    Uniform-cost Search (Busca de custo uniforme)
    Busca sem informação

    - Expande sempre o nó de menor custo de caminho. Se o custo de todos
      os passos for o mesmo, o algoritmo acaba sendo o mesmo que a busca
      em largura

    - Usa a priority queue.
'''
def ucs(root_node, animate_progress):
  iterations = 0 
  aux = 0

  visited = set()
  queue = PriorityQueue()
  queue.put((0, root_node))  # coloca nó na lista de prioridade

  def queue_entry(node): 
    return (1+aux, node)

  def unvisited_children(node):
    return filter(
      lambda child: child.tilehash() not in visited,
      node.children())

  while not queue.empty():
    iterations = iterations + 1
    animate_progress(iterations)

    node = queue.get()[1] # pega menor custo
    visited.add(node.tilehash()) # marca nó como visitado

    if node.is_goal():
      return result(iterations, queue.queue, 1, node) # checa se atingiu goal


    for entry in map(queue_entry, unvisited_children(node)):
      queue.put(entry)
      aux = aux + 1 # apenas pra fazer com que a priority queue se comporte como uma fifo

  # Não encontrou uma solução
  return result(iterations, 0, queue)



'''
    A* Search
    Busca com informação
    
    -  Expandir o nó que pertence ao caminho com um menor custo associado.
    - Função de avaliação: f(n) = g(n) + h(n), onde g(n) dá o valor do custo do caminho percorrido desde
      a raiz até o nó e h(n) o custo mais barato do nó até o goal.

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
      return result(iterations, queue.queue, 1, node) # checa se atingiu goal

    for entry in map(queue_entry, unvisited_children(node)):
      queue.put(entry)

  # Não encontrou uma solução
  return result(iterations, 0, queue)

'''
    Greedy Best-First Search
    Busca com informação

    - Expande nós com menor custo até o goal.
    - Função de avaliação: f(n) = h(n)
'''
def gbfs(root_node, animate_progress, heuristic):
  iterations = 0 
  visited = set()
  queue = PriorityQueue()
  queue.put((0, root_node))

  # Custo estimado = custo estimado pela heuristica
  def estimate_cost(node): return heuristic(node)
  def queue_entry(node): return (estimate_cost(node), node)

  def unvisited_children(node):
    return filter(
      lambda child: child.tilehash() not in visited,
      node.children())

  while not queue.empty():
    iterations = iterations + 1
    animate_progress(iterations)

    # print(queue.get()[1])

    node = queue.get()[1] # pega nó de maior prioridade
    visited.add(node.tilehash()) # marca nó como visitado

    if node.is_goal():
      return result(iterations, queue.queue, 1, node) # checa se atingiu goal

    # checo se os vizinhos tem menor custo
    for entry in map(queue_entry, unvisited_children(node)):
      queue.put(entry)

  # Não encontrou uma solução
  return result(iterations, 0, queue)

'''
    Hill Climbing, permitindo movimentos laterais (interrompendo depois de k tentativas).
    Busca Local

    - Política de busca local cujos movimentos se dão impreterivelmente na direção de valores 
      crescentes (no caso, não decrescentes) da função objetivo.
    - Termina quando um pico (mínimo ou máximo) é alcançado.

    Utiliza pouca memória (constante)
'''
def hc(root_node, animate_progress, heuristic):
  iterations = 0 

  queue = deque([root_node])

  while len(queue) > 0:  # verifica se a vizinhança não esta vazia
    iterations = iterations + 1
    animate_progress(iterations)

    node = queue.pop() 

    if node.is_goal():
      return result(iterations, queue, 1, node)

    # Custo estimado = custo estimado pela heuristica
    def estimate_cost(node): return heuristic(node)
    def queue_entry(node): return (estimate_cost(node), node)
   

  # Não encontrou uma solução
  return result(iterations, queue, 1)