library(ggplot2)

# 6939 : HURRICANE, US
df_6939 <- data.frame(year = seq(2000, 2023, 1), 
degree =as.numeric(c(13,37,58,71,417,738,921,985,1433,1764,2451,2878,3863,5048,6216,6627,7842,11417,12534,13399,14681,15930,16867,17395)),
rank = as.numeric(c(239,153,113,109,25,16,13,9,6,7,4,4,2,1,1,1,1,1,1,1,1,1,1,1)))

# 8359 : MTS, RU
df_8359 <- data.frame(year = seq(2000, 2023, 1), 
degree = as.numeric(c(7,9,11,11,11,16,22,83,796,1037,1322,1692,1776,1961,2176,2380,1140,1072,1570,1354,867,1997,1811,2007)),
rank = as.numeric(c(428,610,638,801,916,843,785,266,24,19,18,10,14,10,13,8,95,112,91,127,176,75,101,87)))

# 14840 : BR Digital, BR
df_14840 <- data.frame(year = seq(2000, 2023, 1),
degree = as.numeric(c(NA,2,NA,NA,NA,2,2,4,4,2,5,18,472,656,823,1017,1445,1665,2294,2314,5522,8967,9554,759)),
rank = as.numeric(c(NA,5913,NA,NA,NA,12683,14269,3635,3930,18917,4098,1933,98,99,88,73,55,79,57,65,10,3,2,214)))

# 3303 : SWISSCOM Swisscom Switzerland Ltd, CH
df_3303 <- data.frame(year = seq(2000, 2023, 1),
degree = as.numeric(c(42,96,272,152,819,1025,1051,629,749,844,938,1161,1081,970,860,943,735,739,803,1216,1658,1832,2092,2435)),
rank = as.numeric(c(69,55,21,61,8,7,9,26,26,28,30,25,36,51,83,84,136,144,141,139,121,89,84,68)))





# create the line chart
p <- ggplot() +
  # 8359
  geom_line(data = df_8359, aes(x = year, y = degree), color = "blue") +
  geom_point(data = df_8359,aes(x = year, y = degree), color = ifelse(df_8359$rank > 10, 1, 2), size = 1) +
  geom_text(data = df_8359,aes(x = year, y = degree, label = rank), vjust = -1, size = 2, color = ifelse(df_8359$rank > 10, 1, 2)) +
  # 14840
  geom_line(data = df_14840, aes(x = year, y = degree), color = "blue") +
  geom_point(data = df_14840,aes(x = year, y = degree), color = ifelse(df_14840$rank > 10, 1, 2), size = 1) +
  geom_text(data = df_14840,aes(x = year, y = degree, label = rank), vjust = -1, size = 2, color = ifelse(df_14840$rank > 10, 1, 2)) +
  # 3303
  geom_line(data = df_3303, aes(x = year, y = degree), color = "blue") +
  geom_point(data = df_3303,aes(x = year, y = degree), color = ifelse(df_3303$rank > 10, 1, 2), size = 1) +
  geom_text(data = df_3303,aes(x = year, y = degree, label = rank), vjust = -1, size = 2, color = ifelse(df_3303$rank > 10, 1, 2)) +
  scale_x_continuous(breaks = seq(2000, 2023, 2)) +
  labs(x = "Year", y = "Degree", title = "Degree & Rank of Top 10 ASes") +
  scale_color_manual(values = c("blue", "red"), labels = seq(1,2,1))


ggsave("AS_top_10_degree_rank.png", path = "report/R/AS_top_10_trend/results",plot = p, width = 8, height = 6, dpi = 300, device = "png")
