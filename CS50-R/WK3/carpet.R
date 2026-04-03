calculate_growth_rate <- function(years, visitors) {
  (v[length(v)] - v[1]) / (years[length(years)] - years[1])
}

predict_visitors <- function(years, visitors, year) {
  v[length(v)] + (calculate_growth_rate(years, visitors) * (year - years[length(years)]))
}

visitors <- read.csv("visitors.csv", header = TRUE)
years <- visitors$year
v <- visitors$visitors

year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
