library(ggplot2)


# ID <- c(701,1239,3561,7018,3257,6461,1,209,3549,2914) # 2001 top 10
ID <- c(1)
# ID <- c(701,1239,7018,209,3356,8220,4589,3303,6730,6461) # 2004 top 10
# ID <- c(61568,6939,1828,35280,24482,51185,3356,58511,174,137409) # 2023 top 10
# ID <- c(39120,3356,58511,174,137409,199524)
# ID <- c(209,22822,12389,174,701,13030,7018,3356,9002) # 2010 except 6939
# ID <- c(49605,34224,25091,174,8220,58511,43531,3356,24482) #2017 except 6939
# ID <- c(7018,12989,8492,174,31500,48166,3549,3356,9002) #2014 except 6939
# palette <- as.character(c("yellow","green","pink","orange","brown","purple",""))
palette <- as.character(c("brown","red","orange","yellow","green","skyblue","blue","pink","gray")) #"purple"
idx_color <- 1

# read the file
# format:
# 14840 : BR Digital, BR
# NA,2,NA,NA,NA,2,2,4,4,2,5,18,472,656,823,1017,1445,1665,2294,2314,5522,8967,9554,759
# NA,5913,NA,NA,NA,12683,14269,3635,3930,18917,4098,1933,98,99,88,73,55,79,57,65,10,3,2,214
ifile_path <- "playEgOnData/results/2000-2023/R_track_degree_top_10"
top_AS_info <- readLines(ifile_path)

AS_names = c()
p <- ggplot() +
  scale_x_continuous(breaks = seq(2000, 2023, 2)) +
  labs(x = "Year", y = "Degree", title = "Degree & Rank of Top 10 ASes")
  # scale_color_manual(values = palette, labels = ID) + 
  # guides(color = guide_legend(title = NULL))
  # scale_color_manual(values = c("blue", "red"), labels = seq(1,2,1))



# filter the rows for the specified IDs
for(id in ID){
  idx <- grep(paste0("^", id, " :"), top_AS_info)
  AS_names <- c(AS_names, top_AS_info[idx])
  AS_degree <- as.numeric(scan(text = top_AS_info[idx + 1] , sep = ","))
  AS_rank <- as.numeric(scan(text = top_AS_info[idx + 2] , sep = ","))

  df <- data.frame(year = seq(2000, 2023, 1), 
                   degree = AS_degree,
                   rank = AS_rank)
  p <- p + 
    geom_line(data = df, aes(x = year, y = degree), color = palette[idx_color]) +
    geom_point(data = df,aes(x = year, y = degree), color = ifelse(df$rank > 10, 1, 2), size = 1) +
    geom_text(data = df,aes(x = year, y = degree, label = ifelse(rank <= 30, rank, "")), vjust = -1, hjust = 1, size = 2, color = ifelse(df$rank > 10, 1, 2))
  
  idx_color <- idx_color + 1

}
# p <- p + scale_color_manual(values = palette, labels = ID)
ggsave("ASN1_degree_rank.png", path = "report/R/AS_sample_10_trend/results",plot = p, width = 8, height = 6, dpi = 300, device = "png")




# # 6939 : HURRICANE, US
# df_6939 <- data.frame(year = seq(2000, 2023, 1), 
# degree =as.numeric(c(13,37,58,71,417,738,921,985,1433,1764,2451,2878,3863,5048,6216,6627,7842,11417,12534,13399,14681,15930,16867,17395)),
# rank = as.numeric(c(239,153,113,109,25,16,13,9,6,7,4,4,2,1,1,1,1,1,1,1,1,1,1,1)))






# # create the line chart
#   # 8359
#   geom_line(data = df_8359, aes(x = year, y = degree), color = "blue") +
#   geom_point(data = df_8359,aes(x = year, y = degree), color = ifelse(df_8359$rank > 10, 1, 2), size = 1) +
#   geom_text(data = df_8359,aes(x = year, y = degree, label = rank), vjust = -1, size = 2, color = ifelse(df_8359$rank > 10, 1, 2)) +
#   # 14840
#   geom_line(data = df_14840, aes(x = year, y = degree), color = "blue") +
#   geom_point(data = df_14840,aes(x = year, y = degree), color = ifelse(df_14840$rank > 10, 1, 2), size = 1) +
#   geom_text(data = df_14840,aes(x = year, y = degree, label = rank), vjust = -1, size = 2, color = ifelse(df_14840$rank > 10, 1, 2)) +
#   # 3303
#   geom_line(data = df_3303, aes(x = year, y = degree), color = "blue") +
#   geom_point(data = df_3303,aes(x = year, y = degree), color = ifelse(df_3303$rank > 10, 1, 2), size = 1) +
#   geom_text(data = df_3303,aes(x = year, y = degree, label = rank), vjust = -1, size = 2, color = ifelse(df_3303$rank > 10, 1, 2)) +



