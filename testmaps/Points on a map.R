## Creates a map
library(ggplot2)
library(ggmap)
?get_map

uchicago <- "university of chicago"

ggmap(uchicago, extent = "normal")

paris <- get_map(location = "university of chicago")
ggmap(paris, extent = "normal")

photo_names<-read.csv("../names_list.csv", as.is=T)

theme_set(theme_bw(16))
HoustonMap <- qmap("houston", zoom = 14, color = "bw", legend = "topleft")
HoustonMap +
  geom_point(aes(x = lon, y = lat, colour = offense, size = offense),
             data = violent_crimes)
HoustonMap +
  stat_bin2d(
    aes(x = lon, y = lat, colour = offense, fill = offense),
    size = .5, bins = 30, alpha = 1/2) 
    data = violent_crimes
  )