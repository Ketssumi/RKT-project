import matplotlib.pyplot as plt
import numpy as np
import math

# параметры ракеты и взлёта
time = 250  # время работы первой ступени в секундах
m0 = 2965 * 10 ** 3  # начальная масса корабля в кг (включая топливо)
Ft = 34.5 * 10 ** 6  # тяга первой ступени в Н (34.5 MN для F-1)
k = 1200  # скорость расхода топлива в кг/с (примерно для первой ступени)
b = -0.001  # изменение угла движения ракеты в радианах/с
cf = 0.1  # коэффициент сопротивления
S = 133.01  # площадь лобового сопротивления в м^2

# константы
e = 2.71828  # основание натурального логарифма
shag = 0.1  # шаг времени (по желанию изменяемая переменная)
Ang0 = np.pi / 2  # начальный угол в радианах
G = 9.81  # ускорение свободного падения в м/с^2
M_A = 0.29  # молярная масса газа в кг/моль
R = 8.31  # универсальная газовая постоянная в Дж/(моль·К)
T = 300  # температура в К
P_0 = 10 ** 5  # начальное давление в Па
GAZ_P = M_A / (R * T)  # плотность газа

# инициализация списков для хранения значений
x_values = [0]  # координаты по оси X
y_values = [0]  # координаты по оси Y
vx_values = [0]  # скорость по оси X
vy_values = [0]  # скорость по оси Y
ax_values = [0]  # ускорение по оси X
ay_values = [-9.81]  # ускорение по оси Y (начальное значение - ускорение свободного падения)

# начальные значения
x = 0
y = 0
vx = 0
vy = 0
ax = 0
ay = 0

# основной цикл для расчета движения ракеты
for i in range(int(time // shag)):  # рассчитываем n сек
    t = i * shag  # текущее время
    # расчет плотности воздуха на высоте y
    rho = (GAZ_P * P_0) * (e ** (-G * y * GAZ_P))
    # расчет силы сопротивления по осям X и Y
    f_cx = cf * S * (rho * (vx_values[-1] ** 2) * 0.5)
    f_cy = cf * S * (rho * (vy_values[-1] ** 2) * 0.5)
    # расчет ускорения по оси X
    ax = ((Ft) * np.cos(Ang0 + b * t) - f_cx) / (m0 - k * t)
    # расчет ускорения по оси Y
    ay = ((Ft) * np.sin(Ang0 + b * t) - f_cy) / (m0 - k * t) - G
    # обновление скорости по осям X и Y
    vx = vx_values[-1] + ax * shag
    vy = vy_values[-1] + ay * shag
    # обновление координат по осям X и Y
    x = x_values[-1] + vx * shag
    y = y_values[-1] + vy * shag
    # добавление новых значений в списки
    ax_values.append(ax)
    ay_values.append(ay)
    vx_values.append(vx)
    vy_values.append(vy)
    x_values.append(x)
    y_values.append(y)

# построение графика высоты ракеты от времени
plt.title('Траектория взлета', fontsize=12, fontweight="bold")  # Заголовок графика
plt.xlabel("Время, (с)")  # подпись оси X
plt.ylabel('Высота (м)')  # Подпись оси Y
plt.grid()  # включение сетки на графике
plt.plot(x_values[::int(shag ** -1)], y_values[::int(shag ** -1)], color='green', label='Высота')  # линия высоты
plt.legend()  # отображение легенды
plt.show()  # отображение графика