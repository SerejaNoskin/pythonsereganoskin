import unittest
import sys, os
from builder import *

sys.path.append(os.getcwd())

class Product_Builder_Test(unittest.TestCase):
    director = Director()
    builder = Product_Builder()
    director.builder = builder
    def test_Magnit_builder(self):
       print("Magnit: ")
       self.director.Magnit()
       self.builder.product.list_parts()

    def test_ATAK_builder(self):
        print("\nATAK: ")
        self.director.ATAK()
        self.builder.product.list_parts()

if __name__ == "__main__":
    unittest.main()
