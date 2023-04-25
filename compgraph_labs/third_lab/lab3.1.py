import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def generate_ellipsoid_mesh(a, b, c, num_vertices=20):
    """
    Генерує вершини сітки, яка наближено передає форму еліпсоїда.

    Параметри:
        - a, b, c (float): Розміри еліпсоїда по осях x, y, z відповідно
        - num_vertices (int): Кількість вершин сітки, за замовчуванням 20

    Повертає:
        - vertices (numpy.ndarray): Масив вершин сітки еліпсоїда розміром (num_vertices, 3)
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

# Генерування вершин сітки
vertices = generate_ellipsoid_mesh(a, b, c, num_vertices=20)

# Відображення сітки на графіку
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='black', marker='o', s=10)
plt.show()