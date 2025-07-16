Perfect, Rajib. Let’s get this done like a pro. Here's how we’ll proceed:

---

## ✅ Part 1: `README.md` (Auto-generated for your assignment submission)

You can place this directly under your root folder (`SCRAP_PROJECT/README.md`) before pushing:

---

### ✅ `README.md` Content (Copy this into a file)

```markdown
# 🛒 AI-Powered E-commerce Scraper & Review Analyzer

This project was submitted as a take-home assignment. It demonstrates end-to-end use of AI + Python for automating data collection, analysis, and insight generation on e-commerce product listings and customer reviews.

---

## 📦 Task 1: E-commerce Website Cloning + Scraping

**Goal:** Scrape product data from a small e-commerce site and generate a mock static clone of the site using only AI tools.

### ✅ Features:
- Scraped product names, prices, images, and links from [scrapeme.live](https://scrapeme.live/shop/)
- Saved structured output in both **CSV** and **JSON**
- Downloaded product images and stored locally
- Generated a clean, HTML-based static clone using scraped data

### 📂 Task 1 File Structure:
```

task1\_scraping\_clone/
├── output/
│   ├── products.csv
│   ├── products.json
│   └── images/
├── scrape\_products.py
└── generate\_static\_site.py

```

---

## 💬 Task 2: Shopify Reviews Cleaning + Q&A Assistant

**Goal:** Clean messy customer review data and build a ChatGPT-powered assistant to answer stakeholder questions using Groq API.

### ✅ Features:
- Cleaned raw review data: fixed timestamps, normalized categories, filtered invalid/missing entries
- Answered key questions using LLM (Mixtral via Groq):
  - Most 1-star reviews in Canada?
  - Correlation between order value & rating?
  - Top 5 complaints and compliments?
  - Which fulfillment status has highest negative feedback?
- Built a **Streamlit App** with filters and a QA chat assistant for non-technical users.

### 📂 Task 2 File Structure:
```

task2\_review\_analysis/
├── raw\_reviews.csv
├── cleaned\_reviews.csv
├── data\_cleaning\_script.py
├── insight\_script.py
└── app.py

```

---

## 🎥 Explanation Videos

📌 All steps have been explained clearly via video:
- `Task 1 (Loom):` [Loom Video Link](https://loom.com/your-link)
- `Task 2:` See `explanation_videos/task2_walkthrough.mp4` (or drive link)

---

## 🛠️ Tech Stack

- Python, Pandas, Selenium, BeautifulSoup
- Streamlit, dotenv, JSON/CSV
- Groq (Mixtral API for free LLM inference)
- HTML/CSS (for static site generation)
- VS Code + GitHub Desktop

---

## ⚠️ Notes

- The `.env` file is ignored for safety.
- This repo is temporarily public for submission. Will be made private or removed post-deadline.

---

## 🙌 Author

**Rajib Das**  
