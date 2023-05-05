library(ggplot2)


fluc_node_degree_distribution <- function(version){
    ifile_name <- paste0("playEgOnData/results/",
        version, "/added_AS_degree_distribution")
    # read data from file
    data <- read.table(ifile_name, sep=":", col.names=c("degree", "count"))

    # plot histogram
    ggplot(data, aes(x = degree, y = count)) +
      geom_bar(stat="identity") +
      labs(x="Degree", y="Count", title=paste0("Added AS Degree distribution ",version)) +
      theme_bw()

    # save the plot as a png file
    ggsave(paste0("report/R/node_edge_fluc_degree_distribution/result/added_AS_", version, ".png"), width=8, height=6, dpi=300)

    # plot histogram
    # p <- hist(data$degree, breaks=max(data$degree), main="Degree Distribution", xlab="Degree", ylab="Count")
    # ggsave(,plot = p, width = 8, height = 6, dpi = 300, device = "png")

}


fluc_node_degree_distribution(20230101)

