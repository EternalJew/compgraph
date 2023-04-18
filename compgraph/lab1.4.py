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

# Початкові координати трикутника
x0 = 0
y0 = 0

# Розмір та кольори трикутника
m = 10
clvis = 'blue'
clunvis = 'gray'

# Відображення рухомого зображення фігури ###TASK 4###
# for i in range(101):  # 101 крок
#     plt.clf()  # Очищення попереднього малюнку
#     draw_triangle(x0, y0, m, clvis, clunvis)  # Малювання трикутника
#     x0 += 0.1  # Зміна значення координати Х
#     plt.xlim(0, 10)  # Встановлення меж для осі абсцис
#     plt.ylim(0, 10)  # Встановлення меж для осі ординат
#     plt.pause(0.01)  # Затримка для анімації

# Відображення рухомого зображення фігури вздовж діагоналі ###TASK 5###
for i in range(101):  # 101 крок
    plt.clf()  # Очищення попереднього малюнку
    draw_triangle(x0, y0, m, clvis, clunvis)  # Малювання трикутника
    x0 += 0.1  # Зміна значення координати X
    y0 += 0.1  # Зміна значення координати Y
    m -= 0.1  # Зменшення розміру фігури
    plt.xlim(0, 10)  # Встановлення меж для осі абсцис
    plt.ylim(0, 10)  # Встановлення меж для осі ординат
    plt.pause(0.01)  # Затримка для анімації


plt.show()


