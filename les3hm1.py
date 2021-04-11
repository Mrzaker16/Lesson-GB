def my_func():
    arg1 = int(input("Input dividend "))
    arg2 = int(input("Input divider "))
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Divider can't be null")


print(my_func())
