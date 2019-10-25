import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2-4

def df(x):
    return 2*x

def newton(f, df, xo, tol, max_it):
    raiz=[]
    erro=[]
    raiz.append(xo)
    
    for i in range(max_it):
        raiz.append(raiz[i]-(f(raiz[i])/df(raiz[i])))
        erro.append(abs((raiz[i]-raiz[i-1])/raiz[i])*100)
        
        if erro[-1]<tol:
            break
    return raiz, erro

raiz, erro=newton(f, df, 16, 0.005, 200)

print(raiz)
print(erro)

x=np.arange(-10, 10, 0.1)
y=f(x)

plt.plot(x, y)
plt.grid(True)
plt.show()