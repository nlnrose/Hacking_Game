import unittest
from generator import generator
class generator_test(unittest.TestCase):
    def test_generate_list(self):
        gen = generator()
        self.assertEqual(gen.generate_list().__len__(), 3)
        pass