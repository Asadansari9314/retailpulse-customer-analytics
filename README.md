# RetailPulse
AI-Powered Customer Analytics & Demand Forecasting Platform

## Modules
- Sales analysis and data quality audit
- RFM customer segmentation
- Sales forecasting using Prophet
- Churn prediction evaluation and SHAP analysis
- Inventory reorder recommendations
- Data drift monitoring using PSI
- MLflow experiment tracking
- Streamlit dashboard

## Important limitations
- Churn labels are based on purchase inactivity and are only a proxy.
- Current recorded churn metrics do not meet the target ROC-AUC of 0.88
  or Precision@Top20% of 0.75.
- Forecast source data ends on 2025-12-31. The generated 30-day forecast
  is historical relative to October 2026.
- PSI indicates input distribution change, not model accuracy.

## Run the dashboard
Open Anaconda Prompt and activate the environment used for the project.
Then run:
    python -m streamlit run C:\Users\asada\app.py

## MLflow UI
In the same environment, run:
    python -m mlflow ui

Then open http://localhost:5000
