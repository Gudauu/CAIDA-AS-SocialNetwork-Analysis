library(ggplot2)


function_plot_AS_degree <- function(year,ID){

  palette <- as.character(c("brown","red","orange","yellow","green","skyblue","blue","pink","gray","purple")) #
  idx_color <- 1

  # read the file
  # format:
  # 14840 : BR Digital, BR
  # NA,2,NA,NA,NA,2,2,4,4,2,5,18,472,656,823,1017,1445,1665,2294,2314,5522,8967,9554,759
  # NA,5913,NA,NA,NA,12683,14269,3635,3930,18917,4098,1933,98,99,88,73,55,79,57,65,10,3,2,214
  ifile_path <- "playEgOnData/results/2000-2023/R_track_degree_5000_5010"
  top_AS_info <- readLines(ifile_path)

  p <- ggplot() +
    scale_x_continuous(breaks = seq(2000, 2023, 2)) +
    labs(x = "Year", y = "Degree", title = "Degree & Rank of 10 Tail ASes")
    # scale_color_manual(values = palette, labels = ID) + 
    # guides(color = guide_legend(title = NULL))
    # scale_color_manual(values = c("blue", "red"), labels = seq(1,2,1))


  AS_names = c()
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
      geom_text(data = df,aes(x = year, y = degree, label = ifelse(degree > 300, degree, "")), vjust = -1, hjust = 1, size = 2, color = ifelse(df$rank > 10, 1, 2))
  
    idx_color <- idx_color + 1

  }
  # p <- p + scale_color_manual(values = palette, labels = ID)
  ggsave(paste0("AS_",year,"_tail_10_degree_rank.png"), path = "report/R/AS_sample_10_trend/results",plot = p, width = 8, height = 6, dpi = 300, device = "png")

}

# ID <- c(7018,12989,8492,174,31500,48166,3549,3356,9002) #2014 except 6939
# ID_2004 <- c(24880,12597,15685,21219,27191,29691,6798,15554,4688,17675) # 2004
# ID_2010 <- c(5408,14710,23265,7017,28745,2711,5391,12111,12180,35916) # 2010
# ID_2020 <- c(11014,11537,8839,21472,38195,133613,200794,2764,55329,5429) # 2020
ID_2004 <- c(22403,22413,22421,22486,22497,22503,22504,22518,22526,22527) # 2004
ID_2010 <- c(16399,16455,19479,20018,22562,22938,25048,25273,25582,26259) # 2010
ID_2020 <- c(29465,7604,17990,45194,9822,49666,327935,198191,24641,37515) # 2020
function_plot_AS_degree(2004, ID_2004)
function_plot_AS_degree(2010, ID_2010)
function_plot_AS_degree(2020, ID_2020)




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



