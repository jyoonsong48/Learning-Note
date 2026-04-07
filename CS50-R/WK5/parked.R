library(tidyverse)
library(ggplot2)
library(dplyr)
library(stringr)

lyric <- read_file("beatles.txt")
lyric <-tolower(lyric)
lyric <- gsub(",", " ", lyric)
lyric <- gsub("\"", "", lyric)
lyric <- gsub("[\\\\(\\\\)]", "", lyric)
lyric <- gsub("\n", " ", lyric)
lyric <- gsub("\'", "", lyric)
lyric <- strsplit(lyric, " ")
lyrics <- unlist(lyric)
lyrics <- lyrics[lyrics != '']
l <- table(lyrics)
l <- as.data.frame(l)
l$Freq <- as.numeric(l$Freq)
l$lyrics <- str_to_title(l$lyrics)
l <- l %>% rename(word = lyrics) %>%
  rename(count = Freq) %>%
  filter(count > 3) %>%
  arrange(count)


word_count <- as.data.frame(l)
ggplot(l, aes(x=reorder(word, -count), y=count, fill = count)) +
  labs(title="Here Comes The Sun", x="Word", y="Count") +
  geom_bar(stat="identity") +
  scale_fill_gradient2(low = "#415844", mid = "#457F6F", high = "#B3CCDD", midpoint = 5) +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))
ggsave(, filename="visualization.png", device="png", width=689, height=418, unit="px")
