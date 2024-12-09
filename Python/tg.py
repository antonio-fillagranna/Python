import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y3 = [1,4,9,16,25,36,49,64,81,100]
z3 = np.zeros(10)
dx = np.ones(10)
dy = np.ones(10)
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ax.bar3d(x3,y3,z3, dx, dy, dz, zsort='average')
plt.show()