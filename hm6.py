a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
while a < b:
    a = a + 0.1 * a
    result_days += 1
print("Вы достигнете требуемых показателей на %d день" % result_days)
