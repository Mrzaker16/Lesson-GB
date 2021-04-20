w = {}
with open("file2.txt", "r", encoding='utf-8') as g:
    for line in g:
     w[line.split()[0]] = float(line.split()[1])
print('< 20000')
for name, wage in w.items():
    if wage < 20000:
        print(name)
print(f"Сред  зп равна {sum(w.values()) / len(w)} ")
