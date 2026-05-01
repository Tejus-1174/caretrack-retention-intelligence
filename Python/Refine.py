import pandas as pd
df=pd.read_csv('caretrack_clean.csv')



df['legacy_client'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})
df.drop(columns=['SeniorCitizen'], inplace=True)



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

print(df['care_program_enrollment'].unique())
print(df['evv_timeclock_status'].unique())
print(df['subscription_model'].unique())
print(df['payment_mode'].unique())
print(df['client_type'].unique())

df.to_csv(r'C:\Users\njsam\OneDrive\Desktop\symmetry intel\caretrack_clean_refined.csv', index=False)
print(f"done:{len(df)}rows,{len(df.columns)}columns")