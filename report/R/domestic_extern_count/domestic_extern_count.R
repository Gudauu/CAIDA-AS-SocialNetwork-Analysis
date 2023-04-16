# my_str <- "hello from vscode!"
# print(my_str)

library(ggplot2)

# set the working directory to the directory where your R code is located
setwd("report/R/domestic_extern_count")

# read the data from the file
# data <- read.table("../../../playEgOnData/results/by_country/CN/count_domestic_extern_across_2001_2023", header=FALSE)

lines <- readLines("../../../playEgOnData/results/by_country/CN/count_domestic_extern_across_2001_2023")

line_domestic <- lines[1]
line_foreign <- lines[2]
line_top_foreign <- lines[3]

# assign the two lists to separate variables
# domestic <- as.numeric(unlist(strsplit(as.character(data[1,1]), split=",")))
# foreign <- as.numeric(unlist(strsplit(as.character(data[2,1]), split=",")))

vec_domestic <- scan(text = line_domestic , sep = ",")
vec_foreign <- scan(text = line_foreign , sep = ",")
vec_top_foreign <- scan(text = line_top_foreign , sep = ",")


# create a vector of years from 2001 to 2023
years <- seq(2001, 2023, 1)

df_domestic <- data.frame(x = years, y = vec_domestic)
df_foreign <- data.frame(x = years, y = vec_foreign)
df_top_foreign <- data.frame(x = years, y = vec_top_foreign)


# # create the line chart
# p <- ggplot(df_domestic, aes(x = x, y = y)) + 
#   geom_line(color = "blue") +
#   geom_point(color = "blue", size = 2) +
#   geom_text(aes(label = y), vjust = -1, size = 2, color = "black") +
p <- ggplot() +
  # domestic line
  geom_line(data = df_domestic, aes(x = x, y = y, color = "Domestic")) +
  geom_point(data = df_domestic, aes(x = x, y = y, color = "Domestic"), size = 2) +
  geom_text(data = df_domestic, aes(x = x, y = y, label = y), vjust = -1, size = 2, color = "black") +
  # foreign line
  geom_line(data = df_foreign, aes(x = x, y = y, color = "Foreign")) +
  geom_point(data = df_foreign, aes(x = x, y = y, color = "Foreign"), size = 2) +
  geom_text(data = df_foreign, aes(x = x, y = y, label = y), vjust = -1, size = 2, color = "black") +
  # top foreign line
  geom_line(data = df_top_foreign, aes(x = x, y = y, color = "TopForeign")) +
  geom_point(data = df_top_foreign, aes(x = x, y = y, color = "TopForeign"), size = 2) +
  geom_text(data = df_top_foreign, aes(x = x, y = y, label = y), vjust = -1, size = 2, color = "black") +
  # tags, scale, label
  scale_color_manual(values = c("blue", "red","green"), labels = c("domestic count", "foreign count","top foreign country count")) +
  scale_x_continuous(breaks = seq(2001, 2023, 2)) +
  labs(x = "Year", y = "Count of AS relationships", title = "CN domestic and foreign AS rel Count")



ggsave("results/domestic_foreign_CN.png",plot = p, width = 8, height = 6, dpi = 300, device = "png")
