import pandas as pd
import numpy as np

columnas=["S.long","S:anchura","P:londitud","P.anchura","Clase"]

dframe = pd.read_csv("iris.csv",names=columnas)

print(dframe.head())
print(dframe.describe())

print(dframe.cov())
print(dframe.corr())
tipos= dframe["Clase"].unique()
print(tipos)

#correlacion de cada tipo
for tipo in tipos:
    print(tipo+"  "+dframe["Clase"]==tipo)
    print()
    frameTipo=dframe[dframe["Clase"]==tipo]
    print("*"*35)
    print("Datos por tipo : {}".format(tipo))
    print("HEAD ")
    print(frameTipo.head())
    print("Descripcion")
    print(frameTipo.describe())
    print("Por cov")
    print(frameTipo.cov())
    print("Por corr")
    print(frameTipo.corr())
    print("Hay que borrar la columna clase para poder sacar la media ")
    del frameTipo["Clase"]
    print(frameTipo.mean())

