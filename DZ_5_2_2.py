import numpy


def same_genre_serials(show, genre):
    massive = []
    for key, value in show.items():
        if value == genre:
            massive.append(key)
    return massive


def shows_rating(rating, movies):
    average_list = []
    for key, value in rating.items():
        if key in movies:
            average_list.append(value)
    return numpy.mean(average_list)


