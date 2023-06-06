#!/usr/bin/env python
# coding: utf-8

# ### Consider a dataset containing the heights (in centimeters) of 1000 individuals. The
# mean height is 170 cm with a standard deviation of 10 cm. The dataset is approximately
# normally distributed, and its skewness is approximately zero. Based on this information,
# answer the following questions:
# a. What percentage of individuals in the dataset have heights between 160 cm
# and 180 cm?
# b. If we randomly select 100 individuals from the dataset, what is the probability
# that their average height is greater than 175 cm?
# c. Assuming the dataset follows a normal distribution, what is the z-score
# corresponding to a height of 185 cm?
# d. We know that 5% of the dataset has heights below a certain value. What is
# the approximate height corresponding to this threshold?
# e. Calculate the coefficient of variation (CV) for the dataset.
# f. Calculate the skewness of the dataset and interpret the result.

# In[4]:



import numpy as np
from scipy.stats import norm

# Given information
mean_height = 170
std_dev_height = 10

# a. Percentage of individuals with heights between 160 cm and 180 cm
percentage_between_160_and_180 = norm.cdf(180, mean_height, std_dev_height) - norm.cdf(160, mean_height, std_dev_height)
percentage_between_160_and_180 *= 100
print(f"Percentage between 160 cm and 180 cm: {percentage_between_160_and_180}%")

# b. Probability that the average height of 100 individuals is greater than 175 cm
sample_mean_height = mean_height
sample_std_dev_height = std_dev_height / np.sqrt(100)
probability_avg_height_greater_175 = 1 - norm.cdf(175, sample_mean_height, sample_std_dev_height)
print(f"Probability that average height > 175 cm for a sample of 100 individuals: {probability_avg_height_greater_175}")

# c. Z-score corresponding to a height of 185 cm
z_score_height_185 = (185 - mean_height) / std_dev_height
print(f"Z-score for a height of 185 cm: {z_score_height_185}")

# d. Approximate height corresponding to the threshold where 5% of the dataset is below
threshold_height_5_percent = norm.ppf(0.05, mean_height, std_dev_height)
print(f"Approximate height corresponding to the 5% threshold: {threshold_height_5_percent}")

# e. Coefficient of Variation (CV) for the dataset
coefficient_variation = (std_dev_height / mean_height) * 100
print(f"Coefficient of Variation (CV): {coefficient_variation}")

# f. Skewness of the dataset
skewness = 0  # As given that the dataset has an approximate skewness of zero
print(f"Skewness of the dataset: {skewness}")

