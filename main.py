import pandas as pd
import numpy as np
df=pd.read_csv('Telco-Customer-Churn.csv')
print(df.head())
print(df.columns)
print(df.info())  
df.isnull().sum()
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
df.rename(columns={
    'customerID'       : 'client_account_id',
    'gender'           : 'client_type',
    'Partner'          : 'partner_agency_associated',
    'Dependents'       : 'dependent_care_units',
    'tenure'           : 'months_on_system',
    'PhoneService'     : 'care_support_line',
    'MultipleLines'    : 'multi_support_queue',
    'InternetService'  : 'care_program_enrollment',
    'OnlineSecurity'   : 'hipaa_security_pack',
    'OnlineBackup'     : 'audit_compliance_pack',
    'DeviceProtection' : 'device_sync_pack',
    'TechSupport'      : 'evv_timeclock_status',
    'StreamingTV'      : 'clinical_reporting_pack',
    'StreamingMovies'  : 'revenue_analytics_pack',
    'Contract'         : 'subscription_model',
    'PaperlessBilling' : 'digital_invoice_enabled',
    'PaymentMethod'    : 'payment_mode',
    'MonthlyCharges'   : 'monthly_recurring_fee',
    'TotalCharges'     : 'lifetime_account_value',
    'Churn'            : 'account_churned',
}, inplace=True)
df['care_program_enrollment'] = df['care_program_enrollment'].replace({
    'DSL': 'Standard Care Program',
    'Fiber optic': 'Advanced Care Program',
    'No': 'No Program Access'
})

df['evv_timeclock_status'] = df['evv_timeclock_status'].replace({
    'Yes': 'Activated',
    'No': 'Not Activated',
    'No internet service': 'No Program Access'
})

df['subscription_model'] = df['subscription_model'].replace({
    'Month-to-month': 'Monthly Subscription',
    'One year': 'Annual Subscription',
    'Two year': 'Enterprise Subscription'
})
print(df.head())
print(df.info())
df.to_csv('caretrack_clean.csv', index=False)
print(f'Done: {len(df)} rows, {len(df.columns)} columns')
   