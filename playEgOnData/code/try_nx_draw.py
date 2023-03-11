from include import *
import networkx as nx
import matplotlib.pyplot as plt

# Create an example graph
G = nx.DiGraph()
# G = getG('19980101',flag_nx=True)
G.add_edges_from([(1,2),(2,3),(3,4)])

# Define the edges to be colored red
red_edges = [(2,3)]
# (1,33),
# (1,34),
# (1,46),
# (1,48),
# (1,49),
# (1,70),
# (1,71),
# (1,77),
# (1,90),
# (1,109),
# (1,111),
# (1,140),
# (1,144),
# (1,157),
# (1,174),
# (1,199),
# (1,201),
# (1,286),
# (1,293),
# (1,557),
# (1,613),
# (1,625),
# (1,701),
# (1,714)]

# Draw the graph
pos = nx.spring_layout(G)  # Define the layout of the graph
nx.draw_networkx_nodes(G, pos,node_size=30,alpha=0)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r')  # Draw red edges
nx.draw_networkx_labels(G, pos)

plt.axis('off')  # Turn off the axis
plt.show()  # Display the graph
