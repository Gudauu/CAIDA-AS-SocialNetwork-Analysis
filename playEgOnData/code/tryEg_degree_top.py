
from include import *




if __name__ == '__main__':
    DEBUG = 0
    versions = ['19980101','19980201','19980301','19980401',]
    for version in versions:
        G = getG(version)
        ofile = open('playEgOnData/results/'+version+'/degree_top','w')

        try:
            for node, degree in sorted((G.degree()).items(), key=lambda x: -x[1]):
                ofile.write(str(node) + ": "+str(degree)+'\n')

        except Exception as e:
            print(str(e))
            pass

   

    
    

    
    
    
    