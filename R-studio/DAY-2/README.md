## $\color{#fffff}{\text{DAY 2}}$
### $\color{#fffff}{\text{Lab 4 result: Tables}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>R</b>
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
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{Lab 5 result: Tables, Graph}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>R</b>
# ==========================================================
# Project: 4006BIO - Lab 5: Blood Pressure
# By: Jiyoon Song
# Content: BP and Pulse
# ==========================================================
# 4006BIO_Lab 5
library(knitr)
library(ggplot2)
library(tidyr) 

#A
Lab_data <- data.frame(
  "Attempt" = c(1, 2),
  "Systolic Pressure (mmHg)" = c(120, 120),
  "Diastolic Pressure (mmHg)"= c(90, 90),
  check.names = FALSE
)

kable(Lab_data, 
      align = "lcc",
      caption = "Blood Pressure Using Stethoscope Method")

#B

Lab_data_B <- data.frame(
  "Pulse Detection Method" = c("Arm at heart level", "Arm above head"),
  "Estimated Systolic Pressure (mmHg)" = c(148.8, 98.68),
  check.names = FALSE
)

kable(Lab_data_B, 
      align = "lc",
      caption = "Blood Pressure and Finger Pulse")

#C

Lab_data_C <- data.frame(
  "Rate of pressure change" = c("Slow", "Medium", "Fast"),
  "Systolic Pressure (mmHg)" = c(74.75, 81.29, 91.49),
  "Diastolic Pressure (mmHg)"= c(69.88, 87.65, 87.28),
  check.names = FALSE
)

kable(Lab_data_C, 
      align = "lcc",
      caption = "Blood Pressure and Finger Pulse")
 
#D

Lab_data_D <- data.frame(
  "Cuff Size" = c("Infant", "Child", "Adult", "Leg"),
  "Systolic Pressure (mmHg)" = c(NA, NA, 95.31, NA),
  "Diastolic Pressure (mmHg)"= c(NA, NA, 68.36, NA),
  check.names = FALSE
)

data_long <- pivot_longer(Lab_data_D, 
                          cols = c("Systolic Pressure (mmHg)", "Diastolic Pressure (mmHg)"),
                          names_to = "BP",
                          values_to = "mmHg")  


plot_summary <- ggplot(data = data_long, aes(x = `Cuff Size`, y = mmHg, fill = BP)) +
  geom_bar(stat = "identity", position = "dodge", width = 0.5) +
  scale_fill_manual(values = c("Systolic Pressure (mmHg)" = "red", "Diastolic Pressure (mmHg)" = "blue")) +
  labs(title = "Effect of Cuff Size on Measured Blood Pressure",
       x = "Cuff Size",
       y = "Blood Pressure (mmHg)",
       fill = "Blood Pressure Type") +
  
  theme_bw()

plot_summary #w/o this -> no graph on screen!!

#E

Lab_data_E <- data.frame(
  "Position" = c("Arm at heart level", "Arm hanging loosely by side", "Arm at head level"),
  "Systolic Pressure (mmHg)" = c(75.69, 114.2, 106.3),
  "Diastolic Pressure (mmHg)"= c(64.95, 90.42, 64.71),
  check.names = FALSE
)

kable(Lab_data_E, 
      align = "lll",
      caption = "Effects of Arm Position on Blood Pressure")
# Measurement Site = Elbow

Lab_data_F <- data.frame(
  "Position" = c("Cuff-to-heart height difference (cm)", "Systolic Pressure (mmHg)", "Diastolic Pressure (mmHg)", "Extra Hydrostatic Pressure (mmHg)", "Corrected Systolic Pressure (mmHg)", "Corrected Diastolic Pressure (mmHg)"),
  "Thigh Lying" = c(0, 88.94, 75.2, 0, 88.94, 75.20),
  "Thigh Standing"= c(NA, 103.5, 48.5, NA, NA, NA),
  "Calf Lying" = c(0, 73.78, 50.7, 0, 73.78, 50.70),
  "Calf Standing" =c(NA, 105.7, 51.69, NA, NA, NA),
  check.names = FALSE
)

kable(Lab_data_F, 
      align = "lllll",
      caption = "Height Difference from Heart to Blood Pressure Cuff")

# Remember to put ) at the end!!!!
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{Lab 2 re-result: Graph}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>R</b>
# ==========================================================
# Project: 4006BIO - Lab 2: Nerve Conduction Study
# By: Jiyoon Song
# Content: Latency and Amplitude comparison on site of stimulation (wrist vs elbow)
# ==========================================================

library(ggplot2)
library(patchwork) # tool to combine two graphs under one title (left&right)

# Data Input
Lab_data <- data.frame(
  "Site of Stimulation"= c("Wrist", "Elbow"), 
  "Latency" = c(4, 1),
  "Amplitude" = c(4.734, 0.125),
  check.names = FALSE
)

# Making left part of the graph
p_left <- ggplot(Lab_data, aes(x = `Site of Stimulation`, y = Latency, fill = `Site of Stimulation`)) +
  geom_bar(stat = "identity", width = 0.5) +
  scale_fill_manual(values = c("Wrist" = "#E41A1C", "Elbow" = "#377EB8")) +
  labs(title = "Latency (ms)", x = NULL, y = "ms") +
  theme_bw() +
  theme(legend.position = "none")

# Making right part of the graph
p_right <- ggplot(Lab_data, aes(x = `Site of Stimulation`, y = Amplitude, fill = `Site of Stimulation`)) +
  geom_bar(stat = "identity", width = 0.5) +
  scale_fill_manual(values = c("Wrist" = "#4DAF4A", "Elbow" = "#984EA3")) +
  labs(title = "Amplitude (mV)", x = NULL, y = "mV") +
  theme_bw() +
  theme(legend.position = "none")

# Combine two graphs
combined_plot <- p_left + p_right

# Adding the title, caption, and theme
combined_plot + plot_annotation(
  title = "Nerve Conduction Study: Detailed Comparison",
  caption = "Wrist-elbow distance: 220mm, Conduction velocity: -73.33m/s",
  theme = theme(plot.title = element_text(size = 18, face = "bold", hjust = 0.5))
) # hjust -> centre alignment
# remember not to use “” inside aes()
# better to use patchwork when two different y axis needed!!
<b></b>
</pre> 
</details>
