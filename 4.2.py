import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print("Alphabet:", ", ".join(self.letters))

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self, lang='En'):
        super().__init__(lang, string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "This is an example text in English."

# Пример использования классов
alphabet_obj = Alphabet('Custom', 'ABCDE')
alphabet_obj.print()
print(f"Number of letters: {alphabet_obj.letters_num()}")

eng_alphabet_obj = EngAlphabet()
eng_alphabet_obj.print()
print(f"Number of English letters: {eng_alphabet_obj.letters_num()}")

letter_to_check = 'A'
print(f"Is '{letter_to_check}' an English letter? {'Yes' if eng_alphabet_obj.is_en_letter(letter_to_check) else 'No'}")

example_text = EngAlphabet.example()
print(f"Example text in English: {example_text}")
