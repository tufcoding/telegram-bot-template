from logger.logger import logger

import json
import os

class LanguageManager:
    def __init__(self):
        self.languages = {}
        self.language_codes = []
        self._load_languages()
        self._verify_texts()
    
    def _get_language_dir(self) -> str:
        return os.path.dirname(os.path.abspath(__file__))
    
    def _load_language_file(self, file_path: str) -> dict:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _save_language_file(self, lang_code: str, lang_data: dict):
        file_path = os.path.join(self._get_language_dir(), f"{lang_code}.json")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lang_data, f, ensure_ascii=False, indent=4)
    
    def _load_languages(self):
        current_dir = self._get_language_dir()
        
        for filename in os.listdir(current_dir):
            if filename.endswith('.json'):
                lang_code = filename[:-5]
                file_path = os.path.join(current_dir, filename)
                self.languages[lang_code] = self._load_language_file(file_path)
        
        self.language_codes = list(self.languages.keys())
    
    def _get_all_keys(self) -> set:
        all_keys = set()
        for lang_texts in self.languages.values():
            all_keys.update(lang_texts.keys())
        return all_keys
    
    def _verify_texts(self):
        all_keys = self._get_all_keys()
        
        for lang_code, lang_texts in self.languages.items():
            updated = False
            for key in all_keys:
                if key not in lang_texts:
                    self.languages[lang_code][key] = "Missing Text"
                    updated = True
                    logger.info(f"Key '{key}' is missing in language '{lang_code}'")
            
            if updated:
                self._save_language_file(lang_code, lang_texts)
    
    def get_text(self, lang_code: str, key: str, *args) -> str:
        texts = self.languages.get(lang_code, self.languages['en'])
        text = texts.get(key, self.languages['en'][key])
        return text.format(*args) if args else text
    
    def get_next_language(self, current_lang: str) -> str:
        current_index = self.language_codes.index(current_lang)
        next_index = (current_index + 1) % len(self.language_codes)
        return self.language_codes[next_index]