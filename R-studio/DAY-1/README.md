## $\color{#fffff}{\text{DAY 1}}$
### $\color{#fffff}{\text{Lab 1 result: Basic Graphs (line, bar)}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>R</b>

# ==========================================================
# Project: 4006BIO: Human Physiology - Homeostasis and Health (Lab 1)
# by. Jiyoon Song
# Contents: Visualisation of data: EMG, Muscle Fatigue, Changes in Force over time
# ==========================================================

# 0. Import Library
library(ggplot2)  # Tool to draw the graph
library(tidyr)    # changing the data into ‘long-form’


# ----------------------------------------------------------
# PART A: Relationship between Raw and Processed Traces
# ----------------------------------------------------------

# 1. Data Input
Lab_data_A <- data.frame(
  Weight = c(1, 2, 3, 4),
  Biceps = c(0.048, 0.0885, 0.143, 0.154),
  Triceps = c(0.0223, 0.0384, 0.0669, 0.0692)
)

# 2. Reshape data: Combine Biceps/Triceps columns into a single 'Muscle' column
data_long_A <- pivot_longer(Lab_data_A, 
                            cols = c("Biceps", "Triceps"),
                            names_to = "Muscle",
                            values_to = "mV")

# 3. Generate the graph
ggplot(data = data_long_A, aes(x = Weight, y = mV, color = Muscle)) +
  geom_line(size = 1) +                  # Draw the line
  geom_point(size = 3) +                 # Dots
  scale_color_manual(values = c("Biceps" = "red", "Triceps" = "blue")) + # Give colour
  labs(title = "Relationship between Raw and Processed Traces",
       x = "Weights (Kg)", y = "Amplitude (mV)") +
  theme_bw()                             # Theme 😊


# ----------------------------------------------------------
# PART B: Effect of Effort Intensity on Muscle Fatigue
# ----------------------------------------------------------

# 1. Data Input
# Handle special characters (%) in column names using backticks (``)
Lab_data_B <- data.frame(
  `Time` = c(1, 5, 10, 20),
  `Effort (25%)` = c(1.042, 21.41, 9.251, 10.24),
  `Effort (50%)` = c(65.28, 21.15, 26.36, 19.2),
  `Effort (75%)` = c(95.38, 19.97, 25.3, 27.49),
  `Effort (100%)` = c(25.91, 11.34, 5.757, 8.38),
  check.names = FALSE # Keep the name of the column
)

# 2. Data Form: Merge 'Effort xxx' into 'Effort_Level'
data_long_B <- pivot_longer(Lab_data_B, 
                            cols = starts_with("Effort"),
                            names_to = "Effort_Level",
                            values_to = "mV")

# 3. Generate the graph
ggplot(data = data_long_B, aes(x = `Time`, y = mV, color = Effort_Level)) +
  geom_line(size = 1) +
  geom_point(size = 3) +
    # When giving colour: exact name w/o ``
  scale_color_manual(values = c("Effort (25%)" = "red", "Effort (50%)" = "blue", 
                                "Effort (75%)" = "green", "Effort (100%)" = "orange")) +
  labs(title = "Effect of Effort Intensity on Muscle Fatigue Over Time",
       x = "Time (s)", y = "Amplitude (mV)", color = "Effort Level") +
  theme_bw()


# ----------------------------------------------------------
# PART C: Grip Force Analysis (Samples & Summary)
# ----------------------------------------------------------

# 1. Data input (top part of a table)
top_part <- data.frame(
  `Δ Grip Force (%)` = c("Encouragement", "Brief rest"),
  `Sample 1` = c(14.42, 13.2),
  `Sample 2` = c(35.6, 33.71),
  `Sample 3` = c(13.44, 15.31),
  check.names = FALSE
)

# 2. Summary data (Mean, SD) input (bottom part)
summary_data <- data.frame(
  Condition = c("Encouragement", "Brief rest"),
  Mean = c(21.15, 20.74),
  SD = c(12.52, 11.28)
)

# 3. Graph C-1: Bar graph comparing each sample
long_samples <- pivot_longer(top_part, cols = starts_with("Sample"), 
                             names_to = "Sample_ID", values_to = "Grip_Force")

ggplot(long_samples, aes(x = Sample_ID, y = Grip_Force, fill = `Δ Grip Force (%)`)) +
  geom_bar(stat = "identity", position = "dodge") + # Position bars side-by-side using 'dodge'
  labs(title = "Individual Sample Results by Condition", x = "Sample Number", y = "Δ Grip Force (%)") +
  theme_minimal() +
  scale_fill_manual(values = c("Encouragement" = "skyblue", "Brief rest" = "salmon"))

# 4. Graph C-2: Mean, SD
ggplot(summary_data, aes(x = Condition, y = Mean, fill = Condition)) +
  geom_bar(stat = "identity", width = 0.5) +
  geom_errorbar(aes(ymin = Mean - SD, ymax = Mean + SD), width = 0.1) + # margin of error
  labs(title = "Changes in Average Grip Force with Standard Deviation",
       x = "Experimental Condition", y = "Mean Grip Force (%)") +
  theme_bw() +
  guides(fill = "none") # Remove legend duplication

