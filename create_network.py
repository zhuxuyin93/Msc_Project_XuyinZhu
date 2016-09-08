import networkx as nx
import csv

def creatNetwork():

    G = nx.MultiDiGraph()

    graph = file("/Users/zxy/Desktop/project/data/graph.csv", "rb")
    reader = csv.reader(graph)

    # create the network
    for line in reader:
        G.add_node(line[0])
        G.add_node(line[1])
        G.add_edge(line[0], line[1])

    # calculate network attributes
    degreeCentrality = nx.degree_centrality(G)
    betweennessCentrality = nx.betweenness_centrality(G)
    closenessCentrality = nx.closeness_centrality(G)

    # output result
    graphWithAttributes = file("/Users/zxy/Desktop/project/data/graphWithAttributes.csv", 'wb')
    writer = csv.writer(graphWithAttributes)

    writer.writerow(["nodeID", "degree", "in degree", "out degree",
                     "degree centrality", "betweenness centrality","closeness centrality"])

    for n in G.nodes():
        writer.writerow([str(n), str(G.degree(n)), str(G.in_degree(n)), str(G.out_degree(n)),
                         str(degreeCentrality[n]),str(betweennessCentrality[n]), str(closenessCentrality[n])])

if __name__ == '__main__':
    creatNetwork()

