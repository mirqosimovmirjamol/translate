from translate import Translator


def en_uz(text):
    translator = Translator(to_lang='uz', from_lang='en')
    natija = translator.translate(text)
    return natija


def uz_en(text):
    translator = Translator(to_lang='en', from_lang='uz')
    natija = translator.translate(text)
    return natija

def ru_en(text):
    translator = Translator(to_lang='en', from_lang='ru')
    natija = translator.translate(text)
    return natija

def ru_uz(text):
    translator = Translator(to_lang='uz', from_lang='ru')
    natija = translator.translate(text)
    return natija


def uz_ru(text):
    translator = Translator(to_lang='ru', from_lang='uz')
    natija = translator.translate(text)
    return natija


def en_ru(text):
    translator = Translator(to_lang='ru', from_lang='en')
    natija = translator.translate(text)
    return natija


# print(en_ru('apple'))

