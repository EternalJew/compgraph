import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Вхідні параметри многогранника
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]])
faces = np.array([[ 1, 2, 3], [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4]])

# Кут обертання
angle = np.pi/4

# Матриця обертання по вісі Z
rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                            [np.sin(angle), np.cos(angle), 0],
                            [0, 0, 1]])

# Виконати обертання вершин многогранника
rotated_vertices = np.dot(vertices, rotation_matrix.T)

# Функція для визначення видимості ребра на екрані
def is_edge_visible(vertex1, vertex2, view_vector):
    normal_vector = np.cross(vertex1, vertex2)
    return np.dot(normal_vector, view_vector) >= 0

# Визначити видимі ребра та їхні координати
visible_edges = []
for face in faces:
    for i in range(len(face)):
        vertex1 = rotated_vertices[face[i]]
        vertex2 = rotated_vertices[face[(i+1) % len(face)]]
        if is_edge_visible(vertex1, vertex2, [0, 0, 1]):
            visible_edges.append([vertex1, vertex2])

# Візуалізація результату
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

for edge in visible_edges:
    xs = [edge[0][0], edge[1][0]]
    ys = [edge[0][1], edge[1][1]]
    zs = [edge[0][2], edge[1][2]]
    ax.plot(xs, ys, zs)

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

plt.show()