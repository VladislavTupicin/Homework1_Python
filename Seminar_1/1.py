# Номер 1
#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day = int(input())
# if day in range(1, 8):
#     if day == 6 or day == 7:
#         print('ДА')
#     else:
#         print('НЕТ')   
# else:
#     print('Неправильное число') 


# Номер 2
#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in (0, 1):
#     for y in (0, 1):
#         for z in (0, 1):
#             print(x, y, z, end=' : ')
#             print(not (x or y or z) == ((not x) and (not y) and (not z)))


# Номер 3
# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x, y = int(input()), int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)


# Номер 4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input())
# if a in range(1, 5):
#     if a == 1:
#         print('x > 0 ; y > 0')
#     elif a == 2:
#         print('x < 0 ; y > 0')
#     elif a == 3:
#         print('x < 0 ; y < 0')
#     elif a == 4:
#         print('x > 0 ; y < 0')
# else:
#     print('Введите чило от 1 до 4') 


# Номер 5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# import math
# x1, y1 = int(input('x1 = ')), int(input('y1 = '))
# x2, y2 = int(input('x2 = ')), int(input('y2 = '))
# bc = x1 - x2
# ac = y2 - y1
# print(int(math.sqrt(ac ** 2 + bc ** 2) * 100) / 100)
