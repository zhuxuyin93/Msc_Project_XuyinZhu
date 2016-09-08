import csv

def add_attributes():

    # open the graph
    graph = file("/Users/zxy/Desktop/project/data/graphWithAttributes.csv", "rb")
    readerGraph = csv.reader(graph)

    nodes = dict()
    for line in readerGraph:
        nodes[line[0]] = line[1]+","+line[2]+","+line[3]+","+line[4]+","+line[5]+","+line[6]

    # open the loan data
    loan = file("/Users/zxy/Desktop/project/data/listing.csv", "rb")
    readerLoan = csv.reader(loan)

    listingWithNetwork = file("/Users/zxy/Desktop/project/data/listingWithNetwork.csv", 'wb')
    writer = csv.writer(listingWithNetwork)

    for line in readerLoan:
        list = []
        for i in range(0,82):
            list.append(line[i])

        nodeId = line[81]
        if nodes.has_key(nodeId):
            attributes = nodes[nodeId].split(',')
            for i in range(0,6):
                list.append(attributes[i])

        writer.writerow(list)

if __name__ == '__main__':
    add_attributes()