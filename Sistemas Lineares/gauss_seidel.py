import numpy as np

def gauss_seidel(A, it_max, tol):
  M=A.copy()
  erro=np.zeros(M.shape[0])        #Matriz de erros
  x=np.zeros(M.shape[0])           #Matriz das raizes atuais
  x_ant=np.zeros(M.shape[0])       #Matriz das raizes anteriores
  test=0                           #Variáveis test e count para testar convergência do sistema
  count=0
  
  for l in range(M.shape[0]):      #Teste da convergência
    for c in range(M.shape[0]-1):
      if l!=c:
        test+=abs(M[l,c])
    if abs(M[l,l])<=test:
      count+=1
      
  if count>0:
    print("Sistema linear pode não convergir.")

  for it in range(it_max):        #Defini o limite de iterações pela quantidade especificada
    for i in range(M.shape[0]):   #Obtenção das raízes
      independente=M[i,-1]
      soma=0.0

      for j in range(M.shape[0]):
        if j!=i:
          soma+=M[i,j]*x[j]
      x[i]=(independente-soma)/M[i,i]

    erro[i]=abs((x[i]-x_ant[i])/x[i])*100  #Cálculo do erro
    x_ant=x.copy()

    if erro.max()<=tol:                    #Verificação do erro de maior valor
      break                                #Causa a parada quando o valor máximo do erro entre as 3 raízes chega ao limite de tolerância

  return x, erro
