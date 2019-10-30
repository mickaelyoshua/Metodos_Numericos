import numpy as np

def gauss_piv(A):
  M=A.copy()
  x=np.zeros(M.shape[0])
  
  for j in range(M.shape[0]-1):         #Loop para pivotação parcial
    indice=np.argmax(M[j:,j])+j
    M[[indice,j]]=M[[j,indice]]
    
    for i in range(M.shape[0]-1):       #Gera a matriz triangular superior
      if i==j:
        pivo=M[i,j]
      mul=M[i+1,j]/pivo
      M[i+1,:]=M[i+1,:]-M[j,:]*mul
      
  for j in range(M.shape[0]-1, -1, -1): #Obtém as raízes
    x[j]=M[j,-1]/M[j,j]
    for i in range(j):
      M[i,-1]=M[i,-1]-x[j]*M[i,j]
      M[i,j]=0.0
  return x
