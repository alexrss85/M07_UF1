import numpy as np

print("Función crear array 1: ")
def ex1(param1, param2, param3, param4):
    a = np.array([param1, param2, param3, param4])
    return a

print(ex1(88,23,39,41))

print("Función crear array 2: ")

def ex2(param1, param2, param3, param4, param5, param6):
    a = np.array([[param1, param2, param3], [param4, param5, param6]])
    return a

print(ex2(76.4,21.7,38.4,41.2,52.8,68.9))

print("Función crear array 3: ")
def ex3():
    a = np.array([[12], [4], [9], [8]])
    return a

print(ex3())

