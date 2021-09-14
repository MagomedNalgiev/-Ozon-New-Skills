filename = 'diary.txt'
# Открываем файл в режиме записи
with open(filename, 'a') as diary:
    # Просим пользователя ввести дату и события для записи в дневник
    date = str(input('Введите дату в формате dd.mm.yyyy:\n'))
    text = str(input('Расскажите о прошедших событиях\n'))

    # Запись данных, введенных пользователем в файл diary.txt
    diary.write(f'{date}\n')
    diary.write(f'{text}\n\n')

    diary.close()
