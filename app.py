
from pathlib import Path
import pandas as pd
import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="RetailPulse Analytics",
    page_icon="📊",
    layout="wide"
)

BASE = Path(r"C:\Users\asada\RetailPulse_Final\reports")


@st.cache_data
def load_file(filename):
    path = BASE / filename
    if not path.exists():
        return pd.DataFrame()

    df = pd.read_csv(path)
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df


rfm = load_file("customer_rfm.csv")
segments = load_file("segment_summary.csv")
monthly = load_file("monthly_sales_summary.csv")
forecast = load_file("future_sales_forecast_prophet.csv")
inventory = load_file("demand_based_inventory.csv")
churn = load_file("xgboost_churn_predictions.csv")

st.title("📊 RetailPulse Analytics Platform")
st.caption(
    "Customer Segmentation | Sales Forecasting | "
    "Churn Analytics | Inventory Optimization"
)

# ---------------- OVERVIEW ----------------
total_customers = len(rfm)
total_inventory = len(inventory)
total_sales = (
    pd.to_numeric(monthly["sales"], errors="coerce").sum()
    if "sales" in monthly.columns else 0
)
high_risk = (
    int((churn["predicted_churn"] == 1).sum())
    if "predicted_churn" in churn.columns else 0
)

a, b, c, d = st.columns(4)
a.metric("Total Customers", f"{total_customers:,}")
b.metric("Total Sales", f"₹{total_sales:,.0f}")
c.metric("Inventory Records", f"{total_inventory:,}")
d.metric("Predicted High-Risk Customers", f"{high_risk:,}")

st.divider()

tabs = st.tabs([
    "🏠 Overview",
    "📈 Sales & Forecast",
    "👥 Customer Analytics",
    "⚠️ Churn Analysis",
    "📦 Inventory Analytics"
])

# ---------------- 1. OVERVIEW ----------------
with tabs[0]:
    st.subheader("Business Performance Overview")

    left, right = st.columns(2)

    with left:
        st.write("Monthly Sales Trend")
        if {"month", "sales"}.issubset(monthly.columns):
            m = monthly.copy()
            m["month"] = pd.to_datetime(m["month"], errors="coerce")
            m["sales"] = pd.to_numeric(m["sales"], errors="coerce")
            m = m.dropna(subset=["month", "sales"]).sort_values("month")
            if not m.empty:
                st.line_chart(m.set_index("month")[["sales"]])

    with right:
        st.write("Customer Segment Distribution")
        if {"segment", "customers"}.issubset(segments.columns):
            s = segments.copy()
            s["customers"] = pd.to_numeric(
                s["customers"], errors="coerce"
            )
            s = s.dropna(subset=["customers"])
            if not s.empty:
                st.bar_chart(s.set_index("segment")[["customers"]])

    st.write("Monthly Sales and Quantity")
    if {"month", "sales", "quantity"}.issubset(monthly.columns):
        m = monthly.copy()
        m["month"] = pd.to_datetime(m["month"], errors="coerce")
        for col in ["sales", "quantity"]:
            m[col] = pd.to_numeric(m[col], errors="coerce")
        m = m.dropna(subset=["month"]).sort_values("month")
        if not m.empty:
            st.line_chart(m.set_index("month")[["quantity"]])

    if monthly.empty:
        st.warning("Monthly sales report nahi mili.")

