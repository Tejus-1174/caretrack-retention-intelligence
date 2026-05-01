
WITH client_health AS (
    SELECT
        client_account_id,
        subscription_model,
        payment_mode,
        evv_timeclock_status,
        monthly_recurring_fee,
        months_on_system,

        CASE
            WHEN months_on_system > 24 THEN 40
            WHEN months_on_system BETWEEN 12 AND 24 THEN 25
            ELSE 10
        END AS tenure_score,

        CASE
            WHEN monthly_recurring_fee > 70 THEN 40
            WHEN monthly_recurring_fee BETWEEN 40 AND 70 THEN 25
            ELSE 10
        END AS revenue_score,

        CASE
            WHEN evv_timeclock_status = 'Activated' THEN 20
            ELSE 10
        END AS adoption_score
    FROM clients
)

SELECT
    client_account_id,
    subscription_model,
    payment_mode,
    evv_timeclock_status,
    monthly_recurring_fee,
    months_on_system,
    tenure_score,
    revenue_score,
    adoption_score,
    (tenure_score + revenue_score + adoption_score) AS health_score,

    CASE
        WHEN (tenure_score + revenue_score + adoption_score) >= 80 THEN 'Healthy'
        WHEN (tenure_score + revenue_score + adoption_score) >= 50 THEN 'At Risk'
        ELSE 'Critical'
    END AS risk_band

FROM client_health
ORDER BY health_score ASC;