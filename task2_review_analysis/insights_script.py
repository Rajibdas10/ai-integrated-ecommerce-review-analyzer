import pandas as pd

df = pd.read_csv("task2_review_analysis/cleaned_reviews.csv")

# 1. Product categories with most 1-star reviews in Canada
canada_1stars = df[(df["Rating"] == 1) & (df["Shipping Country"] == "Canada")]
category_counts = canada_1stars["Product Category"].value_counts()
print("1. 1-Star Reviews in Canada by Category:\n", category_counts.head(), "\n")

# 2. Correlation between order value and rating
correlation = df["Order Value"].corr(df["Rating"])
print(f"2. Correlation between Order Value and Rating: {correlation:.2f}\n")

# 3. Summarize top complaints and compliments (placeholder — will add AI prompt later)
complaints = df[df["Rating"] <= 2]["Review Content"].dropna().tolist()
compliments = df[df["Rating"] >= 4]["Review Content"].dropna().tolist()
print("3. Sample Complaints:", complaints[:5])
print("3. Sample Compliments:", compliments[:5])

# 4. Fulfillment status most associated with negative reviews
negatives = df[df["Rating"] <= 2]
fulfillment_counts = negatives["Fulfillment Status"].value_counts()
print("4. Fulfillment status with most negative reviews:\n", fulfillment_counts.head())
