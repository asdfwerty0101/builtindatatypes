# Операции с int и float
# ---------------------------------------
a = 12
b = 5
print(a, b)
print(a + b)
c = a + b
print("c =", c)
x = 12.3
y = 5.8
print(x + y)
# + сложение
a = 20
b = 7
# - вычитание
print("a =", a)
print("b =", b)
print(a - b)
print(x - y)
# * умножение
print(a * b)
print("x =", x)
print("y =", y)
print(x * y)
# / деление (результат всегда float)
a = 6
b = 2
c = a / b
print(c, type(c))
# // целочисленное деление (результат всегда float)
c = a / b
print(c, type(int(c)))
print(6 // 4)
print(type(a))
a = 13.3
print(type(a))
print(12 // 5)
print(12.3 // 5)
print(12 // 5.1)
# % остаток от деления
print(14 % 5)
# возведение в степень 2  3
print(2 ** 3)   # 2 * 2 * 2
# -x унарный минус
print(3 ** 4)   # 3 * 3 * 3 * 3
print(10 ** 3)
print(4 ** 2)
print(3 ** 3)
print(8 ** 2)
print(2 ** 1)
print(2 ** -1)
print(2 ** -2)
# abs(x) модуль числа
print(abs(-4000))
print(abs(4000))
# round(x, n) округление round(3.14159, 2) 3.14
print(round(3.14159))
print(round(3.6))
print(round(3.14159, 3))
# min/max(a, b)
print(min(5, 2, 10))
print(min(5, 10))
print(min(5, 34, 234, 200, 234, 1))
print(max(5, 34, 234, 200, 234, 1))
print(max(-1, -3, -5))
# Сравнения чисел: ==, !=, <, >,
print(3 == 4)
z = 3 == 4
print(z)
print(3 != 4)
print(3 < 4)
print(3 > 4)
# <=, >= [0 < x < 20] and or not
print(3 <= 3)
print(x)
x = -20
print(0 < x <= 20)
# группировка скобками ()
print((2 + 3) * 4)
a = 2
b = 3
c = 4
print((a + b) * c)
x = -20
x = -20
print(x)
print(-x)
# is (идентичность объека)
a = 10
b = 10
print(a == b)
a = 2570
b = 2570
print(a is b)
