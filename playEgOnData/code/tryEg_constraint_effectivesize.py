from include import *

if __name__ == '__main__':
    DEBUG = 0
    for fn in listFileName_1998:
        G = buildAsRelGraph(fn)

        version = fn[31:39]


        # constraints = eg.constraint(G)
        # ofile = open('playEgOnData/results/'+version+'/constraint','w')
        # for node,con in sorted(constraints.items(), key=lambda x: -x[1]):
        #     ofile.write(str(node)+':'+str(con)+'\n')
        # ofile.close()

        effective_size = eg.effective_size(G)
        # deal with 'nan'
        for node, es in effective_size.items():
            if str(es) == 'nan':
                effective_size[node] = -1

        ofile = open('playEgOnData/results/'+version+'/effective_size','w')
        for node,es in sorted(effective_size.items(), key=lambda x: -x[1]):
            ofile.write(str(node)+':'+str(es)+'\n')
        ofile.close()

        # Draw the Graph, and the shs is marked by red star
        # eg.draw_SHS_center(G, shs)

        # Draw CDF curves of "Number of Followers" of SH spanners and ordinary users in G.
        # eg.plot_Followers(G, shs)
    

    
    
    
    