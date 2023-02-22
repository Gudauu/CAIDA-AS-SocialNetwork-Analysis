from include import *


if __name__ == '__main__':
    DEBUG = True
    # versions = ['19980101','19980201','19980301','19980401']
    for fn in dictInfile.values():
        G = buildAsRelGraph_nx(fn, flag_directed = True)

        dict_edge_betweenness_centrality = nx.edge_betweenness_centrality(G)

        version = getVersionFromName(fn)
        ofile = open('playEgOnData/results/'+version+'/edge_betweenness_centrality','w')

        for edge, value in dict_edge_betweenness_centrality.items():
            ofile.write(f"{edge}:{value}")

        ofile.close()

    

    
    
    
    