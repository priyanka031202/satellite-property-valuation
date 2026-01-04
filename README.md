Satellite Property Valuation

This project predicts house prices using a combination of property details and satellite images.
The goal is to understand whether satellite imagery improves price prediction compared to using tabular data alone.

Project Overview

Uses structured housing data (bedrooms, bathrooms, square footage, location, etc.)

Extracts visual features from satellite images using ResNet-18

Combines tabular and image features into a single model

Trains a Random Forest Regressor

Compares results with a tabular-only baseline model

Project Structure
data/
 ├── train1.csv
 ├── test2.csv
 └── images/

notebooks/
 ├── preprocessing.ipynb
 └── model_training.ipynb

src/
 └── data_fetcher.py

requirements.txt
.gitignore

Model & Results

The multimodal model (tabular + satellite images) performed better than the tabular-only model.

RMSE: ~194,914

R² Score: ~0.64

This indicates that satellite imagery adds useful neighborhood-level information.

How to Run the Project

Install dependencies:

pip install -r requirements.txt


Run notebooks in this order:

preprocessing.ipynb

model_training.ipynb

Conclusion

Satellite images help capture environmental and neighborhood features that are not available in structured data.
Combining visual and numerical inputs leads to improved property valuation performance.

Author

Priyanka Choudhary
