import numpy as np

def gauss_seidel(M, it_max, tol):
  
  erro=np.zeros(M.shape[0])
  x=np.zeros(M.shape[0])
  x_ant=np.zeros(M.shape[0])
  test=0
  count=0
  
  for l in range(M.shape[0]):
    for c in range(M.shape[0]):
      if l!=c:
        test+=abs(M[l,c])
    if abs(M[l,l])<=test:
      count+=1
      
  if count>0:
    print("Sistema linear pode não convergir.")

  for it in range(it_max):
    for i in range(M.shape[0]):
      independente=M[i,-1]
      soma=0.0

      for j in range(M.shape[0]):
        if j!=i:
          soma+=M[i,j]*x[j]
      x[i]=(independente-soma)/M[i,i]

    erro[i]=abs((x[i]-x_ant[i])/x[i])*100
    x_ant=x.copy()

    if erro.max()<=tol:
      break

  return x, erro

A=np.array([[3, -0.1, -0.2, 7.85],[.1,7,-.3,-19.3],[.3,-.2,10,71.4]], dtype=float)

x, erro = gauss_seidel(A, 100, 0.001)
print(x)
print(erro)