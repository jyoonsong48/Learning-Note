bus <- read.csv("bus.csv")
rail <- read.csv("rail.csv")
r <- readline("Route :")

ontime <- function(r, rail, bus) {
  ROUTE <- c(unique(rail$route), unique(bus$route))
  for (candidate in ROUTE) {
    if (grepl(r, candidate)) {
      r <- candidate
      break
    }
  }
    if (r %in% ROUTE) {
     nrailproutes <- rail[rail$route %in% r & rail$peak == "PEAK" & rail$denominator != 0, ]$numerator
     nrailoffproutes <- rail[rail$route %in% r & rail$peak == "OFF_PEAK" & rail$denominator != 0, ]$numerator
     nbusproutes <- bus[bus$route %in% r & bus$peak == "PEAK" & bus$denominator != 0, ]$numerator
     nbusoffproutes <- bus[bus$route %in% r & bus$peak == "OFF_PEAK" & bus$denominator != 0, ]$numerator
     drailproutes <- rail[rail$route %in% r & rail$peak == "PEAK" & rail$denominator != 0, ]$denominator
     drailoffproutes <- rail[rail$route %in% r & rail$peak == "OFF_PEAK" & rail$denominator != 0, ]$denominator
     dbusproutes <- bus[bus$route %in% r & bus$peak == "PEAK" & bus$denominator != 0, ]$denominator
     dbusoffproutes <- bus[bus$route %in% r & bus$peak == "OFF_PEAK" & bus$denominator != 0, ]$denominator

     railproutes <- as.numeric(nrailproutes) / as.numeric(drailproutes)
     busproutes <- as.numeric(nbusproutes) / as.numeric(dbusproutes)
     railoffproutes <- as.numeric(nrailoffproutes) / as.numeric(drailoffproutes)
     busoffproutes <- as.numeric(nbusoffproutes) / as.numeric(dbusoffproutes)

     proutes <- c(railproutes, busproutes)
     offproutes <- c(railoffproutes, busoffproutes)

     PEAK <- round(mean(as.numeric(proutes), na.rm = TRUE) * 100)
     OFFPEAK <- round(mean(as.numeric(offproutes), na.rm = TRUE) * 100)
     print(paste0("On time ", PEAK, "% of the time during peak hours."))
     print(paste0("On time ", OFFPEAK, "% of the time during off-peak hours."))
   }
}
ontime(r, rail, bus)