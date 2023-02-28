
from include import *




if __name__ == '__main__':
    DEBUG = 0
    versions = [str(x) + '0101' for x in range(2000, 2023+1)]
    for version in versions:
        G = getG(version)
        # G = buildAsRelGraph(fn)
        # version = fn[31:39]
        ofile = open('playEgOnData/results/'+version+'/degree_top','w')

        try:
            for node, degree in sorted((G.degree()).items(), key=lambda x: -x[1]):
                ofile.write(str(node) + ": "+str(degree)+'\n')

        except Exception as e:
            print(str(e))
            pass

   

    
    

    
    
    
    