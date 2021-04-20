import json

with open('text5.json', 'w', encoding='utf-8') as fe:
    with open('file_7.txt', encoding='utf-8') as fe1:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in fe1}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, fe, ensure_ascii=False, indent=4)