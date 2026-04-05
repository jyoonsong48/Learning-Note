library(dplyr)
load("/workspaces/265637370/air/air.RData")
air$emissions <- gsub(",", "", air$emissions)
air$emissions <- as.numeric(air$emissions)
result <- air %>%
  group_by(county) %>%
  arrange(desc(emissions)) %>%
  slice(1) %>%
  ungroup()  %>%
  arrange(desc(emissions))
air <- result %>% as_tibble()
save(air, file = "5.RData")


# 93.08707 /472.40440 / 1,336.49200