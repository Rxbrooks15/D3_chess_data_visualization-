#Proj3

library(readxl)
library(tidyverse)

library(gganimate)
library(readr)
library(readxl)
library(gridExtra)
# install.packages("rvest")
library(rvest)

library(sf)
library(sp)
library(magick)
library(jpeg)
library(lubridate)
library(urbnmapr)
library(cr)
install.packages(cr)
library(gifski)
library(ggtext)
library(ggplot2)
library(plotly)


data <- read_csv(file.choose())

data %>% 
  View

total_chess <- read_csv(file.choose()) 

total_chess %>% 
  View

total_chess %>% 
  filter(timeClass =="rapid" ) %>% 
  ggplot(aes(x = date, y = userRating))+
  geom_point()+

  labs(title = "Rapid chess.com rating over the years", y = "Chess ELO", 
       x = "Date ")+
  Rain_theme()+
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))

Rain_theme <- function() {
  theme_minimal() +
    theme(
      text = element_text(size = 12, family = "Times New Roman"), # change font size and family
      plot.background = element_rect(fill = "#E7FFF2"),  # change background color
      panel.grid.major = element_blank(),                  # remove major gridlines
      panel.grid.minor = element_blank(),                  # remove minor gridlines
      panel.border = element_blank(),                      # remove plot border
      axis.line = element_line(color = "black")             # change axis line color
    )
}

total_chess %>%
  filter(timeClass == "rapid") %>%
  plot_ly(x = ~date, y = ~userRating, type = "scatter", mode = "markers",  text = ~paste("Rating:", userRating, "<br>Date:", date, "<br>Time Class:", timeClass, "<br>Result:", result)) %>%
  layout(
    title = "Rapid chess.com rating over the years",
    yaxis = list(title = "Chess ELO"),
    xaxis = list(title = "Date"),
    font = list(family = "Times New Roman", size = 12),
    plot_bgcolor = "#E7FFF2",

    showlegend = FALSE

  )
# 
#   
# xaxis_tickangle = 90,
# xaxis_tickfont = list(size = 12, family = "Times New Roman"),
# yaxis_tickfont = list(size = 12, family = "Times New Roman"),
  
  

# average_chess <- total_chess %>% 
#   filter(timeClass =="rapid" ) %>% 
#   
#   average_chess <- total_chess %>%
#   filter(timeClass == "rapid") %>%
#   group_by(year = lubridate::year(date)) %>%
#   summarise(average_rating = mean(userRating))
#   
# total_chess %>%
#   group_by(opening) %>% 
#   count()
# 
# top_openings <- total_chess %>%
#   group_by(opening) %>%
#   count() %>%
#   filter(n >= 79) %>% 
#   ungroup() %>% 
#   View
#   ggplot
#   # top_n(5, n) %>%
#   # arrange(desc(n))
# 
# top_openings %>% 
#   View
# 
# total_chess %>% 
#   group_by(W)
# 
# 
# total_chess %>% 
#   View


#


