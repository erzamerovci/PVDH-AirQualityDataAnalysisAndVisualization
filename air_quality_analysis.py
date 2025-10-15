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

df_athens = df_athens.sort_values(['station_name', 'Date'])
df_athens[cols_to_fill] = df_athens.groupby('station_name')[cols_to_fill].fillna(method='ffill')
df_athens = df_athens.reindex(original_index)

df_athens_sorted = df_athens.sort_values(['station_name', 'Date']).copy()
df_athens_sorted['Temp'] = (
    df_athens_sorted
    .groupby('station_name')['Temp']
    .transform(lambda x: x.interpolate(method='linear', limit_direction='both'))
)
df_athens = df_athens_sorted.reindex(original_index)
