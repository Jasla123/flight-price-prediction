## Flight Price Prediction using Machine Learning

## Project Overview

Flight ticket prices can change depending on several factors such as airline, source, destination, travel class, departure time, arrival time, journey duration, and number of stops.

This project uses Machine Learning to predict the approximate price of a flight based on these details.

The project also includes a Streamlit web application, where users can enter flight details and get an estimated flight price.

---

## Objective

The main objective of this project is to:

- Predict flight ticket prices using Machine Learning.
- Identify important factors that influence flight prices.
- Compare different regression algorithms.
- Build a Machine Learning pipeline.
- Deploy the model using Streamlit.
- Provide a simple and user-friendly interface for flight price prediction.

---

## Dataset

- Dataset: Flight Price Dataset
- Number of Rows: 300,257
- Number of Columns: 25
- Target Variable: Price

The dataset contains information related to airlines, routes, travel class, dates, timings, duration, stops, and flight prices.

---

## Features Used

The final model uses the following features:

- Airline
- From
- To
- Class
- Day
- Month
- Departure Hour
- Arrival Hour
- Departure Period
- Arrival Period
- Duration in Minutes
- Number of Stops
- Arrival Daytime
- Departure Daytime

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook
- Git
- GitHub
- Git LFS

---

## Project Workflow

Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Random Forest Selection
   ↓
Machine Learning Pipeline
   ↓
Streamlit Application
   ↓
Flight Price Prediction

---

## Data Preprocessing

The dataset contains both categorical and numerical features.

The preprocessing steps include:

- Handling categorical features
- Encoding categorical variables
- Processing numerical features
- Extracting useful information from date and time
- Converting flight duration into minutes
- Preparing the data for Machine Learning

---

## Feature Engineering

New useful features were created from the existing data.

Examples include:

- Extracting day and month from travel date
- Extracting departure hour
- Extracting arrival hour
- Creating departure and arrival time periods
- Converting duration into minutes

These features help the Machine Learning model understand flight-related patterns better.

---

## Machine Learning Models

Different regression algorithms were trained and compared:

1. Linear Regression

Used as a basic regression model for comparison.

2. Random Forest Regressor

Random Forest combines multiple decision trees to produce a better prediction.

It achieved the best performance among the tested models.

3. Gradient Boosting Regressor

Another ensemble regression technique used for comparison.

---

## Model Performance

The final selected model is Random Forest Regressor.

Final Results

Metric| Score
R² Score| 0.9885
RMSE| 2441.54

The Random Forest model provided the best performance among the tested models.

---

## Machine Learning Pipeline

A Machine Learning pipeline was created to combine:

- Data preprocessing
- Feature transformation
- Trained Random Forest model

The trained pipeline was saved as:

flight_price_pipeline.pkl

This pipeline is used by the Streamlit application to make predictions for new inputs.

---

## Streamlit Application

The project includes a Streamlit-based web application.

Users can enter:

- Airline
- Source
- Destination
- Travel Class
- Day
- Month
- Departure Time
- Arrival Time
- Departure Period
- Arrival Period
- Duration
- Number of Stops
- Arrival Daytime
- Departure Daytime

After entering the details, the user can click the Predict Price button to get an estimated flight price.

---

## Example Prediction

For one sample input, the model predicted an approximate flight price of:

₹2,352.85

The prediction is an estimate and does not guarantee the actual ticket price.

Actual flight prices may vary depending on factors such as demand, availability, season, booking time, and other market conditions.

---

## Challenges Faced

During the development of this project, we faced several challenges:

Pipeline Integration

The input features from the Streamlit application had to exactly match the features expected by the trained pipeline.


## Streamlit Deployment

Initially, there were issues while running the Streamlit application. The application was successfully configured and executed after troubleshooting.

Large Pipeline File

The trained pipeline was initially very large, making it difficult to upload directly to GitHub.

The pipeline size was reduced, and Git LFS (Git Large File Storage) was used to handle the large model file.

GitHub Configuration

Git username, email configuration, authentication, and large-file handling were also part of the deployment process.

---

## Real-World Applications

This project can be useful for:

- Travelers planning their trips
- Passengers estimating their travel budget
- Travel agencies
- Flight booking platforms
- Comparing different travel options

The system can help users get an approximate idea of the expected flight price before booking.

---

## Limitations

The current dataset has a limited number of routes and mainly represents domestic flight data.

The model does not include all factors that can influence real-world flight prices.

The predicted price should therefore be considered an estimated price, not a guaranteed ticket price.

---

## Future Improvements

In future versions, the project can be improved by:

- Adding more domestic cities and routes
- Including international destinations such as Dubai, Singapore, London, and Bangkok
- Adding more airlines
- Including seasonal information
- Including holidays and special events
- Adding advance booking days
- Including real-time seat availability
- Using real-time flight price data
- Exploring more advanced Machine Learning and Deep Learning models

A larger and more diverse dataset can help the model learn a wider range of real-world flight pricing patterns.

---

## How to Run the Project

1. Clone the repository

git clone <your-github-repository-link>

2. Navigate to the project folder

cd flight-price-prediction

3. Install the required libraries

pip install -r requirements.txt

4. Run the Streamlit application

python -m streamlit run app.py

The application will open in your browser.

---

## Conclusion

This project demonstrates the complete workflow of a Machine Learning regression project, starting from data preprocessing and feature engineering to model training, evaluation, pipeline creation, and deployment.

Among the tested models, Random Forest Regressor achieved the best performance with an R² score of approximately 0.9885 and an RMSE of approximately 2441.54.

The final model was integrated with Streamlit to create a simple and user-friendly Flight Price Prediction application.

---
