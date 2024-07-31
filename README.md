# Demand-Forecasting-using-LSTM

## Project Overview

The fashion industry is highly dynamic, with trends changing rapidly. Retailers face significant challenges in predicting demand for fashion items, often leading to overstocking or stockouts, which are both costly and inefficient. There is a need for a solution that can predict demand accurately in real-time to optimize inventory management and meet customer expectations.

The objective of this project is to develop a machine learning model that predicts fashion item demand based on historical sales data, social media trends, and seasonal factors.

## Solution

This project utilizes Long Short-Term Memory (LSTM) Neural Networks for time-series forecasting. The model integrates seasonal patterns and other relevant features to improve the accuracy of demand predictions.

## Dataset

The dataset used in this project includes sales data from 2018 to 2022, detailing various aspects of fashion products such as gender preference, category, pattern, color, age group target, seasonal preference, material, price, sales count, reviews, ratings, and more.

You can download the dataset from [Kaggle](https://www.kaggle.com/datasets/fashionworldda/fashion-trend-dataset).

## Data Preprocessing

The preprocessing techniques used in this project include:

1. *Label Encoding:* Converting categorical data into numerical form.
2. *Aggregating Sales Data:* Grouping sales data by product, year, and month to obtain aggregated metrics.
3. *Scaling Numerical Features:* Using MinMaxScaler to ensure consistent data ranges for effective model training.


## Repository Files

- *demand_forecasting_based_on_avg_rating.ipynb:* Jupyter Notebook containing the code for demand forecasting based on average ratings. This is an another approach,which uses average rating as the target variable, predicting sales count based on the average customer ratings.
- *main.py.ipynb:* Jupyter Notebook containing the main code for the project. This is the main code based on seasonal factors.
- *predicted_sales_2023_monthly.csv:* CSV file containing the output predictions for the year 2023.

## Web Application

A user-friendly web application has been developed using Streamlit to provide a seamless interface for users to interact with the model. Users can select a product from a dropdown menu and view the predicted demand for the next year. The application also provides additional features such as charts for visualizing predictions, enhanced styling, and a responsive layout for an optimal user experience.

## How to Use

1. *Clone the repository:*
   bash
   git clone https://github.com/akshitha1705/Demand-Forecasting-using-LSTM.git
   cd Demand-Forecasting-using-LSTM
   

2. *Install required dependencies:*
   bash
   pip install -r requirements.txt
   

3. *Run the notebooks:*
   Open the Jupyter notebooks (demand_forecasting_based_on_avg_rating.ipynb and main.py.ipynb(main code)) and run the cells to execute the code.

   
4. *Run the Application:*
   Open the terminal and execute the command  streamlit run app.py


5. *Check the predictions:*
   The output predictions can be found in the predicted_sales_2023_monthly.csv file.

## Conclusion

This project demonstrates the use of LSTM Neural Networks for demand forecasting in the fashion industry. By leveraging historical sales data, social media trends, and seasonal factors, the model aims to provide accurate demand predictions to help retailers optimize inventory management and meet customer demands. The accompanying web application offers a user-friendly platform for exploring and visualizing these predictions, making it a valuable tool for decision-makers in the retail sector.
