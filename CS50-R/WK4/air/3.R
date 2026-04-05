load("/workspaces/265637370/air/air.RData")
airfilter <- air[air$county == "OR - Josephine", ]
air <- airfilter %>% as_tibble()
save(air, file = "3.RData")