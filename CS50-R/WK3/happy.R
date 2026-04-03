cou <- readline("Country: ")
data_by_year <- list("2020" = read.csv("2020.csv"), "2021" = read.csv("2021.csv"), "2022" = read.csv("2022.csv"), "2023" = read.csv("2023.csv"),"2024" = read.csv("2024.csv"))


happy <- function (cou, data_by_year) {
  for(i in 2020:2024) {
    is_country <- grepl(cou, data_by_year[[as.character(i)]]$country, ignore.case = TRUE)
    country <- data_by_year[[as.character(i)]]$country[is_country]
    sum_by_year <- sum(as.numeric(data_by_year[[as.character(i)]][is_country, -1], na.rm = TRUE))
    sum_by_yr <- round(sum_by_year, digits = 2)
      if (is.na(sum_by_yr)) {cat(paste0(cou, "(", i, "): unavailable \n"))}
      else {cat(paste0(country, "(", i, "):", sum_by_yr, "\n"))}
  }
}

happy(cou, data_by_year)