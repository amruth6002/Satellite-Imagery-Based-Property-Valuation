import os
import pandas as pd
import requests
from tqdm import tqdm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
DATA_FILE = "data/train.csv"
OUTPUT_DIR = "data/images"
STADIA_API_KEY = os.getenv("STADIA_API_KEY")

def download_image(lat, lon, image_id):
    """
    Downloads a static map image from Stadia Maps API.
    """
    if not STADIA_API_KEY:
        print("Error: STADIA_API_KEY not found in .env")
        return

    # Stadia Maps Static API URL
    # Format: https://tiles.stadiamaps.com/static/{style_id}/{lon},{lat},{zoom}/{width}x{height}.jpg?api_key={key}
    # Using 'alidade_satellite' if available, otherwise 'alidade_smooth'
    # Note: Stadia Maps primarily provides vector-based styles (maps), not satellite imagery, 
    # unless you have a specific plan or they added it recently. 
    # I will use 'alidade_smooth' as a reliable default for now, which is a Map View.
    # If specifically needing satellite, we might need a different provider later.
    style_id = "alidade_satellite" 
    
    # Stadia Maps Static API with query parameters
    # Format: https://tiles.stadiamaps.com/static/{style_id}?center={lat},{lon}&zoom={zoom}&size={width}x{height}&api_key={key}
    url = f"https://tiles.stadiamaps.com/static/{style_id}?center={lat},{lon}&zoom=18&size=400x400&api_key={STADIA_API_KEY}"

    image_path = os.path.join(OUTPUT_DIR, f"{image_id}.jpg")
    
    if os.path.exists(image_path):
        return # Skip if already exists

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
        elif response.status_code == 403:
             print(f"Error 403: Key invalid or quota exceeded for ID {image_id}")
        elif response.status_code == 404:
             print(f"Error 404: Style not found or invalid location for ID {image_id}")
        else:
            print(f"Failed to download image for ID {image_id}: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image for ID {image_id}: {e}")

def main():
    if not STADIA_API_KEY:
        print("Please add STADIA_API_KEY to your .env file")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Read data
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print(f"File not found: {DATA_FILE}")
        return

    print(f"Found {len(df)} rows. Starting download...")
    
    # Check for likely column names
    lat_col = 'lat' if 'lat' in df.columns else 'latitude'
    lon_col = 'long' if 'long' in df.columns else 'longitude'
    
    if 'id' not in df.columns:
        df['id'] = df.index

    # Limit to 2,000 images to respect typical free tier limits (usually 2,500/day)
    # You can remove .head(2000) if you have a paid plan and want all 16k images
    print("Downloading first 2,000 images...")
    subset = df.head(2000)
    
    for index, row in tqdm(subset.iterrows(), total=len(subset)):
        image_id = str(row['id']) 
        lat = row[lat_col]
        lon = row[lon_col]
        
        download_image(lat, lon, image_id)

    print("Download complete. Check data/images folder.")

if __name__ == "__main__":
    main()
