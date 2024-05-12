import networkx as nx
from collections import deque
from task1 import getGraph

def my_dfs(graph, vertex, visited=None):
    '''Recursive Depth-first search'''
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ') 
    for neighbor in graph[vertex]:
            if neighbor not in visited:
                my_dfs(graph, neighbor, visited)

def my_bfs(graph, queue, visited=None):
    '''Recursive Breadth-first search'''
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    my_bfs(graph, queue, visited)

if __name__ == "__main__":
    G = getGraph();
    print("DFS path: ", end='')
    my_dfs(G, 'A')
    print("\nBFS path: ", end='')
    my_bfs(G, deque(['A']))
    print('')