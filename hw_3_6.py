def int_func(word):
    """Возвращает слово с первой заглавной буквой"""
    cap_word = word.capitalize()

    return cap_word


words_str = input("Введите слова через пробел: ")

# разбиваем строку в список слов и для каждого вызываем функцию int_func
new_words_str = list(map(int_func, words_str.split(' ')))

print(f"Результат обработки: {' '.join(new_words_str)}")
