library(dplyr)
library(tidyr)
load("zelda.RData")
zelda_result <- zelda %>%
  count(year, name = "releases") %>%
  mutate(releases = as.numeric(releases)) %>%
  arrange(desc(releases))
zelda <- as_tibble(zelda_result)
save(zelda, file = "2.RData")