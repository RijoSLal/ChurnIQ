# ChurnIQ - Customer Churn Prediction

ChurnIQ is a Streamlit app that predicts customer churn based on inputted customer details. Using a trained machine learning model, it helps businesses anticipate whether customers will stay or leave
Here's a sample README for your Streamlit application:

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Training](#model-training)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)

## Overview
This application is built to predict customer churn based on customer demographics, account information, and usage patterns. It uses a machine learning model trained in Jupyter Notebook and saved with `joblib`. This model is deployed within a Streamlit interface to make it accessible for non-technical users.

## Features
- Interactive form to collect customer information.
- Predictions based on various customer attributes (demographics, tenure, billing details, and service usage).
- Clear visual output indicating if a customer is likely to leave (churn) or stay.

## Installation

### Prerequisites
- Python 3.8+
- Streamlit
- joblib
- pandas

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ChurnIQ.git
   cd ChurnIQ
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your browser as directed by Streamlit.
2. Enter customer details such as gender, age, tenure, internet service, monthly charges, etc.
3. Click on the "Predict" button to get the churn prediction.
4. The application will display whether the customer is likely to "stay" or "leave."

## Model Training
The machine learning model used in ChurnIQ was trained using a Jupyter Notebook and saved as `model.joblib`. Key steps in the model training include:
- **Data Preprocessing**: Handling missing values, encoding categorical features, and feature scaling.
- **Model Selection**: Testing multiple algorithms and selecting the best-performing model based on accuracy and recall metrics.
- **Evaluation**: Using metrics like accuracy, precision, recall, and F1-score to evaluate the model performance.

The training notebook and additional details on model training are available in this repository.

## Technologies Used
- **Python**: Programming language
- **Streamlit**: Web framework for building interactive applications
- **joblib**: For model serialization
- **pandas**: Data manipulation library
- **scikit-learn**: For model building and evaluation

## Contributing
Feel free to fork the repository and make pull requests with improvements or new features.