<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{Lab 2 result: Separating Graphs (Using facet)}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>R</b>
# ==========================================================
# Project: 4006BIO - Lab 2: Nerve Conduction Study
# By: Jiyoon Song
# Content: Latency and Amplitude comparison on site of stimulation (wrist vs elbow)
# ==========================================================

# Data Input
Lab_data_2 <- data.frame(
  # space in column name -> cover with backticks ``
  `Site of Stimulation` = c("Wrist", "Elbow"), 
  Latency = c(4, 1),
  Amplitude = c(4.734, 0.125),

  # !!  to keep the original name (space won’t be replaced by .):
  check.names = FALSE 
)


# Data Transformation
library(tidyr)
data_long_2 <- pivot_longer(Lab_data_2, 
                            cols = c("Latency", "Amplitude"), 
                            names_to = "Signal", 
                            values_to = "Value")


# 3.  Visualisation
library(ggplot2)

ggplot(data_long_2, aes(x = `Site of Stimulation`, y = Value, fill = Signal)) +
  # stat="identity" -> plot the actual values from the data
  geom_bar(stat = "identity", width = 0.5) +

  # facet_wrap -> separate graph from “Signal”
  # scales = "free_y" -> separate y-axis
  facet_wrap(~Signal, scales = "free_y") + 
  scale_fill_manual(values = c("Latency" = "red", "Amplitude" = "blue")) +
  labs(title = "Nerve Conduction Study: Wrist vs Elbow",
       subtitle = "Independent visual analysis by signal types (Time vs Voltage)",
       x = "Measurement Site",
       y = "Measured Value (ms / mV)",
       caption = "Wrist-elbow distance: 220mm, Conduction velocity: -73.33m/s") +
 theme_bw() +
  
  # Detailed design
  theme(
    strip.text = element_text(face = "bold", size = 12), # make face text bold
    legend.position = "none" # hide legends (already have it!)
  )
<b></b>
</pre> 
</details>

### $\color{#fffff}{\text{Lab 3 result: Generating Table and Changing table format into Markdown}}$ 
<details><summary>$\color{#fffff}{\text{Open/Close}}$ </summary> 

<pre>
<b>R</b>
# ==========================================================
# Project: 4006BIO - Lab 3: Spirometry
# By: Jiyoon Song
# Content: Pulmonary Function Test
# ==========================================================

# 4006BIO_Lab 3_A
# Data Input
Lab_data <- data.frame(
  "Respiratory Parameter" = c("Peak inspiratory flow (PIF), L/s", 
                              "Peak expiratory flow (PEF), L/s", 
                              "Time for forced vital capacity (FVC), s", 
                              "Forced vital capacity (FVC), L", 
                              "Forced expiratory volume in 1 second (FEV_1), L", 
                              "% FVC expired (in 1s), %"),
  "Normal Breathing" = c(1.437, -2.019, -4.28, 2.602, 2.667, 102.50),
  "Obstructed Breathing" = c(0.4128, -0.3639, -10.75, 3.783, 3.527, 93.23),
  check.names = FALSE
)
# print(Lab_data) 

library(knitr) #tool for generating a Markdown table
kable(Lab_data, 
      align = "lcc", #alignment: left/centre/right, write in order of columns
      caption = "Table: Pulmonary Function Test Results")

# 4006BIO_Lab 3_B
#Data Input
Lab_data_B1 <- data.frame(
  "Description" = c("Respiratory rate (RR), breaths/min (BPM)", "Tidal volume (Vᴛ), L", "Expired minute volume (Vᴇ(=Vᴛ*BPM)), L/min", "Inspiratory reserve volume (IRV), L", "Expiratory reserve volume (ERV), L", "Sample's predicted RV (RV), L"),
# subscript: either copy&paste / []
  "Normal Breathing" = c(16.38, 1.38, 22.60, 2.821, 1.073, NA),
  check.names = FALSE
)

Lab_data_B2 <- data.frame(
  "Lung Capacities (L)" = c("Inspiratory capacity (IC=Vᴛ+IRV)", "Expiratory capacity (EC=Vᴛ+ERV)","Vital capacity (VC=IRV+ERV+Vᴛ)", "Functional residual capacity (FRC=ERV+RV)", "Total lung capacity (TLC=VC+RV)"),
  "Calculated Value-Normal Breathing" =c(4.20, 2.45, 5.27, NA, NA),
  check.names = FALSE
)
# B1, B2 division bc: diff column content but same category (c.f.ed OG data)

library(knitr)
kable(Lab_data_B1, 
      align = "lc",
      caption = "Pulmonary Function Test Results: Static Measurements")

kable(Lab_data_B2, 
      align = "lc",
      caption = "Pulmonary Function Test Results: Static Measurements")
<b></b>
</pre> 
</details>
