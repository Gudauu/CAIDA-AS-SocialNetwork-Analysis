library(ggplot2)


function_fluc_relation_across_years <- function(year_start, year_end){
    lines <- readLines(paste0("report/R/node_edge_fluc_relation/middle/", year_start, "_", year_end))

    added_ratio <- scan(text = lines[1], sep = ",")
    added_pct <- scan(text = lines[2], sep = ",")
    deleted_ratio <- scan(text = lines[3], sep = ",")
    deleted_pct <- scan(text = lines[4], sep = ",")
    added_ratio_both <- scan(text = lines[5], sep = ",")
    deleted_ratio_both <- scan(text = lines[6], sep = ",")

    years <- seq(year_start + 1,year_end,1)
    added_std <- sapply(added_pct, function(x) 2*x - 2*(x^2))
    added_both_std <- sapply(added_pct, function(x) x^2)
    deleted_std <- sapply(deleted_pct, function(x) 2*x - 2*(x^2))
    deleted_both_std <- sapply(deleted_pct, function(x) x^2)


    # Create data frame
    df <- data.frame(years, added_ratio, added_ratio_both, added_std, added_both_std,
        deleted_ratio, deleted_ratio_both, deleted_std, deleted_both_std)
    # print(df)

    p <- ggplot(data = df, aes(x = years)) +
        # added ratio line
        geom_line(aes(y = added_ratio, color = "ASR with one end in added AS")) +
        geom_point(aes(y = added_ratio, color = "ASR with one end in added AS"), size = 2) +
        geom_text(aes(y = added_ratio, label = round(added_ratio, digits = 3)), vjust = -1, size = 2, color = "black") +
        # added ratio line
        geom_line(aes(y = added_ratio_both, color = "ASR with both ends in added AS")) +
        geom_point(aes(y = added_ratio_both, color = "ASR with both ends in added AS"), size = 2) +
        geom_text(aes(y = added_ratio_both, label = round(added_ratio_both, digits = 3)), vjust = -1, size = 2, color = "black") +
        # added standard line
        geom_line(aes(y = added_std, color = "pivot for one")) +
        geom_point(aes(y = added_std, color = "pivot for one"), size = 2) +
        geom_text(aes(y = added_std, label = round(added_std, digits = 3)), vjust = -1, size = 2, color = "black") +
        # added standard line(both)
        geom_line(aes(y = added_both_std, color = "pivot for both")) +
        geom_point(aes(y = added_both_std, color = "pivot for both"), size = 2) +
        geom_text(aes(y = added_both_std, label = round(added_both_std, digits = 3)), vjust = -1, size = 2, color = "black") +
        # scale_fill_manual(values=c("#d95f02","#FDD835","#01579B","#42A5F5"), 
                            # labels=c("added ASR with one end in added AS", "added AS","deleted ASR with one end in deleted AS","deleted AS")) +
        labs(title=paste0("Added AS(ASR) ratio compared to ",year_start),
            x="Year",
            y="Ratio") +
        # hide title on color legend
        guides(color = guide_legend(title = NULL)) +
        scale_x_continuous(breaks = seq(year_start + 1, year_end, 2))

    ggsave(paste0("report/R/node_edge_fluc_relation/result/add_", year_start,"_", year_end, ".png"),plot = p, width = 8, height = 6, dpi = 300, device = "png")
  

    p <- ggplot(data = df, aes(x = years)) +
    # deleted ratio line
    geom_line(aes(y = deleted_ratio, color = "ASR with one end in deleted AS")) +
    geom_point(aes(y = deleted_ratio, color = "ASR with one end in deleted AS"), size = 2) +
    geom_text(aes(y = deleted_ratio, label = round(deleted_ratio, digits = 3)), vjust = -1, size = 2, color = "black") +
    # deleted ratio line(both)
    geom_line(aes(y = deleted_ratio_both, color = "ASR with both ends in deleted AS")) +
    geom_point(aes(y = deleted_ratio_both, color = "ASR with both ends in deleted AS"), size = 2) +
    geom_text(aes(y = deleted_ratio_both, label = round(deleted_ratio_both, digits = 3)), vjust = -1, size = 2, color = "black") +
    # deleted standard line
    geom_line(aes(y = deleted_std, color = "pivot for one")) +
    geom_point(aes(y = deleted_std, color = "pivot for one"), size = 2) +
    geom_text(aes(y = deleted_std, label = round(deleted_std, digits = 3)), vjust = -1, size = 2, color = "black") +
    # deleted standard line
    geom_line(aes(y = deleted_both_std, color = "pivot for both")) +
    geom_point(aes(y = deleted_both_std, color = "pivot for both"), size = 2) +
    geom_text(aes(y = deleted_both_std, label = round(deleted_both_std, digits = 3)), vjust = -1, size = 2, color = "black") +

    # scale_fill_manual(values=c("#d95f02","#FDD835","#01579B","#42A5F5"), 
                        # labels=c("added ASR with one end in added AS", "added AS","deleted ASR with one end in deleted AS","deleted AS")) +
    labs(title=paste0("Deleted AS(ASR) ratio compared to ",year_start),
        x="Year",
        y="Ratio") +
    # hide title on color legend
    guides(color = guide_legend(title = NULL)) +
    scale_x_continuous(breaks = seq(year_start + 1, year_end, 2))
    ggsave(paste0("report/R/node_edge_fluc_relation/result/del_", year_start,"_", year_end, ".png"),plot = p, width = 8, height = 6, dpi = 300, device = "png")


}

function_fluc_relation_across_years(2002, 2022)

