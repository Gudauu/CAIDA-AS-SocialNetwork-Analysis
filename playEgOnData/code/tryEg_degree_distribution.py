
from include import *




if __name__ == '__main__':
    DEBUG = 0
    for year in range(2000,2022+1):
        version = f'{year}0101' #'19980101'
        G = getG(version)
        

        try:
            # ofile = open('playEgOnData/result_connected_components','w')
            # components = eg.connected_components(G)

            # for cc in components:
            #     ofile.write(str(cc))
            #     ofile.write('\n')

            # ofile.close()
            dictDegree = {}
            for node,degree in (G.degree()).items():
                if degree not in dictDegree:
                    dictDegree[degree] = 1
                else:
                    dictDegree[degree] += 1
            ofile = open('playEgOnData/results/'+version+'/degree_distribution','w')
            # dictDegree = sorted(dictDegree.items(), key=lambda x:x[0])
            for k in reversed(sorted(dictDegree.keys())):
                ofile.write(str(k) + ": "+str(dictDegree[k])+'\n')
    
        except Exception as e:
            print(str(e))
            pass

   

    
    

    
    
    
    