# Импорт библиотек: модуль работы со строками, модуль для
# определения кодировки текста, модуль работы с регулярными выражениями
import string
import chardet
import re

# Определение класса WordsFinder
class WordsFinder:
    # Конструктор для хранения произвольного количества имён файлов
    def __init__(self, *file_names):
        self.file_names = file_names

    # Функция извлечения слов из файлов и составления словаря
    def get_all_words(self):
        all_words = {}

        # Цикл чтения файлов с определенгием кодировки
        for file_name in self.file_names:
            try:
                with open(file_name, 'rb') as file:
                    rawdata = file.read()
                    result = chardet.detect(rawdata)
                    encoding = result['encoding']

                with open(file_name, 'r', encoding=encoding) as file:
                    text = file.read().lower()  # Приводим текст к нижнему регистру
                    # Удаляем пунктуацию, включая апостроф
                    text = re.sub(r"[{}]+".format(re.escape(string.punctuation.replace("'", ""))), ' ', text).strip()
                    words = text.split() # Разделение текста на слова с пробелами и сохранение их в словарь
                    all_words[file_name] = words
            except FileNotFoundError: # Обраблотка ошибок
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при обработке файла {file_name}: {e}")

        return all_words # Возврат результата (словарь)

    # Функция поиска позиции первого вхождения слова в каждом файле
    # Приводит искомое слово к нижнему регистру и инициализирует пустой словарь для хранения позиций
    def find(self, word):
        word = word.lower()
        found_positions = {}
        all_words = self.get_all_words()

        # Цикл проходит по всем словам в каждом файле и, если слово найдено,
        # сохраняет его позицию (индекс + 1, чтобы сделать его более понятным для пользователя)
        for file_name, words in all_words.items():
            if word in words:
                found_positions[file_name] = words.index(word) + 1
        return found_positions

    # Метод для подсчета количества вхождений слова в каждом файле
    # Приводит искомое слово к нижнему регистру и инициализирует пустой словарь для хранения подсчетов
    def count(self, word):
        word = word.lower()
        word_counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)
        # Возвращает словарь с количеством вхождений слова
        return word_counts


# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))  # Позиция слова 'TEXT'
print(finder.count('teXT'))  # Количество слов 'teXT'