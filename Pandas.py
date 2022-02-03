import pandas as pd
import numpy as np

print(pd.__version__)

s2=pd.Series([23,12,-25,74,91])
print(s2)

s3=pd.Series([23,12,-25,74,91], index=[23,12,-25,74,91])
print(s3)

array=np.array([1,2,3,4])
s4=pd.Series(array)
print(s4)
s3=pd.Series([12,-4,7,9],index=[1,2,3,4])
print(s3)
print(s3[s3<9])
#Funciones basicas

serieR=pd.Series([1,1,1,1,1,2,2,2,2,2,3,3,3,3,44,4,4,4,4,4,4,5])
print(serieR)
print(serieR.unique())
print(serieR.value_counts())


datosFrame={"color":["azul","rojo","blanco","verde","azul"],
            "objeto":["pelota","lapiz","papel","pañuelo","taza"],
            "precio":[15,2,5,9,14.5]}
dFrame= pd.DataFrame(datosFrame)
print(dFrame)
matrizDeclarada= np.arange(16).reshape((4,4))
#se debe de crear los indices y columnas
dFrame4=pd.DataFrame(matrizDeclarada,index=[1,2,3,4],
                     columns=["colA","colB","colC","colD"])
print(dFrame4)