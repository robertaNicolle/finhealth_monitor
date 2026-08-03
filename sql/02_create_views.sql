-- View: public.vw_anomaly_summary

-- DROP VIEW public.vw_anomaly_summary;

CREATE OR REPLACE VIEW public.vw_anomaly_summary
 AS
 SELECT transaction_date::date AS transaction_day,
    count(*) AS total_alerts,
    sum(
        CASE
            WHEN zscore_alert THEN 1
            ELSE 0
        END) AS zscore_alerts,
    sum(
        CASE
            WHEN if_alert THEN 1
            ELSE 0
        END) AS isolation_forest_alerts
   FROM transaction_alerts
  GROUP BY (transaction_date::date)
  ORDER BY (transaction_date::date);

ALTER TABLE public.vw_anomaly_summary
    OWNER TO postgres;


-- View: public.vw_forecast

-- DROP VIEW public.vw_forecast;

CREATE OR REPLACE VIEW public.vw_forecast
 AS
 SELECT ds,
    yhat,
    yhat_lower,
    yhat_upper
   FROM revenue_forecast
  ORDER BY ds;

ALTER TABLE public.vw_forecast
    OWNER TO postgres;


-- View: public.vw_monthly_revenue

-- DROP VIEW public.vw_monthly_revenue;

CREATE OR REPLACE VIEW public.vw_monthly_revenue
 AS
 SELECT month,
    revenue,
    transaction_volume,
    total_transactions,
    active_customers,
    new_customers,
    churn_rate,
    fraud_rate,
    anomaly_rate,
    cac,
    ltv
   FROM monthly_business_metrics
  ORDER BY month;

ALTER TABLE public.vw_monthly_revenue
    OWNER TO postgres;

