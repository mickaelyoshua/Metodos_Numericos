import numpy as np

def pivotacao(M):                # Função para prática de pivotação
  for i in range(M.shape[0]-1):
    indice=np.argmax(M[i:,i])+i
    M[[indice,i]]=M[[i,indice]]
  return M

A=np.array([[1,2,1,12],[1,-3,5,1],[2,-1,3,10]], dtype=float)

print(pivotacao(A))