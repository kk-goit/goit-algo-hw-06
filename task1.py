import networkx as nx
import matplotlib.pyplot as plt

def getGraph():
    # Створення графа
    G = nx.Graph()

    # Груба транспортна схема м. Бровари
    G.add_edge('A', 'B', weight=2)
    G.add_edge('A', 'C', weight=15)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('B', 'E', weight=2)
    G.add_edge('C', 'G', weight=4)
    G.add_edge('C', 'L', weight=10)
    G.add_edge('D', 'G', weight=2)
    G.add_edge('D', 'K', weight=1)
    G.add_edge('E', 'F', weight=1)
    G.add_edge('E', 'I', weight=1)
    G.add_edge('F', 'D', weight=1)
    G.add_edge('F', 'J', weight=1)
    G.add_edge('G', 'L', weight=7)
    G.add_edge('I', 'J', weight=1)
    G.add_edge('I', 'M', weight=5)
    G.add_edge('J', 'K', weight=1)
    G.add_edge('L', 'M', weight=5)

    return G

if __name__ == "__main__":
    G = getGraph()

    print(f"Graph have {G.number_of_nodes()} nodes and {G.number_of_edges()} edges and is {'' if nx.is_connected(G) else 'not '}connected")
    print("Degree Centrality: {", end='')
    frst = True
    for v,dc in nx.degree_centrality(G).items():
        if frst:
            frst = False
        else:
            print(", ", end='')
        print(f"'{v}': {dc:.4f}", end='')
    print('}')
    print(f"Average shotests path: {nx.average_shortest_path_length(G):.4f}")
    # Візуалізація графа
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=400, node_color="skyblue", font_size=12, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
