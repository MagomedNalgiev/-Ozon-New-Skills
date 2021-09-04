anya = {'Секретные материалы': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
olya = {'Клан Сопрано': 'криминал', '24': 'драма', 'Во все тяжкие': 'криминал', 'Карточный домик': 'драма'}
nastya = {'Ведьмак': 'фэнтази', 'Игра престолов': 'фэнтази'}
sveta = {'Черное зеркало': 'фантастика', 'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

# Находим количество общих фильмов в словарях 'anya' и 'olya'
matches_with_olya = set(anya) & set(olya)
print(f'Число общих любимых сериалов с Олей: {len(matches_with_olya)}')

# Находим количество общих фильмов в словарях 'anya' и 'nastya'
matches_with_nastya = set(anya) & set(nastya)
print(f'Число общих любимых сериалов с Настей: {len(matches_with_nastya)}')

# Находим количество общих фильмов в словарях 'anya' и 'sveta'
matches_with_sveta = set(anya) & set(sveta)
print(f'Число общих любимых сериалов со Светой: {len(matches_with_sveta)}\n')


# Данное условие выводит результат с подругой, у которой больше всего общих любимых сериалов с Аней
if matches_with_olya == max(matches_with_olya, matches_with_nastya, matches_with_sveta):
  print(f'У Оли больше всего общих любимых сериалов с Аней.\n')
elif matches_with_nastya == max(matches_with_olya, matches_with_nastya, matches_with_sveta):
  print(f'У Насти больше всего общих любимых сериалов с Аней.')
else:
  print(f'У Светы больше всего общих любимых сериалов с Аней.')
