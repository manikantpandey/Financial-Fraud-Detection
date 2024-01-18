# Rock Fraud Detection System
## Overview
Welcome to Rock, Your Guardian Against Fraud! This Fraud Detection System is designed to help users identify and prevent potential fraud in their transactions. Whether you want to analyze overall data, upload a dataset for analysis, or search for specific transactions, Rock has got you covered.

# Table of Contents
1. Introduction
2. Features
3. About Dataset
4. Installation
5. Usage
6. Contributing
7. License

# Features 
Effortless CSV Upload:

- Upload transaction data in CSV format for analysis.
Smart Random Forest Algorithm:

- Detect unusual patterns and potential fraud using a Random Forest model.
Quick Search:

- Search for transactions by MerchantID or CustomerID.
Detailed Analysis:

- View detailed statistics and predictions for uploaded datasets.
# Financial Fraud Detection Dataset Stracture

## 🔒 Dataset Description
The Financial Fraud Detection Dataset contains data related to financial transactions and fraudulent patterns. It is designed for the purpose of training and evaluating machine learning models for fraud detection.

## 📁 Dataset Structure
The dataset is organized within the "data" folder and consists of several subfolders, each containing CSV files with specific information related to financial transactions, customer profiles, fraudulent patterns, transaction amounts, and merchant information. The dataset structure is as follows:

### 📂 data
#### 📂 Transaction Data
- `transaction_records.csv`: Contains transaction records with details such as transaction ID, date, amount, and customer ID.
- `transaction_metadata.csv`: Contains additional metadata for each transaction.

#### 📂 Customer Profiles
- `customer_data.csv`: Includes customer profiles with information such as name, age, address, and contact details.
- `account_activity.csv`: Provides details of customer account activity, including account balance, transaction history, and account status.

#### 📂 Fraudulent Patterns
- `fraud_indicators.csv`: Contains indicators of fraudulent patterns and suspicious activities.
- `suspicious_activity.csv`: Provides specific details of transactions flagged as suspicious.

#### 📂 Transaction Amounts
- `amount_data.csv`: Includes transaction amounts for each transaction.
- `anomaly_scores.csv`: Provides anomaly scores for transaction amounts, indicating potential fraudulence.

#### 📂 Merchant Information
- `merchant_data.csv`: Contains information about merchants involved in transactions.
- `transaction_category_labels.csv`: Provides category labels for different transaction types.

### 📂 src
- `data.py`: Python file containing code to generate the dataset based on real-world data.

# Installation 
To use Rock Fraud Detection System, follow these steps:

1. Clone the repository:
```
git clone https://github.com/manikantpandey/RJPOLICE_HACK_620_Phoenix_7.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
streamlit run app.py
```
4. Access the system in your web browser


# Usage 
1. Home:

- Read the welcome message and explore key features.
2. Upload Data File:

- Upload a CSV file for analysis.
Explore detailed statistics and predicted frauds.
3. Search:

- Upload a CSV file to search for specific transactions.
Choose between searching by CustomerID or MerchantID.

# Contributing
Contributions are welcome! If you have ideas for improvements or find issues, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.
