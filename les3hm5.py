def my_sum ():
    sum_res = 0
    while True:
        number = input('Input numbers or Q for quit - ').split()
        res = 0
        for s in number:
            if s == 'q' or s == 'Q':
                break
            else:
                res = res + int(s)
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()
