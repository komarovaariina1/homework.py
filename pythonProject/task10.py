#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16]
#[2, 3, 5, 6] => [12, 15]



from random import randint


num = int(input('Введите размер списка:  '))
list = []
list_prod = []

for i in range(num):
    list.append(randint(0, 20))

for i in range(len(list)):
    while i < len(list)/2 and num > len(list)/2:
        num = num - 1
        a = list[i] * list[num]
        list_prod.append(a)
        i += 1

print(f'{list} => {list_prod}')
