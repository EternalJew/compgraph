import matplotlib.pyplot as plt
import numpy as np


def draw_triangle(x0, y0, m, clvis, clunvis):
    # Визначення координат вершин трикутника
    x1, y1 = x0, y0 + m
    x2, y2 = x0 + m, y0 + m
    x3, y3 = x0 + m/2, y0

    # Малювання видимих ребер трикутника
    plt.plot([x1, x2], [y1, y2], color=clvis)
    plt.plot([x2, x3], [y2, y3], color=clvis)
    plt.plot([x3, x1], [y3, y1], color=clvis)

    # Малювання невидимих ребер трикутника
    plt.plot([x1, x0], [y1, y0], color=clunvis)
    plt.plot([x2, x0], [y2, y0], color=clunvis)
    plt.plot([x3, x0], [y3, y0], color=clunvis)


###TASK 1###

#     # Відображення малюнка
#     plt.show()
#
# # Параметри фігури клин
# x0 = 0
# y0 = 0
# m = 5
# clvis = 'blue'
# clunvis = 'red'
#
# # Виклик функції для малювання фігури клин
# draw_triangle(x0, y0, m, clvis, clunvis)

###TASK 2###

# Генерація випадкових координат, розмірів та кольорів для 50 фігур
n_figures = 50
x0_values = np.random.randint(0, 100, size=n_figures)
y0_values = np.random.randint(0, 100, size=n_figures)
m_values = np.random.randint(5, 20, size=n_figures)
clvis_values = np.random.choice(['blue', 'green', 'red', 'orange'], size=n_figures)
clunvis_values = np.random.choice(['gray', 'black', 'purple'], size=n_figures)

# Розмір вкладених фігур  ###TASK 3###
nested_m = 5

# Малювання фігур з випадковими параметрами
for i in range(n_figures):
    draw_triangle(x0_values[i], y0_values[i], m_values[i], clvis_values[i], clunvis_values[i])

# Малювання вкладених фігур ###TASK3###
    for j in range(1, nested_m+1):
        nested_m_size = m_values[i] * j / nested_m
        nested_x0 = x0_values[i] + (m_values[i] - nested_m_size) / 2
        nested_y0 = y0_values[i] + (m_values[i] - nested_m_size) / 2
        draw_triangle(nested_x0, nested_y0, nested_m_size, clvis_values[i], clunvis_values[i])


# Відображення малюнків
plt.show()