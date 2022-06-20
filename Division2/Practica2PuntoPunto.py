from re import sub
import numpy as np   
from mpi4py import MPI
from time import time
#SACAR TIEMPO DE PROCESOS CON MPI
#HACER CON 4 PROCESOS DE MATRICES

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank)
start_time = MPI.Wtime()
if rank==0:
    size_ = (10000,10000)
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    matriz2 = np.random.randint(10, size=size_).astype("float") / 100
    x=np.hsplit(matriz1,2)
    y=np.hsplit(matriz2,2)
    comm.send(matriz1,dest=3)
    comm.send(matriz2,dest=3)

    mitad1 = (x[0],y[0])
    comm.send(mitad1,dest=1)
    mitad2 = (x[1],y[1])
    comm.send(mitad2,dest=2)

   
if rank==1:
    recvbuf = comm.recv(source=0)
    A=recvbuf[0]
    B=recvbuf[1]
    suma = np.zeros(dtype=float, shape=np.shape(A))
    resta = np.zeros(dtype=float, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]
    comm.send(suma, dest=3)
    comm.send(resta,dest=3)

if rank==2:
    recvbuf = comm.recv(source=0)
    A=recvbuf[0]
    B=recvbuf[1]
    suma = np.zeros(dtype=float, shape=np.shape(A))
    resta = np.zeros(dtype=float, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]
    comm.send(suma, dest=3)
    comm.send(resta,dest=3)


if rank==3:
    matriz1 = comm.recv(source=0)
    matriz2 = comm.recv(source=0)
    suma1 = comm.recv(source=1)
    suma2 = comm.recv(source=2)


    resta1 = comm.recv(source=1)
    resta2 = comm.recv(source=2)

    matrizSuma = np.concatenate((suma1,suma2),axis=1)
    matrizResta = np.concatenate((resta1,resta2),axis=1)
    #print("Suma de matrices")
    #for i in range(5):
    #    print("%f + %f = %f" % (matriz1[i][i], matriz2[i][i], matrizSuma[i][i]))

    #print("Resta de matrices")
    #for i in range(5):
     #   print("%f - %f = %f" % (matriz1[i][i], matriz2[i][i], matrizResta[i][i]))

  


