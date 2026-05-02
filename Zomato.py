# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

# Set plot style
sns.set_theme(style="whitegrid")

# Load the dataset (Zomato dataset often uses 'latin-1' encoding)
df = pd.read_csv('zomato.csv', encoding='latin-1')

# Standardize column names to expected names
rename_map = {
    'name': 'Restaurant Name',
    'location': 'City',
    'cuisines': 'Cuisines',
    'approx_cost(for two people)': 'Average Cost for two',
    'rate': 'Aggregate rating',
    'votes': 'Votes',
    'rest_type': 'Rest Type',
    'listed_in(type)': 'Listed In'
}
df.rename(columns=rename_map, inplace=True)

# Display the first 5 rows
print(df.head())
print(df.info())

# 1. Check for missing values
print("Missing values before cleaning:\n", df.isnull().sum())

# Fill missing 'Cuisines' with 'Unknown'
if 'Cuisines' in df.columns:
    df['Cuisines'] = df['Cuisines'].fillna('Unknown')

# 2. Drop duplicates
df.drop_duplicates(inplace=True)

# 3. Clean text fields (convert to string and strip whitespaces)
for col in ['Restaurant Name', 'City', 'Cuisines']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Convert numeric columns
if 'Aggregate rating' in df.columns:
    df['Aggregate rating'] = df['Aggregate rating'].astype(str).str.split('/').str[0]
    df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

if 'Votes' in df.columns:
    df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce').fillna(0).astype(int)

if 'Average Cost for two' in df.columns:
    df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')

print("\nMissing values after cleaning:\n", df.isnull().sum())

# Use cost directly as INR when no currency column exists
if 'Average Cost for two' in df.columns:
    if 'Currency' in df.columns:
        exchange_rates = {
            'Indian Rupees(Rs.)': 1.0,
            'Dollar($)': 83.0,
            'Pounds(£)': 105.0,
            'NewZealand($)': 50.0,
            'Emirati Diram(AED)': 22.6,
            'Brazilian Real(R$)': 16.5,
            'Turkish Lira(TL)': 2.6,
            'Omani Rial(OMR)': 215.0,
            'Sri Lankan Rupee(LKR)': 0.28,
            'Indonesian Rupiah(IDR)': 0.0053,
            'Rand(RSA)': 4.4,
            'Qatari Rial(QR)': 22.8,
            'Botswana Pula(P)': 6.0
        }
        df['Cost_in_INR'] = df.apply(
            lambda row: row['Average Cost for two'] * exchange_rates.get(row['Currency'], 1), axis=1
        )
    else:
        df['Cost_in_INR'] = df['Average Cost for two']

    df = df[df['Cost_in_INR'] > 0]

    plt.figure(figsize=(12, 6))
    top_cities = df['City'].value_counts().head(15)
    sns.barplot(x=top_cities.index, y=top_cities.values, palette='viridis')
    plt.title('Top 15 Cities with Most Restaurants (Location Hotspots)', fontsize=15)
    plt.xlabel('City')
    plt.ylabel('Number of Restaurants')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    if 'Cuisines' in df.columns and 'Aggregate rating' in df.columns:
        plt.figure(figsize=(12, 6))
        top_cuisines = df['Cuisines'].value_counts().head(10).index
        cuisine_df = df[df['Cuisines'].isin(top_cuisines)]
        sns.boxplot(x='Cuisines', y='Aggregate rating', data=cuisine_df, palette='Set2')
        plt.title('Rating Distribution for Top 10 Cuisines', fontsize=15)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    numeric_cols = [col for col in ['Aggregate rating', 'Votes', 'Cost_in_INR'] if col in df.columns]
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='YlGnBu', linewidths=0.5)
        plt.title('Correlation Heatmap of Numeric Features', fontsize=15)
        plt.show()

    if 'Cuisines' in df.columns:
        plt.figure(figsize=(10, 8))
        cuisine_text = ' '.join(df['Cuisines'].astype(str).tolist())
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='inferno').generate(cuisine_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Most Popular Cuisines Wordcloud', fontsize=15)
        plt.show()
else:
    print("Required column 'Average Cost for two' not found in the dataset.")
    