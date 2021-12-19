import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class Test_task_1(unittest.TestCase):
    def test_task_1(self):
        one_to_many = [(b.naz, b.kol_str, c.mode)
                       for c in computers
                       for b in browsers
                       if b.kol_zap == c.id]

        self.assertEqual(Task1(one_to_many), [('Амиго', 'Леново')])

class Test_task_2(unittest.TestCase):
    def test_task_2(self):
        one_to_many = [(b.naz, b.kol_str, c.mode)
                       for c in computers
                       for b in browsers
                       if b.kol_zap == c.id]

        self.assertEqual(Task2(one_to_many),[('Асер', 30), ('Леново', 44), ('МСИ', 45)])


class Test_task_3(unittest.TestCase):
    def test_task_3(self):
        many_to_many_temp = [(c.mode, cb.computers_id, cb.browsers_id)
                             for c in computers
                             for cb in computers_browsers
                             if c.id == cb.computers_id]

        many_to_many = [(b.naz, b.kol_str, computers_name)
                        for computers_name, computers_id, browsers_id in many_to_many_temp
                        for b in browsers if b.id == browsers_id]
        self.assertEqual(Task3(many_to_many),
                         [('Гугл', 'МСИ'), ('Гугл', 'Асер'), ('Мозилла', 'Леново'), ('Яндекс', 'Асус')])
if __name__ == "__main__":
    unittest.main()