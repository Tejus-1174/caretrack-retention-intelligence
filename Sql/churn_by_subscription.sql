SELECT
    subscription_model,
    COUNT(*) AS total_clients,
    SUM(CASE WHEN account_churned = 'Yes' THEN 1 ELSE 0 END) AS churned_count,
    ROUND(AVG(monthly_recurring_fee)::numeric, 2) AS avg_monthly_fee,
    ROUND(
        SUM(CASE WHEN account_churned = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        1
    ) AS churn_rate_pct
FROM clients
GROUP BY subscription_model
ORDER BY churn_rate_pct DESC;
