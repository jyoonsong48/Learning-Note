library(dplyr)
library(tidyr)
load("zelda.RData")
zelda <- zelda %>%
  group_by(title) %>%
  filter(year == min(year)) %>%
  ungroup() %>%
  arrange(year)
zelda <- as_tibble(zelda)
save(zelda, file = "3.RData")