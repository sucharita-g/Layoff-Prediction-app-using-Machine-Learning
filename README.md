# Layoff Prediction App Using Machine Learning

## Project Overview

This project builds a **Machine Learning model** to predict whether a company is likely to have layoffs based on various company features. It aims to help stakeholders assess the **risk of layoffs** early by analyzing company data such as industry, country, funding raised, company stage, and year.

***The project includes:***

⮞ Data exploration and preprocessing

⮞ Training a Random Forest classification model

⮞ Building a user-friendly web app using Streamlit for predictions

⮞ Deployment on Streamlit Cloud for easy access




---

##  Problem Statement

In recent years, layoffs across industries have increased due to economic uncertainty, market shifts, and organizational restructuring. However, early prediction of potential layoffs can help companies, employees, and policymakers take proactive measures. This project aims to build a machine learning-based system that predicts whether a company is likely to experience layoffs based on key features such as industry type, country of operation, funding stage, amount raised, and year. By analyzing historical layoff data, the model provides a data-driven prediction to assess the risk of layoffs in real time.

---

## Table of Contents

⬤ Project Overview

⬤ Dataset

⬤ Features Used

⬤ Machine Learning Model

⬤ How Prediction Works

⬤ Web Application

⬤ Installation & Usage

⬤ Deployment

⬤ Folder Structure

⬤ Future Enhancements

⬤ Author



### Dataset

The dataset consists of company information related to layoffs, collected from various sources. The data includes:

➤ Industry type (e.g., AI, Finance, Healthcare)

➤ Country of operation

➤ Amount of funding raised (in millions)

➤ Company stage (Seed, Series A, IPO, etc.)

➤ Year of data capture

➤ Layoff status (target variable)

The raw data was cleaned, encoded, and processed for use in the model.


---

### Features Used


| Feature Name | Description                                | Type                  |
|--------------|--------------------------------------------|-----------------------|
| Industry     | Sector the company operates in             | Categorical (Encoded) |
| Country      | Country where the company is located       | Categorical (Encoded) |
| Raised       | Total funding raised (in millions USD)     | Numerical             |
| Stage        | Company development stage                  | Categorical (Encoded) |
| Year         | Year of the record/data                    | Numerical             |



---

## Machine Learning Model
✦ **Algorithm**: Random Forest Classifier

✦ **Reason**: Robust to overfitting, handles categorical + numerical data well, interpretable, and efficient.

✦ **Training**: Used the processed dataset with encoded categorical variables.

✦ **Evaluation**: Model accuracy and other metrics were evaluated on a test set to ensure reliable predictions.


---

##  How Prediction Works

When a user inputs company features in the web app:

1. The app converts string inputs (like industry name) to the encoded numeric values expected by the model.
2. These values are combined into a feature array.
3. The trained Random Forest model predicts if layoffs are likely (`1`) or not (`0`).
4. The app displays a clear message:
   - ⚠️ **High Risk: Layoff is likely.**
   - ✅ **Good News: Layoff is not likely.**


### Web Application

- Built using **Streamlit** — a lightweight Python framework for data apps.
- User interface elements include dropdowns for **Industry**, **Country**, and **Stage**, and numeric inputs for **Funding Raised** and **Year**.
- Real-time prediction triggered by a **button click**, displaying clear risk alerts.
- Designed with a **minimalistic, user-friendly interface** for quick insights.

## Installation & Usage

### Prerequisites
- Python 3.7 or higher
- `pip` package manager

### Clone the repo

git clone https://github.com/sucharita-g/Layoff-Prediction-app-using-Machine-Learning.git

cd Layoff-Prediction-app-using-Machine-Learning

### Install dependencies
pip install -r requirements.txt

### Run the app locally
streamlit run app/app.py
---

## Deployment

- Deployed on **Streamlit Cloud** for public access.
- **Live Demo**: [Layoff Prediction App](https://layoff-prediction-app-using-machine-learning-nde2zbgbcbheaf9eu.streamlit.app/)

### Deployment Steps

- Push your full codebase to **GitHub**.
- Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub repo.
- Make sure the model file (`random_forest_model.pkl`) and any required datasets are included in the repository.

---
### Folder Structure

Layoff-Prediction-app-using-Machine-Learning/
├── app/
│   └── app.py                     # Main Streamlit app code
├── data/
│   ├── layoffs_raw.csv            # Raw dataset
│   └── layoffs_cleaned.csv        # Cleaned dataset used for training
├── models/
│   └── random_forest_model.pkl    # Trained Random Forest model saved with joblib
├── notebooks/
│   └── layoff_eda_modeling.ipynb # Jupyter notebook for EDA & modeling
├── requirements.txt               # Required Python packages
├── README.md                     # This file
└── .gitignore                    # Git ignore file


---
## Future Enhancements

- Add more features such as employee count, revenue, or market trends  
- Implement advanced ML models or ensemble methods  
- Add explainability features like SHAP or LIME to interpret predictions  
- Improve UI with more interactive visualization and better styling  
- Add authentication and user data saving for personalized predictions  

---
## Author

**Sucharita G**  
🔗 GitHub: [sucharita-g](https://github.com/sucharita-g)  
🔗 LinkedIn: [linkedin.com/in/sucharita-g](https://linkedin.com/in/sucharita-g)


