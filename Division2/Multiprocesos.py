import multiprocessing
import numpy as np
import Metodos
size_ = (1000,1000)
rows, columns = size_

matriz1 = Metodos.generacionMatriz(size_)
matriz2 = Metodos.generacionMatriz(size_)
#print("MATRIZ 1-----")
#print(matriz1)
#print("MATRIZ 2-----")
#print(matriz2)
#print("************************")

x=np.hsplit(matriz1,2)
y=np.hsplit(matriz2,2)
suma1 = np.zeros(dtype=float, shape=(rows,int(columns/2)))
resta1 = np.zeros(dtype=float, shape=(rows,int(columns/2)))
suma2 = np.zeros(dtype=float, shape=(rows,int(columns/2)))
resta2 = np.zeros(dtype=float, shape=(rows,int(columns/2)))

if __name__ == "__main__":  
    procs = 2
    job = []
    process = multiprocessing.Process\
                    (target=Metodos.sumar, args = (x[0],y[0],suma1,resta1))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar, args = (x[1],y[1],suma2,resta2))
    job.append(process)

    
    for j in job:
            j.start()

    for j in job:
            j.join()

    #Concatenacion de matrices
    #sumaTotal=np.concatenate((suma1,suma2),axis=1,out=None)
    #restaTotal=np.concatenate((resta1,resta2),axis=1,out=None)

    #print("Suma de matrices")
    #for i in range(5):
    #    print("%f + %f = %f" % (matriz1[i][i], matriz2[i][i], sumaTotal[i][i]))

    #print("Resta de matrices")
    #for i in range(5):
     #   print("%f - %f = %f" % (matriz1[i][i], matriz2[i][i], restaTotal[i][i]))