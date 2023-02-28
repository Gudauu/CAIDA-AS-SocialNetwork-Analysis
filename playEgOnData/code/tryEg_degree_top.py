
from include import *




if __name__ == '__main__':
    DEBUG = 0
    versions = [str(x) + '0101' for x in range(2000, 2023+1)]
    dict_ASN_info = readDict('dataCAIDA/ASN_lookup/ASN_lookup')
    for version in versions:
        G = getG(version)
        # G = buildAsRelGraph(fn)
        # version = fn[31:39]
        ofile = open('playEgOnData/results/'+version+'/degree_top','w')

        for node, degree in sorted((G.degree()).items(), key=lambda x: -x[1]):
            # ofile.write(str(node) + ": "+str(degree)+'\n')
            
            ASN_info = 'Unknown'
            if str(node) in dict_ASN_info:
                ASN_info = dict_ASN_info[str(node)]
            ofile.write(f'{node}: {degree}:{ASN_info}\n')


   

    
    

    
    
    
    