# Satellite Imagery-Based Real Estate Valuation

## Project Overview
This project implements a **Multimodal Neural Network** to value real estate properties by combining traditional tabular data (bedrooms, square footage, year built) with satellite imagery. This approach quantifies the "location value" of a property by visually analyzing its surroundings (greenery, density, proximity to highways) using Computer Vision.

## Key Features
*   **Multimodal Architecture**: Fuses a ResNet-18 CNN (for images) with a Multi-Layer Perceptron (for tabular specs).
*   **Visual Forensics**: Uses Grad-CAM to visualize what features (trees vs. pavement) drive property value.
*   **Geospatial Analysis**: Incorporates Latitude/Longitude to map price hotspots.
*   **Log-Price Modeling**: handles the skewed distribution of high-value properties.

## Repository Structure
```
.
├── 23117140_final.csv     # Final Predictions Submission for Test Set
├── 23117140_report.pdf    # Comprehensive Project Report
├── data_fetcher.py        # Script to download satellite images from Google/Mapbox
├── model_training.ipynb   # Main notebook: Training, Validation, and Explanation (Grad-CAM)
├── preprocessing.ipynb    # Notebook for EDA and generating visualizations
├── requirements.txt       # Python dependencies
└── README.md              # This documentation
```

## Setup Instructions

### 1. Environment Setup
Create a virtual environment and install the required dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Data Acquisition
This project requires a dataset of house metadata (`train.csv`) and corresponding satellite images.
To download images (if you have an API key):
```bash
python data_fetcher.py
```
*Note: Ensure you have a valid Google Maps Static API key stored in a `.env` file as `GOOGLE_MAPS_API_KEY`.*

## Usage

### Training the Model
Open `model_training.ipynb` in Jupyter Notebook/Lab:
1.  **Run All Cells** to:
    *   Load and preprocess the dataset.
    *   Train the Multimodal Network (ResNet + MLP).
    *   Compare performance against an XGBoost baseline.
    *   Generate a `submission.csv` (renamed to `23117140_final.csv`).

### Visual Analysis (EDA & Forensics)
Run `preprocessing.ipynb` to generate the project's visual artifacts:
*   Price Distribution Histograms
*   Geospatial Price Maps
*   Sample Image Grids
*   Grad-CAM Explanation Heatmaps

## Results
The multimodal model demonstrates that visual signals from satellite imagery provide a measurable improvement in valuation accuracy over tabular-only baselines, specifically by capturing neighborhood context (density, greenery) that simple metadata misses.

## License
[MIT License](LICENSE)
