#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#6 -> да
#7 -> да
#1 -> нет

print('введите число, обозначающее день недели')
a = float(input())
if  6 <= a <=7:
    print('Да')
elif 0 < a < 6:
    print('Нет')
else:
    print('В неделе всего 7 дней')