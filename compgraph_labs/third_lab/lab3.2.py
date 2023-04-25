import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_ellipsoid_mesh(a, b, c, num_vertices=20):
    """
    Генерує вершини сітки, яка наближено передає форму еліпсоїда.

    Параметри:
        - a, b, c (float): Розміри еліпсоїда по осях x, y, z відповідно
        - num_vertices (int): Кількість вершин сітки, за замовчуванням 20

    Повертає:
        - vertices (numpy.ndarray): Масив вершин сітки еліпсоїда розміром (num_vertices^2, 3)
    """
    u = np.linspace(0, 2 * np.pi, num=num_vertices)  # Кути на площині x-y
    v = np.linspace(0, np.pi, num=num_vertices)  # Кути на площині y-z

    # Генерування масиву координат вершин
    vertices = []
    for uu in u:
        for vv in v:
            x = a * np.cos(uu) * np.sin(vv)
            y = b * np.sin(uu) * np.sin(vv)
            z = c * np.cos(vv)
            vertices.append([x, y, z])

    return np.array(vertices)


# Параметри еліпсоїда
a = 1.0
b = 0.5
c = 0.3

# Кількість вершин сітки
num_vertices = 20

# Генерування вершин сітки
vertices = generate_ellipsoid_mesh(a, b, c, num_vertices=num_vertices)

# Відображення сітки на графіку
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for i in range(num_vertices - 1):
    for j in range(num_vertices - 1):
        ax.plot([vertices[i * num_vertices + j, 0], vertices[i * num_vertices + j + 1, 0]],
                [vertices[i * num_vertices + j, 1], vertices[i * num_vertices + j + 1, 1]],
                [vertices[i * num_vertices + j, 2], vertices[i * num_vertices + j + 1, 2]],
                color='black')
        ax.plot([vertices[i * num_vertices + j, 0], vertices[(i + 1) * num_vertices + j, 0]],
                [vertices[i * num_vertices + j, 1], vertices[(i + 1) * num_vertices + j, 1]],
                [vertices[i * num_vertices + j, 2], vertices[(i + 1) * num_vertices + j, 2]],
                color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()