from include import *

if __name__ == '__main__':
    DEBUG = 0
    for year in range(2000,2023+1):
        version = f'{year}0101'
        G = getG(version)

        ofile = open('playEgOnData/results/'+version+'/basic','w')
        ofile.write('node size: '+str(len(G.nodes))+'\n')
        ofile.write('edge size: '+str(len(G.edges))+'\n')
        ofile.write('number of connected comp:'+str(eg.number_connected_components(G))+'\n')
        ofile.write('average degree:'+str(sum(G.degree().values())/len(G.degree()))+'\n')


    
    