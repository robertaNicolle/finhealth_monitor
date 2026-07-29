from pydantic import BaseModel


class OverviewMetrics(BaseModel):

    total_customers: int

    total_transactions: int

    transaction_volume: float

    total_revenue: float

    avg_transaction_value: float

    fraud_rate: float
    