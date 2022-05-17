import pandas as pd
import numpy as np

df_data = pd.read_csv('assets/real_estate.csv',sep=';') 

#print(df_data.head(5))
print(df_data.describe())

