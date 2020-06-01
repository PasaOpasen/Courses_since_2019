

library(readxl)

data = read_excel('data.xlsx',sheet = 2)

loss =function(pred,expect){
  tmp = -expect*log(pred)-(1-expect)*log(1-pred)
  return(mean(tmp))
}


w1=0
w2=0
for(iter in 1:10){
  z = w1 * data$X1 + w2* data$X2
  s = 1/(1+exp(-z))
  cat('iter = ',iter,' loss = ',loss(s,data$Label),'\n')
  
  w1 = w1 + mean(data$X1*s*(data$Label*exp(-z)+data$Label-1))
  w2 = w2 + mean(data$X2*s*(data$Label*exp(-z)+data$Label-1))
}

z = w1 * data$X1 + w2* data$X2
s = 1/(1+exp(-z))
cat('end loss = ',loss(s,data$Label),'\n')


