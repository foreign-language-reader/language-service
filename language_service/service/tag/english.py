import en_core_web_sm
from language_service.dto.word import Word

parser = en_core_web_sm.load()


def tag_english(text):
    return [
        Word(token=word.text, tag=word.pos_, lemma=word.lemma_) for word in parser(text)
    ]
