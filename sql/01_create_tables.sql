-- Table: public.customers

-- DROP TABLE IF EXISTS public.customers;

CREATE TABLE IF NOT EXISTS public.customers
(
    customer_id bigint,
    full_name text COLLATE pg_catalog."default",
    email text COLLATE pg_catalog."default",
    birth_date text COLLATE pg_catalog."default",
    gender text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    signup_date text COLLATE pg_catalog."default",
    customer_segment text COLLATE pg_catalog."default",
    acquisition_channel text COLLATE pg_catalog."default",
    monthly_income bigint,
    credit_score bigint,
    risk_level text COLLATE pg_catalog."default",
    is_active boolean,
    churn_flag boolean
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.customers
    OWNER to postgres;

-- Table: public.customer_metrics

-- DROP TABLE IF EXISTS public.customer_metrics;

CREATE TABLE IF NOT EXISTS public.customer_metrics
(
    customer_id bigint,
    total_transactions bigint,
    total_volume double precision,
    total_revenue double precision,
    avg_transaction_value double precision,
    fraud_transactions bigint,
    anomaly_transactions bigint,
    signup_date text COLLATE pg_catalog."default",
    customer_segment text COLLATE pg_catalog."default",
    acquisition_channel text COLLATE pg_catalog."default",
    churn_flag boolean,
    customer_age_days bigint,
    cac bigint,
    ltv double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.customer_metrics
    OWNER to postgres;


-- Table: public.monthly_business_metrics

-- DROP TABLE IF EXISTS public.monthly_business_metrics;

CREATE TABLE IF NOT EXISTS public.monthly_business_metrics
(
    month text COLLATE pg_catalog."default",
    revenue double precision,
    transaction_volume double precision,
    total_transactions bigint,
    fraud_rate double precision,
    anomaly_rate double precision,
    new_customers bigint,
    churn_rate double precision,
    cac double precision,
    ltv double precision,
    active_customers bigint
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.monthly_business_metrics
    OWNER to postgres;


-- Table: public.revenue_forecast

-- DROP TABLE IF EXISTS public.revenue_forecast;

CREATE TABLE IF NOT EXISTS public.revenue_forecast
(
    ds text COLLATE pg_catalog."default",
    yhat double precision,
    yhat_lower double precision,
    yhat_upper double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.revenue_forecast
    OWNER to postgres;


-- Table: public.transaction_alerts

-- DROP TABLE IF EXISTS public.transaction_alerts;

CREATE TABLE IF NOT EXISTS public.transaction_alerts
(
    transaction_id bigint,
    customer_id bigint,
    transaction_date text COLLATE pg_catalog."default",
    transaction_type text COLLATE pg_catalog."default",
    amount double precision,
    transaction_fee double precision,
    status text COLLATE pg_catalog."default",
    merchant_category text COLLATE pg_catalog."default",
    device_type text COLLATE pg_catalog."default",
    country text COLLATE pg_catalog."default",
    is_fraud boolean,
    anomaly_flag boolean,
    rule_alert boolean,
    z_score double precision,
    zscore_alert boolean,
    if_prediction bigint,
    if_alert boolean
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.transaction_alerts
    OWNER to postgres;


-- Table: public.transactions

-- DROP TABLE IF EXISTS public.transactions;

CREATE TABLE IF NOT EXISTS public.transactions
(
    transaction_id bigint,
    customer_id bigint,
    transaction_date text COLLATE pg_catalog."default",
    transaction_type text COLLATE pg_catalog."default",
    amount double precision,
    transaction_fee double precision,
    status text COLLATE pg_catalog."default",
    merchant_category text COLLATE pg_catalog."default",
    device_type text COLLATE pg_catalog."default",
    country text COLLATE pg_catalog."default",
    is_fraud boolean,
    anomaly_flag boolean,
    if_prediction bigint,
    if_alert boolean,
    rule_alert boolean,
    z_score double precision,
    zscore_alert boolean
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.transactions
    OWNER to postgres;
