with open("file.txt", encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        num = len(value.split())
        print(f"Строка {index} содержит {num} слов")
