import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(map):
    matrix = list()
    # turn map to a matrix
    for line in map:
        matrix.append(list(line.strip()))

    # generate the graph form the matrix
    graph = nx.DiGraph()

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != "*":
                if j + 1 < len(matrix) and matrix[i][j + 1] != "*":
                    graph.add_edge(f'{i},{j}', f'{i},{j+1}',
                                   Action="DOWN", gn=1)
                if j - 1 >= 0 and matrix[i][j - 1] != '*':
                    graph.add_edge(f'{i},{j}', f'{i},{j-1}', Action="UP", gn=1)
                if i + 1 < len(matrix) and matrix[i + 1][j] != '*':
                    graph.add_edge(f'{i},{j}', f'{i+1},{j}',
                                   Action="LEFT", gn=1)
                if i - 1 >= 0 and matrix[i - 1][j] != '*':
                    graph.add_edge(f'{i},{j}', f'{i-1},{j}',
                                   Action="RIGHT", gn=1)

    edge_labels = nx.get_edge_attributes(graph, "Action")
    plt.rcParams['figure.figsize'] = (13, 13)
    pos = nx.spring_layout(graph, k=0.5)
    nx.draw(graph, pos, width=1, linewidths=1, node_size=500,
            labels={node: node for node in graph.nodes()})
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels=edge_labels, label_pos=0.65)
    plt.axis("off")
    plt.savefig('result2.png')
    plt.show()
    # plt.savefig("res.png")  # save as png
    # plt.show()


with open("./map3.txt") as f:
    generate_graph(f)
