import sympy
from sympy.plotting import plot, plot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# configuração para outputs melhores no artigo, pode ser ignorado
sympy.init_printing(use_latex='png', scale=1.0, order='grlex',
                    forecolor='Black', backcolor='White',)


fig = plt.figure(figsize=(6, 4), facecolor=(1, 1, 1))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(*data, cmap='rainbow')
ax.set_xlabel('Pressure / atm')
ax.set_ylabel('Temperature / K')
ax.set_zlabel('Volume / l')

def animate(angle):    
    ax = plt.gca()  # gca = get current axis
    ax.view_init(30, angle)    
    
anim = animation.FuncAnimation(fig,
                               animate,
                               frames=361,  # 360° rotation  
                               interval=1,
                               repeat=False)

plt.show()