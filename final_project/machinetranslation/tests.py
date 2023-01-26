import unittest 

from translator import french_to_english, english_to_french

class TestEtoF(unittest.TestCase):
    def test1(self):
        self.assertIsNot(english_to_french(''), 'Bonjour')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
class TestFtoE(unittest.TestCase):
    def test1(self):
        self.assertIsNot(french_to_english(''), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()