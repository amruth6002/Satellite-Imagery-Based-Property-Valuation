# Satellite Imagery-Based Property Valuation

## Project Overview
This project implements a **Multimodal Regression Pipeline** that predicts property prices using:
1.  **Tabular Data:** House features (Bedrooms, Square Footage, Year Built).
2.  **Visual Data:** Satellite Imagery (captured via Stadia Maps Static API).

## Repository Structure
- `data/`: Contains `train.csv`, `test.csv`, and the `images/` directory.
- `model_training.ipynb`: **The Main Code**. Trains the Multimodal Neural Network (ResNet18 + MLP) and generates predictions.
- `preprocessing.ipynb`: Exploratory Data Analysis (EDA) and visualization generation.
- `data_fetcher.py`: Script used to download satellite imagery.
- `project_report_content.txt`: Text content for the final project report.
- `report_structure.md`: Outline for the report.
- `requirements.txt`: List of Python dependencies.

## How to Run (Kaggle)
1.  **Upload Data:** Upload the `data` folder to your Kaggle dataset.
2.  **Upload Code:** Upload `model_training.ipynb` to Kaggle (or copy-paste its content).
3.  **Run All:** Execute the notebook cells.
    - **Step 1:** Training (Baselines + Deep Learning).
    - **Step 2:** Evaluation (RMSE/R2 Scores).
    - **Step 3:** Visual Analysis (Grad-CAM maps).
    - **Step 4:** Submission (Generates `submission.csv`).

## Requirements
- Python 3.8+
- PyTorch & torchvision
- pandas, numpy, scikit-learn
- PIL (Pillow) & opencv-python

## Authors
- [Your Name]
