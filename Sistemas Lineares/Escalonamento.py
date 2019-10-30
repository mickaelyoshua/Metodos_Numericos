import numpy as np

def trian_sup(M):
  for j in range(M.shape[0]-1):
    for i in range(M.shape[0]-1):
      if i==j:
        pivo=M[i,j]
      mul=M[i+1,j]/pivo
      M[i+1,:]=M[i+1,:]-M[j,:]*mul
  return M

def trian_inf(M):
  for j in range(M.shape[0]-1, 0, -1):
    for i in range(M.shape[0]-1, 0, -1):
      if i==j:
        pivo=M[i,j]
      mul=M[i-1,j]/pivo
      M[i-1,:]=M[i-1,:]-M[j,:]*mul
  return M
