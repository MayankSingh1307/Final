import unittest
from translator import translate_french_to_english

class TranslatorTest(unittest.TestCase):

    def test_french_to_english_translation(self):
        french_text = "Bonjour, comment ça va ?"
        expected_english_text = "Hello, how are you?"
        translated_text = translate_french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