# ---------------- 2. SALES & FORECAST ----------------
with tabs[1]:
    st.subheader("Historical Sales Analysis")

    if {"month", "sales"}.issubset(monthly.columns):
        m = monthly.copy()
        m["month"] = pd.to_datetime(m["month"], errors="coerce")
        for col in ["sales", "quantity", "transactions"]:
            if col in m.columns:
                m[col] = pd.to_numeric(m[col], errors="coerce")
        m = m.dropna(subset=["month"]).sort_values("month")

        x, y = st.columns(2)
        with x:
            st.write("Monthly Revenue")
            st.line_chart(m.set_index("month")[["sales"]])
        with y:
            if "transactions" in m.columns:
                st.write("Monthly Transactions")
                st.bar_chart(m.set_index("month")[["transactions"]])

        st.write("Monthly Sales Data")
        st.dataframe(m, use_container_width=True)

    st.divider()
    st.subheader("Sales Forecast")

    if {"ds", "yhat"}.issubset(forecast.columns):
        f = forecast.copy()
        f["ds"] = pd.to_datetime(f["ds"], errors="coerce")
        f["yhat"] = pd.to_numeric(f["yhat"], errors="coerce")
        f = f.dropna(subset=["ds", "yhat"]).sort_values("ds")

        if not f.empty:
            st.line_chart(f.set_index("ds")[["yhat"]])
            st.dataframe(f, use_container_width=True)
            st.info(
                "Forecast ki dates verify karein. Existing report "
                "January 2026 ki hai, isliye ise current future forecast "
                "mat samjhein."
            )
    else:
        st.warning("Forecast report mein ds/yhat columns nahi mile.")

# ---------------- 3. CUSTOMER ANALYTICS ----------------
with tabs[2]:
    st.subheader("Customer Segmentation")

    if {"segment", "customers"}.issubset(segments.columns):
        s = segments.copy()
        s["customers"] = pd.to_numeric(s["customers"], errors="coerce")
        for col in ["avg_recency", "avg_frequency", "avg_monetary"]:
            if col in s.columns:
                s[col] = pd.to_numeric(s[col], errors="coerce")

        left, right = st.columns(2)
        with left:
            st.write("Customers by Segment")
            st.bar_chart(s.set_index("segment")[["customers"]])

        with right:
            if "avg_monetary" in s.columns:
                st.write("Average Monetary Value by Segment")
                st.bar_chart(s.set_index("segment")[["avg_monetary"]])

        if {"avg_recency", "avg_frequency"}.issubset(s.columns):
            st.write("Segment Recency vs Frequency")
            st.scatter_chart(
                s,
                x="avg_recency",
                y="avg_frequency",
                size="customers",
                color="segment"
            )

        st.dataframe(s, use_container_width=True)
    else:
        st.warning("Segment summary mein required columns nahi mile.")

    st.divider()
    st.subheader("RFM Customer Analysis")

    if not rfm.empty:
        left, right = st.columns(2)

        with left:
            if "recency" in rfm.columns:
                st.write("Customer Recency Distribution")
                st.bar_chart(
                    rfm["recency"].dropna().value_counts(
                        bins=10, sort=False
                    ).sort_index()
                )

        with right:
            if "monetary" in rfm.columns:
                st.write("Customer Spending Distribution")
                st.bar_chart(
                    rfm["monetary"].dropna().value_counts(
                        bins=10, sort=False
                    ).sort_index()
                )

        if {"frequency", "monetary"}.issubset(rfm.columns):
            st.write("Purchase Frequency vs Spending")
            st.scatter_chart(
                rfm,
                x="frequency",
                y="monetary",
                color="segment" if "segment" in rfm.columns else None
            )

        st.write("Customer RFM Details")
        st.dataframe(rfm.head(100), use_container_width=True)

