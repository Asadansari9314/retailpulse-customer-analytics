📊 RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

An end-to-end retail analytics and machine learning project designed to analyze customer behavior, forecast sales, evaluate churn risk, and support inventory replenishment decisions.

**Live Dashboard:** [https://retailpulse-customer-analytics.streamlit.app/](https://retailpulse-customer-analytics.streamlit.app/)
**GitHub Repository:** [https://github.com/Asadansari9314/retailpulse-customer-analytics](https://github.com/Asadansari9314/retailpulse-customer-analytics)

---

🚀 Project Overview

RetailPulse is an AI-powered customer analytics platform that combines data analysis, machine learning, forecasting, and interactive visualization to support retail business decisions.

The project focuses on understanding sales trends, identifying customer segments, evaluating potential churn, forecasting demand, and generating inventory reorder recommendations.

It also includes model experiment tracking and data drift monitoring to demonstrate important aspects of a practical machine learning workflow.

🎯 Business Problems

Retail businesses face several challenges:

- Difficulty understanding sales trends and future demand.
- Limited visibility into customer purchasing behavior.
- Challenges identifying customers at potential churn risk.
- Inventory shortages and excess stock.
- Difficulty monitoring changes in incoming data.

RetailPulse addresses these challenges through analytics and machine learning techniques.

✨ Key Modules

### 1. Sales Analysis and Data Quality Audit

- Analyzes sales transactions and revenue trends.
- Checks missing values, duplicates, and data inconsistencies.
- Generates business-oriented sales summaries.

### 2. RFM Customer Segmentation

- Uses Recency, Frequency, and Monetary analysis.
- Applies K-Means clustering to identify customer groups.
- Helps understand customer purchasing patterns.

### 3. Sales Forecasting

- Uses Facebook Prophet for time-series forecasting.
- Analyzes historical sales patterns.
- Generates a 30-day forecast for the original forecasting experiment.

### 4. Churn Prediction and SHAP Analysis

- Uses XGBoost to evaluate potential customer churn risk.
- Evaluates model performance using classification metrics and ROC-AUC.
- Uses SHAP to interpret feature contributions.

### 5. Inventory Reorder Recommendations

- Analyzes stock availability and demand risk.
- Identifies critical and reorder stock.
- Calculates recommended replenishment quantities.

### 6. Data Drift Monitoring

- Uses Population Stability Index (PSI) to monitor changes in input feature distributions.
- Helps identify potential changes in incoming data.

### 7. MLflow Experiment Tracking

- Tracks machine learning experiments.
- Supports model performance comparison and experiment management.

### 8. Streamlit Dashboard

- Provides an interactive interface for project insights.
- Includes sales forecasting, customer analytics, churn analysis, and inventory analytics.

🛠  Technology Stack

| Technology          | Purpose                                |
| ------------------- | -------------------------------------- |
| Python              | Main programming language              |
| Pandas, NumPy       | Data cleaning and manipulation         |
| Matplotlib, Seaborn | Data visualization                     |
| Scikit-learn        | K-Means and machine learning utilities |
| XGBoost             | Churn prediction                       |
| Prophet             | Time-series forecasting                |
| SHAP                | Model explainability                   |
| MLflow              | Experiment tracking                    |
| Streamlit           | Interactive dashboard                  |
| Jupyter Notebook    | Data analysis and experimentation      |

## Dataset Overview

The project works with retail sales, customer, product, store, promotion, and inventory data.

| Dataset Component  | Records / Details |
| ------------------ | ----------------: |
| Customer Master    |  10,000 customers |
| Inventory Snapshot |    21,228 records |
| Product Master     |    5,000 products |
| Sales Transactions | 1,048,575 records |

*Record counts reflect the project dataset used during analysis.*

## Key Results

### Customer Segmentation

- Analyzed 10,000 customers.
- Identified 6 customer segments using RFM and K-Means.

### Sales Forecasting

- Prophet model evaluation:
  - MAPE: 8.50%
  - MAE: 102,128
  - RMSE: 124,515

### Churn Prediction

- Model: XGBoost
- ROC-AUC: 0.777
- Precision\@Top20%: 0.082 (8.2%)

### Inventory Analysis

- Total inventory records: 21,228
- Critical stock records: 3,888
- Reorder stock records: 1,974
- Recommended order quantity: 77,166 units

### Data Drift Monitoring

PSI results for selected input features:

| Feature     |    PSI |
| ----------- | -----: |
| Quantity    | 0.0000 |
| Unit Price  | 0.0002 |
| Total Value | 0.0016 |

These PSI values indicate low distribution change for the listed features in the evaluated comparison.

## Important Limitations

- Churn labels are based on purchase inactivity and represent a churn proxy, not verified customer cancellations.
- The current churn model ROC-AUC of 0.777 and Precision\@Top20% of 0.082 do not meet the project targets of 0.88 and 0.75, respectively.
- Forecasting source data ends on 2025-12-31. The generated 30-day forecast relates to January 2026 and is historical as of October 2026.
- PSI measures changes in input data distributions; it does not measure model accuracy or guarantee model performance.
- Model predictions should be validated before being used for real business decisions.

## Project Structure

```text
retailpulse-customer-analytics/
│
├── app.py
├── README.md
├── requirements.txt
│
├── notebooks/
│   └── RetailPulse_Analysis.ipynb
│
├── reports/
│   ├── customer_rfm.csv
│   ├── segment_summary.csv
│   ├── monthly_sales_summary.csv
│   ├── future_sales_forecast_prophet.csv
│   ├── demand_based_inventory.csv
│   ├── xgboost_churn_predictions.csv
│   └── data_drift_report.csv
│
└── screenshots/
    ├── overview.png
    ├── sales_forecast.png
    ├── customer_analytics.png
    ├── churn_analysis.png
    └── inventory_analytics.png
```

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Asadansari9314/retailpulse-customer-analytics.git
```

### 2. Open the project folder

```bash
cd retailpulse-customer-analytics
```

### 3. Activate your project environment

```bash
conda activate data
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit dashboard

```bash
python -m streamlit run app.py
```

---

## Conclusion

RetailPulse demonstrates an end-to-end retail analytics workflow, combining data quality checks, customer segmentation, sales forecasting, churn evaluation, inventory recommendations, and interactive dashboard development.

The project highlights practical applications of Python, machine learning, time-series forecasting, model explainability, and experiment tracking to support data-driven retail decisions.

---

## 👩‍💻 Author

**Md Asad Ansari**

Computer Science & Engineering Student
**Data Analyst | Data Science Enthusiast | Machine Learning

### Skills

- Python
- SQL
- Excel
- Power BI
- Pandas and NumPy
- Matplotlib and Seaborn
- Data Cleaning and Exploratory Data Analysis (EDA)
- Data Visualization and Dashboard Development
- Machine Learning
- Statistical Analysis

### Areas of Interest

- Data Analytics
- Business Intelligence
- Data Science
- Machine Learning
- Business and Customer Analytics

---

## 📜 License

This project is developed for:

- Educational Purpose
- Portfolio Showcase
- Zidio Data Science & Analytics Submission

---

⭐ If you found this project useful, consider giving it a star!

