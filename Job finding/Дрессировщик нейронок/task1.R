

f = function(a,b,c){
  if(a>c & b >c){
    cat('no solutions \n')
    return()
  }
  
  exist_sol = F
  
  for(apples in 0:(c%/%a))
    for(pears in 0:((c-apples*a)%/%b))
      if(apples*a+pears*b == c){
        cat(apples,' apples, ',pears,' pears\n')
        exist_sol = T
      }
  
  if(!exist_sol){
    cat('no solutions \n')
  }
}




