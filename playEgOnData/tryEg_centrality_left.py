

import easygraph as eg 

import warnings

def buildAsRelGraph(ifileName) -> eg.DiGraph:
    ifile = open(ifileName,'r')
    G = eg.DiGraph()

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
    warnings.filterwarnings("ignore") # suppress warnings about hypergraph 

    ifileNames = [
        'dataCAIDA/AS_relationships/raw/20230101.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20221001.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20180701.as-rel.txt',
        'dataCAIDA/AS_relationships/raw/20110401.as-rel.txt'
    ]
    DEBUG = True
    

    if DEBUG:
        G = eg.DiGraph()
        G.add_edges([(5,6),(7,8),(6,5)])
        pagerank = eg.pagerank(G)
        print(pagerank)
    else:
        fn = ifileNames[0]
        G = buildAsRelGraph(fn)


    
    if not DEBUG:
        try:
            # need to choose ego  
            # ofile = open('playEgOnData/result_ego_betweenness','w')
            # ego_betweenness = eg.ego_betweenness(G)
            # ofile.write("ego_betweenness"+str(ego_betweenness)+'\n')
            # ofile.close()

            ofile = open('playEgOnData/result_pagerank','w')
            pagerank = eg.pagerank(G)
            ofile.write("pagerank"+str(pagerank)+'\n')
            ofile.close()

            # ofile = open('playEgOnData/result_in_degree_centrality','w')
            # in_degree_c = eg.in_degree_centrality(G)
            # ofile.write("in_degree_centrality"+str(in_degree_c)+'\n')
            # ofile.close()


            # out_degree_c = eg.out_degree_centrality(G)
            # ofile.write("out_degree_centrality"+str(out_degree_c)+'\n')

        except Exception as e:
            print(str(e))
            pass

   

    
    

    
    
    
    