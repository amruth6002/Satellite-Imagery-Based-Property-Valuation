# Satellite Imagery-Based Property Valuation

## Project Overview
This project implements a **Multimodal Regression Pipeline** that predicts property prices using:
1.  **Tabular Data:** House features (Bedrooms, Square Footage, Year Built).
2.  **Visual Data:** Satellite Imagery (captured via Stadia Maps Static API).

## Repository Structure
- `data/`: Contains `train.csv`, `test.csv`, and the `images/` directory (~8,000 images).
- `notebooks/`:
  - `preprocessing.ipynb`: Data cleaning and EDA.
  - `model_training.ipynb`: The main Multimodal Neural Network training loop.
- `src/`: Python scripts used for data acquisition.
- `report_structure.md`: Outline for the final project report.

## How to Run (Kaggle)
1.  **Upload Data:** Upload the `data` folder (or `project_upload.zip`) to your Kaggle dataset.
2.  **Open Notebook:** Open `notebooks/model_training.ipynb`.
3.  **Run All:** Execute the cells.
    - The model uses **ResNet18** (Pretrained) for images.
    - It uses **HuberLoss** for robust regression.
    - It will output a `submission.csv` file.

## Requirements
- Python 3.8+
- PyTorch
- torchvision
- pandas, numpy, scikit-learn
- PIL (Pillow)
- opencv-python

## Authors
- [Your Name]
