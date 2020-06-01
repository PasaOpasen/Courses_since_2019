
library(readxl)
library(dplyr)

data = read_excel('data.xlsx') %>% mutate(Date = as.Date(Date))

data2 = data %>% filter(Date >= as.Date('2016-03-01') & Date < as.Date('2018-11-26'))



library(corrplot)

corrplot(cor(data2[,-1]), method ='number')


library(ggplot2)

ggplot(tibble(Date=rep(data2$Date,5), 
              TSs=c(data2$TS1,data2$TS2,data2$TS3,data2$TS4,data2$TS5), 
              Number = sort(rep(1:5,nrow(data2)))),
       aes(x=Date,y=TSs,col = factor(Number)))+theme_bw()+
  geom_line()


regress = function(y,x){
  
  fit = lm(y~x[[1]]+x[[2]]+x[[3]]+x[[4]]-1)
  print(summary(fit))
}

for(regressant in 1:5){
  cat('---------- regressant = ', colnames(data2)[1+regressant],'\n')
  cat('---------- regressors = ', colnames(data2)[-c(1,1+regressant)],'\n')
  regress(data2[[1+regressant]], data2[,-c(1,regressant)])
  cat('\n')
}






summary(lm(TS1~TS5+TS2+TS3+TS4-1,data2))
summary(lm(TS2~TS1+TS5+TS3+TS4-1,data2))
summary(lm(TS3~TS1+TS2+TS5+TS4-1,data2))
summary(lm(TS4~TS1+TS2+TS3+TS5-1,data2))
summary(lm(TS5~TS1+TS2+TS3+TS4-1,data2))



fit = lm(TS2~TS1+TS3+TS5+TS4-1,data2)

fit = lm(TS1~TS5+TS2+TS3+TS4-1,data2)
fit = lm(TS2~TS1+TS5+TS3+TS4-1,data2)
fit = lm(TS4~TS1+TS2+TS3+TS5-1,data2)
fit = lm(TS5~TS1+TS2+TS3+TS4-1,data2)

shapiro.test(fit$residuals)


durbinWatsonTest(fit)


library(car)
mysummary=function(mdl){
  
  cat("-----> ОБЩАЯ ИНФОРМАЦИЯ О МОДЕЛИ:\n");cat("\n")
  gvlma::gvlma(mdl) %>% summary() %>% print();cat("\n")
  
  
  cat("-----> БАЗОВЫЕ ГРАФИКИ:\n");cat("\n")
  par(mfrow=c(2,2))
  plot(mdl)
  par(mfrow=c(1,1)) ;cat("\n")
  
  
  cat("-----> ТЕСТ НА НОРМАЛЬНОСТЬ РАСПРЕДЕЛЕНИЯ ОСТАТКОВ\n");cat("\n")
  shapiro.test(mdl$residuals) %>% print();cat("\n")
  
  
  cat("-----> ФАКТОР ИНФЛЯЦИИ ДИСПЕРСИЙ:\n");cat("\n")
  vif(mdl)%>% print();cat("\n")
  
  cat("-----> ТЕСТ НА АВТОКОРРЕЛЯЦИЮ:\n");cat("\n")
  durbinWatsonTest(mdl) %>% print();cat("\n")   #тест на автокорреляцию
  
  # cat("-----> ТЕСТ НА ОДНОРОДНОСТЬ ДИСПЕРСИИ:\n");cat("\n")
  # ncvTest(mdl)%>% print();cat("\n")    #однородность дисперсии
  
  cat("-----> ТЕСТ НА ВЫБРОСЫ И ВЛИЯТЕЛЬНЫЕ НАБЛЮДЕНИЯ:\n");cat("\n")
  
  outs=outlierTest(mdl)
  outs%>% print()
  
  
  influ=influencePlot(mdl,main="Диаграмма влияния",sub="Размеры кругов пропорциональны расстояниям Кука")
  gb=capture.output(influ %>% print())  
  
}


mysummary(fit)

summary(step(fit))





fit = lm(TS2~TS1+TS5+TS3+TS4-1,data2)

ggplot(
  tibble(date = rep(data2$Date,2),
         values = c(data2$TS2 , predict(fit,data2)),
         type = sort(rep(c('expected','predicted'),nrow(data2)))
         ),
         aes(x=date,y=values,col = factor(type)))+geom_line()+
  theme_bw()+theme(legend.position = c(0.9,0.1))+
  labs(col='series')










