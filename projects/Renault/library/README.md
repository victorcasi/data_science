# 📊 **Bootstrap Confidence Intervals Library**

Welcome to the **Bootstrap Confidence Intervals Library**! This Python library was developed during my internship at Renault to provide a comprehensive tool for statistical analysis and visualization of data. It combines the bootstrap method with plotting confidence intervals for specified percentiles, making it versatile for various applications within Renault. The library includes a Python script that leverages the NumPy, Matplotlib, and SciPy libraries to calculate confidence intervals for specified percentiles of data using the bootstrap technique. It also visualizes these intervals alongside the cumulative distribution function (CDF) of the data.

## Features
- **Calculate Confidence Intervals**: Computes confidence intervals for specified percentiles using the bootstrap technique.
- **Visualize Data**: Generates plots of confidence intervals alongside the cumulative distribution function (CDF) for better data interpretation.
- **Robust Statistical Analysis**: Offers reliable statistical measures to understand data variability and distribution.

## Library Components
The library includes a Python script with the following main functions:
1. **Calculate CDF**: The `calculate_cdf` function computes the cumulative distribution function for the given dataset. It sorts the data and returns both the sorted data and its CDF, which is essential for understanding the distribution of the dataset.
    ```python
    def calculate_cdf(data):
        # Implementation code
        pass
    ```

2. **Bootstrap Confidence Interval**: The `bootstrap_confidence_interval` function calculates confidence intervals for specified percentiles using the bootstrap method. This function accepts parameters such as the dataset, desired percentiles, confidence level, and the number of bootstrap samples. It generates bootstrap samples, computes the specified percentiles for each sample, and returns the confidence intervals, facilitating robust statistical analysis.
    ```python
    def bootstrap_confidence_interval(data, percentiles, confidence_level, n_samples):
        # Implementation code
        pass
    ```

3. **Plotting Function**: The `plot_confidence_intervals` function visualizes the S-curves and confidence intervals for one or all columns of a DataFrame. It handles NaN values, calculates necessary statistical measures, and plots the results, including annotations for clarity. This visualization aids in interpreting the data and understanding the confidence intervals in relation to the distribution.
    ```python
    def plot_confidence_intervals(data, percentiles):
        # Implementation code
        pass
    ```

## Requirements
To use this library, you need to have the following Python libraries installed: **NumPy**, **Matplotlib**, and **SciPy**. You can install these libraries using pip:
```bash
pip install numpy matplotlib scipy
