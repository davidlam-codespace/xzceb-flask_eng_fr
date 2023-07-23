"""
  The module translates Enlgish to French and French to English
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    English to French
    """
    my_translator = MyMemoryTranslator("english","french")
    return my_translator.translate(english_text)


def french_to_english(french_text):
    """
    French to English
    """
    my_translator = MyMemoryTranslator("french","english")
    return my_translator.translate(french_text)
