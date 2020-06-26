f_lines = []
# создаем словарь замен для заданных слов
word_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

# Открываем заданный файл для чтения всех строк в нем
with open('hw_5_4_text.txt', 'r') as f:
    f_lines = f.readlines()

# Записываем построчно новый файл с замененными значениями
with open('hw_5_4_ntext.txt', 'w') as f:
    for line in f_lines:
        print(word_dict.get(line.split('-')[0]) + '-' + line.split('-')[1], file=f, end='')
