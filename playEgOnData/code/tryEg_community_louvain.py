from include import *
from time import *

if __name__ == '__main__':
    DEBUG = False
    versions = ['19980101','19980201','19980301','19980401']
    for version in versions:

        G = getG(version,DEBUG)

        ofile = open('playEgOnData/results/'+version+'/communityDetection_louvain','w')

        for i in range(10):
            sleep(2)
            ofile.write(str(i)+'\n')


        # communities = eg.LPA(G)

        # for k,v in communities.items():
        #     ofile.write("community "+str(k)+'\n')
        #     ofile.write(str(v))
        #     ofile.write('\n')
        ofile.close()
        break


    

    
    
    
    