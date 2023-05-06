library(ggplot2)
library(dplyr)


function_community_rank_CDF <- function(year, flag_add){
    version <- "0101"

    if(flag_add) {
        ifile_name <- paste0("playEgOnData/results/", year, version, "/added_ASR_community_distribution")
        ofile_name <- paste0("report/R/edge_fluc_community_distribution/result/added_ASR_community_rank_cdf_",year,version,".png")
        gtitle <- paste0("CDF of added ASR Community Ranks ",year)
    }else {
        ifile_name <- paste0("playEgOnData/results/", year, version, "/deleted_ASR_community_distribution")
        ofile_name <- paste0("report/R/edge_fluc_community_distribution/result/deleted_ASR_community_rank_cdf_",year,version,".png")
        gtitle <- paste0("CDF of deleted ASR Community Ranks ",year)
    }

    data <- read.table(ifile_name, sep=":", col.names=c("asn1", "asn2", "num", "rank1", "rank2"))
    # aggregate the data based on rank1
    cdf_data <- data %>%
      group_by(rank1) %>%
      summarize(count = sum(num)) %>%
      mutate(percent = cumsum(count)/sum(count))


    data2 <- data %>% arrange(rank2)
     # aggregate the data based on rank2
    cdf_data2 <- data2 %>%
      group_by(rank2) %>%
      summarize(count = sum(num)) %>%
      mutate(percent = cumsum(count)/sum(count))
    
    percentage_same = read.table(paste0("report/R/edge_fluc_community_distribution/middle/", year, version, flag_add))

    p <- ggplot() +
        geom_line(data = cdf_data, aes(x=rank1, y=percent, color = "One end")) +
        geom_line(data = cdf_data2, aes(x=rank2, y=percent, color = "Both end")) +
        geom_step() +
        xlab("Community Rank(by size)") +
        ylab("Percentage of ASR") +
        ggtitle(gtitle) +
        annotate("text", x=9, y=0.08, label=paste0("Percentage of ASR within same community: ", percentage_same)) +
        scale_x_continuous(breaks = seq(min(data$rank2), max(data$rank2), by = 2)) +
        scale_y_continuous(breaks = seq(round(min(cdf_data$percent),digits = 1), max(cdf_data$percent), by = 0.1)) +
        scale_fill_manual(values=c("#FDD835","#1b9e77"), 
            labels=c("One end", "Both end")) +
        guides(color = guide_legend(title = NULL))

    ggsave(ofile_name, plot = p, width = 8, height = 6, dpi = 300)
}

# years <- seq(2000, 2023, 1)
function_community_rank_CDF(2001, 1)
function_community_rank_CDF(2001, 0)

