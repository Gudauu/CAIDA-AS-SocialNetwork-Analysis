

import easygraph as eg 

def buildAsRelGraph(ifileName) -> eg.Graph:
    ifile = open(ifileName,'r')
    G = eg.Graph()

    for line in ifile:
        if line[0] == '#': # comment
            continue
        listLine = line.split('|')  # ASN|ASN|type
        G.add_edge(int(listLine[0]),int(listLine[1]),edge_attr={'type':int(listLine[2])})
    return G







if __name__ == '__main__':
    # G = eg.Graph()
    # G.add_edges([(5,6),(7,8)])
    # print(G.nodes)
    # G.edges
    ifileNames = [
        'dataCAIDA/AS_relationships/raw/20230101.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20221001.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20180701.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20110401.as-rel.txt'
    ]
    listG = []
    listNodes = []
    for fn in ifileNames:
        G = buildAsRelGraph(fn)
        listNodes.append(G.nodes)
        # print(G.size())
        print('size',len(G.nodes))
        listG.append(G)
    for i in range(len(listNodes)-1):
        print(str(i)+'-'+str(i+1)+str(len(set(listNodes[i])-set(listNodes[i+1]))))
        print(str(i+1)+'-'+str(i)+str(len(set(listNodes[i+1])-set(listNodes[i]))))
    
    