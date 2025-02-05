import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Definir las variables simbólicas
x, y = sp.symbols('x y')

# Definir la función multivariable
f = x**2 + 3*x*y

# Calcular las derivadas parciales
fx = sp.diff(f, x)
fy = sp.diff(f, y)

# Convertir a funciones numéricas
fx_lambda = sp.lambdify((x, y), fx, 'numpy')
fy_lambda = sp.lambdify((x, y), fy, 'numpy')
f_lambda = sp.lambdify((x, y), f, 'numpy')

# Crear una malla de valores para X e Y
X = np.linspace(-5, 5, 30)
Y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(X, Y)
Z = f_lambda(X, Y)
ZX = fx_lambda(X, Y)
ZY = fy_lambda(X, Y)

# Graficar la función
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
ax.quiver(X, Y, Z, ZX, ZY, np.zeros_like(Z), color='r', length=0.5, normalize=True, label='Derivadas Parciales')

# Etiquetas y leyenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
ax.set_title('Visualización de Derivadas Parciales')
plt.show()
