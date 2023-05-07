library(ggplot2)


function_fluc_relation_across_years <- function(year_start, year_end){
    lines <- readLines(paste0("report/R/node_edge_fluc_relation/middle/", year_start, "_", year_end))

    added_ratio <- scan(text = lines[1], sep = ",")
    added_std <- scan(text = lines[2], sep = ",")
    deleted_ratio <- scan(text = lines[3], sep = ",")
    deleted_std <- scan(text = lines[4], sep = ",")

    years <- seq(year_start + 1,year_end,1)

    # Create data frame
    df <- data.frame(years, added_ratio, added_std, deleted_ratio, deleted_std)
    print(df)

    p <- ggplot(data = df, aes(x = years)) +
        # added ratio line
        geom_line(aes(y = added_ratio, color = "added ASR within added AS")) +
        geom_point(aes(y = added_ratio, color = "added ASR within added AS"), size = 2) +
        geom_text(aes(y = added_ratio, label = round(added_ratio, digits = 3)), vjust = -1, size = 2, color = "black") +
        # added standard line
        geom_line(aes(y = added_std, color = "added AS")) +
        geom_point(aes(y = added_std, color = "added AS"), size = 2) +
        geom_text(aes(y = added_std, label = round(added_std, digits = 3)), vjust = -1, size = 2, color = "black") +
        # deleted ratio line
        geom_line(aes(y = deleted_ratio, color = "deleted ASR within deleted AS")) +
        geom_point(aes(y = deleted_ratio, color = "deleted ASR within deleted AS"), size = 2) +
        geom_text(aes(y = deleted_ratio, label = round(deleted_ratio, digits = 3)), vjust = -1, size = 2, color = "black") +
        # deleted standard line
        geom_line(aes(y = deleted_std, color = "deleted AS")) +
        geom_point(aes(y = deleted_std, color = "deleted AS"), size = 2) +
        geom_text(aes(y = deleted_std, label = round(deleted_std, digits = 3)), vjust = -1, size = 2, color = "black") +

        scale_fill_manual(values=c("#d95f02","#FDD835","#01579B","#42A5F5"), 
                            labels=c("added ASR with one end in added AS", "added AS","deleted ASR with one end in deleted AS","deleted AS")) +
        labs(title="Added(Deleted) AS(ASR) ratio",
            x="Year",
            y="Ratio") +
        # hide title on color legend
        guides(color = guide_legend(title = NULL)) +
        scale_x_continuous(breaks = seq(year_start + 1, year_end, 1))

    ggsave(paste0("report/R/node_edge_fluc_relation/result/", year_start,"_", year_end, ".png"),plot = p, width = 8, height = 6, dpi = 300, device = "png")
  
}

function_fluc_relation_across_years(2000, 2010)

