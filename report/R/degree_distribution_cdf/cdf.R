library(ggplot2)


function_degree_CDF <- function(year){
    version <- "0101"
    # Read data from file
    data <- readLines(paste0("playEgOnData/results/", year, version, "/degree_distribution"))
    degrees <- rev(as.numeric(sapply(strsplit(data, ": "), "[[", 1)))
    counts <- rev(as.numeric(sapply(strsplit(data, ": "), "[[", 2)))  

    # degree: low to high

    # Calculate cumulative percentages
    total_nodes <- sum(counts) 
    cumulative_counts <- cumsum(counts)
    cumulative_percentages <- 100 * cumulative_counts / total_nodes

    df <- data.frame(x = degrees, y = cumulative_percentages)

    # Plot CDF using ggplot2
    p <- ggplot(df, aes(x = x, y = y, color = "#EF5350")) +
        geom_step() +
        labs(x = "Degree", y = "Percentage",
            title = paste0("Degree Distribution CDF ", year)) +
        # hide title on color legend
        guides(colour = FALSE)

    # Save plot as PNG using ggsave
    ggsave(paste0("report/R/degree_distribution_cdf/result/degree_distribution_cdf_", year, ".png"),
        plot = p, width = 8, height = 6, dpi = 300)
}

years <- seq(2023, 2023, 1)
for (year in years){
    function_degree_CDF(year)
}

