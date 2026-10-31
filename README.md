# 📊 RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

> **Sales Forecasting • Customer Segmentation • Churn Analysis • Inventory Optimization • Data Drift Monitoring**

RetailPulse is an end-to-end retail analytics and machine learning platform designed to help businesses understand customer behavior, analyze sales trends, forecast demand, evaluate customer churn risk, and make better inventory decisions.

🔗 **Live Dashboard:** [RetailPulse Dashboard](https://retailpulse-customer-analytics.streamlit.app/)

💻 **GitHub Repository:** [RetailPulse – GitHub](https://github.com/Asadansari9314/retailpulse-customer-analytics)

---

# 🚀 Project Overview

Retail businesses generate large amounts of sales, customer, and inventory data. However, converting this data into useful business insights can be challenging.

**RetailPulse** combines Data Analytics, Machine Learning, Time-Series Forecasting, and an interactive Streamlit dashboard to support data-driven retail decisions.

### 🎯 What RetailPulse Does

- 📈 Analyzes sales performance and trends.
- 👥 Identifies customer segments using RFM analysis.
- 🔮 Forecasts sales using Prophet.
- ⚠️ Evaluates customer churn risk using XGBoost.
- 📦 Generates inventory reorder recommendations.
- 🔍 Monitors input data distribution changes using PSI.
- 🧪 Tracks machine learning experiments using MLflow.
- 📊 Presents insights through an interactive dashboard.

---

# 🎯 Business Problem

Retail businesses commonly face challenges such as:

- Uncertainty in future sales demand.
- Difficulty understanding customer purchasing behavior.
- Customer inactivity and potential churn.
- Overstocking and stock shortages.
- Poor visibility into inventory performance.
- Difficulty monitoring changes in incoming data.

**RetailPulse addresses these challenges** by combining analytical techniques and machine learning models to generate useful business insights.

### 💡 Project Objectives

- Improve visibility into sales performance.
- Understand customer purchasing patterns.
- Identify customers with potential churn risk.
- Support demand forecasting and inventory planning.
- Monitor input data distribution changes.
- Present business insights through an interactive dashboard.

---

# ✨ Key Features & Modules

## 1️⃣ 📈 Sales Analysis & Data Quality Audit

Analyzes retail transactions to understand business performance and data quality.

**Key Activities:**

- Sales and revenue trend analysis.
- Missing value identification.
- Duplicate transaction detection.
- Data consistency checks.
- Monthly sales summaries.

## 2️⃣ 👥 Customer Segmentation – RFM + K-Means

Groups customers based on their purchasing behavior.

**Techniques Used:**

- Recency – How recently a customer purchased.
- Frequency – How frequently a customer purchased.
- Monetary – How much a customer spent.
- K-Means clustering.
- Customer segment analysis.

**Result:** Analyzed 10,000 customers and identified 6 customer segments.

## 3️⃣ 🔮 Sales Demand Forecasting – Prophet

Uses time-series forecasting to analyze historical sales patterns and estimate future sales.

**Model Used:**

- Facebook Prophet.

**Evaluation Metrics:**

| Metric |  Result |
| ------ | ------: |
| MAPE   |   8.50% |
| MAE    | 102,128 |
| RMSE   | 124,515 |

The original forecasting experiment generated a 30-day forecast for January 2026.

## 4️⃣ ⚠️ Customer Churn Prediction – XGBoost

Evaluates potential customer churn risk based on purchasing inactivity and customer behavior.

**Model Used:**

- XGBoost Classifier.

**Evaluation Results:**

| Metric            | Result |
| ----------------- | -----: |
| ROC-AUC           |  0.777 |
| Precision\@Top20% |   8.2% |

**Model Explainability:**

- SHAP analysis.
- Feature contribution analysis.
- Churn risk evaluation.

## 5️⃣ 📦 Inventory Reorder Recommendations

Analyzes inventory availability and demand risk to support replenishment decisions.

**Key Features:**

- Stock availability analysis.
- Critical stock identification.
- Reorder stock identification.
- Demand risk analysis.
- Recommended replenishment quantities.

**Inventory Results:**

| Metric                  | Result |
| ----------------------- | -----: |
| Inventory Records       | 21,228 |
| Sufficient Stock        | 15,366 |
| Critical Stock          |  3,888 |
| Reorder Stock           |  1,974 |
| Recommended Order Units | 77,166 |

## 6️⃣ 🔍 Data Drift Monitoring – PSI

Uses Population Stability Index (PSI) to monitor changes in selected input feature distributions.

**PSI Results:**

| Feature     |    PSI |
| ----------- | -----: |
| Quantity    | 0.0000 |
| Unit Price  | 0.0002 |
| Total Value | 0.0016 |

The evaluated features show low distribution change in the comparison performed.

## 7️⃣ 🧪 MLflow Experiment Tracking

Uses MLflow to organize and track machine learning experiments.

**Key Activities:**

- Experiment tracking.
- Model parameter logging.
- Performance metric tracking.
- Experiment comparison.

## 8️⃣ 📊 Interactive Streamlit Dashboard

Provides an interactive interface to explore RetailPulse analytics and model outputs.

**Dashboard Modules:**

- 📈 Sales & Forecasting
- 👥 Customer Analytics
- ⚠️ Churn Analysis
- 📦 Inventory Analytics

---

# 🏗️ Project Architecture

The following diagram represents the overall analytical workflow of RetailPulse.

```text
              📂 Retail Dataset
                     |
                     ▼
           🧹 Data Cleaning & Audit
                     |
                     ▼
            ⚙️ Data Preparation
                     |
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      👥 Customer  📈 Sales   📦 Inventory
      Analytics   Analysis   Analysis
          |          |          |
          ▼          ▼          ▼
      RFM +       Prophet    Reorder
      K-Means     Forecast   Analysis
          |          |          |
          ▼          ▼          |
      ⚠️ Churn      🔮 Sales     |
      Evaluation   Forecast     |
          |          |          |
          └──────────┼──────────┘
                     |
                     ▼
             🔍 PSI Monitoring
                     |
                     ▼
             🧪 MLflow Tracking
                     |
                     ▼
            📊 Streamlit Dashboard
                     |
                     ▼
              Business Insights
```

---

# 🛠️ Technology Stack

| Category                | Technologies          |
| ----------------------- | --------------------- |
| Programming Language    | Python                |
| Data Analysis           | Pandas, NumPy         |
| Data Visualization      | Matplotlib, Seaborn   |
| Machine Learning        | Scikit-learn, K-Means |
| Churn Prediction        | XGBoost               |
| Time-Series Forecasting | Prophet               |
| Model Explainability    | SHAP                  |
| Experiment Tracking     | MLflow                |
| Dashboard Development   | Streamlit             |
| Development Environment | Jupyter Notebook      |

---

# 📂 Dataset Overview

The project uses retail sales, customer, product, store, promotion, and inventory datasets.

| Dataset            |   Records |
| ------------------ | --------: |
| Customer Master    |    10,000 |
| Inventory Snapshot |    21,228 |
| Product Master     |     5,000 |
| Sales Transactions | 1,048,575 |

*Record counts represent the dataset used during project analysis.*

---

# 📊 Key Project Results

| Project Area          | Key Result                           |
| --------------------- | ------------------------------------ |
| Customer Analytics    | 10,000 customers analyzed            |
| Customer Segmentation | 6 segments identified                |
| Sales Forecasting     | Prophet MAPE: 8.50%                  |
| Churn Evaluation      | XGBoost ROC-AUC: 0.777               |
| Inventory Analysis    | 21,228 inventory records analyzed    |
| Inventory Planning    | 77,166 recommended order units       |
| Data Drift            | Low PSI for three evaluated features |

---

# ⚠️ Important Limitations

- Churn labels are based on purchase inactivity and represent a churn proxy, not verified customer cancellations.
- The current churn model ROC-AUC of 0.777 and Precision\@Top20% of 0.082 do not meet the project targets of 0.88 and 0.75, respectively.
- Forecasting source data ends on 2025-12-31. The generated 30-day forecast relates to January 2026 and is historical as of October 2026.
- PSI measures changes in input data distributions; it does not measure model accuracy or guarantee model performance.
- Model predictions and inventory recommendations should be validated before real-world business use.

---

# 📁 Project Structure

```text
retailpulse-customer-analytics/
│
├── 📄 app.py
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📊 customer_rfm.csv
├── 📊 segment_summary.csv
├── 📊 monthly_sales_summary.csv
├── 📊 future_sales_forecast_prophet.csv
├── 📊 demand_based_inventory.csv
├── 📊 xgboost_churn_predictions.csv
│
└── 📂 reports/
    └── 📊 data_drift_report.csv
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Asadansari9314/retailpulse-customer-analytics.git
```

## 2. Open the Project Folder

```bash
cd retailpulse-customer-analytics
```

## 3. Activate the Conda Environment

```bash
conda activate data
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

---

# 🔮 Future Improvements

- Improve churn prediction through better labels and feature engineering.
- Retrain forecasting models using newer sales data.
- Improve inventory planning with lead-time and safety-stock analysis.
- Add automated model monitoring and retraining workflows.
- Expand dashboard KPIs and business insights.
- Improve model evaluation and experiment management.

---

# 📚 Key Learnings

Through this project, I gained practical experience in:

- Retail data cleaning and exploratory data analysis.
- RFM analysis and customer segmentation.
- Time-series forecasting.
- Classification model evaluation.
- Model explainability using SHAP.
- Inventory analytics and reorder planning.
- Data drift monitoring using PSI.
- MLflow experiment tracking.
- Interactive dashboard development using Streamlit.

---

# 👨‍💻 Author

## **Md Asad Ansari**

**Final Year Computer Science & Engineering Student**

**Data Analyst | Data Science Enthusiast**

### 💻 Technical Skills

- Python
- SQL
- Microsoft Excel
- Power BI
- Pandas & NumPy
- Matplotlib & Seaborn
- Exploratory Data Analysis (EDA)
- Data Cleaning & Data Visualization
- Machine Learning
- Statistical Analysis

### 🎯 Areas of Interest

- Data Analytics
- Business Intelligence
- Data Science
- Machine Learning
- Customer Analytics

---

# 📜 License

This project is developed for:

- 🎓 Educational Purpose
- 💼 Portfolio Showcase
- 🏢 Zidio Data Science & Analytics Submission

---

⭐ **If you found this project useful, consider giving it a star!**
