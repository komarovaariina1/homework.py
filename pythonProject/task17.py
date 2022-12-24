# Реализовать алгоритм перемешивания списка.

import random
my_list = [random.randint(0,10) for i in range(random.randint(5,41))]
print(f"исходный список:\n {my_list}")
random.shuffle(my_list)
print(f"список после перемешивания:\n{my_list}")