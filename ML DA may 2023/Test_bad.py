import pandas as pd
import numpy as np

#pip install -U memory_profiler
#pip install psutil
#python -m memory_profiler .\Test_bad.py

df = pd.read_csv('SampleSuperstore.csv', encoding='cp1251')
df.dropna(axis=0, inplace=True)

@profile
def dfbad(df):
    df_bad = df.query("Sales > 15 & Quantity == 2.0")
    df_bad['summary'] = df_bad.Sales * df_bad.Quantity
    df_bad = df_bad[['Sub-Category', 'Sales']]
    df_bad = df_bad.groupby('Sub-Category').agg(['count', 'mean'])
    df_bad = df_bad.droplevel(axis=1, level=0)
    df_bad = df_bad.query('count > 50')
    return df_bad

print(pd.DataFrame(dfbad(df)))