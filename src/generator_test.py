import unittest
from generator import generator
class generator_test(unittest.TestCase):
    def test_generate_list(self):
        gen = generator()
        generated_list = gen.generate_list()
        generated_list2 = gen.generate_list(3)
        generated_list3 = gen.generate_list(7)
        generated_list4 = gen.generate_list(2)
        self.assertEqual(generated_list.__len__(), 5)
        self.assertEqual(generated_list2.__len__(), 7)
        self.assertEqual(generated_list3.__len__(), 5)
        self.assertEqual(generated_list4.__len__(), 6)
        for option in generated_list:
            self.assertTrue(isinstance(option, str))
        for option in generated_list2:
            self.assertTrue(isinstance(option, str))
        for option in generated_list3:
            self.assertTrue(isinstance(option, str))
        for option in generated_list4:
            self.assertTrue(isinstance(option, str))
        pass