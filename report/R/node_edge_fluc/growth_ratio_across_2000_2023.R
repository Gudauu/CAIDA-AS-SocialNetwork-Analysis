library(ggplot2)

# Example data
years <- 2001:2023


# ratio: amount of new / amount of delted. When ratio is 1, no delta.
ratio_node <- as.numeric(c(7.65,3.14,2.37,2.59,3.17,3.18,3.35,3.15,3.43,2.48,2.88,3.08,2.73,2.49,1.00,4.38,2.51,2.51,2.29,2.39,2.24,1.77,1.48))
ratio_edge <- as.numeric(c(3.47,1.79,1.53,1.58,1.91,1.69,1.69,1.72,1.64,1.41,1.49,2.07,1.62,2.11,1.33,1.89,1.61,1.39,1.91,1.49,0.91,1.31,0.99))

# Create data frame
df <- data.frame(years, ratio_node, ratio_edge)

p <- ggplot() +
    # node ratio line
    geom_line(data = df, aes(x = years, y = ratio_node, color = "AS")) +
    geom_point(data = df, aes(x = years, y = ratio_node, color = "AS"), size = 2) +
    geom_text(data = df, aes(x = years, y = ratio_node, label = ratio_node), vjust = -1, size = 2, color = "black") +
    # edge ratio line
    geom_line(data = df, aes(x = years, y = ratio_edge, color = "ASR")) +
    geom_point(data = df, aes(x = years, y = ratio_edge, color = "ASR"), size = 2) +
    geom_text(data = df, aes(x = years, y = ratio_edge, label = ratio_edge), vjust = -1, size = 2, color = "black") +

    scale_fill_manual(values=c("#FDD835","#1b9e77"), 
                        labels=c("AS", "ASR")) +
    labs(title="Added / Deleted by Year",
        x="Year",
        y="Ratio") +
    # hide title on color legend
    guides(color = guide_legend(title = NULL)) +
    scale_x_continuous(breaks = seq(2001, 2023, 2))


ggsave("report/R/node_edge_fluc/result/ratio_2000_2023.png",plot = p, width = 8, height = 6, dpi = 300, device = "png")


