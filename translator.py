# translate str_to_translate.txt file to spanish
from translate import Translator

with open('str_to_translate.txt', 'r') as file:
    translator = Translator(to_lang='es')
    text = file.read()
    translation = translator.translate(text)
    print(translation)