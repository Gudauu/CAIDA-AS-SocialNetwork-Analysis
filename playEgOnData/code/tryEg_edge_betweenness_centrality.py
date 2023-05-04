from include import getG
import networkx as nx



if __name__ == '__main__':
    DEBUG = True
    # versions = ['19980101','19980201','19980301','19980401']
    # list_temp = list(dictInfile.values()) + listFileName_1998

    for year in range(2006,2023+1):
        version = f"{year}0101"
        # G = buildAsRelGraph_nx(fn, flag_directed = True)
        G = getG(version, flag_nx = True)

        dict_edge_betweenness_centrality = nx.edge_betweenness_centrality(G)

        ofile = open('playEgOnData/results/'+version+'/edge_betweenness_centrality','w')

        for edge, value in dict_edge_betweenness_centrality.items():
            ofile.write(f"{edge}:{value}\n")

        ofile.close()

    

    
    
    
    