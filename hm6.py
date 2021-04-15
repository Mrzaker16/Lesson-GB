from itertools import count, cycle

for el in count(int(input('Введите стартовое число до 10'))):
    if el == 10 or el > 10:
        break
    print(el)

my_cycle = cycle("ABC")
for _ in range(5):
    print("(my_cycle) = ({})".format(next(my_cycle)))