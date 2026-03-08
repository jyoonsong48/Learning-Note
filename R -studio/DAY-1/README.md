DAY 1

<pre>
<b>```R</b>

# ==========================================================
# Project: 4006BIO: Human Physiology - Homeostasis and Health (Lab 1)
# 작성자: Jiyoon Song
# 분석 내용: Visualisation of data: EMG, Muscle Fatigue, Changes in Force over time
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

<b>```</b>
</pre>