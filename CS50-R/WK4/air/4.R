library(dplyr)
load("/workspaces/265637370/air/air.RData")
air$emissions <- as.numeric(air$emissions)
sorted_air <- air %>% arrange(desc(emissions)) %>%
filter(!is.na(emissions))
airfilter <- sorted_air[sorted_air$county == "OR - Josephine", ]
air <- airfilter %>% as_tibble()
save(air, file = "4.RData")