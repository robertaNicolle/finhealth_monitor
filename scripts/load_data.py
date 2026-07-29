import pandas as pd
from sqlalchemy import create_engine

# ======================
# DATABASE CONFIGURATION
# ======================

DB_USER = "postgres"
DB_PASSWORD = "88852229"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "finhealth_monitor"

# ======================
# CREATE CONNECTION
# ======================

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("Connected to PostgreSQL successfully!")

# ======================
# LOAD CSV FILES
# ======================

customers = pd.read_csv("data/customers.csv")
transactions = pd.read_csv("data/transactions.csv")
transaction_alerts = pd.read_csv("data/transaction_alerts.csv")
revenue_forecast = pd.read_csv("data/revenue_forecast.csv")
customer_metrics = pd.read_csv("data/customer_metrics.csv")
monthly_business_metrics = pd.read_csv("data/monthly_business_metrics.csv")

# ======================
# SEND TO POSTGRESQL
# ======================

customers.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("customers loaded")

transactions.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False,
    method="multi"
)

print("transactions loaded")

transaction_alerts.to_sql(
    "transaction_alerts",
    engine,
    if_exists="replace",
    index=False
)

print("transaction_alerts loaded")

revenue_forecast.to_sql(
    "revenue_forecast",
    engine,
    if_exists="replace",
    index=False
)

print("revenue_forecast loaded")

customer_metrics.to_sql(
    "customer_metrics",
    engine,
    if_exists="replace",
    index=False
)

print("customer_metrics loaded")

monthly_business_metrics.to_sql(
    "monthly_business_metrics",
    engine,
    if_exists="replace",
    index=False
)

print("monthly_business_metrics loaded")

print("\nAll tables loaded successfully!")