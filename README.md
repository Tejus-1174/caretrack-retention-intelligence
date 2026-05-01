# CareTrack — Client Retention Intelligence Dashboard

## Problem
B2B Healthcare SaaS company facing 26.54% churn with 214K revenue at risk across 7043 active clients.

## Solution
End-to-end retention intelligence system to identify at-risk clients before they churn.

## Health Score Model
| Component | Weight |
|---|---|
| Engagement Depth | 40 pts |
| Revenue Value | 40 pts |
| Module Adoption | 20 pts |

## Key Findings
- 1869 clients churned (26.54% churn rate)
- Monthly subscription = highest churn (43%)
- EVV Not Activated segment = highest churn risk (42%)
- Electronic check payment mode = most churned segment
- 1428 clients currently need attention

## Tech Stack
Python (Pandas) → PostgreSQL (Views) → Power BI

## Project Structure
- `/Python` — Data cleaning and transformation scripts
- `/SQL` — PostgreSQL views and health score queries
- `/PowerBI` — Dashboard file and screenshots
