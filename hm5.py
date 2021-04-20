from  random import randint


with open("text33.txt", 'w', encoding='utf-8') as f:
    my_list = [randint(1, 100) for _ in range(5)]
    f.write(' '.join(map(str, my_list)))

print(f'Сумма чисел равна {sum(my_list)}')