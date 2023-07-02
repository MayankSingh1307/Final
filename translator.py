from deep_translator import MyMemoryTranslator

def translate_english_to_french(text):
    translator = MyMemoryTranslator(source='en', target='fr')
    translated_text = translator.translate(text)
    return translated_text
