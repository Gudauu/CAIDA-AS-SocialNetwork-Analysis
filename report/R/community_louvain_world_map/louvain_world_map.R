
# Generate num random colors
generate_color <- function(num) {
  colors <- vector(mode = "character", length = num)
  for (i in 1:30) {
    # Generate a random color
    color <- paste0("#", paste0(sample(c(0:9, letters[1:6]), 6, replace=TRUE), collapse=""))
    
    # Check if the color has already been used
    while (color %in% colors) {
      # If the color has already been used, generate a new one
      color <- paste0("#", paste0(sample(c(0:9, letters[1:6]), 6, replace=TRUE), collapse=""))
    }
    
    # Add the color to the vector
    colors[i] <- color
  }

  return(colors)
}

# version: eg 20020101


function_visualize_louvain <- function(version,palette){
  # Load required libraries
  library(ggplot2)
  library(dplyr)


  # Load community louvain data
  communities <- readLines(paste0("playEgOnData/results/",version,"/community_louvain"))
  # Read in coordinates file
  coordinates <- read.table("dataCAIDA/ASN_lookup/country_code_full_name_location", sep=":", header=FALSE, col.names=c("code", "country", "latitude", "longitude"))

  unique_codes <- c()

  # Get unique country codes
  for (community in communities) {
    countries <- strsplit(community, ",")[[1]]
    unique_codes <- c(unique_codes,countries)
  }


  # Merge coordinates with unique country codes
  coordinates <- merge(data.frame(code = unique_codes), coordinates, by = "code")

  # Create a data frame with community and coordinates information
  df <- data.frame(code=coordinates$code, country=coordinates$country, community=NA, latitude=coordinates$latitude, longitude=coordinates$longitude, stringsAsFactors=FALSE)



  # Generate colors
  my_palette <- palette

  # Assign a community(marked by color) to each country
  idx_community <- 1
  for (community in communities) {
    countries <- strsplit(community, ",")[[1]]
    df$community[df$code %in% countries] <- my_palette[idx_community] 
    idx_community <- idx_community + 1
  }

  # print(communities)
  xmin <- -140
  xmax <- 180
  ymin <- -50
  ymax <- 75

  # Define the range of the world map
  xlim <- c(xmin, xmax)
  ylim <- c(ymin, ymax)



  # Create a ggplot object with the world map
  nodes <- ggplot() + 
    coord_cartesian(xlim=xlim, ylim=ylim) +
    geom_point(data=df, aes(x=longitude, y=latitude, color = community), size = 0.5) +
    geom_text(data = df, aes(x=longitude, y=latitude, label = code), vjust = -1, size = 1, color = "black") +
    # scale_color_discrete(name="Community")+
    # scale_x_continuous(breaks = seq(xmin, xmax, 5)) +
    labs(x = "Longitude", y = "Latitude", title = paste0("communities_",version,"")) +
    # hide title on color legend
    guides(color = guide_legend(title = NULL))


  # # save the plot
  graph_save_path <- paste0("./report/R/community_louvain_world_map/results/communities_",version,".png")

  ggsave(graph_save_path,plot = nodes, width = 8, height = 6, dpi = 300, device = "png")

  
}

# Generate a color palette with num_colors colors
num_colors <- 30
palette <- generate_color(num_colors)
years <- seq(2000, 2023, by = 1)
for(year in years){
  version <- paste0(year,"0101")
  function_visualize_louvain(version,palette)
}







