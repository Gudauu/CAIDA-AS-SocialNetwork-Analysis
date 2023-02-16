from include import *

if __name__ == '__main__':
    DEBUG = False
    for fn in listFileName_1998[1:]:
        G = buildAsRelGraph(fn)

        version = fn[31:39]        

        ofile = open('playEgOnData/results/'+version+'/communityDetection_LPA','w')

        communities = eg.LPA(G)

        for k,v in communities.items():
            ofile.write("community "+str(k)+'\n')
            ofile.write(str(v))
            ofile.write('\n')
        ofile.close()


    

    
    
    
    