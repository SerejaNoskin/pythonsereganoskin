import unittest
import sys, os
from tdd_test.TDD_test import *

sys.path.append(os.getcwd())

class TestBot(unittest.TestCase):
    def test_1(self):
        self.assertEqual('Сергей','Сергей')

    def test_2(self):
        self.assertEqual(20, 20)

if __name__ == '__main__':
    unittest.main()