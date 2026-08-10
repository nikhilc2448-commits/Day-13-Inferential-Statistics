# Day 13 - Inferential Statistics & A/B Testing

This repository contains my Day 13 training work on Inferential Statistics and A/B Testing using Python.

## Topics Covered

- Population vs Sample
- Sampling and Sampling Bias
- Confidence Intervals
- Hypothesis Testing
- Null and Alternative Hypothesis
- P-value
- Significance Level (0.05)
- T-test
- A/B Testing

## Part A - Sampling

In this part, I worked with the Capstone Orders dataset.

- Took a random sample of 50 orders.
- Took another random sample of 50 orders.
- Calculated the mean Sales for both samples.
- Calculated the mean Sales of the full dataset.
- Compared the sample means with the full dataset mean.

## Part B - Comparing Two Groups

In this part, I compared the Profit values of two regions:

- South
- West

The mean Profit for both regions was calculated and an independent t-test was performed using `scipy.stats.ttest_ind`.

The p-value was compared with the 0.05 significance level to determine whether the difference was statistically significant.

## Part C - A/B Test

This part covers a written A/B testing scenario.

It includes:

- Comparing the performance of Version A and Version B.
- Calculating the relative improvement.
- Understanding what should be checked before recommending a change.
- Identifying factors that could make the results misleading.
- Giving a business recommendation while considering uncertainty.

## Files

- `day13_inferential_stats.py` - Python code for the Day 13 task.
- `Capstone Orders.csv` - Orders dataset.
- `Capstone Customers.csv` - Customers dataset.

## Tools Used

- Python
- Pandas
- SciPy
- Jupyter/VS Code

## Conclusion

This task helped me understand how sampling, hypothesis testing, p-values and t-tests can be used to make conclusions from data. It also helped me understand how A/B testing can be used to compare two versions and make better business decisions.

## Author

Nikhil Chougale
