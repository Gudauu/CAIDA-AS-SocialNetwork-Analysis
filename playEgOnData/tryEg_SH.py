

import easygraph as eg 

def buildAsRelGraph(ifileName) -> eg.Graph:
    ifile = open(ifileName,'r')
    G = eg.Graph()

    for line in ifile:
        if line[0] == '#': # comment
            continue
        listLine = line.split('|')  # ASN|ASN|type
        type_edge = int(listLine[2])
        G.add_edge(int(listLine[0]),int(listLine[1]),edge_attr={'type':type_edge})
        if type_edge == 0: # peer edge
            G.add_edge(int(listLine[1]),int(listLine[0]),edge_attr={'type':type_edge})
    return G


if __name__ == '__main__':
    # G = eg.Graph()
    # G.add_edges([(5,6),(7,8)])
    # ofile.write(G.nodes)
    # G.edges
    ifileNames = [
        'dataCAIDA/AS_relationships/raw/20230101.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20221001.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20180701.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20110401.as-rel.txt'
    ]
    ofile = open('playEgOnData/result_SH','w')

    fn = ifileNames[0]
    G = buildAsRelGraph(fn)
    shs = eg.common_greedy(G, 5)

    # Draw the Graph, and the shs is marked by red star

    eg.draw_SHS_center(G, shs)

    # Draw CDF curves of "Number of Followers" of SH spanners and ordinary users in G.

    eg.plot_Followers(G, shs)
    

    
    
    
    