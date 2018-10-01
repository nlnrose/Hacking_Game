import unittest
from generator import generator
class generator_test(unittest.TestCase):
    def generate_list_test(self):
        self.assertEqual(generator.generate_list().length, 3)
        pass