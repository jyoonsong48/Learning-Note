library(dplyr)
library(tidyr)
z <- read.csv("zelda.csv")
z <- z %>%
  group_by(title, release, role) %>%
  summarize(names = paste(names, collapse = ", "), .groups = "drop") %>%
  pivot_wider(names_from = role, values_from = names) %>%
  separate(release, into = c("year", "system"), sep = " - ")
zelda <- as_tibble(z)
names(zelda) <- tolower(names(zelda))

save(zelda, file = "zelda.RData")