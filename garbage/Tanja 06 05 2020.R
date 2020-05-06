

pow = function(val, degree){
  
  if(val>=0){
    return(val^degree)
  }
  
  return(sign(val)*abs(val)^degree)
  
}

 f =function(t) 0.955654100053241*pow(0.388975151328782 - t,2/3) + 0.880095973789201*pow(1 - 0.631289512049639*t,1/3)- 7



x=seq(-1000,1000,length.out = 1000)
y= sapply(x, f)

plot(x, y)





