import unittest

from translator import english_to_french, french_to_english

class TestE2f(unittest.TestCase): 
    def test1(self):
        self.assertIsNotNone(english_to_french(not None),not None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        

class TestF2e(unittest.TestCase): 
    def test1(self):
        self.assertIsNotNone(french_to_english(not None),not None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':        
    unittest.main()