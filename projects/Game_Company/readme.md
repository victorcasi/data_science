# 🎮 Player Ranking Prediction Model for Game Post-Statistics

This project involves developing a machine learning model to predict the final rank of a player (on a scale from 1 for first place to 0 for last) based on post-game statistics. The dataset includes anonymized information on various aspects of gameplay, such as kills, assists, distances traveled, and more. This project showcases my end-to-end data science workflow, from data cleaning and exploration to feature engineering and modeling, presented in a Jupyter notebook format for clarity and replicability.

## 📜 Project Overview

In this project, I predict a player’s final ranking based on their post-game statistics. The dataset includes approximately 50k training entries and 5k testing entries. Each row represents the stats of a single player after a match. The game types include solo, duo, and team modes, with varied team sizes and player counts per game.

## 🚀 Approach Summary

Here is a brief summary of my approach:

### Data Analysis
The data analysis phase provided valuable initial insights into variable distributions, behaviors, and correlations. During this phase, I identified potential issues and interesting relationships, establishing a foundational understanding for further refinements and enhancements.

### Data Cleaning
During the data cleaning phase, I recategorized the `gameType` variable and removed problematic or redundant data points. I experimented with outlier removal but found it did not significantly improve model outcomes. Careful preprocessing ensured that the data was well-structured and primed for effective feature engineering.

### Feature Engineering
I categorized features into quantitative and qualitative types and applied techniques like one-hot encoding and standard scaling. I tested additional features, such as total distance traveled and combined weapons statistics, but found these yielded limited improvements in model performance.

### Modeling and Explainability
In the modeling stage, I implemented various models, aligning metrics with project objectives. I also explored deep learning approaches, performed hyperparameter tuning through grid search, and assessed feature importance. This thorough approach aimed to maximize model robustness and derive actionable insights for business applications.

## 🎯 Project Objectives

**Main Objectives**:

- Predict players' ranks based on their post-game statistics.
- Extract meaningful insights through data analysis and feature engineering.
- Build and validate models that are both accurate and interpretable.

## 🔧 Data Processing & Methodology

To build a high-performing model, I conducted various data processing and feature engineering tasks:

- **Data Cleaning**: Removed or recategorized outliers and unnecessary features.
- **Data Analysis**: Performed distribution analysis, correlation studies, and visualization.
- **Feature Engineering**: Applied one-hot encoding, scaling, and various feature transformations.
- **Modeling & Evaluation**: Implemented deep learning and machine learning models, hyperparameter tuning, and feature importance assessments.

## 🔍 Key Data Points and Variables

- **assists**: Number of enemy players damaged and then killed by teammates.
- **damages**: Total damage dealt, with self-inflicted damage removed.
- **kills, headshots, roadKills**: Various kill metrics, including the number of kills and specific actions such as headshots or kills while driving.
- **distances**: Metrics for distances traveled on foot, by vehicle, or swimming.
- **gameType**: Game mode, such as solo or team-based modes.
- **rankPts & winPts**: External ranking metrics similar to Elo ratings, based on kills or wins.
- **winRankPercentage**: The target variable for the prediction (0 - 1 scale representing last to first place).

## 🛠️ Technology Stack & Tools

- **Python**: For data manipulation, modeling, and analysis.
- **Pandas & NumPy**: Data handling and preprocessing.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-Learn & XGBoost**: Model building and evaluation.
- **TensorFlow/Keras**: For deep learning model experimentation.
- **Jupyter Notebook**: Code and analysis presentation.

## 📈 Project Impact & Insights

The final models provide reliable predictions for player rankings based on post-game stats, offering insights into factors influencing game outcomes. This approach and methodology can be adapted for similar prediction challenges involving time-series or event-driven data, contributing to improved decision-making based on player behavior and game dynamics.

## 📊 Files & Notebooks

The project files are as follows:

- **train.csv**: Training dataset (50k rows, games from 2024-01-01 to 2024-04-30).
- **test.csv**: Testing dataset (5k rows, games from 2024-05-01 to 2024-05-31).
- **WinnerAnalysis.ipynb**: Jupyter notebook containing data cleaning, analysis, feature engineering, and modeling.


Enjoy exploring the project, and if you find it useful, don’t hesitate to give it a ⭐!
