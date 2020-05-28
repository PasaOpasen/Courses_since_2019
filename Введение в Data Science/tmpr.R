

library(tidyverse)


dt = read_csv('iris.csv')


dt= dt[,-1]

colnames(dt) = str_replace(colnames(dt),' ','.')


ggplot(dt, aes(x=sepal.length))+geom_density()#u
ggplot(dt, aes(x=sepal.width))+geom_density()#u
ggplot(dt, aes(x=petal.length))+geom_density()#b
ggplot(dt, aes(x=petal.width))+geom_density()#b
ggplot(dt, aes(x=species))+geom_density()#b









dt = read_table2('dataset_209770_6.txt')

ggplot(dt, aes(x=x,y=y))+geom_point()












dt = read_csv('event_data_train.csv')

dt %>% select(user_id) %>%group_by(factor(user_id)) %>% summarise(count = n()) %>% arrange(-count)



dt = read_csv('submissions_data_train.csv')

dt %>% filter(submission_status == 'wrong') %>% group_by(factor(step_id))%>% summarise(count = n()) %>% arrange(-count)

















