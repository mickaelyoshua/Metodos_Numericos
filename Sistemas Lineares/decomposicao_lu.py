def calcular_LU(M):
  U=M.copy()
  L=np.identity(U.shape[0])
  
  for j in range(U.shape[0]-1):
    for i in range(j+1,U.shape[0]):
        mul=U[i,j]/U[j,j]
        U[i,:]=U[i,:]-U[j,:]*mul     #Transformação em triangular superior
        L[i,j]=mul                   #Transformação em triangular inferior colocando os múltiplos na matriz
        
  return L, U
  
  def calcular_Z(L,B):                        #Cálculo da matriz z dos resultados transitórios
  Z=np.zeros(L.shape[0])

  for i in range(L.shape[0]):
    Z[i]=B[i]
    
    for j in range(i):
      Z[i]=Z[i]-L[i,j]*Z[j]
      
  return Z

def calcular_X(U,Z):                       #Cálculo das raizes do sitema linear
  X=np.zeros(U.shape[0])

  for i in range(U.shape[0]-1, -1, -1):
    X[i]=Z[i]
    
    for j in range(i+1, U.shape[0]):
      X[i]=X[i]-U[i,j]*X[j]
    X[i]=X[i]/U[i,i]
    
  return X
