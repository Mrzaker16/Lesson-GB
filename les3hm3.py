def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(
    f'Result - {my_func(int(input("Enter first argument ")), int(input("Enter second argument ")), int(input("Enter third argument ")))}')
