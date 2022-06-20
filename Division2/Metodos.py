import numpy as np  

def generacionMatriz(size_): 
    
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    return matriz1


def sumar(A,B,su,rest):
  for i in range(np.shape(A)[0]):
    for j in range(np.shape(B)[1]):
      su[i][j] = A[i][j] + B[i][j]
      rest[i][j] = A[i][j] - B[i][j]


