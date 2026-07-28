# FinHealth Monitor

**AI-powered financial intelligence platform for fraud detection, anomaly monitoring, forecasting and executive decision support.**

FinHealth Monitor is a portfolio project that simulates how a fintech company can monitor operational performance, detect suspicious financial behaviour and support executive decision-making using machine learning, SQL analytics and Large Language Models.

Instead of analysing isolated metrics, the platform integrates data engineering, business intelligence, anomaly detection, forecasting and AI-generated executive reports into a unified financial monitoring pipeline.

---

## Business Problem

Financial institutions process thousands of transactions every day.

Monitoring business performance requires much more than tracking revenue. Risk teams must identify fraudulent behaviour, detect operational anomalies, understand customer dynamics and anticipate future trends before they become business problems.

Although these analyses often exist separately, executive teams need a single source of truth capable of transforming raw data into actionable business insights.

FinHealth Monitor was developed to simulate this decision-support workflow.

---

## Solution

FinHealth Monitor combines multiple analytical components into a single financial intelligence pipeline.

The project integrates:

- SQL-based business metrics
- Machine Learning anomaly detection
- Revenue forecasting
- Fraud monitoring
- Customer analytics
- Executive reports generated with Large Language Models
- REST API built with FastAPI

The objective is to simulate how a financial institution could centralise operational intelligence and support executive decision-making.

---

## Architecture

The platform follows an end-to-end analytical pipeline, transforming raw transactional data into business insights and executive decision support.

```text
Synthetic Data
        │
        ▼
 PostgreSQL Database
        │
        ▼
 SQL Business Views
        │
        ├──────────────┐
        ▼              ▼
Machine Learning   Revenue Forecasting
(Isolation Forest,     (Prophet)
 Z-Score)
        │              │
        └──────┬───────┘
               ▼
      FastAPI REST API
               │
               ▼
 Claude AI Executive Reports
```

---

## Key Features

- Synthetic financial data generation
- PostgreSQL relational database
- SQL analytical views
- Fraud detection rules
- Anomaly detection using Isolation Forest
- Statistical anomaly detection using Z-Score
- Revenue forecasting with Prophet
- AI-generated executive reports using Claude
- REST API built with FastAPI
- Modular project structure

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Database | PostgreSQL |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Forecasting | Prophet |
| API | FastAPI |
| ORM | SQLAlchemy |
| AI | Anthropic Claude |
| Visualisation | Power BI |

---

## Project Structure

```text
finhealth_monitor/
│
├── api/
├── dashboard/
├── data/
├── notebooks/
├── scripts/
├── sql/
├── README.md
└── requirements.txt
```

---

## Machine Learning

FinHealth Monitor combines multiple analytical techniques to identify suspicious financial behaviour.

### Fraud & Anomaly Detection

- Rule-based fraud detection
- Isolation Forest for unsupervised anomaly detection
- Z-Score statistical anomaly detection

The combination of these approaches increases the reliability of anomaly identification by comparing business rules with machine learning predictions.

### Revenue Forecasting

Future revenue is estimated using Facebook Prophet, allowing the platform to project business performance and support strategic planning.

---

## AI Executive Reports

One of the main features of the platform is the integration with Anthropic Claude.

Instead of displaying only charts and KPIs, the system automatically generates executive reports that transform business metrics into actionable insights.

Each report includes:

- Executive Score
- Risk Level
- Business Performance
- Fraud Analysis
- Anomaly Analysis
- Customer Analysis
- Key Strengths
- Main Risks
- Executive Recommendations

This simulates how executives consume analytical information inside modern financial institutions.

---

## REST API

The project exposes its analytical services through a FastAPI application.

### Main Endpoints

| Endpoint | Description |
|----------|-------------|
| `/executive-summary` | AI-generated executive report |
| `/forecast` | Revenue forecast |
| `/anomalies` | Detected anomalies |
| `/monthly-metrics` | Business metrics |
| `/health` | API health check |

Interactive documentation is available through Swagger UI.

---

## Results

The project demonstrates an end-to-end analytical workflow, covering:

- Data generation
- SQL modelling
- Business analytics
- Machine Learning
- Forecasting
- AI-generated executive reporting
- REST API development

Rather than focusing on a single model or dashboard, FinHealth Monitor integrates multiple technologies into a unified financial intelligence platform.

---

## Future Improvements

- Interactive Power BI dashboard
- Real-time data ingestion
- Authentication and user management
- Cloud deployment
- CI/CD pipeline
- Automated monitoring

---

## How to Run

```bash
git clone https://github.com/robertaNicolle/finhealth_monitor.git

cd finhealth_monitor

pip install -r requirements.txt

uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to access the interactive API documentation.

---

## Author

**Roberta Soares**

Data Analytics | Data Science | Machine Learning | Artificial Intelligence

GitHub: https://github.com/robertaNicolle

LinkedIn: https://linkedin.com/in/roberta-soares-dev