# 💼 Layoff Prediction App using Machine Learning

## 📌 Overview

This project aims to predict whether a company is likely to lay off employees based on historical layoff data and company-related features such as **industry**, **country**, **funding stage**, **year**, and **investment raised**. The prediction is powered by a machine learning model and served through an interactive **Streamlit** web application with a clean, AI-themed UI.

---

## 🧠 Problem Statement

Layoffs have a significant impact on companies and employees. Being able to predict layoffs can help stakeholders make data-driven decisions in advance. Our goal is to analyze patterns in past layoffs and build a model that predicts the **likelihood of layoffs** for given company parameters.

---

## 📊 Dataset

- **Source**: Kaggle (Layoff dataset)
- **Raw file**: `data/layoffs_raw.csv`
- **Cleaned file**: `data/layoffs_cleaned.csv`

### 🔑 Key Features Used:

| Feature Name    | Description |
|----------------|-------------|
| `Industry`      | Encoded industry type (e.g., AI, Retail, Finance) |
| `Country`       | Encoded country of the company |
| `$ Raised (mm)` | Investment raised in millions |
| `Stage`         | Funding stage (e.g., Seed, Series A, IPO) |
| `year`          | Year of data record |
| `will_layoff`   | Target: 1 = Layoff occurred, 0 = No layoff |

---

## 🛠️ Data Preprocessing

Performed in `notebooks/layoff_eda_modeling.ipynb`:

- Removed missing or irrelevant entries
- Encoded categorical variables (Industry, Country, Stage) using `LabelEncoder`
- Feature engineering
- Scaling numerical features
- Handled class imbalance using **SMOTE**
- Split into train-test sets
- Evaluated using **accuracy**, **precision**, **confusion matrix**

---

## 🤖 Model Training

- **Model Used**: XGBoost Classifier
- **Accuracy Achieved**: ~65% (on imbalanced real-world data)
- Saved model: `models/layoff_model.pkl`

---

## 🌐 Streamlit App

All UI logic is written in:  
`app/app.py`

### ✅ Features:

- User-friendly input fields with dropdowns for industry, country, stage
- Backend model prediction using real-time user input
- Clear output messages (Layoff Likely / Not Likely)
- Beautiful, compact UI with custom CSS (`app/style.css`)

### 🧠 How Prediction Works:

Inputs from user like:
- Industry (e.g., AI)
- Country (e.g., USA)
- Stage (e.g., Series A)
- Investment (e.g., $100 million)
- Year (e.g., 2023)

These are encoded and passed to the ML model, which then outputs whether the company is likely to **lay off** employees.

---

## 🧪 How to Run Locally

### 🔧 Setup

1. **Clone the Repo**
   ```bash
   git clone https://github.com/yourusername/layoff-predictor-app.git
   cd layoff-predictor-app
