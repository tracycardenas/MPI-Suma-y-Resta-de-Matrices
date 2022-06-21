from unittest.mock import sentinel
import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD 
size = comm.size 
rank = comm.rank
print("my rank is %i" % (rank))

size_ = (1000,1000)
rows, columns = size_
recvdata = np.zeros((rows,int( columns/2)),dtype=float)
recvdata2 = np.zeros((rows,int( columns/2)),dtype=float)

recvdataResta = np.zeros((rows,int( columns/2)),dtype=float)
recvdata2Resta = np.zeros((rows,int( columns/2)),dtype=float)


if rank==0:
    matriz1 = np.random.randint(10, size=size_).astype("float") / 100
    matriz2 = np.random.randint(10, size=size_).astype("float") / 100
    #print("Suma de matrices")
    #for i in range(5):
    #    print("%f + %f = " % (matriz1[i][i], matriz2[i][i]))

    #print("Resta de matrices")
    #for i in range(5):
    #    print("%f - %f =" % (matriz1[i][i], matriz2[i][i]))

    x=np.hsplit(matriz1,2)
    y=np.hsplit(matriz2,2)
    
    mitad1 = (x[0],y[0])
    comm.send(mitad1,dest=1)
    mitad2 = (x[1],y[1])
    comm.send(mitad2,dest=1)


    senddata = np.zeros((rows,int( columns/2)),dtype=float)
    senddata2 = np.zeros((rows,int( columns/2)),dtype=float)

    senddataResta = np.zeros((rows,int( columns/2)),dtype=float)
    senddata2Resta = np.zeros((rows,int( columns/2)),dtype=float)

    
if rank==1:
    mitad1 = comm.recv(source=0)
    mitad2 = comm.recv(source=0)

    A1=mitad1[0]
    B1=mitad1[1]

    A2=mitad2[0]
    B2=mitad2[1]

    comm.send(B1,dest=2)
    comm.send(B2,dest=2)
    senddata = A1
    senddata2 = A2

    senddataResta =A1
    senddata2Resta = A2

if rank==2:
    B1 = comm.recv(source=1)
    B2 = comm.recv(source=1)
    senddata=B1
    senddata2=B2

    senddataResta=B1*(-1)
    senddata2Resta=B2*(-1)

    
comm.Reduce(senddata,recvdata,root=2,op=MPI.SUM)
comm.Reduce(senddata2,recvdata2,root=2,op=MPI.SUM)
comm.Reduce(senddataResta,recvdataResta,root=2,op=MPI.SUM)
comm.Reduce(senddata2Resta,recvdata2Resta,root=2,op=MPI.SUM)

sumaTotal = np.concatenate((recvdata, recvdata2), axis=1)
restaTotal = np.concatenate((recvdataResta, recvdata2Resta), axis=1)
#print("RESULTADOS SUMA")
#for i in range(5):
#  print(" = %f" % (sumaTotal[i][i]))

#print("RESULTADOS RESTA")
#for i in range(5):
#  print("= %f" % (restaTotal[i][i]))


