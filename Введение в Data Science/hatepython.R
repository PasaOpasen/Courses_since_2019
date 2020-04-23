
library(tidyverse)

dt=read_csv('dota_hero_stats.csv')

dt$legs %>% factor() %>% summary()






dt=read_csv('accountancy.csv')

dt %>% group_by(Executor,Type) %>% summarise(m=mean(Salary))




