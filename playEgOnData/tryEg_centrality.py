

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
    ofile = open('playEgOnData/result_centrality','w')
    ifileNames = [
        'dataCAIDA/AS_relationships/raw/20230101.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20221001.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20180701.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20110401.as-rel.txt'
    ]

    fn = ifileNames[0]
    G = buildAsRelGraph(fn)

    try:
        betweeness_c = eg.betweenness_centrality(G)
        ofile.write("betweenness_centrality"+str(betweeness_c)+'\n')

        closeness_c = eg.closeness_centrality(G)
        ofile.write("closeness_centrality"+str(closeness_c)+'\n')

        # in_degree_c = eg.in_degree_centrality(G)
        # ofile.write("in_degree_centrality"+str(in_degree_c)+'\n')

        # out_degree_c = eg.out_degree_centrality(G)
        # ofile.write("out_degree_centrality"+str(out_degree_c)+'\n')

        # ego_betweenness = eg.ego_betweenness(G)
        # ofile.write("ego_betweenness"+str(ego_betweenness)+'\n')

        flowbetweenness_c = eg.flowbetweenness_centrality(G)
        ofile.write("flowbetweenness_centrality"+str(flowbetweenness_c)+'\n')

        laplacian_c = eg.laplacian(G)
        ofile.write("laplacian"+str(laplacian_c)+'\n')

        # pagerank = eg.pagerank(G)
        # ofile.write("pagerank"+str(pagerank)+'\n')
    except Exception:
        print(Exception)
        pass

   

    
    

    
    
    
    