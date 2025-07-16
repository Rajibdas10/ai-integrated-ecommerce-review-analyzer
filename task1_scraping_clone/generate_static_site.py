import json
import os

OUTPUT_FOLDER = "task1_scraping_clone/output"
STATIC_FOLDER = "task1_scraping_clone/static_site"
IMAGE_PATH = "output/images"  # relative for HTML
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Load JSON data
with open(os.path.join(OUTPUT_FOLDER, "products.json")) as f:
    products = json.load(f)

# HTML layout
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pokémon Store Clone</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>🛒 Pokémon Store Clone</h1>
    <div class="container">
"""

for p in products:
    html += f"""
        <div class="card">
            <img src="../{IMAGE_PATH}/{p['image_filename']}" alt="{p['name']}">
            <h2>{p['name']}</h2>
            <p class="price">{p['price']}</p>
            <a href="{p['product_url']}" target="_blank">🔗 View Product</a>
        </div>
    """

html += """
    </div>
</body>
</html>
"""

# Save HTML
with open(os.path.join(STATIC_FOLDER, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("[✅] Static HTML site generated!")
