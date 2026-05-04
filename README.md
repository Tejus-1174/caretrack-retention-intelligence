# CareTrack — Client Retention Intelligence Dashboard

## Project Resources
- [Case Study (Notion)](https://mixed-animantarx-6d4.notion.site/CareTrack-Client-Retention-Intelligence-Suite-3560e6e4fe8080edb1f6e03b2592963d))
- [GitHub Repository](https://github.com/Tejus-1174/caretrack-retention-intelligence)
- [Document](https://docs.google.com/presentation/d/11qM4PyjEX1azu61Ota7gAtBTI4Vz7ve9bWFsiNxkdtA/edit?slide=id.p#slide=id.p)

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
