import numpy as np

def trian_sup(M):
  for j in range(M.shape[0]-1):
    for i in range(M.shape[0]-1):
      if i==j:
        pivo=M[i,j]
      mul=M[i+1,j]/pivo
      M[i+1,:]=M[i+1,:]-M[j,:]*mul
  return M

def gauss_ingenuo(M):
  x=np.zeros(M.shape[0])
  M=trian_sup(M)
  for j in range(M.shape[0]-1, -1, -1):
    independente=M[j,-1]
    soma=0.0
    for i in range(M.shape[0]):
      if j!=i:
        soma+=M[j,i]*x[i]
    x[j]=(independente-soma)/M[j,j]
    
  return x

A=np.array([[1,2,1,12],[1,-3,5,1],[2,-1,3,10]], dtype=float)

print(gauss_ingenuo(A))