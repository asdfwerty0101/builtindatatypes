"""
Создать калькулятор.
Входные данные - 2 строки, которые должны
представлять собой 2 числа типа int или float.
Входные строки должны вводиться с консоли.
Необходимо реализовать операции + - * /
Результат вывести в консоль.
предусмотреть exception при делении на 0
"""
frame_str = "=" * 12
print(f"{frame_str} Простой калькулятор {frame_str}")
a_number_str = input("Введите число A:")
print(a_number_str)
print(type(a_number_str))
b_number_str = input("Введите число B:")
print(b_number_str)
print(type(b_number_str))

a_number = int(a_number_str)
