library(ggplot2)
library(reshape2)

# Example data
years <- 2001:2023
lines <- readLines("playEgOnData/results/2000-2023/edge_fluc")
# lines <- readLines("playEgOnData/results/2000-2023/node_fluc")
added_amount <- scan(text = lines[1], sep = ",")
deleted_amount <- scan(text = lines[2], sep = ",")
delta_amount <- scan(text = lines[3], sep = ",")

# Create data frame
df <- data.frame(years, added_amount, deleted_amount, delta_amount)

# Melt data for stacked bar chart
df.melt <- melt(df, id.vars="years")

# Create stacked bar chart
p <- ggplot(df.melt, aes(x=years, y=value, fill=variable)) +
    geom_bar(stat="identity") +
    scale_fill_manual(values=c("#d95f02", "#FDD835","#1b9e77"), 
                        labels=c("Added ASR", "Deleted ASR", "Delta ASR")) +
    labs(title="ASR Added and Deleted by Year",
        x="Year",
        y="Number of ASR") +
    geom_text(aes(label=value, group=variable),
        position=position_stack(vjust=0.5),
        size = 2.3,
        color="#424242") +
    scale_x_continuous(breaks = seq(2001, 2023, 2)) +
    theme(legend.position = "middle")

ggsave("report/R/node_edge_fluc/result/ASR_2000_2023.png",plot = p, width = 8, height = 6, dpi = 300, device = "png")


