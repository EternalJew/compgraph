import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Генерація вершин сітки еліпсоїда
num_vertices = 50
a = 1  # напіввелика вісь
b = 2  # напівменша вісь
c = 3  # напіввисота
theta = np.linspace(0, 2*np.pi, num_vertices)
phi = np.linspace(0, np.pi, num_vertices)
theta, phi = np.meshgrid(theta, phi)
x = a * np.sin(phi) * np.cos(theta)
y = b * np.sin(phi) * np.sin(theta)
z = c * np.cos(phi)
vertices = np.array([x, y, z]).reshape(3, -1).T

# Відображення проекції на площину XY
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Проекція на площину XY')
for i in range(num_vertices-1):
    for j in range(num_vertices-1):
        ax.plot([vertices[i*num_vertices+j,0], vertices[i*num_vertices+j+1,0]],
                [vertices[i*num_vertices+j,1], vertices[i*num_vertices+j+1,1]],
                color='black')
        ax.plot([vertices[i*num_vertices+j,0], vertices[(i+1)*num_vertices+j,0]],
                [vertices[i*num_vertices+j,1], vertices[(i+1)*num_vertices+j,1]],
                color='black')
plt.show()

# Відображення проекції на площину XZ
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_title('Проекція на площину XZ')
for i in range(num_vertices-1):
    for j in range(num_vertices-1):
        ax.plot([vertices[i*num_vertices+j,0], vertices[i*num_vertices+j+1,0]],
                [vertices[i*num_vertices+j,2], vertices[i*num_vertices+j+1,2]],
                color='black')
        ax.plot([vertices[i*num_vertices+j,0], vertices[(i+1)*num_vertices+j,0]],
                [vertices[i*num_vertices+j,2], vertices[(i+1)*num_vertices+j,2]],
                color='black')
plt.show()

# Відображення проекції на площину YZ
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('Y')
ax.set_ylabel('Z')
ax.set_title('Проекція на площину YZ')
for i in range(num_vertices-1):
    for j in range(num_vertices-1):
        ax.plot([vertices[i * num_vertices + j, 1], vertices[i * num_vertices + j + 1, 1]],
                [vertices[i * num_vertices + j, 2], vertices[i * num_vertices + j + 1, 2]],
                color='black')
        ax.plot([vertices[i*num_vertices+j, 1], vertices[(i+1)*num_vertices+j, 1]],
                [vertices[i*num_vertices+j, 2], vertices[(i+1)*num_vertices+j, 2]],
                color='black')

plt.show()

# Відображення проекції на площину XYZ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Тривимірна проекція')
for i in range(num_vertices-1):
    for j in range(num_vertices - 1):
        ax.plot([vertices[i*num_vertices+j, 0], vertices[i*num_vertices+j+1, 0]],
                [vertices[i*num_vertices + j, 1], vertices[i*num_vertices + j + 1, 1]],
                [vertices[i*num_vertices + j, 2], vertices[i*num_vertices + j + 1, 2]],
                color='black')
        ax.plot([vertices[i * num_vertices + j, 0], vertices[(i + 1)*num_vertices + j, 0]],
                [vertices[i*num_vertices + j, 1], vertices[(i + 1)*num_vertices + j, 1]],
                [vertices[i*num_vertices + j, 2], vertices[(i + 1) * num_vertices + j, 2]],
                color = 'black')

plt.show()