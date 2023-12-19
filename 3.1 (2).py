# Открываем файл для чтения с явным указанием кодировки
file_path = 'C:\\Users\\ConceptD\\Desktop\\3.2\\students.txt'  # Путь к файлу
with open(file_path, 'r', encoding='utf-8') as file:
    # Читаем строки из файла
    lines = file.readlines()

# Инициализируем пустые списки для каждого диапазона баллов
range_4_to_6 = []
range_6_to_8 = []
above_8 = []

# Инициализируем переменную для хранения максимального балла и фамилии студента с этим баллом
max_score = 0
max_score_student = ""

# Анализируем каждую строку файла
for line in lines:
    # Разделяем строку на фамилию и средний балл
    parts = line.split()
    if len(parts) == 2:
        surname = parts[0]
        score = float(parts[1])

        # Добавляем фамилию в соответствующий диапазон баллов
        if 4 <= score < 6:
            range_4_to_6.append(surname)
        elif 6 <= score < 8:
            range_6_to_8.append(surname)
        elif score >= 8:
            above_8.append(surname)

        # Проверяем, является ли текущий балл максимальным
        if score > max_score:
            max_score = score
            max_score_student = surname

# Выводим результаты
print("Студенты с баллами от 4 до 6:", ', '.join(range_4_to_6))
print("Студенты с баллами от 6 до 8:", ', '.join(range_6_to_8))
print("Студенты с баллами выше 8:", ', '.join(above_8))
print(f"Студент с максимальным баллом: {max_score_student} ({max_score})")
