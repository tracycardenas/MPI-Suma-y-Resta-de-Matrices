import numpy as np   
from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.Get_rank()
print("my rank is %i" % (rank))


if rank==0:
    size_ = (10000,10000)
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    matriz2 = np.random.randint(10, size=size_).astype("float") / 100
    x=np.hsplit(matriz1,4)
    y=np.hsplit(matriz2,4)
    array_to_share=[(x[0],y[0]),(x[0],y[0]),(x[1],y[1]),(x[2],y[2]),(x[3],y[3]),(matriz1,matriz2)]
    comm.scatter(array_to_share, root=0)
else:
    array_to_share=None


if rank==1:
    recvbuf = comm.scatter(array_to_share, root=0)
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
    comm.send((suma,resta),dest=5)

if rank==2:
    
    recvbuf = comm.scatter(array_to_share, root=0)
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
    comm.send((suma,resta),dest=5)

if rank==3:
    recvbuf = comm.scatter(array_to_share, root=0)
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
    comm.send((suma,resta),dest=5)

if rank==4:
    
    recvbuf = comm.scatter(array_to_share, root=0)
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
    comm.send((suma,resta),dest=5)


  
if rank==5:
    
    recvbuf = comm.scatter(array_to_share, root=0)
    mat1=recvbuf[0]
    mat2=recvbuf[1]
    data_received=comm.recv(source=1)
    A=data_received[0]
    A1=data_received[1]
    data_received=comm.recv(source=2)
    B=data_received[0]
    B1=data_received[1]
    data_received=comm.recv(source=3)
    C=data_received[0]
    C1=data_received[1]
    data_received=comm.recv(source=4)
    D=data_received[0]
    D1=data_received[1]


    sumaTotal=np.concatenate((A,B,C,D),axis=1,out=None)
    restaTotal=np.concatenate((A1,B1,C1,D1),axis=1,out=None)
    print("Suma de matrices")
    for i in range(5):
        print("%f + %f = %f" % (mat1[i][i], mat2[i][i], sumaTotal[i][i]))
    
    print("Resta de matrices")
    for i in range(5):
        print("%f - %f = %f" % (mat1[i][i], mat2[i][i], restaTotal[i][i]))

 
    
    
   