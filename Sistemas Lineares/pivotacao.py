import numpy as np

def pivotacao(M):                # Função para prática de pivotação
  for i in range(M.shape[0]-1):
    indice=np.argmax(M[i:,i])+i
    M[[indice,i]]=M[[i,indice]]
  return M
