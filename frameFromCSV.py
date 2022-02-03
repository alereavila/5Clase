import pandas as pd
import numpy as np

df=pd.read_csv("archivo_csv.csv",index_col=0)
print(df)
print(df.head())
print(df["valores4"])
print(df.valores3.mean())
print(df.describe())