import pandas as pd
from scipy.stats import ttest_ind


# Load datasets

orders = pd.read_csv("Capstone Orders.csv", encoding="latin1")
customers = pd.read_csv("Capstone Customers.csv", encoding="latin1")


# Basic Inferential Statistics Concepts

# Population means the complete group or dataset we are interested in.
# A sample is a smaller part taken from the population.
# Sampling is useful because it is not always practical to work with the
# complete population.

# Sampling bias happens when the sample does not properly represent the
# population. For example, selecting only a certain type of customer
# may give a misleading result.

# A confidence interval gives a range of values that is likely to contain
# the true population value.

# In hypothesis testing, the null hypothesis means there is no real
# difference between the groups.
# The alternative hypothesis means there is a real difference between
# the groups.

# A p-value tells us how unusual the result would be if the null hypothesis
# were true.
# A small p-value gives stronger evidence against the null hypothesis.
# A p-value does not tell us the probability that the null hypothesis is true.

# 0.05 is commonly used as the significance level.
# It is a convention and not a rule that applies to every situation.

# A t-test is used to compare the means of two groups and check whether
# their difference is statistically significant.

# In an A/B test, the control is the existing version and the variant
# is the new version.
# A fair A/B test should randomly assign similar users to both groups
# and keep other conditions as similar as possible.


# Part A - Sampling

# Remove rows where Sales is missing

orders_sales = orders.dropna(subset=["Sales"])


# Take first random sample of 50 orders

sample1 = orders_sales.sample(50, random_state=10)


# Take another random sample of 50 orders

sample2 = orders_sales.sample(50, random_state=20)


# Calculate mean Sales of both samples

sample1_mean = sample1["Sales"].mean()
sample2_mean = sample2["Sales"].mean()


# Calculate mean Sales of full dataset

full_mean = orders_sales["Sales"].mean()


print("PART A - SAMPLING")
print("------------------")
print("Mean Sales of sample 1:", round(sample1_mean, 2))
print("Mean Sales of sample 2:", round(sample2_mean, 2))
print("Mean Sales of full dataset:", round(full_mean, 2))

print()


# Sample means can be different because each sample contains different orders.
# They can also be different from the full dataset mean because a sample
# contains only part of the population.
# This shows why we should not depend on only one sample when making
# conclusions about the full dataset.


# Part B - Comparing two groups

# Add Region to orders using CustomerID

data = orders.merge(
    customers[["CustomerID", "Region"]],
    on="CustomerID",
    how="left"
)


# Clean region names

data["Region"] = data["Region"].str.strip().str.title()


# Select two regions

south = data[data["Region"] == "South"]["Profit"].dropna()
west = data[data["Region"] == "West"]["Profit"].dropna()


# Calculate average Profit

south_mean = south.mean()
west_mean = west.mean()


# Run t-test

t_stat, p_value = ttest_ind(
    south,
    west,
    equal_var=False
)


print("PART B - COMPARING TWO GROUPS")
print("-----------------------------")
print("South mean Profit:", round(south_mean, 2))
print("West mean Profit:", round(west_mean, 2))
print("t-statistic:", round(t_stat, 4))
print("p-value:", round(p_value, 4))

print()


# Check statistical significance

if p_value < 0.05:
    print("The difference is statistically significant at 0.05.")
else:
    print("The difference is not statistically significant at 0.05.")

print()


# The null hypothesis is that there is no real difference in the average
# Profit between South and West.
# The alternative hypothesis is that there is a real difference.

# If the p-value is below 0.05, we reject the null hypothesis.
# If the p-value is 0.05 or higher, we do not reject the null hypothesis.

# For this test, the p-value is greater than 0.05, so the difference
# between South and West is not statistically significant.

# South has a higher average profit, but the difference may not be strong
# enough to say that the region caused it.

# The difference may still be useful for the business depending on business
# goals, even if it is not statistically significant.

# Statistical significance and practical significance are not the same.
# Statistical significance tells us whether the evidence is strong enough
# to support a difference.
# Practical significance asks whether the difference is large enough to
# actually matter to the business.


# Part C - A/B test scenario

# Part C is a written task, so the answers are given below as comments.


# 1. Which version performed better, and by how much?

# Version B performed better.

# Version A conversion rate was 8% and Version B was 9%.

# The increase is 1 percentage point.
# In relative terms, this is a 12.5% improvement.


# 2. What would you need to know before recommending the change?

# We should check whether the difference is statistically significant.

# We should also check whether both groups were selected fairly and tested
# under similar conditions.

# It is also useful to check the test duration and other business metrics.


# 3. Name two things that could make this result misleading.

# 1. The users in A and B may not be similar.

# 2. An outside factor such as a promotion or holiday could affect one
# group more than the other.


# 4. What would you recommend to the business?

# I would first check the statistical significance and make sure the test
# was fair before recommending the change.

# If the result is statistically significant and the test was fair,
# Version B would be a good option.

# If someone asks whether I am certain, I would say no because there is
# always some uncertainty in an A/B test.