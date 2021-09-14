filename = 'lesson05_cats_of_ulthar.txt'

# Открытие файла в режиме чтения
with open(filename, 'r') as file_object:
    lines = file_object.readlines()


cat_count = 0
# Цикл перебирает все слова в файле и считает, сколько раз встречается слово "кошка"
for line in lines:
    for word in line.split():
        if word == 'кошка':
            cat_count += 1

print(f'Слово "кошка" встречается в файле {cat_count} раз\n')

# Цикл перебирает все строки в файле и выводит те, в которых встречается слово "кошка"
for line in lines:
    if 'кошка' in line.split():
        print(line.strip())
        