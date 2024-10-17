# Automated-Expense-Categorization

develop an automated system that categorizes business expenses from accounts payable transaction history

## Project Overview

The Automated Expense Categorization System aims to streamline the bookkeeping process and enhance financial analysis accuracy for businesses by automating the categorization of business expenses based on accounts payable transaction history. This project addresses the inefficiencies and errors inherent in manual expense categorization and leverages machine learning (ML) to predict the appropriate Cost Centre for invoice approval, ultimately reducing time spent on administrative tasks and increasing the efficiency and accuracy of the financial reporting process.

## Ethical Considerations

The development and deployment of the Automated Expense Categorization System involved several ethical considerations to ensure privacy, fairness, and security. These considerations were carefully addressed during the project, as outlined below:

1. Data Privacy and Confidentiality:
All sensitive information was removed from the dataset before processing. Personally identifiable information (PII) was anonymized, and encoded variables were used to maintain confidentiality, ensuring that no individuals or organizations could be identified from the data.
2. Transparency and Accountability:
The system’s design and implementation prioritize transparency. The users are informed of how the system is used for automated categorization.
3. Security and Data Protection:
All data, even after being anonymized, is securely stored and encrypted to protect against unauthorized access or data breaches.

## Problem Statement

Finance teams spend significant time categorizing expenses manually, leading to:

* Time-consuming processes
* Human error
* Inefficiencies in financial reporting
* Delayed decision-making

As outlined in the use case: If an accounting clerk is responsible for processing 10,000 transaction lines per year, with an average of 12 minutes per line, reducing the processing time by 25% (to 9 minutes per transaction) could lead to annual savings of $12.5K. By automating the categorization process, the clerk would also have more time to focus on analyzing financial data, resulting in better decision-making and financial insight.

## Proposed Solution

An automated system based on machine learning models will predict the correct Cost Centre for each invoice based on transaction descriptions. This system uses historical transaction data to train models that can automate the categorization process, reducing both the time required and the potential for human error.

Key Technologies: Python, Pandas, Scikit-learn, TensorFlow, Streamlit.

## How the System Works

Input: Users upload or enter transaction data into the Streamlit-based interface.
Preprocessing: The system cleans and prepares the data for prediction, applying the same transformations used during the training phase.
Prediction: The selected machine learning model categorizes the transaction by predicting the department or project based on transaction descriptions.
Output: The system displays the predicted Cost Centre.

## Future Improvements

* Model Optimization: Additional hyperparameter tuning and model experimentation could further improve prediction accuracy.
* Integration with Existing Financial Systems: Integrating this tool with popular accounting software would make it more accessible to businesses.
