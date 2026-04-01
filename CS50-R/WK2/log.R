authors <- read.csv("authors.csv")
books <- read.csv("books.csv")
answers <- readLines("answers.txt")
questions <- c(answers)

# library info + prepare questions from answer.txt file

w <- books[books$author == "Mia Morgan", ]$title # for the writer
m <- books[books$topic == "Music" & books$year == 1613, ]$title #musician
tr <- books[(books$author == "Lysandra Silverleaf" | books$author == "Elena Petrova") & books$year == 1775, ]$title # traveler
p <- books[books$pages >= 200 & books$pages <= 300 & (books$year == 1990 | books$year == 1992), ]$title # painter
s <- books[grepl("Quantum Mechanics", books$title), ]$title # scientist
teauthor <- authors[authors$hometown == "Zenthia", ]$author # searching author first
te <- books[books$topic == "Education" & books$year >= 1700 & books$year < 1800 & books$author %in% teauthor, ]$title

answer <- c(w, m, tr, p, s, te)

finalanswer <- paste(questions, answer) # combining question & answer

writeLines(finalanswer, "answers.txt") # write combined q&a to answers.txt