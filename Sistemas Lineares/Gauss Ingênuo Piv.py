import numpy as np

def gauss_ingenuo_piv(M):
  x=np.zeros(M.shape[0]) #gera o vetor de respostas nulo
  
  for j in range(M.shape[0]-1):
    indice=np.argmax(M[j:,j])+j #faz pivotamento
    M[[indice,j]]=M[[j,indice]]
    
    for i in range(M.shape[0]-1): #gera a matriz triângular superior
      if i==j:
        pivo=M[i,j]
      mul=M[i+1,j]/pivo
      M[i+1,:]=M[i+1,:]-M[j,:]*mul
      
  for j in range(M.shape[0]-1, -1, -1): #obtém as raízes
    x[j]=M[j,-1]/M[j,j]
    for i in range(j):
      M[i,-1]=M[i,-1]-x[j]*M[i,j]
      M[i,j]=0.0
  return x

A=np.array([[1,2,1,12],[1,-3,5,1],[2,-1,3,10]], dtype=float)

print(gauss_ingenuo_piv(A))