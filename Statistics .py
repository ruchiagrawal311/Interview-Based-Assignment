#!/usr/bin/env python
# coding: utf-8

# ### Answer 3 
# Consider the ‘Blood Pressure Before’ and ‘Blood Pressure After’ columns from the data and calculate the following 
# https://drive.google.com/file/d/1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y/view?usp=share_
# 
# a. Measure the dispersion in both and interpret the results. 
# b. Calculate mean and 5% confidence interval and plot it in a graph 
# c. Calculate the Mean absolute deviation and Standard deviation and interpret the results. 
# d. Calculate the correlation coefficient and check the significance of it at 1% level of significance. 
# 

# In[39]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Read the data from the provided Google Drive link
data_url = "https://drive.google.com/uc?id=1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y"
data = pd.read_csv(data_url)

# Extract the ' Blood Pressure Before (mmHg)' and ' Blood Pressure After (mmHg)' columns
bp_before = data[' Blood Pressure Before (mmHg)']
bp_after = data[' Blood Pressure After (mmHg)']

# a. Measure the dispersion in both and interpret the results
dispersion_bp_before = np.var(bp_before)
dispersion_bp_after = np.var(bp_after)
print("Dispersion (Variance) in Blood Pressure Before: ", dispersion_bp_before)
print("Dispersion (Variance) in Blood Pressure After: ", dispersion_bp_after)

# b. Calculate mean and 5% confidence interval and plot it in a graph
mean_bp_before = np.mean(bp_before)
mean_bp_after = np.mean(bp_after)
confidence_interval_bp_before = stats.t.interval(0.95, len(bp_before)-1, loc=mean_bp_before, scale=stats.sem(bp_before))
confidence_interval_bp_after = stats.t.interval(0.95, len(bp_after)-1, loc=mean_bp_after, scale=stats.sem(bp_after))

# Plotting the mean and confidence interval
plt.errorbar(['Blood Pressure Before', 'Blood Pressure After'], [mean_bp_before, mean_bp_after], yerr=[confidence_interval_bp_before[1]-mean_bp_before, confidence_interval_bp_after[1]-mean_bp_after], fmt='o')
plt.title("Mean and 5% Confidence Interval")
plt.ylabel("Mean")
plt.ylim([70, 100])
plt.show()

# c. Calculate the Mean Absolute Deviation and Standard Deviation and interpret the results
mad_bp_before = np.mean(np.abs(bp_before - mean_bp_before))
mad_bp_after = np.mean(np.abs(bp_after - mean_bp_after))
std_bp_before = np.std(bp_before)
std_bp_after = np.std(bp_after)
print("Mean Absolute Deviation (MAD) in Blood Pressure Before: ", mad_bp_before)
print("Mean Absolute Deviation (MAD) in Blood Pressure After: ", mad_bp_after)
print("Standard Deviation (SD) in Blood Pressure Before: ", std_bp_before)
print("Standard Deviation (SD) in Blood Pressure After: ", std_bp_after)

# d. Calculate the correlation coefficient and check the significance of it at 1% level of significance
correlation_coefficient, p_value = stats.pearsonr(bp_before, bp_after)
print("Correlation Coefficient: ", correlation_coefficient)
print("p-value: ", p_value)

if p_value < 0.01:
    print("The correlation is statistically significant at 1% level of significance.")
else:
    print("The correlation is not statistically significant at 1% level of significance.")


# ### Answer 4
#  A group of 20 friends decide to play a game in which they each write a number between 1 and 20 on a slip of paper and put it into a hat. They then draw one slip of paper at random. What is the probability that the number on the slip of paper is a perfect square (i.e., 1, 4, 9, or 16)?

# In[7]:


total_friends = 20  # Total number of friends
perfect_squares = [1, 4, 9, 16]  # Perfect square numbers
total_possible_outcomes = len(perfect_squares)  # Number of perfect squares

probability_perfect_square = total_possible_outcomes / total_friends

print(f"The probability of drawing a perfect square number: {probability_perfect_square}")


# ### Answer 5
# 
# A certain city has two taxi companies: Company A has 80% of the taxis and Company B has 20% of the taxis. Company A's taxis have a 95% success rate for picking up passengers on time, while Company B's taxis have a 90% success rate. If a randomly selected taxi is late, what is the probability that it belongs to Company A? 
# 

# In[4]:


p_company_a = 0.8  # Probability of selecting a taxi from Company A
p_company_b = 0.2  # Probability of selecting a taxi from Company B
p_success_a = 0.95  # Probability of a taxi from Company A being on time
p_success_b = 0.90  # Probability of a taxi from Company B being on time

# Calculate the probability of a taxi being late from each company
p_late_a = 1 - p_success_a
p_late_b = 1 - p_success_b

