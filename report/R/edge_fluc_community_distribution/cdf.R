library(ggplot2)


function_community_rank_CDF <- function(year){
    version <- "0101"

    data <- readLines(paste0("playEgOnData/results/", year, version, "/added_ASR_community_distribution"))
    data_df <- data.frame(do.call(rbind, strsplit(data, ":|,")))


    data_df[,1:4] <- lapply(data_df[,1:4], as.integer)
    data_df[,5] <- as.numeric(data_df[,5])


    cum_instances <- tapply(data_df[,3], data_df[,4], cumsum)
    print(cum_instances)

    cum_instances <- unlist(cum_instances)
    # print(cum_instances)
    total_instances <- sum(data_df[,3])

    # print(cum_counts)
    cdf_values <-  100 * cumsum(cum_instances) / total_instances

    # abline(h = 0.5, lty = 2)

    ggplot(data = data.frame(Rank = names(cdf_values), CDF = cdf_values), aes(x = Rank, y = CDF)) +
      geom_line() +
      xlab("Rank") +
      ylab("CDF")

    # Step 8
    ggsave(paste0("report/R/edge_fluc_community_distribution/result/added_ASR_community_rank_cdf_",year,version,".png"),
        width = 6, height = 4, dpi = 300)
}

# years <- seq(2000, 2023, 1)
function_community_rank_CDF(2001)

