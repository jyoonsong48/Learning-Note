library(dplyr)
library(tidyverse)
load("zelda.RData")
zelda <- zelda %>%
  mutate(year = as.numeric(year)) %>%
  group_by(title) %>%
  filter(year == min(year)) %>%
  mutate(producer_num = (str_count(producers, ",") + 1)) %>%
  filter(producer_num >= 2) %>%
  arrange(year)
zelda <- zelda %>% select(-producer_num)
zelda <- as_tibble(zelda)
save(zelda, file = "5.RData")