# ---------------- 4. CHURN ANALYSIS ----------------
with tabs[3]:
    st.subheader("Customer Churn Risk")

    if "churn_probability" in churn.columns:
        ch = churn.copy()
        ch["churn_probability"] = pd.to_numeric(
            ch["churn_probability"], errors="coerce"
        )
        ch = ch.dropna(subset=["churn_probability"])
        ch["churn_probability"] = ch["churn_probability"].clip(0, 1)

        ch["risk_level"] = pd.cut(
            ch["churn_probability"],
            bins=[-0.001, 0.30, 0.60, 1.0],
            labels=["Low Risk", "Medium Risk", "High Risk"]
        )

        left, right = st.columns(2)

        with left:
            st.write("Churn Probability Distribution")
            st.bar_chart(
                ch["churn_probability"].value_counts(
                    bins=10, sort=False
                ).sort_index()
            )

        with right:
            st.write("Customers by Risk Level")
            st.bar_chart(
                ch["risk_level"].value_counts().reindex(
                    ["Low Risk", "Medium Risk", "High Risk"],
                    fill_value=0
                )
            )

        if {"actual_churn", "predicted_churn"}.issubset(ch.columns):
            st.write("Actual vs Predicted Churn")
            comparison = pd.crosstab(
                ch["actual_churn"],
                ch["predicted_churn"]
            )
            st.dataframe(comparison, use_container_width=True)
            st.bar_chart(comparison)

        st.write("Top 20 Customers by Churn Probability")
        st.dataframe(
            ch.sort_values("churn_probability", ascending=False).head(20),
            use_container_width=True
        )
    else:
        st.warning("Churn probability column nahi mili.")
        st.dataframe(churn.head(20), use_container_width=True)

# ---------------- 5. INVENTORY ANALYTICS ----------------
with tabs[4]:
    st.subheader("Inventory & Demand Analysis")

    if not inventory.empty:
        inv = inventory.copy()

        for col in [
            "stock_on_hand", "reorder_point", "safety_stock",
            "recommended_order_qty", "units_sold",
            "avg_daily_demand", "stock_coverage_days",
            "demand_based_order_qty", "unit_price"
        ]:
            if col in inv.columns:
                inv[col] = pd.to_numeric(inv[col], errors="coerce")

        left, right = st.columns(2)

        with left:
            st.write("Stock Status")
            if "stock_status" in inv.columns:
                st.bar_chart(inv["stock_status"].value_counts())

        with right:
            st.write("Demand Risk")
            if "demand_risk" in inv.columns:
                st.bar_chart(inv["demand_risk"].value_counts())

        left, right = st.columns(2)

        with left:
            st.write("Top Categories by Recommended Order")
            if {"category", "demand_based_order_qty"}.issubset(inv.columns):
                cat = (
                    inv.groupby("category")["demand_based_order_qty"]
                    .sum().sort_values(ascending=False).head(10)
                )
                st.bar_chart(cat)

        with right:
            st.write("Top 10 Products to Reorder")
            if {"sku_name", "demand_based_order_qty"}.issubset(inv.columns):
                top = (
                    inv.groupby("sku_name")["demand_based_order_qty"]
                    .sum().sort_values(ascending=False).head(10)
                )
                st.bar_chart(top)

        if {"stock_on_hand", "reorder_point"}.issubset(inv.columns):
            st.write("Current Stock vs Reorder Point")
            sample = inv.dropna(
                subset=["stock_on_hand", "reorder_point"]
            ).head(20)
            if not sample.empty:
                st.bar_chart(
                    sample.set_index("sku_id")[
                        ["stock_on_hand", "reorder_point"]
                    ] if "sku_id" in sample.columns else
                    sample[["stock_on_hand", "reorder_point"]]
                )

        st.write("Inventory What-If Analysis")
        if {
            "avg_daily_demand", "safety_stock", "stock_on_hand"
        }.issubset(inv.columns):
            days = st.slider(
                "Target stock coverage (days)", 7, 60, 30
            )
            inv["what_if_order_qty"] = (
                inv["avg_daily_demand"].fillna(0) * days
                + inv["safety_stock"].fillna(0)
                - inv["stock_on_hand"].fillna(0)
            ).clip(lower=0).round().astype(int)

            st.metric(
                "Suggested Order Units",
                f"{inv['what_if_order_qty'].sum():,}"
            )
            st.dataframe(
                inv.sort_values(
                    "what_if_order_qty", ascending=False
                ).head(20),
                use_container_width=True
            )
        else:
            st.info("What-if calculation ke liye demand/stock columns nahi mile.")

        st.write("Complete Inventory Table")
        st.dataframe(inv.head(200), use_container_width=True)
    else:
        st.warning("Inventory report nahi mili. Reports folder check karo.")

st.divider()
st.caption("RetailPulse | Analytics Dashboard")
