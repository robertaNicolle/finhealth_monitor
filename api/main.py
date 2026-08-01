from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api.database import get_db

from api.services import (
    get_overview_metrics,
    get_anomaly_summary,
    get_customer_metrics,
    get_forecast_data,
    test_claude,
    get_llm_metrics,
    generate_executive_summary,
)

from api.schemas.overview import OverviewMetrics
from api.schemas.anomalies import AnomalySummary
from api.schemas.customer import CustomerMetrics
from api.schemas.forecast import ForecastData
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