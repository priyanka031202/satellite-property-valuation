import os
import requests
import pandas as pd
from tqdm import tqdm

# ==============================
# CONFIGURATION
# ==============================

# 🔴 PASTE YOUR MAPBOX TOKEN HERE
MAPBOX_TOKEN = "pk.eyJ1IjoicHJpeWFua2ExMjEiLCJhIjoiY21qeTZnMmFhMDN5YTNlczgxdzczOWoxdyJ9.QGeSxU7NSyq63aSwKAQQdw"

# Path to training data
CSV_PATH = "data/train1.csv"

# Folder where images will be saved
IMAGE_DIR = "data/images"

# Satellite image settings
ZOOM_LEVEL = 16
IMAGE_SIZE = "256x256"

# Limit number of images (SAFE for free tier)
MAX_IMAGES = 2000   # you can change later

# ==============================
# SETUP
# ==============================

# Create image directory if not exists
os.makedirs(IMAGE_DIR, exist_ok=True)

# Load CSV
df = pd.read_csv(CSV_PATH)

print(f"Total rows in dataset: {len(df)}")
print(f"Downloading first {MAX_IMAGES} images...")

# ==============================
# DOWNLOAD SATELLITE IMAGES
# ==============================

for _, row in tqdm(df.head(MAX_IMAGES).iterrows(), total=MAX_IMAGES):

    lat = row["lat"]
    lon = row["long"]
    house_id = row["id"]

    image_path = f"{IMAGE_DIR}/{house_id}.png"

    # Skip if image already exists
    if os.path.exists(image_path):
        continue

    url = (
        f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
        f"{lon},{lat},{ZOOM_LEVEL}/{IMAGE_SIZE}"
        f"?access_token={MAPBOX_TOKEN}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        with open(image_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"❌ Failed for ID {house_id} | Status: {response.status_code}")

print("✅ Image download completed")

