#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).


lst = [2.3, 1, 3.3, 4.1, 5, 6.8]
new_lst = [round(i%1,2) for i in lst]
print(lst, '=>', max(new_lst) - min(new_lst))

