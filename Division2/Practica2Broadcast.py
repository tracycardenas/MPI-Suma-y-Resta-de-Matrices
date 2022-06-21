import numpy as np   
from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is %i" % (rank))



if rank==0:
    size_ = (10000,10000)
    matriz1 = np.random.randint(10, size=size_)
    #print("MATRIZ 1")
    #print(matriz1)
 
    matriz2 = np.random.randint(10, size=size_)
    #print("MATRIZ 2")
    #print(matriz2)
    variable_to_share=(matriz1,matriz2)
    comm.bcast (variable_to_share, root=0)
else:
    variable_to_share=None


if rank==1:
    variable_to_share = comm.bcast(variable_to_share, root=0)
    x=np.hsplit(variable_to_share[0],4)
    y=np.hsplit(variable_to_share[1],4)
    A=x[0]
    B=y[0]
    suma = np.zeros(dtype=int, shape=np.shape(A))
    resta = np.zeros(dtype=int, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]
    respuestas1 = (suma, resta)
    comm.send(respuestas1,dest=5)    



if rank==2:
    
    variable_to_share = comm.bcast(variable_to_share, root=0)
    x=np.hsplit(variable_to_share[0],4)
    y=np.hsplit(variable_to_share[1],4)
    A=x[1]
    B=y[1]

    suma = np.zeros(dtype=int, shape=np.shape(A))
    resta = np.zeros(dtype=int, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]
    respuestas2 = (suma, resta)
    comm.send(respuestas2,dest=5)
    

if rank==3:
    variable_to_share = comm.bcast(variable_to_share, root=0)
    x=np.hsplit(variable_to_share[0],4)
    y=np.hsplit(variable_to_share[1],4)
    A=x[2]
    B=y[2]
    suma = np.zeros(dtype=int, shape=np.shape(A))
    resta = np.zeros(dtype=int, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]
    respuestas3 = (suma, resta)
    comm.send(respuestas3,dest=5)

if rank==4:
    
    variable_to_share = comm.bcast(variable_to_share, root=0)
    x=np.hsplit(variable_to_share[0],4)
    y=np.hsplit(variable_to_share[1],4)
    A=x[3]
    B=y[3]
    suma = np.zeros(dtype=int, shape=np.shape(A))
    resta = np.zeros(dtype=int, shape=np.shape(A))
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            suma[i][j] = A[i][j] + B[i][j]
    
    for i in range(np.shape(A)[0]):
        for j in range(np.shape(B)[1]):
            resta[i][j] = A[i][j] - B[i][j]
    respuestas4 = (suma, resta)
    comm.send(respuestas4,dest=5)
  
if rank ==5:
    variable_to_share = comm.bcast(variable_to_share, root=0)
    mat1 = variable_to_share[0]
    mat2 = variable_to_share[1]
    respuestas1 = comm.recv(source=1)
    respuestas2 = comm.recv(source=2)
    respuestas3 = comm.recv(source=3)
    respuestas4 = comm.recv(source=4)
    sumaTotal = np.concatenate((respuestas1[0],respuestas2[0],respuestas3[0],respuestas4[0]))
    restaTotal = np.concatenate((respuestas1[1],respuestas2[1],respuestas3[1],respuestas4[1]))
    print("Suma de matrices")
    for i in range(5):
        print("%f + %f = %f" % (mat1[i][i], mat2[i][i], sumaTotal[i][i]))
    
    print("Resta de matrices")
    for i in range(5):
        print("%f - %f = %f" % (mat1[i][i], mat2[i][i], restaTotal[i][i]))

 

    

    
    
   