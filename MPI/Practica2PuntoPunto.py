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
    #print(matriz1)
    #print("************")
    #print(matriz2)
    x=np.hsplit(matriz1,4)
    y=np.hsplit(matriz2,4)

    mitad1 = (x[0],y[0])
    comm.send(mitad1,dest=1)
    mitad2 = (x[1],y[1])
    comm.send(mitad2,dest=2)

    mitad3 = (x[2],y[2])
    comm.send(mitad3,dest=3)
    mitad4 = (x[3],y[3])
    comm.send(mitad4,dest=4)

    

   
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
    comm.send(suma, dest=5)
    comm.send(resta,dest=5)

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
    comm.send(suma, dest=5)
    comm.send(resta,dest=5)


if rank==3:
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
    comm.send(suma, dest=5)
    comm.send(resta,dest=5)


if rank==4:
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
    comm.send(suma, dest=5)
    comm.send(resta,dest=5)

if rank==5:
    suma1 = comm.recv(source=1)
    suma2 = comm.recv(source=2)
    suma3 = comm.recv(source=3)
    suma4 = comm.recv(source=4)

    resta1 = comm.recv(source=1)
    resta2 = comm.recv(source=2)
    resta3 = comm.recv(source=3)
    resta4 = comm.recv(source=4)

    matrizSuma = np.concatenate((suma1,suma2,suma3,suma4),axis=1)
    matrizResta = np.concatenate((resta1,resta2,resta3,resta4),axis=1)
    #print("MATRIZ SUMA")
    #print(matrizSuma)
    #print("MATRIZ RESTA")
    #print(matrizResta)

  


