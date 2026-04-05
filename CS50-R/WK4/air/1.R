air <- read.csv("air.csv")
air_part <- air[, c("State", "State.County", "POLLUTANT", "Emissions..Tons.", "SCC.LEVEL.1", "SCC.LEVEL.2", "SCC.LEVEL.3", "SCC.LEVEL.4")]
colnames(air_part) <- c("state", "county", "pollutant", "emissions", "level_1", "level_2", "level_3", "level_4")
air <- air_part %>% as_tibble()
save(air, file = "air.RData")
