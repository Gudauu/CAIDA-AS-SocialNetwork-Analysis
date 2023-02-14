from include import *

if __name__ == '__main__':
    DEBUG = 0
    versions = ['19980201','19980301','19980401']
    for version in versions:
    # version = '19980101'

        G = getG(version,DEBUG)

        number_shs = 10

        ofile = open('playEgOnData/results/'+version+'/SHS_common_greedy_'+str(number_shs),'w')

        shs = eg.common_greedy(G, number_shs)
        for p in shs:
            ofile.write(str(p)+'\n')
        ofile.close()

        # Draw the Graph, and the shs is marked by red star
        # eg.draw_SHS_center(G, shs)

        # Draw CDF curves of "Number of Followers" of SH spanners and ordinary users in G.
        # eg.plot_Followers(G, shs)
    

    
    
    
    