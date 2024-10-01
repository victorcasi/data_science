# 📊 **Bootstrap Confidence Intervals Library**

Welcome to the **Bootstrap Confidence Intervals Library**! This Python library was developed during my internship at Renault to provide a comprehensive tool for statistical analysis and visualization of data. It combines the bootstrap method with plotting confidence intervals for specified percentiles, making it versatile for various applications within Renault.

## Features
- **Calculate CDF**: Computes the cumulative distribution function (CDF) for the given dataset.
- **Bootstrap Confidence Intervals**: Calculates confidence intervals for specified percentiles using the bootstrap method.
- **Visualize Data**: Generates plots of confidence intervals alongside the CDF for better data interpretation.

## Library Functions
The library consists of three main functions:

### 1. `calculate_cdf(data)`
Calculates the cumulative distribution function (CDF) for the given dataset.

**Parameters**:
- `data`: The dataset to analyze.

**Returns**: A tuple containing the sorted data and the corresponding CDF values.

### 2. `bootstrap_confidence_interval(data, percentiles=(1, 25, 50, 75, 95, 99), confidence=0.95, n_bootstraps=1000)`
Calculates confidence intervals for specified percentiles using the bootstrap method.

**Parameters**:
- `data`: The dataset to analyze.
- `percentiles`: List of percentiles to calculate (default is [1, 25, 50, 75, 95, 99]).
- `confidence`: Confidence level for the interval (default is 0.95).
- `n_bootstraps`: Number of bootstrap samples to generate (default is 1000).

**Returns**: A dictionary with percentiles as keys and tuples of confidence intervals as values.

### 3. `plot_confidence_intervals(df, column=None, percentiles=[1, 25, 50, 75, 95, 99], confidence=0.95, n_bootstraps=1000)`
Plots S-curves and confidence intervals for one or all columns of a DataFrame.

**Parameters**:
- `df`: DataFrame containing the data.
- `column`: Specific column to plot (None to plot all columns).
- `percentiles`: List of percentiles to calculate (default is [1, 25, 50, 75, 95, 99]).
- `confidence`: Confidence level for the interval (default is 0.95).
- `n_bootstraps`: Number of bootstrap samples to generate (default is 1000).

## Usage Example

You can find the examples and study cases on the folder /notebooks

Here’s a simple example of how to import and use the library:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bootstrap_ci_library import calculate_cdf, bootstrap_confidence_interval, plot_confidence_intervals

### Sample data
data = np.random.randn(1000)
df = pd.DataFrame(data, columns=['Sample Data'])

### Calculate CDF
sorted_data, cdf = calculate_cdf(data)

### Bootstrap confidence intervals
confidence_intervals = bootstrap_confidence_interval(data, percentiles=[1, 25, 50, 75, 95, 99], confidence=0.95, n_bootstraps=1000)

### Plotting
plot_confidence_intervals(df, column='Sample Data', percentiles=[1, 25, 50, 75, 95, 99], confidence=0.95, n_bootstraps=1000)
```
## Conclusion

This library provides a robust framework for statistical analysis and visualization of complex datasets, making it easier for users to interpret data effectively. It is designed to enhance data-driven decision-making processes within Renault and can be adapted for various applications across different sectors.

## Contributing

Contributions are welcome! If you would like to improve this library or add new features, feel free to fork the repository and submit a pull request.

## Contact

For any questions or feedback, please reach out via:

Email: victorcarvsi@gmail.com

Feel free to explore the repository, and if you find the library useful, don't hesitate to give it a ⭐!

