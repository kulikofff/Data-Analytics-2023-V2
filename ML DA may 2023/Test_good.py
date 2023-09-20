import pandas as pd
import numpy as np

#pip install -U memory_profiler
#pip install psutil
#python -m memory_profiler .\Test_bad.py

df = pd.read_csv('SampleSuperstore.csv', encoding='cp1251')
df.dropna(axis=0, inplace=True)

@profile
def dfgood(df):
    df_good = (df
        .query("Sales > 15 & Quantity == 2.0")
        .assign(summary = lambda df_: df_['Sales'] * df_['Quantity'])
        [['Sub-Category', 'Sales']]
        .groupby('Sub-Category').agg(['count', 'mean'])
        .droplevel(axis=1, level=0)
        .query('count > 50')
    )
    return df_good

print(pd.DataFrame(dfgood(df)))