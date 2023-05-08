library(igraph)
library(ggplot2)
library(ggforce)

function_ego_visualize <- function(year,version,asn){
    # Read the graph from the GraphML file
    mygraph <- read_graph(paste0("report/R/AS_ego_network/middle/",asn,"_",year,version,".graphml"), format = "graphml")

    # Convert the igraph object to data frames
    node_df <- as_data_frame(mygraph, "vertices")
    edge_df <- as_data_frame(mygraph, "edges")

    # Plot the graph using ggplot2
    ggplot() +
      geom_link(data = edge_df, aes(x = x, y = y, alpha = weight), color = "gray50") +
      geom_point(data = node_df, aes(x = x, y = y, size = degree, color = name)) +
      geom_text(data = node_df, aes(x = x, y = y, label = name), vjust = 1.5) +
      scale_size_continuous(range = c(5, 15)) +
      scale_color_discrete(guide = FALSE) +
      theme_void()

    # Save the plot using ggsave
    ggsave(paste0("report/R/AS_ego_network/results/ego_",asn,"_",year,version, ".png"), width = 8, height = 8, device = "png")

}

function_ego_visualize(2000,"0101",200)


