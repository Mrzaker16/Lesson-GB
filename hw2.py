create_list = int(input("Введите кол-во элементов списка"))
list_index = []
i = 0
k = 0
while i < create_list:
    list_index.append(input("Введите следующее значение списка "))
    i += 1
for elem in range(1, len(list_index), 2):
    list_index[k + 1], list_index[k] = list_index[k], list_index[k + 1]
print(list_index)
