Select
payment_mode,
Count(*)as total_client,
SUM(CASE WHEN account_churned = 'Yes' THEN 1 ELSE 0 END) AS churned_count,
Round (
SUM(CASE WHEN account_churned = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),1 
)as churned_rate_pct
from Clients
group by payment_mode
Order by churned_rate_pct DESC;
