# Zomato-Restaurant-Data-Analysis

📌 Project Overview

This project focuses on analyzing restaurant and review data from the Zomato dataset to extract actionable insights regarding customer ratings, cuisine preferences, geographical hotspots, and the various factors that influence restaurant success. The analysis serves as a foundation for strategic decision-making for food delivery platforms (such as an Alfido Tech style platform) looking to optimize partnerships and content curation.

🎯 Goal

To analyze restaurant data and extract key business insights on ratings, popular cuisines, location preferences, and the underlying factors affecting customer reviews.

🗂️ Dataset

Source: https://www.kaggle.com/datasets/bhanupratapbiswas/zomato

🛠️ Tech Stack & Requirements

Language: Python

Libraries: pandas, numpy, matplotlib, seaborn, wordcloud

Tools: Jupyter Notebook / Google Colab


🧹 Data Cleaning & Preprocessing

To ensure accurate analysis, the raw dataset underwent rigorous cleaning:

Handling Missing Values: Filled missing Cuisines entries with 'Unknown'.

Text Standardization: Stripped whitespaces and standardized string formatting across categorical columns like Restaurant Name, City, and Cuisines.

Data Type Conversion:

Extracted numeric values from the Aggregate rating column (e.g., stripping the "/5" format).

Converted Votes and Average Cost for two to standard numeric formats.

Currency Normalization: Implemented a conversion matrix to standardize all global costs into Indian Rupees (Cost_in_INR) to allow for accurate price comparisons.

📊 Key Findings & Visualizations

1. Location Hotspots (Top Cities)

Insight: Areas like BTM, HSR, and Whitefield have the highest concentration of listed restaurants. This indicates massive market demand but also high competition in these specific zones.

(See Top 15 Cities bar chart)

2. Rating Distribution by Cuisine

Insight: Cuisines like Desserts and Bakery, Desserts maintain consistently higher median ratings with tighter distributions. Broad categories like North Indian show a massive spread, indicating high variability in quality.

(See Rating Distribution boxplot)

3. Factors Affecting Ratings (Correlation)

Insight: There is a positive correlation (0.35) between Aggregate rating and Votes, suggesting that highly-rated restaurants attract higher user engagement (or vice versa). There is also a mild correlation (0.29) between Cost_in_INR and Votes.

(See Correlation Heatmap)

4. Most Popular Cuisines

Insight: The word cloud reveals that North Indian, Chinese, South Indian, and Fast Food are the most dominant culinary terms across the dataset.

(See Cuisines Wordcloud)
