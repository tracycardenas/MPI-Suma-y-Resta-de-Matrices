import multiprocessing
import numpy as np
import Metodos
import time
size_ = (10000,10000)
rows, columns = size_
matriz1 = Metodos.generacionMatriz(size_)
matriz2 = Metodos.generacionMatriz(size_)

x=np.hsplit(matriz1,8)
y=np.hsplit(matriz2,8)
suma1 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
resta1 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
suma2 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
resta2 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
suma3 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
resta3 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
suma4 = np.zeros(dtype=float, shape=(rows,int(columns/4)))
resta4 = np.zeros(dtype=float, shape=(rows,int(columns/4)))

if __name__ == "__main__":  
    #inicio = time.time()
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
    
    for j in job:
            j.start()

    for j in job:
            j.join()

    #fin = time.time()

    #print("El proceso de sumar y restar las matrices paralelamente se ejecutó en %d segundos" % (fin - inicio))
