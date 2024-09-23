def letters_indexes(startpos: str, endpos: str): # Возвращает индексы буквенных координат для вычисления их числовой дистанции относительно друг друга
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"] 
    letter_index_startpos = letters.index(startpos[0])
    letter_index_endpos = letters.index(endpos[0])
    return letter_index_startpos, letter_index_endpos


def move_figure_check(startpos: str, endpos: str, figure: str) -> bool: # Функция для проверки возможности шахматного хода
    if figure == "Пешка":
        if startpos[0] == endpos[0] and int(startpos[1]) == int(endpos[1]) - 1:
            return True
        else:
            return False

    if figure == "Ладья":
        if startpos[0] == endpos[0] or startpos[1] == endpos[1]:
            return True
        else:
            return False

    if figure == "Конь":
        letter_index_startpos, letter_index_endpos = letters_indexes(startpos, endpos)

        if (
            abs(int(startpos[1]) - int(endpos[1])) == 1
            and abs(letter_index_startpos - letter_index_endpos) == 2
        ) or (
            abs(int(startpos[1]) - int(endpos[1])) == 2
            and abs(letter_index_startpos - letter_index_endpos) == 1
        ):
            return True
        else:
            return False

    if figure == "Король":
        letter_index_startpos, letter_index_endpos = letters_indexes(startpos, endpos)

        if (
            abs(letter_index_endpos - letter_index_startpos) <= 1
            and abs(int(startpos[1]) - int(endpos[1])) <= 1
        ):
            return True
        else:
            return False

    if figure == "Слон":
        letter_index_startpos, letter_index_endpos = letters_indexes(startpos, endpos)

        if abs(letter_index_endpos - letter_index_startpos) == abs(int(startpos[1]) - int(endpos[1])):
            return True
        else:
            return False

    if figure == "Королева":
        letter_index_startpos, letter_index_endpos = letters_indexes(startpos, endpos)

        if (abs(letter_index_endpos - letter_index_startpos) == abs(int(startpos[1]) - int(endpos[1]))) or (
            startpos[0] == endpos[0] or startpos[1] == endpos[1]
        ):
            return True
        else:
            return False


print(move_figure_check("c3", "a1", "Королева"))
print(move_figure_check("c3", "b3", "Ладья"))
print(move_figure_check("a1", "c3", "Слон"))
print(move_figure_check("a1", "b3", "Конь"))
print(move_figure_check("b1", "b2", "Пешка"))
print(move_figure_check("a1", "b2", "Король"))
