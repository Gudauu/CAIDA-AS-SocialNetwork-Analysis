from include import *
from time import *
import community
from cdlib import algorithms


if __name__ == '__main__':
    DEBUG = True
    # versions = ['19980101','19980201','19980301','19980401']
    for fn in listFileName_1998:
        G = buildAsRelGraph_nx(fn, flag_directed = False)

        partition = algorithms.louvain(G, weight="weight", resolution=1.0)
        # Print the communities
        list_communties = partition.communities
        list_communties =  sorted(list_communties,key = lambda x:(-len(x),x))

        version = getVersionFromName(fn)
        ofile = open('playEgOnData/results/'+version+'/communityDetection_louvain','w')

        ofile.close()

    

    
    
    
    