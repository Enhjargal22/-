class MyList:
    def __init__(self):
        self.data = []

    def add_element(self, element):
        """
        Метод для добавления элемента в список.
        """
        self.data.append(element)

    def remove_element(self, element):
        """
        Метод для удаления элемента из списка.
        """
        if element in self.data:
            self.data.remove(element)
            print(f"Элемент {element} удален из списка.")
        else:
            print(f"Элемент {element} не найден в списке.")

    def get_length(self):
        """
        Метод для получения длины списка.
        """
        return len(self.data)

    def get_elements(self):
        """
        Метод для получения всех элементов списка.
        """
        return self.data

    def clear_list(self):
        """
        Метод для очистки списка.
        """
        self.data = []
        print("Список очищен.")

    def find_element(self, element):
        """
        Метод для поиска элемента в списке.
        """
        return element in self.data

# Пример использования класса MyList
my_list = MyList()

my_list.add_element(1)
my_list.add_element(2)
my_list.add_element(3)

print(f"Список: {my_list.get_elements()}")
print(f"Длина списка: {my_list.get_length()}")

my_list.remove_element(2)

print(f"Список после удаления элемента: {my_list.get_elements()}")
print(f"Длина списка: {my_list.get_length()}")

print(f"Элемент 3 {'найден' if my_list.find_element(3) else 'не найден'} в списке.")

my_list.clear_list()

print(f"Список после очистки: {my_list.get_elements()}")
print(f"Длина списка: {my_list.get_length()}")
