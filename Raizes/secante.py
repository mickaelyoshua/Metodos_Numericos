import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2-4

def secante(f, xo, xi, tol, max_it):
    raiz=[]
    erro=[]
    raiz.append(xo)
    raiz.append(xi)
    
    for i in range(1, max_it):
        raiz.append(raiz[i]-f(raiz[i])*(raiz[i]-raiz[i-1])/(f(raiz[i])-f(raiz[i-1])))
        erro.append(abs((raiz[i]-raiz[i-1])/raiz[i])*100)
        
        if erro[-1]<tol:
            break
    return raiz, erro

raiz, erro= secante(f, 6, 8, 0.005, 200)

print(raiz)
print(erro)

x=np.arange(-10, 10, 0.1)
y=f(x)

plt.plot(x, y)
plt.grid(True)
plt.show()