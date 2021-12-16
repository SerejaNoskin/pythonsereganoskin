import unittest
import sys, os
from unittest.mock import patch, Mock

import builder

sys.path.append(os.getcwd())
from builder import *

class Product_Builder_Test(unittest.TestCase):
    @patch.object(builder.Product_Builder(), 'product')
    def test_potato(self, mock_chair):
        mock_potato.return_value = None
        self.assertEqual(Product_Builder().potato(), None)
