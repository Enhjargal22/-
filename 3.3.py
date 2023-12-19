import json

file_path = "C:\\Users\\ConceptD\\Desktop\\3.2\\firms.txt"

firms_list = []  # Список для хранения словарей с прибылью фирм
total_profit = 0  # Переменная для хранения суммы прибыли всех фирм

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.split()
        name, ownership, revenue, costs = parts[0], parts[1], int(parts[2]), int(parts[3])
        profit = revenue - costs

        # Добавляем фирму и её прибыль в список
        firms_list.append({name: profit})

        # Если прибыль положительная, добавляем её к общей прибыли
        if profit > 0:
            total_profit += profit

# Рассчитываем среднюю прибыль (не учитывая убыточные фирмы)
average_profit = total_profit / len([firm for firm in firms_list if list(firm.values())[0] > 0])

# Добавляем словарь с средней прибылью в список
firms_list.append({"average_profit": round(average_profit)})

# Выводим полученный список
print("Список с прибылями и средней прибылью:")
print(firms_list)

# Сохраняем список в JSON-файл
json_file_path = 'firms_data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(firms_list, json_file)

print(f"Список сохранен в файл: {json_file_path}")