# Calculate the probability of a randomly selected taxi being late
p_late = p_company_a * p_late_a + p_company_b * p_late_b

# Calculate the probability that a late taxi belongs to Company A using Bayes' theorem
p_company_a_given_late = (p_company_a * p_late_a) / p_late

print(f"The probability that a randomly selected late taxi belongs to Company A: {p_company_a_given_late}")


# ### Answer 6
# 
# A pharmaceutical company is developing a drug that is supposed to reduce blood pressure. They conduct a clinical trial with 100 patients and record their blood pressure before and after taking the drug. The company wants to know if the change in blood pressure follows a normal distribution. 
# https://drive.google.com/file/d/1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y/view?usp=share_
# 

# In[40]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read the data from the provided Google Drive link
data_url = "https://drive.google.com/uc?id=1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y"
data = pd.read_csv(data_url)

# Extract the relevant columns
bp_before = data[' Blood Pressure Before (mmHg)']
bp_after = data[' Blood Pressure After (mmHg)']

# Calculate the change in blood pressure
change_in_bp = bp_after - bp_before

# Plotting the histogram of the change in blood pressure
plt.hist(change_in_bp, bins=10, edgecolor='black')
plt.title("Histogram of Change in Blood Pressure")
plt.xlabel("Change in Blood Pressure")
plt.ylabel("Frequency")
plt.show()

# Perform normality test using Shapiro-Wilk test
_, p_value = stats.shapiro(change_in_bp)

if p_value > 0.05:
    print("The change in blood pressure follows a normal distribution.")
else:
    print("The change in blood pressure does not follow a normal distribution.")


# ### Answer 7
# The equations of two lines of regression, obtained in a correlation analysis between variables X and Y are as follows: and . 2𝑋 + 3 − 8 = 0 2𝑌 + 𝑋 − 5 = 0 The variance of 𝑋 = 4 Find the 
# a. Variance of Y 
# b. Coefficient of determination of C and Y 
# c. Standard error of estimate of X on Y and of Y on X.
# 

# In[5]:


import numpy as np

variance_x = 4  # Variance of X

# a. Variance of Y
slope_x = 2
intercept_x = -3
variance_y = variance_x * slope_x ** 2
print(f"Variance of Y: {variance_y}")

# b. Coefficient of determination of X and Y
slope_y = -1/2
intercept_y = 5
r_squared_xy = (slope_y * variance_x) / variance_y
print(f"Coefficient of determination of X and Y: {r_squared_xy}")

# c. Standard error of estimate of X on Y and of Y on X
std_error_estimate_xy = np.sqrt(1 - r_squared_xy) * np.sqrt(variance_y)
std_error_estimate_yx = np.sqrt(1 - (variance_y / (slope_x ** 2 * variance_x)))
print(f"Standard error of estimate of X on Y: {std_error_estimate_xy}")
print(f"Standard error of estimate of Y on X: {std_error_estimate_yx}")


# ### Answer 8
# The anxiety levels of 10 participants were measured before and after a new therapy. The scores are not normally distributed. Use the Wilcoxon signed-rank test to test whether the therapy had a significant effect on anxiety levels. The data is given below: Participant Before therapy After therapy Difference

# In[6]:


from scipy.stats import wilcoxon

# Data
before_therapy = [10,8, 12, 15, 6, 9, 11, 7, 14, 10]
after_therapy = [7, 6, 10, 12, 5, 8, 9, 6, 12, 8]

# Perform Wilcoxon signed-rank test
statistic, p_value = wilcoxon(before_therapy, after_therapy)

print(f"Wilcoxon signed-rank statistic: {statistic}")
print(f"P-value: {p_value}")


# ### Answer 9
# Given the score of students in multiple exams
# Test the hypothesis that the mean scores of all the students are the same. If not, name the student with the highest score.

# In[17]:


import pandas as pd
from scipy.stats import f_oneway

# Create a dataframe with student scores
data = {
    'Student': ['Karan', 'Deepa', 'Karthik', 'Chandan', 'Jeevan'],
    'Test1': [85, 70, 90, 75, 95],
    'Test2': [90, 80, 85, 70, 92],
    'Final': [92, 85, 88, 75, 96]
}
df = pd.DataFrame(data)

# Perform ANOVA test
test1_scores = df['Test1']
test2_scores = df['Test2']
final_scores = df['Final']
f_value, p_value = f_oneway(test1_scores, test2_scores, final_scores)

# Print the ANOVA results
print("ANOVA Results:")
print("F-value:", f_value)
print("p-value:", p_value)

