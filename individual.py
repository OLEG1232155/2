import math

a = float(input("Меньшее основание трапеции = "))
b = float(input("Большее основание трапеции = "))
c = float(input("Угол при большем основании = "))

st = (b - a) / 2  # катет треугольниа
h = st * math.tan(c)  # высота трапеции
s = h * ((a + b) / 2)  # формула площади

print("Площадь трапеции = ", '%.3f' % s)
