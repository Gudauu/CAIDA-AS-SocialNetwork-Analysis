library(ggplot2)


function_ASR_size_across_year <- function(version = "0101"){
    # read the data from the file
    years <- seq(2000, 2023, 1)
    vec_size_node <- c()
    vec_size_edge <- c()
    for(year in years){
        file_name <- paste0("./playEgOnData/results/", year, version, "/basic")
        lines <- readLines(file_name)

        line_node <- lines[1]
        line_edge <- lines[2]
        size_node <- sapply(strsplit(line_node, ": "), "[[", 2)#[1]
        # print(size_node)
        size_edge <- sapply(strsplit(line_edge, ": "), "[[", 2)
        vec_size_node <- c(vec_size_node, size_node)
        vec_size_edge <- c(vec_size_edge, size_edge)
    }
    vec_size_edge_expo <- scan(text =  readLines("./report/R/basic/ASR_exponential_pred")[1], sep = ",")

    df_node <- data.frame(x = years, y = as.numeric(vec_size_node))
    df_edge <- data.frame(x = years, y = as.numeric(vec_size_edge))
    df_edge_fit <- data.frame(x = years, y = as.numeric(vec_size_edge_expo))


    p <- ggplot() +
    # edges expo fit line
    geom_line(data = df_edge_fit, aes(x = x, y = y, color = "ASRPredict")) +
    geom_point(data = df_edge_fit, aes(x = x, y = y, color = "ASRPredict"), size = 2) +
    # geom_text(data = df_edge_fit, aes(x = x, y = y, label = y), vjust = -1, size = 2, color = "black") +
    # nodes line
    geom_line(data = df_node, aes(x = x, y = y, color = "AS")) +
    geom_point(data = df_node, aes(x = x, y = y, color = "AS"), size = 2) +
    geom_text(data = df_node, aes(x = x, y = y, label = y), vjust = -1, size = 2, color = "black") +
    # edges line
    geom_line(data = df_edge, aes(x = x, y = y, color = "ASR")) +
    geom_point(data = df_edge, aes(x = x, y = y, color = "ASR"), size = 2) +
    geom_text(data = df_edge, aes(x = x, y = y, label = y), vjust = -1, size = 2, color = "black") +
    # tags, scale, label
    scale_color_manual(values = c("#0277BD", "#E64A19","#4DB6AC"), labels = c("AS count", "ASR count","ASR Prediction")) +
    scale_x_continuous(breaks = seq(2000, 2023, 2)) +
    labs(x = "Year", y = "Total Size", title = "Size of ASes and ASRs") +
    # hide title on color legend
    guides(color = guide_legend(title = NULL))



    ggsave("report/R/basic/result/size_of_ASes_and_ASRs.png",plot = p, width = 8, height = 6, dpi = 300, device = "png")

}


function_ASR_size_across_year("0101")