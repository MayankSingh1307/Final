from deep_translator import MyMemoryTranslator

def translate_french_to_english(text):
    translator = MyMemoryTranslator(source='fr', target='en')
    translated_text = translator.translate(text)
    return translated_text
