library(ggplot2)
library(dplyr)


function_community_rank_CDF <- function(year){
    version <- "0101"

    ifile_name_add <- paste0("playEgOnData/results/", year, version, "/added_ASR_community_distribution")
    ifile_name_del <- paste0("playEgOnData/results/", year, version, "/deleted_ASR_community_distribution")
    ofile_name <- paste0("report/R/edge_fluc_community_distribution/result/fluc_ASR_community_rank_cdf_",year,version,".png")
    gtitle <- paste0("CDF of added & deleted ASR Community Ranks ",year)

    data <- read.table(ifile_name_add, sep=":", col.names=c("asn1", "asn2", "num", "rank1", "rank2"))
    # aggregate the data based on rank1
    cdf_add <- data %>%
      group_by(rank1) %>%
      summarize(count = sum(num)) %>%
      mutate(percent = cumsum(count)/sum(count))


    data2 <- data %>% arrange(rank2)
     # aggregate the data based on rank2
    cdf_add2 <- data2 %>%
      group_by(rank2) %>%
      summarize(count = sum(num)) %>%
      mutate(percent = cumsum(count)/sum(count))
    
    data <- read.table(ifile_name_del, sep=":", col.names=c("asn1", "asn2", "num", "rank1", "rank2"))
    # aggregate the data based on rank1
    cdf_del <- data %>%
      group_by(rank1) %>%
      summarize(count = sum(num)) %>%
      mutate(percent = cumsum(count)/sum(count))


    data2 <- data %>% arrange(rank2)
     # aggregate the data based on rank2
    cdf_del2 <- data2 %>%
      group_by(rank2) %>%
      summarize(count = sum(num)) %>%
      mutate(percent = cumsum(count)/sum(count))
    
    percentage_same = read.table(paste0("report/R/edge_fluc_community_distribution/middle/", year, version, 1))
    middle_x <- round((max(data$rank2) - min(data$rank2))/2 + min(data$rank2))
    p <- ggplot() +
        geom_line(data = cdf_add2, aes(x=rank2, y=percent, color = "Added Both")) +
        geom_line(data = cdf_add, aes(x=rank1, y=percent, color = "Added One")) +
        geom_line(data = cdf_del2, aes(x=rank2, y=percent, color = "Deleted Both")) +
        geom_line(data = cdf_del, aes(x=rank1, y=percent, color = "Deleted One")) +
        geom_step() +
        xlab("Community Rank(by size)") +
        ylab("Percentage of ASR") +
        ggtitle(gtitle) +
        annotate("text", x=middle_x, y=0.08, label=paste0("Percentage of ASR within same community: ", percentage_same)) +
        scale_x_continuous(breaks = seq(min(data$rank2), max(data$rank2), by = round((max(data$rank2)-min(data$rank2))/20,digits = 0))) +
        scale_y_continuous(breaks = seq(round(min(cdf_add$percent),digits = 1), max(cdf_add$percent), by = 0.1)) +
        scale_fill_manual(values=c("#FDD835","#1b9e77","#d95f02","#2196F3"), 
            labels=c("Added: Both end", "Added: One end","Deleted: Both end", "Deleted: One end")) +
        guides(color = guide_legend(title = NULL))

    ggsave(ofile_name, plot = p, width = 8, height = 6, dpi = 300)
}

years <- seq(2001, 2022, 1)
for(year in years) {
    function_community_rank_CDF(year)
    function_community_rank_CDF(year)
}


