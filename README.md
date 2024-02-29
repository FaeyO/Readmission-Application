# Hospital Patient Readmission App

## Table of Contents
  - Project Overview

  - Tools

  - Data Cleaning
    
  - Supervised Machine Learning

  - Deployment

### Project Overview
Hospital patient readmission refers to the scenario where a patient, who has recently been discharged from a hospital, returns to the same hospital for additional medical care within a specified time frame. Readmissions are often monitored as a key healthcare quality metric, and efforts are made to reduce them. High rates of readmission may indicate issues with the initial treatment, discharge process, or ongoing care. 
The Patient Readmission Application would help healthcare professional to quickly and easily detect patient that are at high risk for readmissions.

### Tools
 - MySQL workbench
 - Python - Data Analysis
 - Matplotlib - For Data Visualizations
 - Seaborn - For Data Visualizations
 - Numpy
 - Pandas
 - Scikit-learn
 - Jupyter notebook - Coding Environment
 - Vscode

### Data Cleaning
In the data preparation phase, i performed the following tasks;

1. Data loading
2. Data Validation
3. Data cleaning
4. Handling Missing Data

### Exploratory Data Analysis
EDA involved exploring the Patient Sleep Disorder Data to answer key questions such as;

 - What is the most common primary diagnosis by age group.
 - What is the effect of a diabetes diagnosis on readmission rates.
 - What groups of patients should the hospital focus their follow-up efforts to better monitor patients with a high probability of readmission?
 
### Supervised Machine Learning
Supervised machine learning is a type of machine learning where the algorithm is trained on a labeled dataset, meaning that the input data is paired with corresponding output labels. The goal of supervised learning is to learn a mapping or relationship between input features and their corresponding output labels, allowing the algorithm to make predictions or classifications on new, unseen data. .  RandomForest Classifier was used due to their effectiveness in classification tasks.

### Deployment
 - The model was saved as a pickle file for future use.
 - The application was developed using Streamlit for an interactive user interface.
 - To facilitate efficient execution, the application was deployed on GitHub.
​
