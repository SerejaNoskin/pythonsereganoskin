from operator import itemgetter

class Browser:

    """Браузер"""

    def __init__(self, id, naz, kol_str, kol_zap):
        self.id = id
        self.naz = naz
        self.kol_str = kol_str
        self.kol_zap = kol_zap


class Computer:
    """ Компьютеры """

    def __init__(self, id, mode):
        self.id = id
        self.mode = mode  # виды компьютеров


class ComputerBrowser:

    def __init__(self, browsers_id, computers_id):
        self.browsers_id = browsers_id
        self.computers_id = computers_id


# Компьютеры
computers = [
    Computer(1, 'Асус'),
    Computer(2, 'МСИ'),
    Computer(3, 'Асер'),
    Computer(4, 'Леново'),
]

# Браузеры
browsers = [
    Browser(1, 'Мозилла', 50, 5),
    Browser(2, 'Яндекс', 30, 3),
    Browser(3, 'Гугл', 45, 4),
    Browser(4, 'Амиго', 44, 4),
    Browser(5, 'Ёхо', 45, 2),

]

computers_browsers = [
    ComputerBrowser(1, 4),
    ComputerBrowser(3, 2),
    ComputerBrowser(3, 3),
    ComputerBrowser(4, 5),
    ComputerBrowser(2, 1),
]
def Task1(one_to_many):
    print('Задание В1')
    res_11 = []
    for naz, kol_str, computers_name in one_to_many:
        if 'А' in naz[0]:
            res_11.append((naz, computers_name))
    return res_11
def Task2(one_to_many):
    print('Задание В2')
    buff = []
    for c in computers:
        # список видов компьютеров
        c_modes = list(filter(lambda i: i[2] == c.mode, one_to_many))
        if len(c_modes) > 0:
            c_kol_str = [kol_str for _, kol_str, _ in c_modes]
            min_kol_str = min(c_kol_str)
            buff.append((c.mode, min_kol_str))
    res_12 = sorted(buff, key=itemgetter(1))
    return res_12
def Task3(many_to_many):
    print('Задание В3')
    buff = []
    for naz, kol_str, computers_name in many_to_many:
        buff.append((naz, computers_name))
    res_13 = list(sorted(buff, key=itemgetter(0)))
    return res_13

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(b.naz, b.kol_str, c.mode)
                   for c in computers
                   for b in browsers
                   if b.kol_zap == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.mode, cb.computers_id, cb.browsers_id)
                                          for c in computers
                                          for cb in computers_browsers
                                          if c.id == cb.computers_id]

    many_to_many = [(b.naz, b.kol_str, computers_name)
                    for computers_name, computers_id, browsers_id in many_to_many_temp
                    for b in browsers if b.id == browsers_id]

    print('Test')  # вывод списков со связями 1-м, м-м
    res_0 = (one_to_many)
    print(res_0)
    res_01 = (many_to_many)
    print(res_01)
    Task1(one_to_many)
    Task2(one_to_many)
    Task3(many_to_many)


if __name__ == '__main__':
    main()