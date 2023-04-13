# my_str <- "hello from vscode!"
# print(my_str)

library(ggplot2)

# create a data frame
data <- data.frame(year = seq(2001, 2023, 1), value = c("27", "70", "108", "160", "190", "220", "258", "304", "360", "356", "297", "336", "343", "357", "417", "453", "549", "595", "743", "832", "830", "909", "905"))

# convert value to numeric
data$value <- as.numeric(data$value)

# create the line chart
p <- ggplot(data, aes(x = year, y = value)) +
  geom_line(color = "blue") +
  geom_point(color = "blue", size = 2) +
  geom_text(aes(label = value), vjust = -1, size = 2, color = "black") +
  scale_x_continuous(breaks = seq(2001, 2023, 2)) +
  labs(x = "Year", y = "Count of AS relationships", title = "CN domestic AS rel Count")



ggsave("domestic_ASR_count_CN.png", path = "/home/gudau/Documents/School/year4/graduatePaper/report/R",plot = p, width = 8, height = 6, dpi = 300, device = "png")
