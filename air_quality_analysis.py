import pandas as pd

df_athens = pd.read_csv('athens.csv')

df_athens['Date'] = pd.to_datetime(df_athens['Date'])
df_athens['code'] = df_athens['code'].fillna('ANO001')

cols_to_fill = [
    "Vegitation (High)", "Wind-Speed (U)", "Wind-Speed (V)", 
    "Dewpoint Temp", "Soil Temp", "Total Percipitation", 
    "Vegitation (Low)", "Relative Humidity"
]

original_index = df_athens.index
original_order = df_athens.copy()