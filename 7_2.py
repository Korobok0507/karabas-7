def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1): # Получаем индекс строи начиная с 1
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(string + '\n')  # Записываем строку с переносом
            strings_positions[(index, byte_position)] = string  # Сохраняем информацию в словарь

    return strings_positions # Возвращаем словарь


# Пример использования
info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)