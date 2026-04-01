bahrain.csv <- read.csv("bahrain.csv")
imola.csv <- read.csv("imola.csv")
jeddah.csv <- read.csv("jeddah.csv")
melbourne.csv <- read.csv("melbourne.csv")
miami.csv <- read.csv("miami.csv")
shanghai.csv <- read.csv("shanghai.csv")
suzuka.csv <- read.csv("suzuka.csv")

pitstop <- readline(prompt ="> Give csv file name: ")

if (pitstop == "bahrain.csv") {
  numbers <- bahrain.csv$time
  print(nrow(bahrain.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
} else if (pitstop == "imola.csv") {
  numbers <- imola.csv$time
  print(nrow(imola.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
} else if (pitstop == "jeddah.csv") {
  numbers <- jeddah.csv$time
  print(nrow(jeddah.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
} else if (pitstop == "melbourne.csv") {
  numbers <- melbourne.csv$time
  print(nrow(melbourne.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
} else if (pitstop == "miami.csv") {
  numbers <- miami.csv$time
  print(nrow(miami.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
} else if (pitstop == "shanghai.csv") {
  numbers <- shanghai.csv$time
  print(nrow(shanghai.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
} else if (pitstop == "suzuka.csv") {
  numbers <- suzuka.csv$time
  print(nrow(suzuka.csv))
  print(min(numbers))
  print(max(numbers))
  print(sum(numbers))
}


#The total number of pit stops
#The duration of the shortest pit stop
#The duration of the longest pit stop
#The total time spent on pit stops during the race, across all racers
