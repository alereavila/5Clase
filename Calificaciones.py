import pandas as pd
import numpy as np

archivo=pd.read_csv("datoscalificacion.csv")
print(archivo.head())
print(archivo.count())

#desviacion standard
mediaCalificacion = archivo["calificación"].mean()
standardCalif=archivo["calificación"].std()
rSup=mediaCalificacion+standardCalif*1.96
rInf=mediaCalificacion-standardCalif*1.96

copia=archivo
copia=copia.drop(copia[copia["calificación"]>rSup].index)
copia=copia.drop(copia[copia["calificación"]<rInf].index)

print(copia.head())
print(copia.count())
print(copia.describe())
