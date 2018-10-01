import unittest
from generator import generator
class generator_test(unittest.TestCase):
    def test_generate_list(self):
        self.assertEqual(generator.generate_list().length, 3)
        pass