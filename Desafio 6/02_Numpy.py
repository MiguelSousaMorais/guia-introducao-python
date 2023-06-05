
import numpy as np

#1- Crie uma matriz 1D com números de 0 a 9

matriz_1 = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9]) 
print("Matriz 1: ",matriz_1)

#2- Crie uma matriz booleana numpy 3×3 com ‘True’

matriz_2 = np.full([3,3], True , dtype = bool) 
print("Matriz 2: ",matriz_2)

#3- Extraia todos os números ímpares de ‘arr’

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
matriz_impares = arr[arr % 2 != 0]
print("Matriz_ímpar: ",matriz_impares)

#4- Substitua todos os números ímpares arr por -1
arr[arr % 2 != 0] = -1
print("Matriz 'arr' com -1:", arr)

#5- Substitua todos os números ímpares em arr com -1 sem alterar arr

arr = np.arange(10)
#out = np.where()

#6- Converta uma matriz 1D para uma matriz 2D com 2 linhas:

arr = np.arange(10)
matriz_2D = np.reshape(arr, (2, -2))
print("Matriz 2D: ", matriz_2D)

       
#6- Empilhe matrizes verticalmente:

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print("Empilhamento vertical: \n", np.vstack((a, b)))

#6- Empilhe as matrizes horizontalmente:

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print("Empilhamento horizontal: \n", np.hstack((a, b)))
