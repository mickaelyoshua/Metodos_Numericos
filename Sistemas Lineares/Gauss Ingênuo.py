import numpy as np

def trian_sup(M):                        #Foi feita uma função a parte para deixar a matriz na forma de triângulo superior
  for j in range(M.shape[0]-1):
    for i in range(M.shape[0]-1):
      if i==j:
        pivo=M[i,j]                      #Definição do pivô
      mul=M[i+1,j]/pivo                  #Cálculo do multiplicador
      M[i+1,:]=M[i+1,:]-M[j,:]*mul       #Subtração e substituição das linhas zerando a coluna abaixo do pivô
  return M

def gauss_ingenuo(A):
  M=A.copy()                             #Tirada a cópia da matriz
  x=np.zeros(M.shape[0])                 #Matriz das raizes nulas
  M=trian_sup(M)                         #Retorna uma triângulo superior
  for j in range(M.shape[0]-1, -1, -1):  #Obtenção das raízes através da fórmula apresentada no método de Gauss Seidel
    independente=M[j,-1]
    soma=0.0
    for i in range(M.shape[0]):
      if j!=i:
        soma+=M[j,i]*x[i]
    x[j]=(independente-soma)/M[j,j]
   
