# Satellite Property Valuation

This project predicts house prices using a combination of **property details** and **satellite images**.  
The main goal is to check whether satellite imagery improves price prediction compared to using tabular data alone.

---

## Project Overview

This project follows a multimodal machine learning approach:

- Uses structured housing data (bedrooms, bathrooms, square footage, location, etc.)
- Extracts visual features from satellite images using **ResNet-18**
- Combines tabular and image features into a single feature set
- Trains a **Random Forest Regressor**
- Compares results with a tabular-only baseline model

---

## Project Structure


