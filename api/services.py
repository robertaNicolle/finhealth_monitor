from sqlalchemy import text
from anthropic import Anthropic
from prompts import executive_summary_prompt
from dotenv import load_dotenv
import os
import json

load_dotenv()
print(os.getenv("ANTHROPIC_API_KEY"))
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_customer_metrics(db, limit=100):

    query = text("""

        SELECT *

        FROM customer_metrics

        ORDER BY customer_id

        LIMIT :limit

    """)

    result = db.execute(query, {"limit": limit})

    return [dict(row._mapping) for row in result]

def get_overview_metrics(db):

    query = text("""

        SELECT *

        FROM vw_overview_metrics

    """)

    result = db.execute(query)

    row = result.fetchone()

    if row is None:
        return {}

    return dict(row._mapping)
def get_anomaly_summary(db):

    query = text("""

        SELECT *

        FROM vw_anomaly_summary

    """)

    result = db.execute(query)

    row = result.fetchone()

    if row is None:
        return {}

    return dict(row._mapping)

def get_forecast_data(db):

    query = text("""

        SELECT
            month,
            revenue,
            transaction_volume,
            total_transactions,
            fraud_rate,
            anomaly_rate
        FROM monthly_business_metrics
        ORDER BY month

    """)

    result = db.execute(query)

    return [dict(row._mapping) for row in result]

def get_anomaly_summary(db):

    query = text("""
        SELECT
            COUNT(*) AS total_transactions,

            SUM(
                CASE
                    WHEN anomaly_flag = TRUE THEN 1
                    ELSE 0
                END
            ) AS anomaly_transactions,

            ROUND(
                100.0 *
                SUM(
                    CASE
                        WHEN anomaly_flag = TRUE THEN 1
                        ELSE 0
                    END
                ) /
                COUNT(*),
                2
            ) AS anomaly_rate,

            SUM(
                CASE
                    WHEN is_fraud = TRUE THEN 1
                    ELSE 0
                END
            ) AS fraud_transactions,

            SUM(
                CASE
                    WHEN if_alert = TRUE THEN 1
                    ELSE 0
                END
            ) AS isolation_forest_alerts,

            SUM(
                CASE
                    WHEN zscore_alert = TRUE THEN 1
                    ELSE 0
                END
            ) AS zscore_alerts,

            SUM(
                CASE
                    WHEN rule_alert = TRUE THEN 1
                    ELSE 0
                END
            ) AS rule_based_alerts

        FROM transactions;
    """)

    result = db.execute(query)

    return dict(result.fetchone()._mapping)


def generate_executive_summary(metrics):

    prompt = executive_summary_prompt(metrics)

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=7000,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.content[0].text.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    try:
        return json.loads(content)

    except Exception:

        return {
            "risk_level": "UNKNOWN",
            "overall_health": "UNKNOWN",
            "executive_summary": content,
            "business_performance": "",
            "fraud_analysis": "",
            "anomaly_analysis": "",
            "key_strengths": [],
            "main_risks": [],
            "recommendations": []
        }


def get_llm_metrics(db):

    query = text("""
    SELECT
        revenue,
        total_transactions AS transactions,
        ROUND(
        (revenue / NULLIF(total_transactions, 0))::numeric,
            2
        ) AS average_ticket,
        fraud_rate,
        anomaly_rate,
        new_customers,
        churn_rate,
        cac,
        ltv,
        active_customers
    FROM monthly_business_metrics
    ORDER BY month DESC
    LIMIT 1;
""")

    metrics = dict(db.execute(query).fetchone()._mapping)
    
    history_query = text("""
        SELECT
            month,
            revenue,
            total_transactions,
            fraud_rate,
            anomaly_rate
         FROM monthly_business_metrics
         ORDER BY month;
    """)
    
    metrics["monthly_history"] = [
        dict(row._mapping)
        for row in db.execute(history_query)
    ]        
    
    fraud_query = text("""
    SELECT
        merchant_category,
        COUNT(*) AS total
    FROM transactions
    WHERE is_fraud = TRUE
    GROUP BY merchant_category
    ORDER BY total DESC;
""")

    metrics["fraud_by_category"] = [
    dict(row._mapping)
    for row in db.execute(fraud_query)
]
    
    type_query = text("""
    SELECT
        transaction_type,
        COUNT(*) AS total
    FROM transactions
    GROUP BY transaction_type
    ORDER BY total DESC;
""")

    metrics["transaction_types"] = [
    dict(row._mapping)
    for row in db.execute(type_query)
]
    country_query = text("""
    SELECT
        country,
        COUNT(*) AS total
    FROM transactions
    GROUP BY country
    ORDER BY total DESC
    LIMIT 10;
""")

    metrics["top_countries"] = [
    dict(row._mapping)
    for row in db.execute(country_query)
]
    query2 = text("""
        SELECT
            SUM(CASE WHEN if_alert THEN 1 ELSE 0 END) AS if_alerts,
            SUM(CASE WHEN zscore_alert THEN 1 ELSE 0 END) AS zscore_alerts,
            SUM(CASE WHEN rule_alert THEN 1 ELSE 0 END) AS rule_alerts
        FROM transactions;
    """)
    score = 100

# Fraud
    if metrics["fraud_rate"] >= 1.5:
        score -= 20
    elif metrics["fraud_rate"] >= 1.0:
        score -= 10

    # Anomalies
    if metrics["anomaly_rate"] >= 1.0:
        score -= 15
    elif metrics["anomaly_rate"] >= 0.7:
        score -= 8

    # Customer churn
    if metrics["churn_rate"] >= 10:
        score -= 20
    elif metrics["churn_rate"] >= 5:
        score -= 10

    # LTV/CAC
    ltv_cac = metrics["ltv"] / metrics["cac"]

    if ltv_cac < 3:
        score -= 15
    elif ltv_cac < 5:
        score -= 8

    score = max(0, min(score, 100))

    metrics["executive_score"] = score
    metrics["ltv_cac_ratio"] = round(ltv_cac, 2)
    metrics.update(dict(db.execute(query2).fetchone()._mapping))

    return metrics


def test_claude():
    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=100,
            messages=[
                {
                    "role": "user",
                    "content": "Reply with exactly: Connection successful."
                }
            ]
        )

        return response.content[0].text

    except Exception as e:
        return str(e)