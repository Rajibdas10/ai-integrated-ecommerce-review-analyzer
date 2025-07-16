import pandas as pd
from datetime import datetime

# Load raw data
df = pd.read_csv("task2_review_analysis/raw_reviews.csv")


# Standardize timestamps
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Strip and lowercase category/product names
df['Product Name'] = df['Product Name'].astype(str).str.strip().str.lower()
df['Product Category'] = df['Product Category'].astype(str).str.strip().str.lower()

# Remove blank or too-short reviews
df['Review Content'] = df['Review Content'].astype(str)
df = df[df['Review Content'].str.strip().str.len() > 20]

# Handle missing ratings
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
mean_rating = df['Rating'].mean()
df['Rating'] = df['Rating'].fillna(round(mean_rating, 1))

# Handle missing order value
df['Order Value'] = pd.to_numeric(df['Order Value'], errors='coerce')
df['Order Value'] = df['Order Value'].fillna(df['Order Value'].median())

# Flag bad fulfillment statuses
df['Fulfillment Status'] = df['Fulfillment Status'].fillna("Unknown")

# Save cleaned data
df.to_csv("cleaned_reviews.csv", index=False)
print("[✅] Cleaned data saved to cleaned_reviews.csv")
