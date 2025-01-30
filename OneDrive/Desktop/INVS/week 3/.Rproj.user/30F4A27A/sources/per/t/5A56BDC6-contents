#loading required libraries

library(readxl)
library(tidyverse)
library(ggplot2)

#read the R.xls file
R <- read_excel("C://Users//rishi//OneDrive//Documents//R//R.xls")

#load data into the software

View(R)

#plotting of the data

ggplot(data = R, mapping = aes(x = `GDP PER CAPITA`, y = `LIFE EXPECTANCY`)) + geom_point(aes(color=`COUNTRY`))
abline(lm(`LIFE EXPECTANCY` ~ `GDP PER CAPITA`, data = R), col = "blue")

#plotting the trend line

plot(`GDP PER CAPITA`, `LIFE EXPECTANCY`, main = "SCATTERPLOT",
          xlab = "GDP PER CAPITA", ylab = "LIFE EXPECTANCY",
          pch = 19, frame = FALSE)
 abline(lm(`LIFE EXPECTANCY` ~ `GDP PER CAPITA`, data = R), col = "blue")
