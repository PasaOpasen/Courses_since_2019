

library(tidyverse)

f = read_csv('a_b_testing.csv')

t.test(f$converted[f$group == 'A'])

t.test(f$converted[f$group == 'A'], f$converted[f$group == 'B'])
