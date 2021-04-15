from functools import reduce


def my_func(el1, el2):
    return el1 * el2


my_list = [el for el in range(99, 1001) if el % 2 == 0]
print(f'Список\n{my_list}\nРезультат перемножения всех элементов списка\n{reduce(my_func, my_list)}')