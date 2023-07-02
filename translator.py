import unittest
from translator import translate_english_to_french

class TranslatorTest(unittest.TestCase):

    def test_english_to_french_translation(self):
        english_text = "Hello, how are you?"
        expected_french_text = "Bonjour, comment ça va ?"
        translated_text = translate_english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

if __name__ == '__main__':
    unittest.main()
