library(dplyr)
load("/workspaces/265637370/air/air.RData")
air$emissions <- as.numeric(air$emissions)
sorted_air <- air %>% arrange(desc(emissions)) %>%
filter(!is.na(emissions))
air <- sorted_air %>% as_tibble()
save(air, file = "2.RData")