import numpy as np

arreglo = np.array([2.1,3,4])
print(arreglo)
print(arreglo.dtype)
#bidimensional
b=np.array([(1.3,4,3),(4,5,8.3)])
print(b)
c=np.array([[1,2],[2,3]], dtype=complex)

print("d es: ", c)
print("Dimensones: ", c.ndim)
print("Forma: ", c.shape)
print("Size: ", c.size)
print("item size : ", c.itemsize)
print("item size : ", c.nbytes)

matrizCeros= np.zeros((3,4))
print(matrizCeros)

matrizUnos= np.ones((2,3,2))
print(matrizUnos)
mLlena= np.full((2,3),10)
print(mLlena)

mIdentidad= np.eye(3,3)
print("Matriz identidad ",mIdentidad)

mat1=np.arange(10,80,5)
print("matriz de 10 a 80 de 5 en 5 ",mat1)

mat3=np.arange(0,100,1).reshape(10,10)
print(mat3)

mat4=np.linspace(0,1,)
print(mat4)

mat5=np.random.random((5,5))
print(mat5)

x=np.array([5,6,7,8,9])

print(x[1:7:2])

arrA=np.array([20,30,40,50])
arrB=np.arange(4)
print(arrA)
print(arrB)
print(arrA-arrB)
print(arrA<35)
matriz1=np.array([[7,2],[10,15]])
matriz2=np.array([[2,3],[4,8]])
print(matriz1*matriz2)
print("producto punto")
print(matriz1.dot(matriz2))
print(matriz1@matriz2)

print("Iterando sobre un arreglo")
for e in arrA:
    print(e)
print("Iterando en matriz")
for renglon in matriz1:
    print(renglon)
for porElemento in matriz1.flat:
    print(porElemento)


print("La media de una matriz")

A=np.random.random((4,4))
print(A)
print(A<.5)
B=A[A<.5]
print(B)

datos=np.random.random((8,8))
print(datos)
#guardarlo
np.save("datosArreglo",datos)

datos2=np.load("datosArreglo.npy")
print(datos2)

#
datosCSV=np.genfromtxt("archivo_csv.csv",delimiter=",",names=True)
print(datosCSV)
print(datosCSV[0])
print(datosCSV["valores1"])