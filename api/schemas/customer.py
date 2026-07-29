from pydantic import BaseModel


class CustomerMetrics(BaseModel):

    customer_id: int
    total_transactions: int
    total_volume: float
    total_revenue: float
    avg_transaction_value: float
    fraud_transactions: int
    anomaly_transactions: int
    signup_date: str
    customer_segment: str
    acquisition_channel: str
    churn_flag: bool
    customer_age_days: int
    cac: float
    ltv: float