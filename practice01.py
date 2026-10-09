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


# int и float можно смешивать -> результат float

# float — приблизительный (
print(0.1 + 0.2 == 0.30000000000000004)

# Операции с str
# ------------------------------------------
print("abc")
print('abc')
# + конкатенация
a = "abc"
b = "xyz"
print(a + b)
# * повторение "ab" * 3
print("za" * 33)
# len()
print("    asd123\b\b\nf\aasdf\b    ")
print(len("    asd\nfasdf   566\t3434 "))
a1 = 45.6
print(a1)
# 1a = 45.6
# print(1a)
afs = 4
a = None
None1 = 34
a = 13
print(a)
A = 10
print(A)
print('I don\'t speak English')
print("I don't speak English")
a = 'это строка'

print(a)
# number = int(input("Введите число:"))
# print(type(number))
# name = input("Введите свое имя:")
# print(type(name))
name = "abcd"
# s[i] индекс "abc"[1]
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(len(name))
# s[i:j] срез "abcde"[1:4] "bcd"
mystring = "abcde"
print(mystring[1:3])
print(mystring[2:4])    # cd
# s[i:j:k] срез с шагом "abcde"[::2] "ace"
mystring = "ABCDEFGHI"
print(mystring[1:7:2])
# s[::-1] переворот "abc"[::-1] "cba"
print(mystring[::-1])
print(mystring[::-2])
# in / not in "bc" in "abcd"
print("BC" in mystring)
print("xyz4" not in "dsafxyzlkj")
mystring = "wetrwqer"

# s.upper()
print("abcd".upper())
print(mystring.upper())
# s.lower()
print("ASFDasdfEFE".lower())
# s.strip()
print("   ASFDasdfEFE  ".strip() + "|")
mystring = "    12345    "
print(mystring.strip() + "|")

# s.replace(a, b)
mystring = "kjhwerkjhwqerYUYqeuiur"
print(mystring.replace("qe", "**"))
print(mystring)
# s.split(sep)
mystring = "молоко, хлеб, сыр, колбаса"
mylist = mystring.split(",")
print("script execution is finished")
# s.find(sub)
mystring = 'Wer1246kjlwerIkj'
print(mystring.find("1"))
print("script execution is finished")
# s.startswith/endswith "abc".startswith("a")
mystring = "AbcdJLKJE2323"
is_starts_with_letter_A = mystring.startswith("Abc3")
print(is_starts_with_letter_A)
is_ends = mystring.endswith("23")
print(is_ends)
# s.isdigit() / isalpha()
mystring = "123478"
print(mystring.isdigit())

mystring = "abcd"
print(mystring.isalpha())
# f-strings
name = "Daulet"
apple_qnt = 4
# f-string
mystring = f"My name is {name}. У меня есть {apple_qnt} яблок"
mystring = f'asdf sadf sadf'
print(mystring)
mystring = "My name is " + name + ". У меня есть " + \
           str(apple_qnt) + " яблок"
print(mystring)
mystring = ("My name is " + name + ". У меня есть " +
           str(apple_qnt) + " яблок")
print(mystring)

# if
try:
    print("Сейчас будем проверять")
    num = int(input("Введите целое число (int):"))
    print("Все ок")
except ValueError as e:
    print("Вы ввели не число!")
    print(str(e))
    exit(10)
except Exception as e:
    print(str(e))
    exit(12)

if num >= 0:
    print(f"Число {num} положительное")
    print("Это ветка для True")

    if num > 10:
        print(f"Число {num} больше 10")

else:
    print(f"Число {num} отрицательное")
    print("Это ветка для False")
print("Программа завершена")
import this


