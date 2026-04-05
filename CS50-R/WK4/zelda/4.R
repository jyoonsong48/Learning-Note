library(dplyr)
library(tidyverse)
load("zelda.RData")
zelda <- zelda %>%
  mutate(year = as.numeric(year)) %>%
  filter(str_detect(producers, "Shigeru Miyamoto")) %>%
  group_by(title) %>%
  filter(year == min(year)) %>%
  ungroup() %>%
  arrange(year, title, system)
zelda <- as_tibble(zelda)
save(zelda, file = "4.RData")