import time
import numpy as np
inicio = time.time()
size_ = (1000,1000)
matriz1 = np.random.randint(10, size=size_).astype("float") / 100
matriz2 = np.random.randint(10, size=size_).astype("float") / 100
suma = np.zeros(dtype=float, shape=size_)
resta = np.zeros(dtype=float, shape=size_)

for i in range(len(matriz1)):
  for j in range(len(matriz1)):
    suma[i][j] = matriz1[i][j] + matriz2[i][j]
    resta[i][j] = matriz1[i][j] - matriz2[i][j]

fin = time.time()
print("El proceso de sumar y restar las matrices secuencialmente se ejecutó en %d segundos" % (fin - inicio))
# obtener los primeros 5 resultados de la suma
print("Suma de matrices")
for i in range(5):
  print("%f + %f = %f" % (matriz1[i][i], matriz2[i][i], suma[i][i]))

print("Resta de matrices")
for i in range(5):
  print("%f - %f = %f" % (matriz1[i][i], matriz2[i][i], resta[i][i]))