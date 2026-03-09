## $\color{#fffff}{\text{DAY 2}}$
### $\color{#fffff}{\text{Lab 4 result: Tables}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>```R</b>
# ==========================================================
# Project: 4006BIO: Human Physiology - Homeostasis and Health (Lab 4)
# by. Jiyoon Song
# Contents: Visualisation of data: ECG and Pulse
# ==========================================================
# Basically same as DAY-1/Lab 3!!
# 4006BIO_Lab 4
Lab_data <- data.frame(
  "Interval" = c("duration (ms)"),
  "PR" = c(20),
  "QRS" = c(47),
  "ST" =c(41),
  "TP" = c(32)
)

library(knitr)
kable(Lab_data, 
      align = "lcccc",
      caption = "ECG Components")

Lab_data_B <- data.frame(
  "R to start of pulse upswing (ms)" = c(237),
  "T to dip after peak of pulse (ms)" = c(291),
  check.names = FALSE
)

kable(Lab_data_B, 
      align = "ll",
      caption = "ECG and Pulse")

Lab_data_B1 <- data.frame(
  "Interval" = c("Duration (ms)"),
  "PR" = c(28),
  "QRS" = c(50),
  "ST" = c(23),
  "TP" = c(24),
  check.names = FALSE
)

kable(Lab_data_B1, 
      align = "lcccc",
      caption = "ECG and Pulse: With Exercise")
<b>```</b>
</pre> 
</details>
