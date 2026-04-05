load("/workspaces/265637370/air/air.RData")
library(dplyr)
air$emissions <- gsub(",", "", air$emissions)
air$emissions <- as.numeric(air$emissions)
result_2 <- air %>%
  group_by(pollutant) %>%
  summarise(emissions = sum(emissions, na.rm = TRUE)) %>%
  arrange(desc(emissions))
air <- result_2 %>% as_tibble()
save(air, file = "6.RData")
