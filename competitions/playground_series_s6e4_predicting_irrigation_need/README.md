# 🌱💧 Predicting Irrigation Need – Kaggle Playground Series S6E4

[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Playground%20Series%20S6E3-blue)](https://www.kaggle.com/competitions/playground-series-s6e4/overview)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🏆 Competition Overview

**Aim:**
Build a machine learning model that predicts the **irrigation need level** of agricultural fields, classified as `Low`, `Medium`, or `High`

**Dataset:**
The provided dataset contains **agricultural field records** with features related to soil conditions, crop characteristics, climate variables, and farming practices.

**Problem Type:**
Multiclass classification problem — evaluated with **Balanced Accuracy**.

**Citation:**
> Yao Yan, Walter Reade, Elizabeth Park. *Predicting Irrigation Need*.
> [https://kaggle.com/competitions/playground-series-s6e4,](https://kaggle.com/competitions/playground-series-s6e4,), 2026. Kaggle.




## 📒 Notebook Information

**Objective:**
The goal of this project is to provide a clear and well-structured **exploratory analysis** of the variables involved in predicting irrigation need, with a strong emphasis on understanding their individual behavior and their relationship with the target variable.

We train and compare three powerful tree-based models, **XGBoost**, **LightGBM**, and **Random Forest**, evaluating their performance under stratified cross-validation and selecting the best one based on **balanced accuracy**, the official competition metric.

**Structure:**
The notebook follows these main sections:

1. 🗂️ **Data structure**.
    * **A. First steps**. Libraries and data loading.
    * **B. Quick overview**. Names, types and missing values.
    * **C. Character features**. Check which of them are categorical or binary and encoding
2. 🔎 **Exploratory Data Analysis (EDA)**.
    * **A. Target Variable - Irrigation Need**.
    * **B. Univariate & target-oriented analysis**. For each feature we explore its distribution and its relationship with Irrigation_Need.
    * **C. Multivariate feature analysis**.
3. 🔧 **Feature Engineering**.
4. ✂️ **Data preparation & preprocessing**. Resampling strategy.
5. 🧠 **Modeling**.
    * **A. Model specification**.
    * **B. Cross-validation evaluation**.
    * **C. Compare models**.
6. 🏆 **Final model**.     
7. 🚀 **Submission**.

📘 The full notebook is available on Kaggle:
🔗 [Predicting Irrigation Need - R code (by Laura Alonso)](https://www.kaggle.com/code/lauraalonso/predicting-irrigation-need-r-code)




## 💾 Data Access

The dataset is hosted on Kaggle and must be downloaded directly through the Kaggle API or competition interface.

**Option 1** – Using Kaggle CLI

**Option 2** – Manual Download. https://www.kaggle.com/competitions/playground-series-s6e4/data




## ⚙️ Environment Setups

To reproduce the results, install dependencies from requirements.txt




## 📜 License

This project is released under the MIT License.
See the LICENSE file for more information.