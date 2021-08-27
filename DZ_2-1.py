import random

gamer_name = input('Введите ваше имя\n')
print(f'Здравствуйте, {gamer_name.title()}')
point = 10000
print(f'На вашем счету {str(point)} единиц')

while point > 0:
    try:
        game = int(input('\nУгадайте выпавшее число\n'))
        if game > 1 and game < 13:
            a = random.randint(2, 12)
            print(f'Вы задумали число {str(game)}, а выпало число {str(a)}')
            if game == a:
                point += 1000
                print('Поздравляем! Вы угадали!')

            else:
                point -= 1000
                print('К сожалению, вы не угадали число')
            print(f'На вашем счету {str(point)} очков')
        else:
            print('Пожалуйста, введите число от 1 до 12')

    except ValueError:
        print('Пожалуйста, введите число от 2 до 12')
print('Игра окончена\n')
