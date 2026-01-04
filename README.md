#Satellite Property Valuation

This project predicts house prices using a combination of property details and satellite images.
The idea is to check whether satellite imagery can improve price prediction compared to using tabular data alone.

#What I Did

1.Used housing features like bedrooms, bathrooms, square footage, and location

2.Extracted visual features from satellite images using a pretrained ResNet-18

3.Combined tabular and image features into a single model

4.Trained a Random Forest Regressor

5.Compared results with a tabular-only baseline model

#Files in This Project
data/
 ├── train1.csv
 ├── test2.csv
 └── images/

#notebooks/
 ├── preprocessing.ipynb
 └── model_training.ipynb

#src/
 └── data_fetcher.py

#requirements.txt
#.gitignore

#Results

1.The model that used tabular data + satellite images performed better than the tabular-only model.

2.RMSE: ~194,914

3.R² Score: ~0.64

4.This shows that satellite images add useful information about the surrounding area.

#How to Run

Install dependencies:

pip install -r requirements.txt


Run notebooks in order:

preprocessing.ipynb

model_training.ipynb

#Conclusion

Satellite imagery helps capture neighborhood characteristics that are not available in structured data.
Combining visual and numerical features leads to better property price predictions.

Author: Priyanka Choudhary
