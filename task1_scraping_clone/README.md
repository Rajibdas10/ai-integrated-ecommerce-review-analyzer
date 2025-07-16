

## 📄 `README.md` (for Task 1 — E-Commerce Scraping + Static Clone)

```markdown
# 🛍️ Task 1: E-Commerce Website Scraping and Static Site Clone

## ✅ Objective

Replicate the functionality and structure of a small e-commerce website using **only AI tools and free technologies**. The task involved:

- Scraping product content, categories, and structure
- Saving data in both CSV and JSON formats
- Generating a static clone of the site using HTML and CSS
- Recording a walkthrough video using Loom

---

## 🧠 Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Core scripting |
| **Selenium** | Headless browser to render JS content |
| **BeautifulSoup** | HTML parsing |
| **Pandas** | CSV/JSON processing |
| **Requests** | Downloading product images |
| **ChatGPT** | Planning, debugging, and code generation |
| **Loom** | Walkthrough video |
| **VS Code** | IDE for development |

---

## 🌐 Website Scraped

**URL:** [https://scrapeme.live/shop/](https://scrapeme.live/shop/)  
✔️ This is a public dummy e-commerce site used for ethical scraping practice.

---

## 📦 Project Structure

```

SCRAP\_PROJECT/
│
├── task1\_scraping\_clone/
│   ├── scrape\_products.py          ← Scrapes the website
│   ├── generate\_static\_site.py     ← Builds HTML/CSS clone
│   ├── output/
│   │   ├── products.csv            ← Clean product data (CSV)
│   │   ├── products.json           ← Product data (JSON)
│   │   └── images/                 ← All downloaded product images
│   ├── static\_site/
│   │   ├── index.html              ← Static mockup site (dark theme)
│   │   └── style.css               ← Responsive dark-themed styling
│   └── screenshot.png              ← Screenshot of the final HTML clone

````

---

## 🚀 How to Run

### 1. Clone / Download the repo

```bash
git clone <your-repo-url>
cd task1_scraping_clone
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run scraper

```bash
python scrape_products.py
```

### 4. Generate static site

```bash
python generate_static_site.py
```

### 5. Open the static site

Open `static_site/index.html` in your browser to view the clone.

---

## 📸 Screenshot

![Screenshot](screenshot.png)

---

## 🎥 Loom Video (Walkthrough)

🔗 \[Insert your Loom video link here]

---

## ✅ Submission Deliverables

* ✅ `scrape_products.py`
* ✅ `products.csv` & `products.json`
* ✅ Downloaded product images
* ✅ `index.html` + `style.css`
* ✅ Screenshot
* ✅ Loom video link

---

## 📌 Notes

* Chose `https://scrapeme.live` as a safe and legal public test site.
* Built the static site using real data scraped by AI-driven tools.
* Used **only free tools and AI assistants** as per instructions.

---
