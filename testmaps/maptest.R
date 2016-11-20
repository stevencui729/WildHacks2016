## Creates a map
library(ggplot2)
library(ggmap)

? "ggmap"
baylor <- "baylor university"
uchicago <- "university of chicago"
qmap(baylor, zoom = 14)
qmap(uchicago, zoom = 14)
     set.seed(500)
df <- round(data.frame(
  x = jitter(rep(-95.36, 50), amount = .3),
  y = jitter(rep( 29.76, 50), amount = .3)
), digits = 2)
map <- get_googlemap('houston', markers = df, path = df, scale = 2)
ggmap(map, extent = 'device')
