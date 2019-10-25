import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2-4

def cordas(f, xmin, xmax, tol, max_it):
    raiz=[]
    erro=[]
    
    if f(xmin)*f(xmax)>0:
        print("Esse intervalo não possui raiz")
        
    else:
        for i in range(max_it):
            raiz.append(xmax+((f(xmax)*(xmax-xmin))/(f(xmin)-f(xmax))))
            if f(xmin)*f(raiz[i])<0:
                xmax=raiz[i]
            elif f(raiz[i])*f(xmax)<0:
                xmin=raiz[i]
            else:
                print("Ocorreu um erro")
                break
            if i>0:
                erro.append(abs((raiz[i]-raiz[i-1])/raiz[i])*100)
                if erro[-1]<tol:
                    break
        return raiz, erro
    
raiz, erro=cordas(f, 1, 16, 0.005, 200)
print(raiz)
print(erro)

x=np.arange(-10, 10, 0.1)
y=f(x)

plt.plot(x, y)
plt.grid(True)
plt.show()