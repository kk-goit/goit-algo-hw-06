import networkx as nx
from task1 import getGraph

def my_dejkstra(graph, start):
    '''Search shortes path from start to all other vertexes'''
    dsts = {vertex: -1 for vertex in graph}
    dsts[start] = 0
    unvisited = list(dsts.keys())

    while unvisited:
        curr = min(unvisited, key=lambda vertex: dsts[vertex] if dsts[vertex] >= 0 else float('infinity'))
        if dsts[curr] == -1:
            break;
        for nvert, prm in graph[curr].items():
            dst = dsts[curr] + prm['weight']
            if dsts[nvert] == -1 or dst < dsts[nvert]:
                dsts[nvert] = dst
        unvisited.remove(curr)

    return dsts

if __name__ == "__main__":
    G = getGraph();
    for vert in G:
        print(f"{vert} -> ", end='')
        frst = True
        for v,l in my_dejkstra(G, vert).items():
            if frst:
                frst = False
            else:
                print(", ", end='')
            print(f"'{v}': {l:2}", end='')
        print('')
