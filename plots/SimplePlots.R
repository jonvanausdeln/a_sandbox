library(ggplot2)
data("midwest")
ggplot(midwest, aes(x=area, y=poptotal)) + geom_point()
