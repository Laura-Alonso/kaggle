# 👥🚪 Predict Customer Churn – Kaggle Playground Series S6E3

[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Playground%20Series%20S6E3-blue)](https://www.kaggle.com/competitions/playground-series-s6e3/overview)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🏆 Competition Overview

**Aim:**
Build a machine learning model that predicts the probability of **customer churn**.

**Dataset:**
The provided dataset contains **customer records** with features related to demographics, service usage, and account details.

**Problem Type:**
Binary classification problem - evaluated with **Area Under the Receiver Operating Characteristic Curve (AUC-ROC)**.

**Citation:**
> Yao Yan, Walter Reade, Elizabeth Park. *Predict Customer Churn*.
> [https://kaggle.com/competitions/playground-series-s6e3,](https://kaggle.com/competitions/playground-series-s6e3,), 2026. Kaggle.




## 📒 Notebook Information

**Objective:**
The goal of this project is to provide a clear and well-structured **exploratory analysis** of the variables involved in customer churn, with a strong emphasis on understanding their individual behavior and their relationship with the target variable.

Rather than testing multiple models, the focus is placed on building and deeply analyzing a single, powerful model — **CatBoost** — in order to better understand its behavior, strengths, and performance in a structured tabular classification setting.

**Structure:**
The notebook follows these main sections:

0. **Previous steps**

* 📚 **Libraries**. Importing required packages and setting configurations.
* 📂 **Data Loading and Preparation**. Importing and inspecting datasets; preparing variables for analysis.

1. 🗂️ **Data structure**. General vision of dataasets.
2. 🔎 **Exploratory Data Analysis (EDA)**. Global overview, target distribution, feature inspection, interactions.
3. 🔧 **Feature Engineering**. Creating and transforming variables for model input.
4. ✂️ **Data preparation**. Train–Validation Split – Splitting data for model evaluation.
5. 🧠 **CatBoots**. Training, evaluate and make predictions using CatBoots model.
6. 🚀 **Submission**. Preparing the submission file.

📘 The full notebook is available on Kaggle:
🔗 [Predict Customer Churn - CatBoost (by Laura Alonso)](https://www.kaggle.com/code/lauraalonso/predict-customer-churn-catboost)




## 💾 Data Access

The dataset is hosted on Kaggle and must be downloaded directly through the Kaggle API or competition interface.

**Option 1** – Using Kaggle CLI

**Option 2** – Manual Download. https://www.kaggle.com/competitions/playground-series-s6e3/data




## ⚙️ Environment Setups

To reproduce the results, install dependencies from requirements.txt




## 📜 License

This project is released under the MIT License.
See the LICENSE file for more information.