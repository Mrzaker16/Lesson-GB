features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
my_list = []
goods = int(input("Введите количество товара "))
feature_ = None
n = 1
while n <= goods:
    my_dict = dict({'name': input("введите название "), 'price': input("Введите цену "),
                    'quantity': input('Введите количество '), 'unit': input("Введите единицу измерения ")})
    my_list.append(my_dict)
    n += 1
analytics.pop(my_list)
print(my_list)
print(analytics)
