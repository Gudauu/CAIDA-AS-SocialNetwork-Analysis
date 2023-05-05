import os
import networkx as nx
import community
# import community.community_louvain

class louvain:
    def community_detection(self,year:int,suffix:str = "0101") -> None:
        # Create an empty undirected graph
        G = nx.Graph()

        # Set the path to the directory containing the data
        time_dir = f"playEgOnData/results/{year}{suffix}"

        # Loop through each ccdirectory in the "by_country" directory
        for ccdir in os.listdir(os.path.join(time_dir, "by_country")):
            if str(ccdir) in ["ZZ","00"]:  
                continue
            # Get the full path to the neighbors_count_by_country file
            filepath = os.path.join(time_dir, "by_country", ccdir, "neighbors_count_by_country")

            # Read in the file and parse each line to get the neighbor and weight
            with open(filepath, "r") as f:
                for line in f:
                    neighbor, weight = line.strip().split(":")
                    if str(neighbor) in ["ZZ","00"]:#[,"et","ts"]:  
                        continue
                    weight = int(weight)
                    # Check if the edge already exists
                    if not G.has_edge(ccdir, neighbor):
                        # Add an edge between the country and its neighbor with the specified weight
                        G.add_edge(ccdir, neighbor, weight=weight)
        # run community detection louvain
        # Run Louvain community detection algorithm
        partition = community.best_partition(G)

        # Create a dictionary to store the communities
        self.communities = {}

        # Loop through each node and its community assignment
        for node, community_id in partition.items():
            # If the community doesn't exist yet, create a new one
            if community_id not in self.communities:
                self.communities[community_id] = []

            # Add the node to the community
            self.communities[community_id].append(node)
        ofile = open(f"{time_dir}/community_louvain","w")
        # Print the communities in an easy-to-read format
        for i, nodes in self.communities.items():
            ofile.write(f"{','.join(sorted(nodes))}\n")
            # print(f"Community {i}: {', '.join(sorted(nodes))}")



if __name__ == '__main__':
    for year in range(2000,2023+1):
        community_detection(year,"0101")


