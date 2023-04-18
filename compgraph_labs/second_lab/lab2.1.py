import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


vertices = np.array([
    [0, 0, 0],  # Вершина 1
    [1, 0, 0],  # Вершина 2
    [0.5, np.sqrt(3)/2, 0],  # Вершина 3
    [0.5, 0.5*np.sqrt(3)/2, np.sqrt(6)/2],  # Вершина 4
    [0, 0, np.sqrt(6)/2],  # Вершина 5
    [1, 0, np.sqrt(6)/2]  # Вершина 6
])

faces = [
    [0, 1, 2],  # Грань 1 (трикутник): вершини 1, 2, 3
    [0, 3, 4],  # Грань 2 (трикутник): вершини 1, 4, 5
    [1, 3, 5],  # Грань 3 (трикутник): вершини 2, 4, 6
    [2, 4, 5],  # Грань 4 (трикутник): вершини 3, 5, 6
    [0, 2, 3, 1],  # Грань 5 (четирикутник): вершини 1, 3, 4, 2
    [1, 5, 4, 3]  # Грань 6 (четирикутник): вершини 2, 6, 5, 4
]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Додати вершини
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='red', marker='o')

# Додати грані
for face in faces:
    ax.add_collection(Poly3DCollection([vertices[face]], alpha=.25, facecolor='cyan', linewidths=1, edgecolors='black'))

# Встановити межі координатних осей
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, np.sqrt(6)/2])

plt.show()

# Функція для обертання моделі
def rotate_prism(theta_x, theta_y, theta_z):
    # Обертання навколо осі X
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(theta_x), -np.sin(theta_x)],
                   [0, np.sin(theta_x), np.cos(theta_x)]])
    # Обертання навколо осі Y
    Ry = np.array([[np.cos(theta_y), 0, np.sin(theta_y)],
                   [0, 1, 0],
                   [-np.sin(theta_y), 0, np.cos(theta_y)]])
    # Обертання навколо осі Z
    Rz = np.array([[np.cos(theta_z), -np.sin(theta_z), 0],
                   [np.sin(theta_z), np.cos(theta_z), 0],
                   [0, 0, 1]])

    # Виконати обертання для кожної вершини
    rotated_vertices = np.dot(Rz, np.dot(Ry, np.dot(Rx, vertices.T))).T

    return rotated_vertices

# Обертати модель навколо осей
theta_x = np.deg2rad(30)  # Кут обертання навколо осі X (30 градусів)
theta_y = np.deg2rad(45)  # Кут обертання навколо осі Y (45 градусів)
theta_z = np.deg2rad(60)  # Кут обертання н

# Оригінальна модель
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Додати вершини
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='red', marker='o')

# Додати грані
for face in faces:
    ax.add_collection(Poly3DCollection([vertices[face]], alpha=.25, facecolor='cyan', linewidths=1, edgecolors='black'))

# Встановити межі координатних осей
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, np.sqrt(6)/2])

plt.show()

# Обернута модель
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Обернуті вершини
rotated_vertices = rotate_prism(theta_x, theta_y, theta_z)

# Додати вершини
ax.scatter(rotated_vertices[:, 0], rotated_vertices[:, 1], rotated_vertices[:, 2], c='red', marker='o')

# Додати грані
for face in faces:
    ax.add_collection(Poly3DCollection([rotated_vertices[face]], alpha=.25, facecolor='cyan', linewidths=1, edgecolors='black'))

# Встановити межі координатних осей
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, np.sqrt(6)/2])

plt.show()