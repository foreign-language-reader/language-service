import zh_core_web_sm
from language_service.dto.word import Word

parser = zh_core_web_sm.load()


def tag_chinese(text):
    return [
        Word(token=word.text, tag=word.pos_, lemma=word.lemma_) for word in parser(text)
    ]
