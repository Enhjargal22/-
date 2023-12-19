file_path = "C:\\Users\\ConceptD\Desktop\\3.2\\subjects.txt"


subject_dict = {}  # Словарь для хранения данных по предметам

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(':')  # Разделяем строку по символу ':'
        subject = parts[0].strip()  # Название предмета
        details = parts[1].split()  # Детали о занятиях
        total_lectures = total_practicals = total_lab = 0

        # Перебираем детали и суммируем количество занятий
        for detail in details:
            if '(л)' in detail:
                total_lectures += int(detail.replace('(л)', ''))
            elif '(пр)' in detail:
                total_practicals += int(detail.replace('(пр)', ''))
            elif '(лаб)' in detail:
                total_lab += int(detail.replace('(лаб)', ''))

        # Суммируем общее количество занятий
        total_lessons = total_lectures + total_practicals + total_lab

        # Записываем данные в словарь
        subject_dict[subject] = total_lessons

# Выводим словарь на экран
print("Словарь с общим количеством занятий по предметам:")
print(subject_dict)
