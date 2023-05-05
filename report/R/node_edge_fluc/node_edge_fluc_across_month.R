library(ggplot2)
library(reshape2)

function_fluc_across_month <- function(year){
    # Example data
    months <- 2:12
    lines <- readLines(paste0("playEgOnData/results/", year, "/node_edge_fluc_by_month"))
    ## node first
    added_amount <- scan(text = lines[1], sep = ",")
    deleted_amount <- scan(text = lines[2], sep = ",")
    delta_amount <- added_amount - deleted_amount
    # Create data frame
    df <- data.frame(months, added_amount, deleted_amount, delta_amount)

    # Melt data for stacked bar chart
    df.melt <- melt(df, id.vars="months")

    # Create stacked bar chart
    p <- ggplot(df.melt, aes(x=months, y=value, fill=variable)) +
        geom_bar(stat="identity") +
        scale_fill_manual(values=c("#d95f02", "#FDD835","#1b9e77"), 
                            labels=c("Added AS", "Deleted AS", "Delta AS")) +
        labs(title= paste0("AS Added and Deleted by Month in ",year),
            x="Month",
            y="Number of AS") +
        geom_text(aes(label=value, group=variable),
            position=position_stack(vjust=0.5),
            size = 2.3,
            color="#424242") +
        scale_x_continuous(breaks = seq(1, 12, 2)) +
        theme(legend.position = "middle")

    ggsave(paste0("report/R/node_edge_fluc/result/across_month/AS_", year, ".png"),plot = p, width = 8, height = 6, dpi = 300, device = "png")
    ## edges next
    added_amount <- scan(text = lines[3], sep = ",")
    deleted_amount <- scan(text = lines[4], sep = ",")
    delta_amount <- added_amount - deleted_amount
    # Create data frame
    df <- data.frame(months, added_amount, deleted_amount, delta_amount)

    # Melt data for stacked bar chart
    df.melt <- melt(df, id.vars="months")

    # Create stacked bar chart
    p <- ggplot(df.melt, aes(x=months, y=value, fill=variable)) +
        geom_bar(stat="identity") +
        scale_fill_manual(values=c("#d95f02", "#FDD835","#1b9e77"), 
                            labels=c("Added ASR", "Deleted ASR", "Delta ASR")) +
        labs(title="ASR Added and Deleted by Month",
            x="Month",
            y="Number of ASR") +
        geom_text(aes(label=value, group=variable),
            position=position_stack(vjust=0.5),
            size = 2.3,
            color="#424242") +
        scale_x_continuous(breaks = seq(1, 12, 2)) +
        theme(legend.position = "middle")

    ggsave(paste0("report/R/node_edge_fluc/result/across_month/ASR_", year, ".png"),plot = p, width = 8, height = 6, dpi = 300, device = "png")
}

years = c(2006, 2010, 2014, 2018)
for(year in years){
    function_fluc_across_month(year)
}

