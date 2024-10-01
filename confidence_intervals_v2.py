import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import percentileofscore

def calculate_cdf(data):
    """
    Calculate the cumulative distribution function (CDF) for the given data.
    """
    sorted_data = np.sort(data)
    return sorted_data, [percentileofscore(sorted_data, value) for value in sorted_data]

def bootstrap_confidence_interval(data, percentiles=(1, 25, 50, 75, 95, 99), confidence=0.95, n_bootstraps=1000):
    """
    Calculate the confidence interval for percentiles using the bootstrap method.
    
    Parameters:
    - data: The dataset to analyze.
    - percentiles: List of percentiles to calculate (default is [1, 25, 50, 75, 95, 99]).
    - confidence: Confidence level for the interval (default is 0.95).
    - n_bootstraps: Number of bootstrap samples to generate (default is 1000).
    """
    bootstraps = [np.percentile(np.random.choice(data, size=len(data), replace=True), percentiles) for _ in range(n_bootstraps)]
    return {p: (np.percentile(bootstraps, (1-confidence)/2*100, axis=0)[i], 
                np.percentile(bootstraps, (1+confidence)/2*100, axis=0)[i]) for i, p in enumerate(percentiles)}

def plot_confidence_intervals(df, column=None, percentiles=[1, 25, 50, 75, 95, 99], confidence=0.95, n_bootstraps=1000):
    """
    Plot S-curves and confidence intervals for one or all columns of a DataFrame.
    
    Parameters:
    - df: DataFrame containing the data.
    - column: Specific column to plot (None to plot all columns).
    - percentiles: List of percentiles to calculate (default is [1, 25, 50, 75, 95, 99]).
    - confidence: Confidence level for the interval (default is 0.95).
    - n_bootstraps: Number of bootstrap samples to generate (default is 1000).
    """
    if column:
        # Plot for a single column
        columns = [column]
    else:
        # Plot for all columns
        columns = df.columns
    
    n_cols = 2  # Number of columns in the subplot grid
    n_rows = (len(columns) + n_cols - 1) // n_cols  # Number of rows in the subplot grid

    fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, 5 * n_rows))
    axs = axs.flatten()

    for i, col in enumerate(columns):
        data = df[col].dropna()  # Remove NaN values
        sorted_data, cdf = calculate_cdf(data)
        intervals = bootstrap_confidence_interval(data, percentiles, confidence, n_bootstraps)
        ax = axs[i]
        
        # Plot the S-curve
        ax.plot(sorted_data, cdf, color='k', label='S Curve')
        
        # Plot confidence intervals and percentiles
        for j, p in enumerate(percentiles):
            interval = intervals[p]
            percentile_value = np.percentile(data, p)
            ax.plot(interval, [p, p], '|-', markersize=20, color=f'C{j}', linewidth=4)
            ax.text(interval[1], p, f'   {p}% ', fontsize=15, verticalalignment='center')
            ax.annotate(f'{interval[0]:.2f} | {percentile_value:.2f} | {interval[1]:.2f}', 
                        (percentile_value, p), textcoords="offset points", xytext=(0, -30), ha='center', 
                        fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor=f'C{j}', facecolor="white"))

        # Set axis limits, labels, and titles
        ax.set_xlabel(col, fontsize=12)
        ax.set_ylabel('Coverage Rate (%)', fontsize=12)
        ax.set_title(f'Confidence Intervals and S-Curve for {col}', fontsize=15)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True)
        ax.tick_params(axis='both', labelsize=10)

    # Turn off unused subplots
    for i in range(len(columns), len(axs)):
        axs[i].axis('off')

    plt.tight_layout()
    plt.show()
