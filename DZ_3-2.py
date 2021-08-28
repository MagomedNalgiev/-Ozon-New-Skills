print('Таблица умножения:\n')

#Задаем цикл для первого множителя
for first_multiplier in range(1, 10):
  print(f'------{first_multiplier}------')


  #Задаем цикл для второго множителя и выводим операции на экран
  for second_multiplier in range(1, 11):
    print(f'{first_multiplier} * {second_multiplier} = {first_multiplier * second_multiplier}')
  print(f'------------\n')