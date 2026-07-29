from pydantic import BaseModel


class AnomalySummary(BaseModel):
    total_transactions: int
    anomaly_transactions: int
    anomaly_rate: float
    fraud_transactions: int
    isolation_forest_alerts: int
    zscore_alerts: int
    rule_based_alerts: int