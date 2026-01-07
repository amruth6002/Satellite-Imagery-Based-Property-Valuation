import os
import pandas as pd
import requests
from tqdm import tqdm
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configuration
DATA_FILE = "data/train.csv"
OUTPUT_DIR = "data/images"
# Reuse Key 2
STADIA_API_KEY = os.getenv("STADIA_API_KEY_2")

def download_image(lat, lon, image_id):
    """
    Downloads a static map image from Stadia Maps API.
    """
    if not STADIA_API_KEY:
        print("Error: STADIA_API_KEY_2 not found in .env")
        return

    style_id = "alidade_satellite" 
    
    # Stadia Maps Static API with query parameters
    url = f"https://tiles.stadiamaps.com/static/{style_id}?center={lat},{lon}&zoom=18&size=400x400&api_key={STADIA_API_KEY}"

    image_path = os.path.join(OUTPUT_DIR, f"{image_id}.jpg")
    
    if os.path.exists(image_path):
        return # Skip if already exists

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
        elif response.status_code == 429:
             print(f"Error 429: Too Many Requests for ID {image_id}. Sleeping 2s...")
             time.sleep(2) # Backoff if we hit rate limits
        elif response.status_code == 403:
             print(f"Error 403: Key invalid or quota exceeded for ID {image_id}")
        else:
            print(f"Failed to download image for ID {image_id}: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image for ID {image_id}: {e}")

def main():
    if not STADIA_API_KEY:
        print("Please add STADIA_API_KEY_2 to your .env file")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Read data
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"File not found: {DATA_FILE}")
        return

    if 'id' not in df.columns:
        df['id'] = df.index

    # BATCH 4: Images 6000 to 8000
    print("Starting BATCH 4 (Images 6000-8000) reusing Key 2...")
    subset = df.iloc[6000:8000]
    
    # Check for likely column names
    lat_col = 'lat' if 'lat' in df.columns else 'latitude'
    lon_col = 'long' if 'long' in df.columns else 'longitude'

    for index, row in tqdm(subset.iterrows(), total=len(subset)):
        image_id = str(row['id']) 
        lat = row[lat_col]
        lon = row[lon_col]
        
        download_image(lat, lon, image_id)

    print("Batch 4 download complete.")

if __name__ == "__main__":
    main()
