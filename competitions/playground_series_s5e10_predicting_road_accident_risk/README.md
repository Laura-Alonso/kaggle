# 🛣️ Road Accident Risk Prediction – Kaggle Playground Series S5E10

[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Playground%20Series%20S5E10-blue)](https://www.kaggle.com/competitions/playground-series-s5e10)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🏆 Competition Overview

**Aim:**
Build a machine learning model that predicts the **risk of road accidents**.

**Dataset:**
The dataset provides information about **road conditions, traffic signs, weather, lighting**, and other contextual features affecting road safety.

**Problem Type:**
Regression task — evaluated using the **Root Mean Squared Error (RMSE)** metric.

**Citation:**
> Walter Reade and Elizabeth Park. *Predicting Road Accident Risk.*
> [https://www.kaggle.com/competitions/playground-series-s5e10](https://www.kaggle.com/competitions/playground-series-s5e10), 2025. Kaggle.




## 📒 Notebook Information

**Objective:**
The goal of this project is to provide a clear and well-structured approach to the competition, explaining every decision regarding feature selection, preprocessing, and model training.
Each step is carefully documented to ensure full transparency and reproducibility.

**Structure:**
The notebook follows these main sections:

1. 📚 **Libraries** – Importing required packages and setting configurations.
2. 📂 **Data Loading and Preparation** – Importing and inspecting datasets; preparing variables for analysis.
3. 🔎 **Exploratory Data Analysis (EDA)** – Global overview, target distribution, feature inspection, interactions, and dataset drift check.
4. 🔧 **Feature Engineering** – Creating and transforming variables for model input.
5. ✂️ **Train–Validation Split** – Splitting data for model evaluation.
6. 🧠 **Model Training** – Training multiple algorithms (Linear Regression, Random Forest, XGBoost) with and without interaction features.
7. 📊 **Results Comparison** – Evaluating models via RMSE and selecting the best configuration.
8. 🚀 **Final Prediction & Submission** – Training the final model on full data and preparing the submission file.

📘 The full notebook is available on Kaggle:
🔗 [Road Accident Risk – XGBoost (by Laura Alonso)](https://www.kaggle.com/code/lauraalonso/road-accident-risk-xgboost)




## 💾 Data Access

The dataset is hosted on Kaggle and must be downloaded directly through the Kaggle API or competition interface.

**Option 1** – Using Kaggle CLI

**Option 2** – Manual Download. https://www.kaggle.com/competitions/playground-series-s5e10/data




## ⚙️ Environment Setups

To reproduce the results, install dependencies from requirements.txt




## 📜 License

This project is released under the MIT License.
See the LICENSE file for more information.