import pandas as pd

df_athens = pd.read_csv('athens.csv')

df_athens['Date'] = pd.to_datetime(df_athens['Date'])
