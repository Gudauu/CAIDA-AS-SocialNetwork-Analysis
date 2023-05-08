library(igraph)
library(ggplot2)
library(ggforce)
library(scales)

function_ego_visualize <- function(year,version,asn){
    mygraph <- read_graph(paste0("report/R/AS_ego_network/middle/",asn,"_",year,version,".graphml"), format = "graphml")

    dictionary_degree <- read.table(paste0("report/R/AS_ego_network/middle/degree_",asn,"_",year,version), sep = ":", col.names = c("ID", "degree"))

    V(mygraph)$degree <- dictionary_degree$degree[match(V(mygraph)$id, dictionary_degree$ID)]

    V(mygraph)$scaled_degree <- rescale(V(mygraph)$degree, to = c(8, 20))

    # mylayout <- layout_with_fr(mygraph, area = 100 * vcount(mygraph))
    # test_layout <- layout_(g,with_dh(weight.edge.lengths = edge_density(g)/1000))

    pdf(paste0("report/R/AS_ego_network/results/ego_",asn,"_",year,version, ".pdf"), width = 8, height = 8)
    plot(mygraph,
         vertex.label = paste(V(mygraph)$id, V(mygraph)$degree, sep="\n"),
         vertex.size = V(mygraph)$scaled_degree,
         vertex.color = ifelse(V(mygraph)$id == asn, "red", "#d2b145"),
         vertex.label.cex = 0.3, vertex.label.dist = 0,
         vertex.label.color = "black",
         vertex.label.family = "Helvetica",
         edge.arrow.size = 0.5) #,
        #  layout = test_layout)
    dev.off()
}

asn <- 855 #6295
# asn <- 9186
years <- seq(2000,2023,1)
for(year in years) {
    function_ego_visualize(year,"0101", asn)
}


