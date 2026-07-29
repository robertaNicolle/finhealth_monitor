from pydantic import BaseModel

class ForecastData(BaseModel):
    month: str
    revenue: float
    transaction_volume: float
    total_transactions: int
    fraud_rate: float
    anomaly_rate: float