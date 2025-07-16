import streamlit as st
import pandas as pd
import os
import groq
from dotenv import load_dotenv


# === CONFIG ===
st.set_page_config(page_title="🧠 Q&A Assistant", layout="centered")
st.title("💬 Q&A Assistant (Powered by Mixtral on Groq)")

# === LOAD CSV ===
DATA_PATH = "task2_review_analysis/cleaned_reviews.csv"
if not os.path.exists(DATA_PATH):
    st.error(f"❌ Could not find {DATA_PATH}. Please check the file path.")
    st.stop()

df = pd.read_csv(DATA_PATH)

# === SIDEBAR FILTERS ===
st.sidebar.header("📊 Apply Filters")
country = st.sidebar.text_input("Shipping Country")
rating_min, rating_max = st.sidebar.slider("Rating Range", 1, 5, (1, 5))
product_name = st.sidebar.text_input("Product Name (partial match)")

filtered_df = df.copy()

if country:
    filtered_df = filtered_df[filtered_df["Shipping Country"].str.lower() == country.lower()]
filtered_df = filtered_df[(filtered_df["Rating"] >= rating_min) & (filtered_df["Rating"] <= rating_max)]
if product_name:
    filtered_df = filtered_df[filtered_df["Product Name"].str.contains(product_name, case=False, na=False)]

st.markdown(f"🧹 Showing **{len(filtered_df)}** filtered reviews.")
st.dataframe(filtered_df.head(10), use_container_width=True)

# === USER QUESTION ===
st.markdown("---")
question = st.text_area("🔍 Ask your question based on these reviews", placeholder="e.g., What are the most common complaints about products in Canada?")
submit = st.button("🧠 Get AI Insight")

load_dotenv()
# === GROQ + MIXTRAL API CALL ===
if submit and question:
    with st.spinner("🤖 Thinking..."):

        # Load API key
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        if not GROQ_API_KEY:
            st.error("❌ Please provide a valid Groq API key (must start with 'gsk-').")
            st.stop()


        # Create client
        groq_client = groq.Client(api_key=GROQ_API_KEY)

        # Prepare prompt with small chunk of filtered data
        csv_snippet = filtered_df.head(30).to_csv(index=False)
        prompt = f"""
You are a data analyst. Based on the following Shopify review data in CSV format, answer the question below.

CSV DATA:
{csv_snippet}

QUESTION:
{question}

Please return a short, clear insight or summary.
"""

        try:
            response = groq_client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=500,
            )

            answer = response.choices[0].message.content
            st.success("✅ Answer Generated")
            st.markdown("### 📈 AI Insight")
            st.write(answer)

        except Exception as e:
            st.error(f"❌ Error: {e}")
