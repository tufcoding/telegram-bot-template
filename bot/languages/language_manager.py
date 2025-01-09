from . import en, ar, es

class LanguageManager:
    def __init__(self):
        self.languages = {
            'en': en.TEXTS,
            'ar': ar.TEXTS,
            'es': es.TEXTS
        }
        self.language_codes = list(self.languages.keys())
    
    def get_text(self, lang_code: str, key: str, *args) -> str:
        texts = self.languages.get(lang_code, self.languages['en'])
        text = texts.get(key, self.languages['en'][key])
        return text.format(*args) if args else text
    
    def get_next_language(self, current_lang: str) -> str:
        current_index = self.language_codes.index(current_lang)
        next_index = (current_index + 1) % len(self.language_codes)
        return self.language_codes[next_index]