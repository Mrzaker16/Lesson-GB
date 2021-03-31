profit = int(input("Введите выручку фирмы "))
loss = int(input("Введите издержки фирмы "))
if profit > loss:
    print("Фирма отработала с прибылью")

    rent = profit // loss
    print(rent)
    workers = int(input("Введите количество сотрудников фирмы"))
    profit_workers = profit // workers
    print("прибыль в расчете на одного сторудника сотавила %d" % profit_workers)
elif profit == loss:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
