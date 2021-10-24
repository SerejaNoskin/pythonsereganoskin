from contextlib import contextmanager# импортируем
import time

@contextmanager#декоратор позволяющий создавать контекстный менеджеры
def cm_timer_1():
    start = time.perf_counter()#начало отсчёта времени
    yield
    print("Время работы блока кода: {} секунд".format(time.perf_counter() - start))#вывод промежутка времени

class cm_timer_2:

    def __init__(self):
        self.start = time.perf_counter()#время начало принимает

    def __enter__(self):
        self.start = time.perf_counter()#присвоил начало

    def __exit__(self, exp_type, exp_value, traceback):#проверка на не 0 значение
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print("Время работы блока кода: {} секунд".format(time.perf_counter() - self.start))

with cm_timer_1():
    time.sleep(2)
with cm_timer_2():#вывод конец и начала
    time.sleep(2)
