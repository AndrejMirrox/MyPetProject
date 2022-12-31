from datetime import date

def add_man():
    """
    Добавление людей
    """

    name = input("Фамилия и инициалы? ")
    post = input("Телефон? ")
    year = input("Год рождения? ")
    year = year.split(".")
    year = date(int(year[0]), int(year[1]), int(year[2]))

    # Создать словарь.
    man = {
        'name': name,
        'tel': post,
        'date': year,
    }

    # Добавить словарь в список.
    return man