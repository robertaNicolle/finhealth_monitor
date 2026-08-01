from pydantic import BaseModel

class OverviewMetrics(BaseModel):
    month: str
    revenue: float
    transaction_volume: float
    total_transactions: int
    fraud_rate: float
    anomaly_rate: float
    new_customers: int
    churn_rate: float
    cac: float
    ltv: float
    active_customers: int