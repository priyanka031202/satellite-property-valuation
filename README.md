# Satellite Property Valuation

This project predicts house prices using both **property details** and **satellite images**.  
The goal is to check whether satellite imagery improves house price prediction compared to using tabular data alone.



## Project Overview

- Uses structured housing data (bedrooms, bathrooms, square footage, location, etc.)
- Extracts visual features from satellite images using **ResNet-18**
- Combines tabular and image features into a single dataset
- Trains a **Random Forest Regressor**
- Compares results with a tabular-only baseline model



## Project Structure

satellite-property-valuation/
1. data/
   - train1.csv
   - test2.csv
   - images/
2. notebooks/
   - preprocessing.ipynb
   - model_training.ipynb
3. src/
4. data_fetcher.py
5. requirements.txt
6. .gitignore
7. README.md



## Model & Results

The multimodal model (tabular + satellite images) performs better than the tabular-only model.

- **RMSE:** ~194,914  
- **R² Score:** ~0.64  

This shows that satellite images add useful neighborhood-level information that improves house price prediction.



## How to run 
1. Insatll despenceriaes
2. Run notebooks in this order:

-> preprocessing.ipynb

-> model_training.ipynb

## Key Takeaways

1. Tabular data captures property-level features

2. Satellite images add visual and neighborhood context

3. Combining both improves prediction accuracy

## Author

Priyanka Choudhary


