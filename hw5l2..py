my_list = [7, 5, 3, 3, 2]
add_element = int(input("Enter new element"))
a = 0
for i in my_list:
    if add_element <= i:
        a += 1
my_list.insert(a, add_element)
print(my_list)