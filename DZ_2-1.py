import random

#Спрашиваем имя игрока и выводим текст с приветствием и количеством очков
gamer_name = input('Введите ваше имя:\n')
print(f'Здравствуйте, {gamer_name.title()}')
point = 10000
print(f'На вашем счету {str(point)} единиц')

while point > 0:
    try:

        #Просим игрока ввести число, которое выпадет
        game = int(input('\nУгадайте выпавшее число\n'))


        #Задаем условие, на случай, если игрок введет число от 2 до 12
        if game > 1 and game < 13:


            #Передаем в переменную dice_roll случайное число от 2 до 12
            dice_roll = random.randint(2, 12)
            print(f'Вы задумали число {str(game)}, а выпало число {str(dice_roll)}')


            #Задаем условие, которое добавляет или отнимает очки в зависимости от того, угадал игрок число или нет
            if game == dice_roll:
                point += 1000
                print('Поздравляем! Вы угадали!')
            else:
                point -= 1000
                print('К сожалению, вы не угадали число')


            #Выводим количество очков игрока
            print(f'На вашем счету {str(point)} очков')


        #Задаем условие, на случай, если игрок введет число не от 2 до 12
        else:
            print('Пожалуйста, введите число от 1 до 12')


    #Задаем исключение на случай, если игрок введет текст вместо числа
    except ValueError:
        print('Пожалуйста, введите число от 2 до 12')

print('Игра окончена\n')
