from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from services import get_overview_metrics
from schemas.overview import OverviewMetrics
from schemas.anomalies import AnomalySummary
from services import get_anomaly_summary
from typing import List
from schemas.customer import CustomerMetrics
from services import get_customer_metrics
from schemas.forecast import ForecastData
from services import get_forecast_data
from schemas.anomalies import AnomalySummary
from services import get_anomaly_summary
from services import test_claude
from services import get_llm_metrics
from services import generate_executive_summary
app = FastAPI(
    title="FinHealth Monitor API",
    description="Executive Analytics API for FinHealth Monitor",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "FinHealth Monitor",
        "status": "API is running successfully",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get(
    "/overview",
    response_model=OverviewMetrics,
    tags=["Business Metrics"],
    summary="Business Overview Metrics"
)
def overview(db: Session = Depends(get_db)):
    return get_overview_metrics(db)    
@app.get(
    "/anomalies",
    response_model=AnomalySummary,
    tags=["Anomaly Detection"],
    summary="Anomaly Detection Summary"
)
def anomalies(db: Session = Depends(get_db)):

    return get_anomaly_summary(db)

@app.get(
    "/customers",
    response_model=List[CustomerMetrics],
    tags=["Customers"],
    summary="Customer Metrics"
)
def customers(limit: int = 100, db: Session = Depends(get_db)):

    return get_customer_metrics(db, limit)

@app.get(
    "/forecast",
    response_model=List[ForecastData],
    tags=["Forecast"],
    summary="Revenue Forecast Data"
)
def forecast(db: Session = Depends(get_db)):

    return get_forecast_data(db)

@app.get(
    "/anomalies",
    response_model=AnomalySummary,
    tags=["Anomalies"],
    summary="Anomaly Detection Summary"
)
def anomalies(db: Session = Depends(get_db)):

    return get_anomaly_summary(db)

@app.get("/executive-summary")
def executive_summary(db: Session = Depends(get_db)):

    metrics = get_llm_metrics(db)

    return generate_executive_summary(metrics)

@app.get("/test-claude")
def test_claude_endpoint():

    return {
        "response": test_claude()
    }