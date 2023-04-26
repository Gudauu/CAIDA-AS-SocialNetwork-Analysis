


# version: eg 20020101


function_visualize_louvain <- function(version){
  # Load required libraries
  library(ggplot2)
  library(dplyr)
  library(RColorBrewer)


  # Load community louvain data
  communities <- readLines(paste0("playEgOnData/results/",version,"/community_louvain"))
  # Read in coordinates file
  coordinates <- read.table("dataCAIDA/ASN_lookup/country_code_location", sep=":", header=FALSE, col.names=c("code", "country", "latitude", "longitude"))

  unique_codes <- c()

  # Get unique country codes
  for (community in communities) {
    countries <- strsplit(community, ",")[[1]]
    unique_codes <- c(unique_codes,countries)
  }


  # Merge coordinates with unique country codes
  coordinates <- merge(data.frame(code = unique_codes), coordinates, by = "code")

  # Create a data frame with community and coordinates information
  df <- data.frame(code=coordinates$code, community=NA, latitude=coordinates$latitude, longitude=coordinates$longitude, stringsAsFactors=FALSE)

  idx_community <- 1
  # Generate a color palette with num_colors colors
  num_colors <- 30
  my_palette <- brewer.pal(num_colors, "Set3")

  # Assign a community to each country
  for (community in communities) {
    countries <- strsplit(community, ",")[[1]]
    df$community[df$code %in% countries] <- my_palette[(idx_community%%num_colors)+1] #my_palette[idx_community]
    idx_community <- idx_community + 1
  }

  print(df)

  # Define the range of the world map
  xlim <- c(-180, 180)
  ylim <- c(-90, 90)

  data <- data.frame(lon = 0, lat = 0)
  # Create a ggplot object with the world map
  world_map <- ggplot() + 
    # geom_rect(xmin=xlim[1], xmax=xlim[2], ymin=ylim[1], ymax=ylim[2], fill="lightblue") + 
    coord_cartesian(xlim=xlim, ylim=ylim) #+
    # theme_void() 
    # geom_point(data=data, aes(x=lon, y=lat), color="red", size=3)
  

  # Add nodes to the world map
  nodes <- world_map + 
    geom_point(data=df, aes(x=longitude, y=latitude, color=community), size=1) +
    scale_color_discrete(name="Community")


  # # save the plot
  graph_save_path <- paste0("./report/R/community_louvain_world_map/results/communities_",version,".png")

  ggsave(graph_save_path,plot = nodes, width = 8, height = 6, dpi = 300, device = "png")

  
}


function_visualize_louvain("20000101")







