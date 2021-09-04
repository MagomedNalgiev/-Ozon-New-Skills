import numpy

try:
# Строки для ввода зарплат
  first_family_member_salary = int(input('Введите зарплату первого члена семьи\n'))
  second_family_member_salary = int(input('Введите зарплату второго члена семьи\n'))
  third_family_member_salary = int(input('Введите зарплату третьего члена семьи\n'))


#Строки для вывода среднего значения всех зарплат
  average_salary = [first_family_member_salary, second_family_member_salary, third_family_member_salary]
  print('Средняя зарплата всех членов семьи:')
  print(int(numpy.mean(average_salary)))


# Исключаем ошибку, если пользователь введет текст
except ValueError:
  print('Пожалуйста, введите число')