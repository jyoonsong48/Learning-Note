load("/workspaces/265637370/air/air.RData")
library(dplyr)
air$emissions <- gsub(",", "", air$emissions)
air$emissions <- as.numeric(air$emissions)
result_3 <- air %>%
  rename(source = level_1) %>%
  group_by(source, pollutant) %>%
  summarise(emissions = sum(emissions, na.rm = TRUE), .groups= "drop") %>%
  arrange(source, pollutant)
air <- result_3 %>% as_tibble()
save(air, file = "7.RData")