# Check if the null hypothesis is rejected
if p_value < 0.05:
    print("The mean scores of the students are not the same.")
    # Find the student with the highest score
    highest_score_student = df.loc[df['Final'].idxmax(), 'Student']
    print("The student with the highest score is:", highest_score_student)
else:
    print("The mean scores of the students are the same.")


# ### Answer 10
# Q-10. A factory produces light bulbs, and the probability of a bulb being defective is 0.05. The factory produces a large batch of 500 light bulbs.
# a.  What is the probability that exactly 20 bulbs are defective?
# b.  What is the probability that at least 10 bulbs are defective?
# c.  What is the probability that at max 15 bulbs are defective?
# d.  On average, how many defective bulbs would you expect in a batch of 500?
# 

# In[8]:


from scipy.stats import binom

total_bulbs = 500
defective_probability = 0.05

# a. Probability of exactly 20 defective bulbs
defective_count_a = 20
probability_a = binom.pmf(defective_count_a, total_bulbs, defective_probability)
print(f"Probability of exactly 20 defective bulbs: {probability_a}")

# b. Probability of at least 10 defective bulbs
defective_count_b = 10
probability_b = 1 - binom.cdf(defective_count_b - 1, total_bulbs, defective_probability)
print(f"Probability of at least 10 defective bulbs: {probability_b}")

# c. Probability of at most 15 defective bulbs
defective_count_c = 15
probability_c = binom.cdf(defective_count_c, total_bulbs, defective_probability)
print(f"Probability of at most 15 defective bulbs: {probability_c}")

# d. Expected number of defective bulbs
expected_defective = total_bulbs * defective_probability
print(f"Expected number of defective bulbs: {expected_defective}")


# ### Answer 11
# Given the data of a feature contributing to different classes
# 
#  
# https://drive.google.com/file/d/1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y/view?usp
# =share_
# 
# a.  Check whether the distribution of all the classes are the same or not.
# b.  Check for the equality of variance/
# c.  Which amount LDA and QDA would perform better on this data for classification and why.
# d.  Check the equality of mean for between all the classes.

# In[76]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.model_selection import cross_val_score

# Read the data from the provided link
data_url = "https://drive.google.com/file/d/1mCjtYHiX--mMUjicuaP2gH3k-SnFxt8Y/view?usp=sharing"
file_id = data_url.split("/")[5].split("?")[0]
download_url = f"https://drive.google.com/uc?id={file_id}"
data = pd.read_csv(download_url)

# Display the column names and a sample of the data
print("Column Names:")
print(data.columns)
print("\nSample Data:")
print(data.head())

# Extract the class labels and corresponding feature values
class_labels = data.columns[1:]
feature_values = data.values[:, 1:]

# Separate feature values for each class
class_data = [feature_values[:, i] for i in range(len(class_labels))]

# Perform Kruskal-Wallis test for equality of distributions
_, p_value = stats.kruskal(*class_data)

if p_value < 0.05:
    print("The distributions of the classes are not the same.")
else:
    print("The distributions of the classes are the same.")
    
# c.  Which amount LDA and QDA would perform better on this data for classification and why.


# d. Check the equality of mean for between all the classes.
# Perform one-way ANOVA test to check the equality of mean between all the classes
_, p_value_anova = stats.f_oneway(*feature_values.T)

if p_value_anova < 0.05:
    print("The means are not equal between the classes.")
else:
    print("The means are equal between the classes.")


# ### Answer 12
# A pharmaceutical company develops a new drug and wants to compare its effectiveness against a standard drug for treating a particular condition. They conduct a study with two groups: Group A receives the new drug, and Group B receives the standard drug. The company measures the improvement in a specific symptom for both groups after a 4-week treatment period.
# a.  The company collects data from 30 patients in each group and calculates the mean improvement score and the standard deviation of improvement for each group. The mean improvement score for Group A is 2.5 with a standard deviation of 0.8, while the mean improvement score for Group B is 2.2 with a standard deviation of 0.6. Conduct a t-test to determine if there is a significant difference in the mean improvement scores between the two groups. Use a significance level of 0.05.
# b.  Based on the t-test results, state whether the null hypothesis should be rejected or not. Provide a conclusion in the context of the study.
# 

# In[12]:


from scipy.stats import ttest_ind

# Group A data
group_a_mean = 2.5
group_a_std = 0.8
group_a_size = 30

# Group B data
group_b_mean = 2.2
group_b_std = 0.6
group_b_size = 30

# Perform t-test
statistic, p_value = ttest_ind(
    [group_a_mean] * group_a_size,
    [group_b_mean] * group_b_size,
    equal_var=False  # Assuming unequal variances
)

alpha = 0.05  # Significance level

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in mean improvement scores between Group A and Group B.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in mean improvement scores between Group A and Group B.")


# In[ ]:




