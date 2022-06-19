import multiprocessing
import numpy as np
import Metodos
size_ = (5000,5000)
rows, columns = size_

matriz1 = Metodos.generacionMatriz(size_)
matriz2 = Metodos.generacionMatriz(size_)
#print("MATRIZ 1-----")
#print(matriz1)
#print("MATRIZ 2-----")
#print(matriz2)
#print("************************")

x=np.hsplit(matriz1,8)
y=np.hsplit(matriz2,8)
suma1 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta1 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma2 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta2 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma3 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta3 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma4 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta4 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma5 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta5 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma6 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta6 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma7 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta7 = np.zeros(dtype=float, shape=(rows,int(columns/8)))
suma8= np.zeros(dtype=float, shape=(rows,int(columns/8)))
resta8 = np.zeros(dtype=float, shape=(rows,int(columns/8)))

if __name__ == "__main__":  
    procs = 8 
    job = []
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[0],y[0],suma1,resta1))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[1],y[1],suma2,resta2))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[2],y[2],suma3,resta3))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[3],y[3],suma4,resta4))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[4],y[4],suma5,resta5))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[5],y[5],suma6,resta6))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[6],y[6],suma7,resta7))
    job.append(process)
    process = multiprocessing.Process\
                    (target=Metodos.sumar(x[7],y[7],suma8,resta8))
    job.append(process)

    
    for j in job:
            j.start()

    for j in job:
            j.join()

    #Concatenacion de matrices
    sumaTotal=np.concatenate((suma1,suma2,suma3,suma4,suma5,suma6,suma7,suma8),axis=1,out=None)
    restaTotal=np.concatenate((resta1,resta2,resta3,resta4,resta5,resta6,resta7,resta8),axis=1,out=None)

    #print("Suma de matrices")
    #for i in range(5):
    #    print("%f + %f = %f" % (matriz1[i][i], matriz2[i][i], sumaTotal[i][i]))

    #print("Resta de matrices")
    #for i in range(5):
     #   print("%f - %f = %f" % (matriz1[i][i], matriz2[i][i], restaTotal[i][i]))