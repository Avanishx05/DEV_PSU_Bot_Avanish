import googletrans
from googletrans import Translator

#runnning the library
translator = Translator()

#get the language codes.
def lang_code(language):
    language = language.lower()
    lang_dict = googletrans.LANGUAGES

    for key in lang_dict.keys():
        if language == lang_dict[key]:
            return key
    
    return 'None'

def translator_func(msg, language='english'):

    if language.lower()  == 'chinese':
        lc = 'zh-cn'
    else:
        lc = lang_code(language)

    if lc == 'None':
        return 'Sorry, Language Not Found'

    return language + ": " + translator.translate(text=msg, dest=lc).text

