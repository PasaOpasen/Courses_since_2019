
library(ggplot2)

test <- structure(list(ebit = c(2421.459, 1928.349, 
                                1914.744, 2134.6, 1534.048), ebit_margin = c(0.05367, 0.04859, 
                                                                             0.04973, 0.06016, 0.04143), year = structure(5:1, .Label = c("2015", 
                                                                                                                                          "2016", "2017", "2018", "2019"), class = "factor")), class = "data.frame", row.names = c("Company1", 
                                                                                                                                                                                                                                   "Company1", "Company1", "Company1", 
                                                                                                                                                                                                                                   "Company1"))
scaleFactor <- max(test$ebit) / max(test$ebit_margin)



ggplot(test, aes(as.factor(year), ebit, label=test$ebit)) + 
  geom_col(width = 0.5, fill = "darkblue", alpha = 0.5) +
  geom_line(aes(as.factor(year), ebit_margin * scaleFactor, group = 1),  size = 1,  col = "red", alpha = 0.5) +
  scale_y_continuous(name = "EBIT Value", sec.axis = sec_axis(~./scaleFactor, name = "EBIT Margin", labels = function(b) { paste0(round(b * 100, 3), "%")})) +
  #geom_text(size = 3, position = position_stack(vjust = 0.5)) + 
  theme_bw()  +
  labs(title = "Key Financials Across Years",
       subtitle = "Earnings Before Interest and Taxation",
       x = "Year") +
  theme(axis.text.x = element_text(angle = 60, hjust = 1)) +
  geom_label(
    label = c(test$ebit),
    position = position_stack(vjust = 0.75),
    check_overlap = T
  )+
  geom_label(
    aes(as.factor(year), ebit_margin * scaleFactor, group = 1),
    label = c(test$ebit),
    position = position_stack(vjust = 0.99),
    check_overlap = T
  )

