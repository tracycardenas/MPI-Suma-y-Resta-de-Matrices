from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
size_ = (1000,1000)
rows, columns = size_
data = np.zeros((rows,int( columns/2)),dtype=int)



if rank == 0:
    matriz1 = np.random.randint(10, size=size_)
    
    print("MATRIZ COMPLETA 1")
    print(matriz1)
   
    x=np.hsplit(matriz1,2)
    
    mitad1 = (x[0],x[1])
    data = mitad1

if rank ==1:
    matriz2 = np.random.randint(10, size=size_)
    print("MATRIZ COMPLETA 2")
    print(matriz2)
    print("**********************************")
    y=np.hsplit(matriz2,2)
    mitad2 = (y[0],y[1])
    data = mitad2

data = comm.gather(data, root=2)

if rank ==2:
    A=data[0]
    B=data[1]
    suma = np.zeros(dtype=int, shape=np.shape(A))
    resta = np.zeros(dtype=int, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]

    print("---------------RESULTADO SUMA---------------")
    print(np.concatenate((suma[0], suma[1]), axis=1))
    print("---------------RESULTADO RESTA---------------")
    print(np.concatenate((resta[0], resta[1]), axis=1))
