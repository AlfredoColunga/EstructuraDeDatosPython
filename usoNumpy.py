import numpy as np
lista1 = [12,13,14,15]
lista2 = [15,14,13,12]
lista3 = [11,22,33,44,55]
lista4 = [21,22,23,24,25,26]
vector1 = np.array(lista1)
vector2 = np.array(lista2)
vector3 = np.array(lista3)
vector4 = np.array(lista4)
print("4 elementos + 4 elementos: " + str(vector1+vector2))
#[27 27 27 27]
print("5 elementos + 4 elementos: " + str(vector3+vector1))
#operands could not be broadcast together with shapes (5,) (4,)
print("5 elementos + 6 elementos: " + str(vector3+vector4))
#operands could not be broadcast together with shapes (5,) (6,)