from include import *


def basic(version)->None:
    G = getG(version)
    ofile = open('playEgOnData/results/'+version+'/basic','w')
    ofile.write('node size: '+str(len(G.nodes))+'\n')
    ofile.write('edge size: '+str(len(G.edges))+'\n')
    ofile.write('number of connected comp:'+str(eg.number_connected_components(G))+'\n')
    ofile.write('average degree:'+str(sum(G.degree().values())/len(G.degree()))+'\n')
    ofile.close()

def connected_components(version) -> None:
    G = getG(version)
    list_cc = eg.connected_components(G)
    if len(list_cc) == 1:
        return
    for cc in list_cc:
        ic(len(cc))
        if len(cc) < 40:
            print(','.join([str(_item) for _item in cc]))
    ofile = open('playEgOnData/results/2000-2023/non_connected_components','a')
    # len_min = -1
    # for cc in list_cc:
    #     if len_min == -1 or len(cc) <= len_min:
    #         len_min = len(cc)
    # for cc in list_cc:
    #     if len_min == len(cc):
    #         ofile.write(f"{version}:{len(list_cc)}:{len(cc)}\n")
    #         ofile.write( + '\n')


if __name__ == '__main__':
    DEBUG = 0
    for year in range(2005,2005+1):
        version = f'{year}0101'
        connected_components(version)
        
        

        


    
    